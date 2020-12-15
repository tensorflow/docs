description: Optimization parameters for Adam with TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.Adam" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.tpu.experimental.embedding.Adam

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L378-L524">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimization parameters for Adam with TPU embeddings.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.Adam`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.Adam(
    learning_rate: Union[float, Callable[[], float]] = 0.001,
    beta_1: float = 0.9,
    beta_2: float = 0.999,
    epsilon: float = 1e-07,
    lazy_adam: bool = (True),
    sum_inside_sqrt: bool = (True),
    use_gradient_accumulation: bool = (True),
    clip_weight_min: Optional[float] = None,
    clip_weight_max: Optional[float] = None,
    weight_decay_factor: Optional[float] = None,
    multiply_weight_decay_factor_by_learning_rate: bool = None,
    slot_variable_creation_fn: Optional[SlotVarCreationFnType] = None,
    clipvalue: Optional[ClipValueType] = None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to <a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> via the `optimizer`
argument to set the global optimizer and its parameters:

NOTE: By default this optimizer is lazy, i.e. it will not apply the gradient
update of zero to rows that were not looked up. You can change this behavior
by setting `lazy_adam` to `False`.

```python
embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    ...
    optimizer=tf.tpu.experimental.embedding.Adam(0.1))
```

This can also be used in a <a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a> as the
optimizer parameter to set a table specific optimizer. This will override the
optimizer and parameters for global embedding optimizer defined above:

```python
table_one = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...,
    optimizer=tf.tpu.experimental.embedding.Adam(0.2))
table_two = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...)

feature_config = (
    tf.tpu.experimental.embedding.FeatureConfig(
        table=table_one),
    tf.tpu.experimental.embedding.FeatureConfig(
        table=table_two))

embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    feature_config=feature_config,
    batch_size=...
    optimizer=tf.tpu.experimental.embedding.Adam(0.1))
```

In the above example, the first feature will be looked up in a table that has
a learning rate of 0.2 while the second feature will be looked up in a table
that has a learning rate of 0.1.

See 'tensorflow/core/protobuf/tpu/optimization_parameters.proto' for a
complete description of these parameters and their impacts on the optimizer
algorithm.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
The learning rate. It should be a floating point value or a
callable taking no arguments for a dynamic learning rate.
</td>
</tr><tr>
<td>
`beta_1`
</td>
<td>
A float value. The exponential decay rate for the 1st moment
estimates.
</td>
</tr><tr>
<td>
`beta_2`
</td>
<td>
A float value. The exponential decay rate for the 2nd moment
estimates.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small constant for numerical stability.
</td>
</tr><tr>
<td>
`lazy_adam`
</td>
<td>
Use lazy Adam instead of Adam. Lazy Adam trains faster.
</td>
</tr><tr>
<td>
`sum_inside_sqrt`
</td>
<td>
When this is true, the Adam update formula is changed
from `m / (sqrt(v) + epsilon)` to `m / sqrt(v + epsilon**2)`. This
option improves the performance of TPU training and is not expected to
harm model quality.
</td>
</tr><tr>
<td>
`use_gradient_accumulation`
</td>
<td>
Setting this to `False` makes embedding
gradients calculation less accurate but faster.
</td>
</tr><tr>
<td>
`clip_weight_min`
</td>
<td>
the minimum value to clip by; None means -infinity.
</td>
</tr><tr>
<td>
`clip_weight_max`
</td>
<td>
the maximum value to clip by; None means +infinity.
</td>
</tr><tr>
<td>
`weight_decay_factor`
</td>
<td>
amount of weight decay to apply; None means that the
weights are not decayed.
</td>
</tr><tr>
<td>
`multiply_weight_decay_factor_by_learning_rate`
</td>
<td>
if true,
`weight_decay_factor` is multiplied by the current learning rate.
</td>
</tr><tr>
<td>
`slot_variable_creation_fn`
</td>
<td>
If you wish do directly control the creation of
the slot variables, set this to a callable taking three parameters: a
table variable, a list of slot names to create for it, and a list of
initializers. This function should return a dict with the slot names
as keys and the created variables as values with types matching the
table variable. When set to None (the default), uses the built-in
variable creation.
</td>
</tr><tr>
<td>
`clipvalue`
</td>
<td>
Controls clipping of the gradient. Set to either a single
positive scalar value to get clipping or a tiple of scalar values (min,
max) to set a separate maximum or minimum. If one of the two entries is
None, then there will be no clipping that direction.
</td>
</tr>
</table>



