description: Apply standard lookup ops with <a href="../../../../tf/tpu/experimental/embedding.md"><code>tf.tpu.experimental.embedding</code></a> configs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.serving_embedding_lookup" />
<meta itemprop="path" content="Stable" />
</div>

# tf.tpu.experimental.embedding.serving_embedding_lookup

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/tpu_embedding_v2.py#L1455-L1560">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Apply standard lookup ops with <a href="../../../../tf/tpu/experimental/embedding.md"><code>tf.tpu.experimental.embedding</code></a> configs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.serving_embedding_lookup`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.serving_embedding_lookup(
    inputs, weights, tables, feature_config
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function is a utility which allows using the
<a href="../../../../tf/tpu/experimental/embedding.md"><code>tf.tpu.experimental.embedding</code></a> config objects with standard lookup functions.
This can be used when exporting a model which uses
<a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> for serving on CPU. In particular
<a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> only supports lookups on TPUs and
should not be part of your serving graph.

Note that TPU specific options (such as `max_sequence_length`) in the
configuration objects will be ignored.

In the following example we take take a trained model (see the documentation
for <a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> for the context) and create a
saved model with a serving function that will perform the embedding lookup and
pass the results to your model:

```python
model = model_fn(...)
embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    feature_config=feature_config,
    batch_size=1024,
    optimizer=tf.tpu.experimental.embedding.SGD(0.1))
checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
checkpoint.restore(...)

@tf.function(input_signature=[{'feature_one': tf.TensorSpec(...),
                               'feature_two': tf.TensorSpec(...),
                               'feature_three': tf.TensorSpec(...)}])
def serve_tensors(embedding_featurese):
  embedded_features = tf.tpu.experimental.embedding.serving_embedding_lookup(
      embedding_features, None, embedding.embedding_tables,
      feature_config)
  return model(embedded_features)

model.embedding_api = embedding
tf.saved_model.save(model,
                    export_dir=...,
                    signatures={'serving_default': serve_tensors})

```

NOTE: Its important to assign the embedding api object to a member of your
model as <a href="../../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> only supports saving variables one `Trackable`
object. Since the model's weights are in `model` and the embedding table are
managed by `embedding`, we assign `embedding` to and attribute of `model` so
that tf.saved_model.save can find the embedding variables.

NOTE: The same `serve_tensors` function and <a href="../../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> call will
work directly from training.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
a nested structure of Tensors, SparseTensors or RaggedTensors.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
a nested structure of Tensors, SparseTensors or RaggedTensors or
None for no weights. If not None, structure must match that of inputs, but
entries are allowed to be None.
</td>
</tr><tr>
<td>
`tables`
</td>
<td>
a dict of mapping TableConfig objects to Variables.
</td>
</tr><tr>
<td>
`feature_config`
</td>
<td>
a nested structure of FeatureConfig objects with the same
structure as inputs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of Tensors with the same structure as inputs.
</td>
</tr>

</table>

