description: Returns input function that would feed dict of numpy arrays into the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.inputs.numpy_input_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.estimator.inputs.numpy_input_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/inputs/numpy_io.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns input function that would feed dict of numpy arrays into the model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.inputs.numpy_input_fn(
    x, y=None, batch_size=128, num_epochs=1, shuffle=None, queue_capacity=1000,
    num_threads=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

This returns a function outputting `features` and `targets` based on the dict
of numpy arrays. The dict `features` has the same keys as the `x`. The dict
`targets` has the same keys as the `y` if `y` is a dict.

#### Example:



```python
age = np.arange(4) * 1.0
height = np.arange(32, 36)
x = {'age': age, 'height': height}
y = np.arange(-32, -28)

with tf.Session() as session:
  input_fn = numpy_io.numpy_input_fn(
      x, y, batch_size=2, shuffle=False, num_epochs=1)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
numpy array object or dict of numpy array objects. If an array, the array
will be treated as a single feature.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
numpy array object or dict of numpy array object. `None` if absent.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Integer, size of batches to return.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
Integer, number of epochs to iterate over data. If `None` will
run forever.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Boolean, if True shuffles the queue. Avoid shuffle at prediction
time.
</td>
</tr><tr>
<td>
`queue_capacity`
</td>
<td>
Integer, size of queue to accumulate.
</td>
</tr><tr>
<td>
`num_threads`
</td>
<td>
Integer, number of threads used for reading and enqueueing. In
order to have predicted and repeatable order of reading and enqueueing,
such as in prediction and evaluation mode, `num_threads` should be 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Function, that has signature of ()->(dict of `features`, `targets`)
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the shape of `y` mismatches the shape of values in `x` (i.e.,
values in `x` have same shape).
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if duplicate keys are in both `x` and `y` when `y` is a dict.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if x or y is an empty dict.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
`x` is not a dict or array.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if 'shuffle' is not provided or a bool.
</td>
</tr>
</table>

