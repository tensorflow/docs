description: Applies the rectified linear unit activation function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.relu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.relu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/activations.py#L198-L235">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies the rectified linear unit activation function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.relu`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.relu(
    x, alpha=0.0, max_value=None, threshold=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

With default values, this returns the standard ReLU activation:
`max(x, 0)`, the element-wise maximum of 0 and the input tensor.

Modifying default parameters allows you to use non-zero thresholds,
change the max value of the activation,
and to use a non-zero multiple of the input for values below the threshold.

#### For example:



```
>>> foo = tf.constant([-10, -5, 0.0, 5, 10], dtype = tf.float32)
>>> tf.keras.activations.relu(foo).numpy()
array([ 0.,  0.,  0.,  5., 10.], dtype=float32)
>>> tf.keras.activations.relu(foo, alpha=0.5).numpy()
array([-5. , -2.5,  0. ,  5. , 10. ], dtype=float32)
>>> tf.keras.activations.relu(foo, max_value=5).numpy()
array([0., 0., 0., 5., 5.], dtype=float32)
>>> tf.keras.activations.relu(foo, threshold=5).numpy()
array([-0., -0.,  0.,  0., 10.], dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Input `tensor` or `variable`.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
A `float` that governs the slope for values lower than the
threshold.
</td>
</tr><tr>
<td>
`max_value`
</td>
<td>
A `float` that sets the saturation threshold (the largest value
the function will return).
</td>
</tr><tr>
<td>
`threshold`
</td>
<td>
A `float` giving the threshold value of the activation function
below which values will be damped or set to zero.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` representing the input tensor,
transformed by the relu activation function.
Tensor will be of the same shape and dtype of input `x`.
</td>
</tr>

</table>

