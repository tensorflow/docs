description: The TPUEmbedding mid level API.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.embedding.TPUEmbedding" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply_gradients"/>
<meta itemprop="property" content="dequeue"/>
<meta itemprop="property" content="enqueue"/>
</div>

# tf.tpu.experimental.embedding.TPUEmbedding

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2.py#L87-L1200">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The TPUEmbedding mid level API.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.embedding.TPUEmbedding`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.embedding.TPUEmbedding(
    feature_config, batch_size, optimizer,
    pipeline_execution_with_tensor_core=(False), initialize_tpu_embedding=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: When instantiated under a TPUStrategy, this class can only be created
once per call to <a href="../../../../tf/tpu/experimental/initialize_tpu_system.md"><code>tf.tpu.experimental.initialize_tpu_system</code></a>. If you wish to
re-initialize the embedding engine you must re-initialize the tpu as well.
Doing this will clear any variables from TPU, so ensure you have checkpointed
before you do this. If a further instances of the class are needed,
set the `initialize_tpu_embedding` argument to `False`.

This class can be used to support training large embeddings on TPU. When
creating an instance of this class, you must specify the complete set of
tables and features you expect to lookup in those tables. See the
documentation of <a href="../../../../tf/tpu/experimental/embedding/TableConfig.md"><code>tf.tpu.experimental.embedding.TableConfig</code></a> and
<a href="../../../../tf/tpu/experimental/embedding/FeatureConfig.md"><code>tf.tpu.experimental.embedding.FeatureConfig</code></a> for more details on the complete
set of options. We will cover the basic usage here.

NOTE: multiple `FeatureConfig` objects can use the same `TableConfig` object,
allowing different features to share the same table:

```python
table_config_one = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...)
table_config_two = tf.tpu.experimental.embedding.TableConfig(
    vocabulary_size=...,
    dim=...)
feature_config = {
    'feature_one': tf.tpu.experimental.embedding.FeatureConfig(
        table=table_config_one),
    'feature_two': tf.tpu.experimental.embedding.FeatureConfig(
        table=table_config_one),
    'feature_three': tf.tpu.experimental.embedding.FeatureConfig(
        table=table_config_two)}
```

There are two modes under which the `TPUEmbedding` class can used. This
depends on if the class was created under a `TPUStrategy` scope or not.

Under `TPUStrategy`, we allow access to the method `enqueue`, `dequeue` and
`apply_gradients`. We will show examples below of how to use these to train
and evaluate your model. Under CPU, we only access to the `embedding_tables`
property which allow access to the embedding tables so that you can use them
to run model evaluation/prediction on CPU.

First lets look at the `TPUStrategy` mode. Initial setup looks like:

```python
strategy = tf.distribute.TPUStrategy(...)
with strategy.scope():
  embedding = tf.tpu.experimental.embedding.TPUEmbedding(
      feature_config=feature_config,
      batch_size=1024,
      optimizer=tf.tpu.experimental.embedding.SGD(0.1))
```

When creating a distributed dataset that is to be passed to the enqueue
operation a special input option must be specified:

```python
distributed_dataset = (
    strategy.experimental_distribute_datasets_from_function(
        dataset_fn=...,
        options=tf.distribute.InputOptions(
            experimental_prefetch_to_device=False))
dataset_iterator = iter(distributed_dataset)
```

To use this API on TPU you should use a custom training loop. Below is an
example of a training and evaluation step:

```python
@tf.function
def training_step(dataset_iterator, num_steps):
  def tpu_step(tpu_features):
    with tf.GradientTape() as tape:
      activations = embedding.dequeue()
      tape.watch(activations)
      model_output = model(activations)
      loss = ...  # some function of labels and model_output

    embedding_gradients = tape.gradient(loss, activations)
    embedding.apply_gradients(embedding_gradients)
    # Insert your model gradient and optimizer application here

  for _ in tf.range(num_steps):
    embedding_features, tpu_features = next(dataset_iterator)
    embedding.enqueue(embedding_features, training=True)
    strategy.run(tpu_step, args=(embedding_features, ))

@tf.function
def evalution_step(dataset_iterator, num_steps):
  def tpu_step(tpu_features):
    activations = embedding.dequeue()
    model_output = model(activations)
    # Insert your evaluation code here.

  for _ in tf.range(num_steps):
    embedding_features, tpu_features = next(dataset_iterator)
    embedding.enqueue(embedding_features, training=False)
    strategy.run(tpu_step, args=(embedding_features, ))
```

NOTE: The calls to `enqueue` have `training` set to `True` when
`embedding.apply_gradients` is used and set to `False` when
`embedding.apply_gradients` is not present in the function. If you don't
follow this pattern you may cause an error to be raised or the tpu may
deadlock.

In the above examples, we assume that the user has a dataset which returns
a tuple where the first element of the tuple matches the structure of what
was passed as the `feature_config` argument to the object initializer. Also we
utilize <a href="../../../../tf/range.md"><code>tf.range</code></a> to get a <a href="../../../../tf/while_loop.md"><code>tf.while_loop</code></a> in order to increase performance.

When checkpointing your model, you should include your
<a href="../../../../tf/tpu/experimental/embedding/TPUEmbedding.md"><code>tf.tpu.experimental.embedding.TPUEmbedding</code></a> object in the checkpoint. It is a
trackable object and saving it will save the embedding tables and their
optimizer slot variables:

```python
checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
checkpoint.save(...)
```

On CPU, only the `embedding_table` property is usable. This will allow you to
restore a checkpoint to the object and have access to the table variables:

```python
model = model_fn(...)
embedding = tf.tpu.experimental.embedding.TPUEmbedding(
    feature_config=feature_config,
    batch_size=1024,
    optimizer=tf.tpu.experimental.embedding.SGD(0.1))
checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
checkpoint.restore(...)

tables = embedding.embedding_tables
```

You can now use table in functions like <a href="../../../../tf/nn/embedding_lookup.md"><code>tf.nn.embedding_lookup</code></a> to perform
your embedding lookup and pass to your model.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`feature_config`
</td>
<td>
A nested structure of
<a href="../../../../tf/tpu/experimental/embedding/FeatureConfig.md"><code>tf.tpu.experimental.embedding.FeatureConfig</code></a> configs.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
The global batch size that you indend to use. Note that is
fixed and the same batch size must be used for both training and
evaluation.
</td>
</tr><tr>
<td>
`optimizer`
</td>
<td>
An instance of one of <a href="../../../../tf/tpu/experimental/embedding/SGD.md"><code>tf.tpu.experimental.embedding.SGD</code></a>,
<a href="../../../../tf/tpu/experimental/embedding/Adagrad.md"><code>tf.tpu.experimental.embedding.Adagrad</code></a> or
<a href="../../../../tf/tpu/experimental/embedding/Adam.md"><code>tf.tpu.experimental.embedding.Adam</code></a>.
</td>
</tr><tr>
<td>
`pipeline_execution_with_tensor_core`
</td>
<td>
If True, the TPU embedding
computations will overlap with the TensorCore computations (and hence
will be one step old). Set to True for improved performance.
</td>
</tr><tr>
<td>
`initialize_tpu_embedding`
</td>
<td>
If False, will not initialize the TPU embedding
engine. If this is set to False and another instance of this class has
not initialized the tpu embedding engine, the creation of this object
will fail.
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
If optimizer is not one of tf.tpu.experimental.embedding.(SGD,
Adam or Adagrad).
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`embedding_tables`
</td>
<td>
Returns a dict of embedding tables, keyed by `TableConfig`.

This property only works when the `TPUEmbedding` object is created under a
non-TPU strategy. This is intended to be used to for CPU based lookup when
creating a serving checkpoint.
</td>
</tr>
</table>



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2.py#L506-L593">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_gradients(
    gradients, name=None
)
</code></pre>

Applies the gradient update to the embedding tables.

If a gradient of `None` is passed in any position of the nested structure,
then an gradient update with a zero gradient is applied for that feature.
For optimizers like SGD or Adagrad, this is the same as applying no update
at all. For lazy Adam and other sparsely applied optimizers with decay,
ensure you understand the effect of applying a zero gradient.

```python
strategy = tf.distribute.TPUStrategy(...)
with strategy.scope():
  embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)

distributed_dataset = (
    strategy.experimental_distribute_datasets_from_function(
        dataset_fn=...,
        options=tf.distribute.InputOptions(
            experimental_prefetch_to_device=False))
dataset_iterator = iter(distributed_dataset)

@tf.function
def training_step():
  def tpu_step(tpu_features):
    with tf.GradientTape() as tape:
      activations = embedding.dequeue()
      tape.watch(activations)

      loss = ... #  some computation involving activations

    embedding_gradients = tape.gradient(loss, activations)
    embedding.apply_gradients(embedding_gradients)

  embedding_features, tpu_features = next(dataset_iterator)
  embedding.enqueue(embedding_features, training=True)
  strategy.run(tpu_step, args=(embedding_features, ))

training_step()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`gradients`
</td>
<td>
A nested structure of gradients, with structure matching the
`feature_config` passed to this object.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the underlying op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If called when object wasn't created under a `TPUStrategy`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If a non-<a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> non-`None` gradient is passed in, or a
<a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> of the incorrect shape is passed in. Also if
the size of any sequence in `gradients` does not match corresponding
sequence in `feature_config`.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If the type of any sequence in `gradients` does not match
corresponding sequence in `feature_config`.
</td>
</tr>
</table>



<h3 id="dequeue"><code>dequeue</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2.py#L595-L700">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>dequeue(
    name=None
)
</code></pre>

Get the embedding results.

Returns a nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> objects, matching the structure of
the `feature_config` argument to the `TPUEmbedding` class. The output shape
of the tensors is `(batch_size, dim)`, where `batch_size` is the per core
batch size, `dim` is the dimension of the corresponding `TableConfig`. If
the feature's corresponding `FeatureConfig` has `max_sequence_length`
greater than 0, the output will be a sequence of shape
`(batch_size, max_sequence_length, dim)` instead.

```python
strategy = tf.distribute.TPUStrategy(...)
with strategy.scope():
  embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)

distributed_dataset = (
    strategy.experimental_distribute_datasets_from_function(
        dataset_fn=...,
        options=tf.distribute.InputOptions(
            experimental_prefetch_to_device=False))
dataset_iterator = iter(distributed_dataset)

@tf.function
def training_step():
  def tpu_step(tpu_features):
    with tf.GradientTape() as tape:
      activations = embedding.dequeue()
      tape.watch(activations)

      loss = ... #  some computation involving activations

    embedding_gradients = tape.gradient(loss, activations)
    embedding.apply_gradients(embedding_gradients)

  embedding_features, tpu_features = next(dataset_iterator)
  embedding.enqueue(embedding_features, training=True)
  strategy.run(tpu_step, args=(embedding_features, ))

training_step()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the underlying op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of tensors, with the same structure as `feature_config`
</td>
</tr>

</table>


passed to this instance of the `TPUEmbedding` object.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If called when object wasn't created under a `TPUStrategy`.
</td>
</tr>
</table>



<h3 id="enqueue"><code>enqueue</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding_v2.py#L1051-L1200">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>enqueue(
    features, weights=None, training=(True), name=None
)
</code></pre>

Enqueues id tensors for embedding lookup.

This function enqueues a structure of features to be looked up in the
embedding tables. We expect that the batch size of each of the tensors in
features matches the per core batch size. This will automatically happen if
your input dataset is batched to the global batch size and you use
<a href="../../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>'s `experimental_distribute_dataset`
or if you use `experimental_distribute_datasets_from_function` and batch
to the per core batch size computed by the context passed to your input
function.

```python
strategy = tf.distribute.TPUStrategy(...)
with strategy.scope():
  embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)

distributed_dataset = (
    strategy.experimental_distribute_datasets_from_function(
        dataset_fn=...,
        options=tf.distribute.InputOptions(
            experimental_prefetch_to_device=False))
dataset_iterator = iter(distributed_dataset)

@tf.function
def training_step():
  def tpu_step(tpu_features):
    with tf.GradientTape() as tape:
      activations = embedding.dequeue()
      tape.watch(activations)

      loss = ... #  some computation involving activations

    embedding_gradients = tape.gradient(loss, activations)
    embedding.apply_gradients(embedding_gradients)

  embedding_features, tpu_features = next(dataset_iterator)
  embedding.enqueue(embedding_features, training=True)
  strategy.run(tpu_step, args=(embedding_features,))

training_step()
```

NOTE: You should specify `training=True` when using
`embedding.apply_gradients` as above and `training=False` when not using
`embedding.apply_gradients` (e.g. for frozen embeddings or when doing
evaluation).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`features`
</td>
<td>
A nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>s, <a href="../../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>s or
<a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s, with the same structure as `feature_config`. Inputs
will be downcast to <a href="../../../../tf.md#int32"><code>tf.int32</code></a>. Only one type out of <a href="../../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>
or <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> is supported per call.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
If not `None`, a nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>s,
<a href="../../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>s or <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s, matching the above, except
that the tensors should be of float type (and they will be downcast to
<a href="../../../../tf.md#float32"><code>tf.float32</code></a>). For <a href="../../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>s we assume the `indices` are the
same for the parallel entries from `features` and similarly for
<a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s we assume the row_splits are the same.
</td>
</tr><tr>
<td>
`training`
</td>
<td>
Defaults to `True`. If `False`, enqueue the batch as inference
batch (forward pass only). Do not call `apply_gradients` when this is
`False` as this may lead to a deadlock.
name: A name for the underlying op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
When called inside a strategy.run call and input is not
directly taken from the args of the `strategy.run` call. Also if
the size of any sequence in `features` does not match corresponding
sequence in `feature_config`. Similarly for `weights`, if not `None`.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
When called inside a strategy.run call and inside XLA
control flow.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If the type of any sequence in `features` does not match
corresponding sequence in `feature_config`. Similarly for `weights`, if
not `None`.
</td>
</tr>
</table>





