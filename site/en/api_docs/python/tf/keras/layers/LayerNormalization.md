description: Layer normalization layer (Ba et al., 2016).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.LayerNormalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.LayerNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/normalization.py#L949-L1284">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer normalization layer (Ba et al., 2016).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.LayerNormalization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.LayerNormalization(
    axis=-1, epsilon=0.001, center=(True), scale=(True), beta_initializer='zeros',
    gamma_initializer='ones', beta_regularizer=None, gamma_regularizer=None,
    beta_constraint=None, gamma_constraint=None, trainable=(True), name=None,
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Normalize the activations of the previous layer for each given example in a
batch independently, rather than across a batch like Batch Normalization.
i.e. applies a transformation that maintains the mean activation within each
example close to 0 and the activation standard deviation close to 1.

Given a tensor `inputs`, moments are calculated and normalization
is performed across the axes specified in `axis`.

#### Example:



```
>>> data = tf.constant(np.arange(10).reshape(5, 2) * 10, dtype=tf.float32)
>>> print(data)
tf.Tensor(
[[ 0. 10.]
 [20. 30.]
 [40. 50.]
 [60. 70.]
 [80. 90.]], shape=(5, 2), dtype=float32)
```

```
>>> layer = tf.keras.layers.LayerNormalization(axis=1)
>>> output = layer(data)
>>> print(output)
tf.Tensor(
[[-1. 1.]
 [-1. 1.]
 [-1. 1.]
 [-1. 1.]
 [-1. 1.]], shape=(5, 2), dtype=float32)
```

Notice that with Layer Normalization the normalization happens across the
axes *within* each example, rather than across different examples in the
batch.

If `scale` or `center` are enabled, the layer will scale the normalized
outputs by broadcasting them with a trainable variable `gamma`, and center
the outputs by broadcasting with a trainable variable `beta`. `gamma` will
default to a ones tensor and `beta` will default to a zeros tensor, so that
centering and scaling are no-ops before training has begun.

So, with scaling and centering enabled the normalization equations
are as follows:
  Let the intermediate activations for a mini-batch to be the `inputs`.

  For each sample `x_i` in `inputs` with `k` features, we compute the mean and
  variance of the sample:

  ```python
  mean_i = sum(x_i[j] for j in range(k)) / k
  var_i = sum((x_i[j] - mean_i) ** 2 for j in range(k)) / k
  ```

  and then compute a normalized `x_i_normalized`, including a small factor
  `epsilon` for numerical stability.

  ```python
  x_i_normalized = (x_i - mean_i) / sqrt(var_i + epsilon)
  ```

  And finally `x_i_normalized ` is linearly transformed by `gamma` and `beta`,
  which are learned parameters:

  ```python
  output_i = x_i_normalized * gamma + beta
  ```

`gamma` and `beta` will span the axes of `inputs` specified in `axis`, and
this part of the inputs' shape must be fully defined.

#### For example:



```
>>> layer = tf.keras.layers.LayerNormalization(axis=[1, 2, 3])
>>> layer.build([5, 20, 30, 40])
>>> print(layer.beta.shape)
(20, 30, 40)
>>> print(layer.gamma.shape)
(20, 30, 40)
```

Note that other implementations of layer normalization may choose to define
`gamma` and `beta` over a separate set of axes from the axes being
normalized across. For example, Group Normalization
([Wu et al. 2018](https://arxiv.org/abs/1803.08494)) with group size of 1
corresponds to a Layer Normalization that normalizes across height, width,
and channel and has `gamma` and `beta` span only the channel dimension.
So, this Layer Normalization implementation will not match a Group
Normalization layer with group size set to 1.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Integer or List/Tuple. The axis or axes to normalize across. Typically
this is the features axis/axes. The left-out axes are typically the batch
axis/axes. This argument defaults to `-1`, the last dimension in the
input.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
Small float added to variance to avoid dividing by zero. Defaults
to 1e-3
</td>
</tr><tr>
<td>
`center`
</td>
<td>
If True, add offset of `beta` to normalized tensor. If False, `beta`
is ignored. Defaults to True.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
If True, multiply by `gamma`. If False, `gamma` is not used. Defaults
to True. When the next layer is linear (also e.g. <a href="../../../tf/nn/relu.md"><code>nn.relu</code></a>), this can be
disabled since the scaling will be done by the next layer.
</td>
</tr><tr>
<td>
`beta_initializer`
</td>
<td>
Initializer for the beta weight. Defaults to zeros.
</td>
</tr><tr>
<td>
`gamma_initializer`
</td>
<td>
Initializer for the gamma weight. Defaults to ones.
</td>
</tr><tr>
<td>
`beta_regularizer`
</td>
<td>
Optional regularizer for the beta weight. None by default.
</td>
</tr><tr>
<td>
`gamma_regularizer`
</td>
<td>
Optional regularizer for the gamma weight. None by
default.
</td>
</tr><tr>
<td>
`beta_constraint`
</td>
<td>
Optional constraint for the beta weight. None by default.
</td>
</tr><tr>
<td>
`gamma_constraint`
</td>
<td>
Optional constraint for the gamma weight. None by default.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` the variables will be marked as trainable.
Defaults to True.
</td>
</tr>
</table>


Input shape: Arbitrary. Use the keyword argument `input_shape` (tuple of
  integers, does not include the samples axis) when using this layer as the
  first layer in a model.
Output shape: Same shape as input.
Reference:
  - [Lei Ba et al., 2016](https://arxiv.org/abs/1607.06450).

