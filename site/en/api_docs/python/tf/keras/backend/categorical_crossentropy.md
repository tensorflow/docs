description: Categorical crossentropy between an output tensor and a target tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.categorical_crossentropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.categorical_crossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L4518-L4583">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Categorical crossentropy between an output tensor and a target tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.categorical_crossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.categorical_crossentropy(
    target, output, from_logits=(False), axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`target`
</td>
<td>
A tensor of the same shape as `output`.
</td>
</tr><tr>
<td>
`output`
</td>
<td>
A tensor resulting from a softmax
(unless `from_logits` is True, in which
case `output` is expected to be the logits).
</td>
</tr><tr>
<td>
`from_logits`
</td>
<td>
Boolean, whether `output` is the
result of a softmax, or is a tensor of logits.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Int specifying the channels axis. `axis=-1` corresponds to data
format `channels_last', and `axis=1` corresponds to data format
`channels_first`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
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
if `axis` is neither -1 nor one of the axes of `output`.
</td>
</tr>
</table>



#### Example:



```
>>> a = tf.constant([1., 0., 0., 0., 1., 0., 0., 0., 1.], shape=[3,3])
>>> print(a)
tf.Tensor(
  [[1. 0. 0.]
   [0. 1. 0.]
   [0. 0. 1.]], shape=(3, 3), dtype=float32)
>>> b = tf.constant([.9, .05, .05, .5, .89, .6, .05, .01, .94], shape=[3,3])
>>> print(b)
tf.Tensor(
  [[0.9  0.05 0.05]
   [0.5  0.89 0.6 ]
   [0.05 0.01 0.94]], shape=(3, 3), dtype=float32)
>>> loss = tf.keras.backend.categorical_crossentropy(a, b)
>>> print(np.around(loss, 5))
[0.10536 0.80467 0.06188]
>>> loss = tf.keras.backend.categorical_crossentropy(a, a)
>>> print(np.around(loss, 5))
[0. 0. 0.]
```