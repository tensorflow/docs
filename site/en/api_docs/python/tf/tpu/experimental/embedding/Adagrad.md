description: Optimization parameters for Adagrad with TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.Adagrad" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.tpu.experimental.embedding.Adagrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2_utils.py#L211-L310">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimization parameters for Adagrad with TPU embeddings.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.Adagrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.Adagrad(
    learning_rate=0.001, initial_accumulator_value=0.1,
    use_gradient_accumulation=(True), clip_weight_min=None, clip_weight_max=None,
    weight_decay_factor=None, multiply_weight_decay_factor_by_learning_rate=None,
    slot_variable_creation_fn=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to <a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> via the `optimizer`
argument to set the global optimizer and its parameters:

```python
embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    ...
    optimizer=tf.tpu.experimental.embedding.Adagrad(0.1))
```

This can also be used in a <a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a> as the
optimizer parameter to set a table specific optimizer. This will override the
optimizer and parameters for global embedding optimizer defined above:

```python
table_one = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...,
    optimizer=tf.tpu.experimental.embedding.Adagrad(0.2))
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
    optimizer=tf.tpu.experimental.embedding.Adagrad(0.1))
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
`initial_accumulator_value`
</td>
<td>
initial accumulator for Adagrad.
</td>
</tr><tr>
<td>
`use_gradient_accumulation`
</td>
<td>
setting this to `False` makes embedding
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
Defaults to `None`. If you wish do directly
control the creation of the slot variables, set this to a callable
taking two parameters, a variable and a list of slot names to create for
it. This function should return a dict with the slot names as keys and
the created variables as values. When set to None (the default), uses
the built-in variable creation.
</td>
</tr>
</table>



