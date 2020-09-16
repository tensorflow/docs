description: Destroys the current TF graph and session, and creates a new one.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.clear_session" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.clear_session

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L241-L284">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Destroys the current TF graph and session, and creates a new one.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.clear_session`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.clear_session()
</code></pre>



<!-- Placeholder for "Used in" -->

Calling clear_session() releases the global graph state that Keras is
holding on to; resets the counters used for naming layers and
variables in Keras; and resets the learning phase. This helps avoid clutter
from old models and layers, especially when memory is limited, and a
common use-case for clear_session is releasing memory when building models
and layers in a loop.

```
>>> import tensorflow as tf
>>> layers = [tf.keras.layers.Dense(10) for _ in range(10)]
>>> new_layer = tf.keras.layers.Dense(10)
>>> print(new_layer.name)
dense_10
>>> tf.keras.backend.set_learning_phase(1)
>>> print(tf.keras.backend.learning_phase())
1
>>> tf.keras.backend.clear_session()
>>> new_layer = tf.keras.layers.Dense(10)
>>> print(new_layer.name)
dense
>>> print(tf.keras.backend.learning_phase())
0
```