description: A mixin for putting Python state in an object-based checkpoint.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.experimental.PythonState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="deserialize"/>
<meta itemprop="property" content="serialize"/>
</div>

# tf.train.experimental.PythonState

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/tracking/python_state.py#L31-L92">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A mixin for putting Python state in an object-based checkpoint.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.experimental.PythonState`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

This is an abstract class which allows extensions to TensorFlow's object-based
checkpointing (see <a href="../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>). For example a wrapper for NumPy
arrays:

```python
import io
import numpy

class NumpyWrapper(tf.train.experimental.PythonState):

  def __init__(self, array):
    self.array = array

  def serialize(self):
    string_file = io.BytesIO()
    try:
      numpy.save(string_file, self.array, allow_pickle=False)
      serialized = string_file.getvalue()
    finally:
      string_file.close()
    return serialized

  def deserialize(self, string_value):
    string_file = io.BytesIO(string_value)
    try:
      self.array = numpy.load(string_file, allow_pickle=False)
    finally:
      string_file.close()
```

Instances of `NumpyWrapper` are checkpointable objects, and will be saved and
restored from checkpoints along with TensorFlow state like variables.

```python
root = tf.train.Checkpoint(numpy=NumpyWrapper(numpy.array([1.])))
save_path = root.save(prefix)
root.numpy.array *= 2.
assert [2.] == root.numpy.array
root.restore(save_path)
assert [1.] == root.numpy.array
```

## Methods

<h3 id="deserialize"><code>deserialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/tracking/python_state.py#L81-L83">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>deserialize(
    string_value
)
</code></pre>

Callback to deserialize the object.


<h3 id="serialize"><code>serialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/tracking/python_state.py#L77-L79">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>serialize()
</code></pre>

Callback to serialize the object. Returns a string.




