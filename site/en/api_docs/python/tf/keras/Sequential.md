description: Sequential groups a linear stack of layers into a <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.Sequential" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="add"/>
<meta itemprop="property" content="compile"/>
<meta itemprop="property" content="evaluate"/>
<meta itemprop="property" content="evaluate_generator"/>
<meta itemprop="property" content="fit"/>
<meta itemprop="property" content="fit_generator"/>
<meta itemprop="property" content="get_layer"/>
<meta itemprop="property" content="load_weights"/>
<meta itemprop="property" content="make_predict_function"/>
<meta itemprop="property" content="make_test_function"/>
<meta itemprop="property" content="make_train_function"/>
<meta itemprop="property" content="pop"/>
<meta itemprop="property" content="predict"/>
<meta itemprop="property" content="predict_classes"/>
<meta itemprop="property" content="predict_generator"/>
<meta itemprop="property" content="predict_on_batch"/>
<meta itemprop="property" content="predict_proba"/>
<meta itemprop="property" content="predict_step"/>
<meta itemprop="property" content="reset_metrics"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="save"/>
<meta itemprop="property" content="save_weights"/>
<meta itemprop="property" content="summary"/>
<meta itemprop="property" content="test_on_batch"/>
<meta itemprop="property" content="test_step"/>
<meta itemprop="property" content="to_json"/>
<meta itemprop="property" content="to_yaml"/>
<meta itemprop="property" content="train_on_batch"/>
<meta itemprop="property" content="train_step"/>
</div>

# tf.keras.Sequential

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/sequential.py#L50-L515">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



`Sequential` groups a linear stack of layers into a <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.models.Sequential`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.Sequential`, `tf.compat.v1.keras.models.Sequential`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.Sequential(
    layers=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`Sequential` provides training and inference features on this model.

#### Examples:



```
>>> # Optionally, the first layer can receive an `input_shape` argument:
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Dense(8, input_shape=(16,)))
>>> # Afterwards, we do automatic shape inference:
>>> model.add(tf.keras.layers.Dense(4))
```

```
>>> # This is identical to the following:
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.Input(shape=(16,)))
>>> model.add(tf.keras.layers.Dense(8))
```

```
>>> # Note that you can also omit the `input_shape` argument.
>>> # In that case the model doesn't have any weights until the first call
>>> # to a training/evaluation method (since it isn't yet built):
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Dense(8))
>>> model.add(tf.keras.layers.Dense(4))
>>> # model.weights not created yet
```

```
>>> # Whereas if you specify the input shape, the model gets built
>>> # continuously as you are adding layers:
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Dense(8, input_shape=(16,)))
>>> model.add(tf.keras.layers.Dense(4))
>>> len(model.weights)
4
```

```
>>> # When using the delayed-build pattern (no input shape specified), you can
>>> # choose to manually build your model by calling
>>> # `build(batch_input_shape)`:
>>> model = tf.keras.Sequential()
>>> model.add(tf.keras.layers.Dense(8))
>>> model.add(tf.keras.layers.Dense(4))
>>> model.build((None, 16))
>>> len(model.weights)
4
```

```python
# Note that when using the delayed-build pattern (no input shape specified),
# the model gets built the first time you call `fit`, `eval`, or `predict`,
# or the first time you call the model on some input data.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(8))
model.add(tf.keras.layers.Dense(1))
model.compile(optimizer='sgd', loss='mse')
# This builds the model for the first time:
model.fit(x, y, batch_size=32, epochs=10)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`layers`
</td>
<td>
Optional list of layers to add to the model.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the model.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`distribute_strategy`
</td>
<td>
The <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> this model was created under.
</td>
</tr><tr>
<td>
`layers`
</td>
<td>

</td>
</tr><tr>
<td>
`metrics_names`
</td>
<td>
Returns the model's display labels for all outputs.

Note: `metrics_names` are available only after a <a href="../../tf/keras/Model.md"><code>keras.Model</code></a> has been
trained/evaluated on actual data.

```
>>> inputs = tf.keras.layers.Input(shape=(3,))
>>> outputs = tf.keras.layers.Dense(2)(inputs)
>>> model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
>>> model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
>>> model.metrics_names
[]
```

```
>>> x = np.random.random((2, 3))
>>> y = np.random.randint(0, 2, (2, 2))
>>> model.fit(x, y)
>>> model.metrics_names
['loss', 'mae']
```

```
>>> inputs = tf.keras.layers.Input(shape=(3,))
>>> d = tf.keras.layers.Dense(2, name='out')
>>> output_1 = d(inputs)
>>> output_2 = d(inputs)
>>> model = tf.keras.models.Model(
...    inputs=inputs, outputs=[output_1, output_2])
>>> model.compile(optimizer="Adam", loss="mse", metrics=["mae", "acc"])
>>> model.fit(x, (y, y))
>>> model.metrics_names
['loss', 'out_loss', 'out_1_loss', 'out_mae', 'out_acc', 'out_1_mae',
'out_1_acc']
```
</td>
</tr><tr>
<td>
`run_eagerly`
</td>
<td>
Settable attribute indicating whether the model should run eagerly.

Running eagerly means that your model will be run step by step,
like Python code. Your model might run slower, but it should become easier
for you to debug it by stepping into individual layer calls.

By default, we will attempt to compile your model to a static graph to
deliver the best execution performance.
</td>
</tr>
</table>



## Methods

<h3 id="add"><code>add</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/sequential.py#L156-L234">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add(
    layer
)
</code></pre>

Adds a layer instance on top of the layer stack.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`layer`
</td>
<td>
layer instance.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `layer` is not a layer instance.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case the `layer` argument does not
know its input shape.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case the `layer` argument has
multiple output tensors, or is already connected
somewhere else (forbidden in `Sequential` models).
</td>
</tr>
</table>



<h3 id="compile"><code>compile</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L462-L555">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>compile(
    optimizer='rmsprop', loss=None, metrics=None, loss_weights=None,
    weighted_metrics=None, run_eagerly=None, **kwargs
)
</code></pre>

Configures the model for training.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`optimizer`
</td>
<td>
String (name of optimizer) or optimizer instance. See
<a href="../../tf/keras/optimizers.md"><code>tf.keras.optimizers</code></a>.
</td>
</tr><tr>
<td>
`loss`
</td>
<td>
String (name of objective function), objective function or
<a href="../../tf/keras/losses/Loss.md"><code>tf.keras.losses.Loss</code></a> instance. See <a href="../../tf/keras/losses.md"><code>tf.keras.losses</code></a>. An objective
function is any callable with the signature `loss = fn(y_true,
y_pred)`, where y_true = ground truth values with shape =
`[batch_size, d0, .. dN]`, except sparse loss functions such as sparse
categorical crossentropy where shape = `[batch_size, d0, .. dN-1]`.
y_pred = predicted values with shape = `[batch_size, d0, .. dN]`. It
returns a weighted loss float tensor. If a custom `Loss` instance is
used and reduction is set to NONE, return value has the shape
[batch_size, d0, .. dN-1] ie. per-sample or per-timestep loss values;
otherwise, it is a scalar. If the model has multiple outputs, you can
use a different loss on each output by passing a dictionary or a list
of losses. The loss value that will be minimized by the model will
then be the sum of all individual losses.
</td>
</tr><tr>
<td>
`metrics`
</td>
<td>
List of metrics to be evaluated by the model during training
and testing. Each of this can be a string (name of a built-in
function), function or a <a href="../../tf/keras/metrics/Metric.md"><code>tf.keras.metrics.Metric</code></a> instance. See
<a href="../../tf/keras/metrics.md"><code>tf.keras.metrics</code></a>. Typically you will use `metrics=['accuracy']`. A
function is any callable with the signature `result = fn(y_true,
y_pred)`. To specify different metrics for different outputs of a
multi-output model, you could also pass a dictionary, such as
`metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}`.
You can also pass a list (len = len(outputs)) of lists of metrics
such as `metrics=[['accuracy'], ['accuracy', 'mse']]` or
`metrics=['accuracy', ['accuracy', 'mse']]`. When you pass the
strings 'accuracy' or 'acc', we convert this to one of
<a href="../../tf/keras/metrics/BinaryAccuracy.md"><code>tf.keras.metrics.BinaryAccuracy</code></a>,
<a href="../../tf/keras/metrics/CategoricalAccuracy.md"><code>tf.keras.metrics.CategoricalAccuracy</code></a>,
<a href="../../tf/keras/metrics/SparseCategoricalAccuracy.md"><code>tf.keras.metrics.SparseCategoricalAccuracy</code></a> based on the loss
function used and the model output shape. We do a similar
conversion for the strings 'crossentropy' and 'ce' as well.
</td>
</tr><tr>
<td>
`loss_weights`
</td>
<td>
Optional list or dictionary specifying scalar coefficients
(Python floats) to weight the loss contributions of different model
outputs. The loss value that will be minimized by the model will then
be the *weighted sum* of all individual losses, weighted by the
`loss_weights` coefficients.
If a list, it is expected to have a 1:1 mapping to the model's
outputs. If a dict, it is expected to map output names (strings)
to scalar coefficients.
</td>
</tr><tr>
<td>
`weighted_metrics`
</td>
<td>
List of metrics to be evaluated and weighted by
sample_weight or class_weight during training and testing.
</td>
</tr><tr>
<td>
`run_eagerly`
</td>
<td>
Bool. Defaults to `False`. If `True`, this `Model`'s
logic will not be wrapped in a <a href="../../tf/function.md"><code>tf.function</code></a>. Recommended to leave
this as `None` unless your `Model` cannot be run inside a
<a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Any additional arguments. Supported arguments:
- `experimental_steps_per_execution`: Int. The number of batches to
run during each <a href="../../tf/function.md"><code>tf.function</code></a> call. Running multiple batches
inside a single <a href="../../tf/function.md"><code>tf.function</code></a> call can greatly improve performance
on TPUs or small models with a large Python overhead. Note that if
this value is set to `N`, `Callback.on_batch` methods will only be
called every `N` batches. This currently defaults to `1`. At most,
one full epoch will be run each execution. If a number larger than
the size of the epoch is passed, the execution will be truncated
to the size of the epoch.
- `sample_weight_mode` for backward compatibility.
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
In case of invalid arguments for
`optimizer`, `loss` or `metrics`.
</td>
</tr>
</table>



<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1242-L1394">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>evaluate(
    x=None, y=None, batch_size=None, verbose=1, sample_weight=None, steps=None,
    callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=(False),
    return_dict=(False)
)
</code></pre>

Returns the loss value & metrics values for the model in test mode.

Computation is done in batches (see the `batch_size` arg.)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
Input data. It could be:
- A Numpy array (or array-like), or a list of arrays
(in case the model has multiple inputs).
- A TensorFlow tensor, or a list of tensors
(in case the model has multiple inputs).
- A dict mapping input names to the corresponding array/tensors,
if the model has named inputs.
- A <a href="../../tf/data.md"><code>tf.data</code></a> dataset. Should return a tuple
of either `(inputs, targets)` or
`(inputs, targets, sample_weights)`.
- A generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> returning `(inputs, targets)`
or `(inputs, targets, sample_weights)`.
A more detailed description of unpacking behavior for iterator types
(Dataset, generator, Sequence) is given in the `Unpacking behavior
for iterator-like inputs` section of `Model.fit`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Target data. Like the input data `x`, it could be either Numpy
array(s) or TensorFlow tensor(s). It should be consistent with `x`
(you cannot have Numpy inputs and tensor targets, or inversely). If
`x` is a dataset, generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instance, `y`
should not be specified (since targets will be obtained from the
iterator/dataset).
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Integer or `None`. Number of samples per batch of
computation. If unspecified, `batch_size` will default to 32. Do not
specify the `batch_size` if your data is in the form of a dataset,
generators, or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instances (since they generate
batches).
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
0 or 1. Verbosity mode. 0 = silent, 1 = progress bar.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional Numpy array of weights for the test samples,
used for weighting the loss function. You can either pass a flat (1D)
Numpy array with the same length as the input samples
(1:1 mapping between weights and samples), or in the case of
temporal data, you can pass a 2D array with shape `(samples,
sequence_length)`, to apply a different weight to every timestep
of every sample. This argument is not supported when `x` is a
dataset, instead pass sample weights as the third element of `x`.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Integer or `None`. Total number of steps (batches of samples)
before declaring the evaluation round finished. Ignored with the
default value of `None`. If x is a <a href="../../tf/data.md"><code>tf.data</code></a> dataset and `steps` is
None, 'evaluate' will run until the dataset is exhausted. This
argument is not supported with array inputs.
</td>
</tr><tr>
<td>
`callbacks`
</td>
<td>
List of <a href="../../tf/keras/callbacks/Callback.md"><code>keras.callbacks.Callback</code></a> instances. List of
callbacks to apply during evaluation. See
[callbacks](/api_docs/python/tf/keras/callbacks).
</td>
</tr><tr>
<td>
`max_queue_size`
</td>
<td>
Integer. Used for generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a>
input only. Maximum size for the generator queue. If unspecified,
`max_queue_size` will default to 10.
</td>
</tr><tr>
<td>
`workers`
</td>
<td>
Integer. Used for generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> input
only. Maximum number of processes to spin up when using process-based
threading. If unspecified, `workers` will default to 1. If 0, will
execute the generator on the main thread.
</td>
</tr><tr>
<td>
`use_multiprocessing`
</td>
<td>
Boolean. Used for generator or
<a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> input only. If `True`, use process-based
threading. If unspecified, `use_multiprocessing` will default to
`False`. Note that because this implementation relies on
multiprocessing, you should not pass non-picklable arguments to the
generator as they can't be passed easily to children processes.
</td>
</tr><tr>
<td>
`return_dict`
</td>
<td>
If `True`, loss and metric results are returned as a dict,
with each key being the name of the metric. If `False`, they are
returned as a list.
</td>
</tr>
</table>


See the discussion of `Unpacking behavior for iterator-like inputs` for
<a href="../../tf/keras/Model.md#fit"><code>Model.fit</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Scalar test loss (if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.
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
If `model.evaluate` is wrapped in <a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
in case of invalid arguments.
</td>
</tr>
</table>



<h3 id="evaluate_generator"><code>evaluate_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1831-L1857">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>evaluate_generator(
    generator, steps=None, callbacks=None, max_queue_size=10, workers=1,
    use_multiprocessing=(False), verbose=0
)
</code></pre>

Evaluates the model on a data generator. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use Model.evaluate, which supports generators.

#### DEPRECATED:

<a href="../../tf/keras/Model.md#evaluate"><code>Model.evaluate</code></a> now supports generators, so there is no longer any need
to use this endpoint.


<h3 id="fit"><code>fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L824-L1146">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>fit(
    x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None,
    validation_split=0.0, validation_data=None, shuffle=(True), class_weight=None,
    sample_weight=None, initial_epoch=0, steps_per_epoch=None,
    validation_steps=None, validation_batch_size=None, validation_freq=1,
    max_queue_size=10, workers=1, use_multiprocessing=(False)
)
</code></pre>

Trains the model for a fixed number of epochs (iterations on a dataset).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
Input data. It could be:
- A Numpy array (or array-like), or a list of arrays
(in case the model has multiple inputs).
- A TensorFlow tensor, or a list of tensors
(in case the model has multiple inputs).
- A dict mapping input names to the corresponding array/tensors,
if the model has named inputs.
- A <a href="../../tf/data.md"><code>tf.data</code></a> dataset. Should return a tuple
of either `(inputs, targets)` or
`(inputs, targets, sample_weights)`.
- A generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> returning `(inputs, targets)`
or `(inputs, targets, sample_weights)`.
A more detailed description of unpacking behavior for iterator types
(Dataset, generator, Sequence) is given below.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Target data. Like the input data `x`,
it could be either Numpy array(s) or TensorFlow tensor(s).
It should be consistent with `x` (you cannot have Numpy inputs and
tensor targets, or inversely). If `x` is a dataset, generator,
or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instance, `y` should
not be specified (since targets will be obtained from `x`).
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Integer or `None`.
Number of samples per gradient update.
If unspecified, `batch_size` will default to 32.
Do not specify the `batch_size` if your data is in the
form of datasets, generators, or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instances
(since they generate batches).
</td>
</tr><tr>
<td>
`epochs`
</td>
<td>
Integer. Number of epochs to train the model.
An epoch is an iteration over the entire `x` and `y`
data provided.
Note that in conjunction with `initial_epoch`,
`epochs` is to be understood as "final epoch".
The model is not trained for a number of iterations
given by `epochs`, but merely until the epoch
of index `epochs` is reached.
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
0, 1, or 2. Verbosity mode.
0 = silent, 1 = progress bar, 2 = one line per epoch.
Note that the progress bar is not particularly useful when
logged to a file, so verbose=2 is recommended when not running
interactively (eg, in a production environment).
</td>
</tr><tr>
<td>
`callbacks`
</td>
<td>
List of <a href="../../tf/keras/callbacks/Callback.md"><code>keras.callbacks.Callback</code></a> instances.
List of callbacks to apply during training.
See <a href="../../tf/keras/callbacks.md"><code>tf.keras.callbacks</code></a>.
</td>
</tr><tr>
<td>
`validation_split`
</td>
<td>
Float between 0 and 1.
Fraction of the training data to be used as validation data.
The model will set apart this fraction of the training data,
will not train on it, and will evaluate
the loss and any model metrics
on this data at the end of each epoch.
The validation data is selected from the last samples
in the `x` and `y` data provided, before shuffling. This argument is
not supported when `x` is a dataset, generator or
<a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instance.
</td>
</tr><tr>
<td>
`validation_data`
</td>
<td>
Data on which to evaluate
the loss and any model metrics at the end of each epoch.
The model will not be trained on this data. Thus, note the fact
that the validation loss of data provided using `validation_split`
or `validation_data` is not affected by regularization layers like
noise and dropuout.
`validation_data` will override `validation_split`.
`validation_data` could be:
- tuple `(x_val, y_val)` of Numpy arrays or tensors
- tuple `(x_val, y_val, val_sample_weights)` of Numpy arrays
- dataset
For the first two cases, `batch_size` must be provided.
For the last case, `validation_steps` could be provided.
Note that `validation_data` does not support all the data types that
are supported in `x`, eg, dict, generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a>.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Boolean (whether to shuffle the training data
before each epoch) or str (for 'batch'). This argument is ignored
when `x` is a generator. 'batch' is a special option for dealing
with the limitations of HDF5 data; it shuffles in batch-sized
chunks. Has no effect when `steps_per_epoch` is not `None`.
</td>
</tr><tr>
<td>
`class_weight`
</td>
<td>
Optional dictionary mapping class indices (integers)
to a weight (float) value, used for weighting the loss function
(during training only).
This can be useful to tell the model to
"pay more attention" to samples from
an under-represented class.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional Numpy array of weights for
the training samples, used for weighting the loss function
(during training only). You can either pass a flat (1D)
Numpy array with the same length as the input samples
(1:1 mapping between weights and samples),
or in the case of temporal data,
you can pass a 2D array with shape
`(samples, sequence_length)`,
to apply a different weight to every timestep of every sample. This
argument is not supported when `x` is a dataset, generator, or
<a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instance, instead provide the sample_weights
as the third element of `x`.
</td>
</tr><tr>
<td>
`initial_epoch`
</td>
<td>
Integer.
Epoch at which to start training
(useful for resuming a previous training run).
</td>
</tr><tr>
<td>
`steps_per_epoch`
</td>
<td>
Integer or `None`.
Total number of steps (batches of samples)
before declaring one epoch finished and starting the
next epoch. When training with input tensors such as
TensorFlow data tensors, the default `None` is equal to
the number of samples in your dataset divided by
the batch size, or 1 if that cannot be determined. If x is a
<a href="../../tf/data.md"><code>tf.data</code></a> dataset, and 'steps_per_epoch'
is None, the epoch will run until the input dataset is exhausted.
When passing an infinitely repeating dataset, you must specify the
`steps_per_epoch` argument. This argument is not supported with
array inputs.
</td>
</tr><tr>
<td>
`validation_steps`
</td>
<td>
Only relevant if `validation_data` is provided and
is a <a href="../../tf/data.md"><code>tf.data</code></a> dataset. Total number of steps (batches of
samples) to draw before stopping when performing validation
at the end of every epoch. If 'validation_steps' is None, validation
will run until the `validation_data` dataset is exhausted. In the
case of an infinitely repeated dataset, it will run into an
infinite loop. If 'validation_steps' is specified and only part of
the dataset will be consumed, the evaluation will start from the
beginning of the dataset at each epoch. This ensures that the same
validation samples are used every time.
</td>
</tr><tr>
<td>
`validation_batch_size`
</td>
<td>
Integer or `None`.
Number of samples per validation batch.
If unspecified, will default to `batch_size`.
Do not specify the `validation_batch_size` if your data is in the
form of datasets, generators, or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instances
(since they generate batches).
</td>
</tr><tr>
<td>
`validation_freq`
</td>
<td>
Only relevant if validation data is provided. Integer
or `collections_abc.Container` instance (e.g. list, tuple, etc.).
If an integer, specifies how many training epochs to run before a
new validation run is performed, e.g. `validation_freq=2` runs
validation every 2 epochs. If a Container, specifies the epochs on
which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
validation at the end of the 1st, 2nd, and 10th epochs.
</td>
</tr><tr>
<td>
`max_queue_size`
</td>
<td>
Integer. Used for generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a>
input only. Maximum size for the generator queue.
If unspecified, `max_queue_size` will default to 10.
</td>
</tr><tr>
<td>
`workers`
</td>
<td>
Integer. Used for generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> input
only. Maximum number of processes to spin up
when using process-based threading. If unspecified, `workers`
will default to 1. If 0, will execute the generator on the main
thread.
</td>
</tr><tr>
<td>
`use_multiprocessing`
</td>
<td>
Boolean. Used for generator or
<a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> input only. If `True`, use process-based
threading. If unspecified, `use_multiprocessing` will default to
`False`. Note that because this implementation relies on
multiprocessing, you should not pass non-picklable arguments to
the generator as they can't be passed easily to children processes.
</td>
</tr>
</table>


Unpacking behavior for iterator-like inputs:
    A common pattern is to pass a tf.data.Dataset, generator, or
  tf.keras.utils.Sequence to the `x` argument of fit, which will in fact
  yield not only features (x) but optionally targets (y) and sample weights.
  Keras requires that the output of such iterator-likes be unambiguous. The
  iterator should return a tuple of length 1, 2, or 3, where the optional
  second and third elements will be used for y and sample_weight
  respectively. Any other type provided will be wrapped in a length one
  tuple, effectively treating everything as 'x'. When yielding dicts, they
  should still adhere to the top-level tuple structure.
  e.g. `({"x0": x0, "x1": x1}, y)`. Keras will not attempt to separate
  features, targets, and weights from the keys of a single dict.
    A notable unsupported data type is the namedtuple. The reason is that
  it behaves like both an ordered datatype (tuple) and a mapping
  datatype (dict). So given a namedtuple of the form:
      `namedtuple("example_tuple", ["y", "x"])`
  it is ambiguous whether to reverse the order of the elements when
  interpreting the value. Even worse is a tuple of the form:
      `namedtuple("other_tuple", ["x", "y", "z"])`
  where it is unclear if the tuple was intended to be unpacked into x, y,
  and sample_weight or passed through as a single element to `x`. As a
  result the data processing code will simply raise a ValueError if it
  encounters a namedtuple. (Along with instructions to remedy the issue.)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `History` object. Its `History.history` attribute is
a record of training loss values and metrics values
at successive epochs, as well as validation loss values
and validation metrics values (if applicable).
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
1. If the model was never compiled or,
2. If `model.fit` is  wrapped in <a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case of mismatch between the provided input data
and what the model expects.
</td>
</tr>
</table>



<h3 id="fit_generator"><code>fit_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1791-L1829">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>fit_generator(
    generator, steps_per_epoch=None, epochs=1, verbose=1, callbacks=None,
    validation_data=None, validation_steps=None, validation_freq=1,
    class_weight=None, max_queue_size=10, workers=1, use_multiprocessing=(False),
    shuffle=(True), initial_epoch=0
)
</code></pre>

Fits the model on data yielded batch-by-batch by a Python generator. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use Model.fit, which supports generators.

#### DEPRECATED:

<a href="../../tf/keras/Model.md#fit"><code>Model.fit</code></a> now supports generators, so there is no longer any need to use
this endpoint.


<h3 id="get_layer"><code>get_layer</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L2365-L2399">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_layer(
    name=None, index=None
)
</code></pre>

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence.
Indices are based on order of horizontal graph traversal (bottom-up).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`name`
</td>
<td>
String, name of layer.
</td>
</tr><tr>
<td>
`index`
</td>
<td>
Integer, index of layer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A layer instance.
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
In case of invalid layer name or index.
</td>
</tr>
</table>



<h3 id="load_weights"><code>load_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L2109-L2211">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>load_weights(
    filepath, by_name=(False), skip_mismatch=(False), options=None
)
</code></pre>

Loads all layer weights, either from a TensorFlow or an HDF5 weight file.

If `by_name` is False weights are loaded based on the network's
topology. This means the architecture should be the same as when the weights
were saved.  Note that layers that don't have weights are not taken into
account in the topological ordering, so adding or removing layers is fine as
long as they don't have weights.

If `by_name` is True, weights are loaded into layers only if they share the
same name. This is useful for fine-tuning or transfer-learning models where
some of the layers have changed.

Only topological loading (`by_name=False`) is supported when loading weights
from the TensorFlow format. Note that topological loading differs slightly
between TensorFlow and HDF5 formats for user-defined classes inheriting from
<a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a>: HDF5 loads based on a flattened list of weights, while the
TensorFlow format loads based on the object-local names of attributes to
which layers are assigned in the `Model`'s constructor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`filepath`
</td>
<td>
String, path to the weights file to load. For weight files in
TensorFlow format, this is the file prefix (the same as was passed
to `save_weights`).
</td>
</tr><tr>
<td>
`by_name`
</td>
<td>
Boolean, whether to load weights by name or by topological
order. Only topological loading is supported for weight files in
TensorFlow format.
</td>
</tr><tr>
<td>
`skip_mismatch`
</td>
<td>
Boolean, whether to skip loading of layers where there is
a mismatch in the number of weights, or a mismatch in the shape of
the weight (only valid when `by_name=True`).
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional <a href="../../tf/train/CheckpointOptions.md"><code>tf.train.CheckpointOptions</code></a> object that specifies
options for loading weights.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
When loading a weight file in TensorFlow format, returns the same status
object as <a href="../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore</code></a>. When graph building, restore
ops are run automatically as soon as the network is built (on first call
for user-defined classes inheriting from `Model`, immediately if it is
already built).

When loading weights in HDF5 format, returns `None`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
If h5py is not available and the weight file is in HDF5
format.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `skip_mismatch` is set to `True` when `by_name` is
`False`.
</td>
</tr>
</table>



<h3 id="make_predict_function"><code>make_predict_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1420-L1484">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_predict_function()
</code></pre>

Creates a function that executes one step of inference.

This method can be overridden to support custom inference logic.
This method is called by <a href="../../tf/keras/Model.md#predict"><code>Model.predict</code></a> and <a href="../../tf/keras/Model.md#predict_on_batch"><code>Model.predict_on_batch</code></a>.

Typically, this method directly controls <a href="../../tf/function.md"><code>tf.function</code></a> and
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> settings, and delegates the actual evaluation
logic to <a href="../../tf/keras/Model.md#predict_step"><code>Model.predict_step</code></a>.

This function is cached the first time <a href="../../tf/keras/Model.md#predict"><code>Model.predict</code></a> or
<a href="../../tf/keras/Model.md#predict_on_batch"><code>Model.predict_on_batch</code></a> is called. The cache is cleared whenever
<a href="../../tf/keras/Model.md#compile"><code>Model.compile</code></a> is called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Function. The function created by this method should accept a
<a href="../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>, and return the outputs of the `Model`.
</td>
</tr>

</table>



<h3 id="make_test_function"><code>make_test_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1182-L1240">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_test_function()
</code></pre>

Creates a function that executes one step of evaluation.

This method can be overridden to support custom evaluation logic.
This method is called by <a href="../../tf/keras/Model.md#evaluate"><code>Model.evaluate</code></a> and <a href="../../tf/keras/Model.md#test_on_batch"><code>Model.test_on_batch</code></a>.

Typically, this method directly controls <a href="../../tf/function.md"><code>tf.function</code></a> and
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> settings, and delegates the actual evaluation
logic to <a href="../../tf/keras/Model.md#test_step"><code>Model.test_step</code></a>.

This function is cached the first time <a href="../../tf/keras/Model.md#evaluate"><code>Model.evaluate</code></a> or
<a href="../../tf/keras/Model.md#test_on_batch"><code>Model.test_on_batch</code></a> is called. The cache is cleared whenever
<a href="../../tf/keras/Model.md#compile"><code>Model.compile</code></a> is called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Function. The function created by this method should accept a
<a href="../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>, and return a `dict` containing values that will
be passed to `tf.keras.Callbacks.on_test_batch_end`.
</td>
</tr>

</table>



<h3 id="make_train_function"><code>make_train_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L762-L822">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_train_function()
</code></pre>

Creates a function that executes one step of training.

This method can be overridden to support custom training logic.
This method is called by <a href="../../tf/keras/Model.md#fit"><code>Model.fit</code></a> and <a href="../../tf/keras/Model.md#train_on_batch"><code>Model.train_on_batch</code></a>.

Typically, this method directly controls <a href="../../tf/function.md"><code>tf.function</code></a> and
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> settings, and delegates the actual training
logic to <a href="../../tf/keras/Model.md#train_step"><code>Model.train_step</code></a>.

This function is cached the first time <a href="../../tf/keras/Model.md#fit"><code>Model.fit</code></a> or
<a href="../../tf/keras/Model.md#train_on_batch"><code>Model.train_on_batch</code></a> is called. The cache is cleared whenever
<a href="../../tf/keras/Model.md#compile"><code>Model.compile</code></a> is called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Function. The function created by this method should accept a
<a href="../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>, and return a `dict` containing values that will
be passed to `tf.keras.Callbacks.on_train_batch_end`, such as
`{'loss': 0.2, 'accuracy': 0.7}`.
</td>
</tr>

</table>



<h3 id="pop"><code>pop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/sequential.py#L236-L259">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>pop()
</code></pre>

Removes the last layer in the model.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if there are no layers in the model.
</td>
</tr>
</table>



<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1486-L1615">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict(
    x, batch_size=None, verbose=0, steps=None, callbacks=None, max_queue_size=10,
    workers=1, use_multiprocessing=(False)
)
</code></pre>

Generates output predictions for the input samples.

Computation is done in batches. This method is designed for performance in
large scale inputs. For small amount of inputs that fit in one batch,
directly using `__call__` is recommended for faster execution, e.g.,
`model(x)`, or `model(x, training=False)` if you have layers such as
<a href="../../tf/keras/layers/BatchNormalization.md"><code>tf.keras.layers.BatchNormalization</code></a> that behaves differently during
inference. Also, note the fact that test loss is not affected by
regularization layers like noise and dropout.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
Input samples. It could be:
- A Numpy array (or array-like), or a list of arrays
(in case the model has multiple inputs).
- A TensorFlow tensor, or a list of tensors
(in case the model has multiple inputs).
- A <a href="../../tf/data.md"><code>tf.data</code></a> dataset.
- A generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instance.
A more detailed description of unpacking behavior for iterator types
(Dataset, generator, Sequence) is given in the `Unpacking behavior
for iterator-like inputs` section of `Model.fit`.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Integer or `None`.
Number of samples per batch.
If unspecified, `batch_size` will default to 32.
Do not specify the `batch_size` if your data is in the
form of dataset, generators, or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> instances
(since they generate batches).
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
Verbosity mode, 0 or 1.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Total number of steps (batches of samples)
before declaring the prediction round finished.
Ignored with the default value of `None`. If x is a <a href="../../tf/data.md"><code>tf.data</code></a>
dataset and `steps` is None, `predict` will
run until the input dataset is exhausted.
</td>
</tr><tr>
<td>
`callbacks`
</td>
<td>
List of <a href="../../tf/keras/callbacks/Callback.md"><code>keras.callbacks.Callback</code></a> instances.
List of callbacks to apply during prediction.
See [callbacks](/api_docs/python/tf/keras/callbacks).
</td>
</tr><tr>
<td>
`max_queue_size`
</td>
<td>
Integer. Used for generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a>
input only. Maximum size for the generator queue.
If unspecified, `max_queue_size` will default to 10.
</td>
</tr><tr>
<td>
`workers`
</td>
<td>
Integer. Used for generator or <a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> input
only. Maximum number of processes to spin up when using
process-based threading. If unspecified, `workers` will default
to 1. If 0, will execute the generator on the main thread.
</td>
</tr><tr>
<td>
`use_multiprocessing`
</td>
<td>
Boolean. Used for generator or
<a href="../../tf/keras/utils/Sequence.md"><code>keras.utils.Sequence</code></a> input only. If `True`, use process-based
threading. If unspecified, `use_multiprocessing` will default to
`False`. Note that because this implementation relies on
multiprocessing, you should not pass non-picklable arguments to
the generator as they can't be passed easily to children processes.
</td>
</tr>
</table>


See the discussion of `Unpacking behavior for iterator-like inputs` for
<a href="../../tf/keras/Model.md#fit"><code>Model.fit</code></a>. Note that Model.predict uses the same interpretation rules as
<a href="../../tf/keras/Model.md#fit"><code>Model.fit</code></a> and <a href="../../tf/keras/Model.md#evaluate"><code>Model.evaluate</code></a>, so inputs must be unambiguous for all
three methods.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Numpy array(s) of predictions.
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
If `model.predict` is wrapped in <a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case of mismatch between the provided
input data and the model's expectations,
or in case a stateful model receives a number of samples
that is not a multiple of the batch size.
</td>
</tr>
</table>



<h3 id="predict_classes"><code>predict_classes</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/sequential.py#L431-L457">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict_classes(
    x, batch_size=32, verbose=0
)
</code></pre>

Generate class predictions for the input samples. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2021-01-01.
Instructions for updating:
Please use instead:* `np.argmax(model.predict(x), axis=-1)`,   if your model does multi-class classification   (e.g. if it uses a `softmax` last-layer activation).* `(model.predict(x) > 0.5).astype("int32")`,   if your model does binary classification   (e.g. if it uses a `sigmoid` last-layer activation).

The input samples are processed batch by batch.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
input data, as a Numpy array or list of Numpy arrays
(if the model has multiple inputs).
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
integer.
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
verbosity mode, 0 or 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A numpy array of class predictions.
</td>
</tr>

</table>



<h3 id="predict_generator"><code>predict_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1859-L1883">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict_generator(
    generator, steps=None, callbacks=None, max_queue_size=10, workers=1,
    use_multiprocessing=(False), verbose=0
)
</code></pre>

Generates predictions for the input samples from a data generator. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use Model.predict, which supports generators.

#### DEPRECATED:

<a href="../../tf/keras/Model.md#predict"><code>Model.predict</code></a> now supports generators, so there is no longer any need
to use this endpoint.


<h3 id="predict_on_batch"><code>predict_on_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1767-L1789">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict_on_batch(
    x
)
</code></pre>

Returns predictions for a single batch of samples.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
Input data. It could be: - A Numpy array (or array-like), or a list
of arrays (in case the model has multiple inputs). - A TensorFlow
tensor, or a list of tensors (in case the model has multiple inputs).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Numpy array(s) of predictions.
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
If `model.predict_on_batch` is wrapped in <a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case of mismatch between given number of inputs and
expectations of the model.
</td>
</tr>
</table>



<h3 id="predict_proba"><code>predict_proba</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/sequential.py#L408-L429">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict_proba(
    x, batch_size=32, verbose=0
)
</code></pre>

Generates class probability predictions for the input samples. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2021-01-01.
Instructions for updating:
Please use `model.predict()` instead.

The input samples are processed batch by batch.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
input data, as a Numpy array or list of Numpy arrays
(if the model has multiple inputs).
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
integer.
</td>
</tr><tr>
<td>
`verbose`
</td>
<td>
verbosity mode, 0 or 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A Numpy array of probability predictions.
</td>
</tr>

</table>



<h3 id="predict_step"><code>predict_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1396-L1418">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict_step(
    data
)
</code></pre>

The logic for one inference step.

This method can be overridden to support custom inference logic.
This method is called by <a href="../../tf/keras/Model.md#make_predict_function"><code>Model.make_predict_function</code></a>.

This method should contain the mathemetical logic for one step of inference.
This typically includes the forward pass.

Configuration details for *how* this logic is run (e.g. <a href="../../tf/function.md"><code>tf.function</code></a> and
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> settings), should be left to
<a href="../../tf/keras/Model.md#make_predict_function"><code>Model.make_predict_function</code></a>, which can also be overridden.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
A nested structure of `Tensor`s.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The result of one inference step, typically the output of calling the
`Model` on data.
</td>
</tr>

</table>



<h3 id="reset_metrics"><code>reset_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1617-L1637">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_metrics()
</code></pre>

Resets the state of all the metrics in the model.


#### Examples:



```
>>> inputs = tf.keras.layers.Input(shape=(3,))
>>> outputs = tf.keras.layers.Dense(2)(inputs)
>>> model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
>>> model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
```

```
>>> x = np.random.random((2, 3))
>>> y = np.random.randint(0, 2, (2, 2))
>>> _ = model.fit(x, y, verbose=0)
>>> assert all(float(m.result()) for m in model.metrics)
```

```
>>> model.reset_metrics()
>>> assert all(float(m.result()) == 0 for m in model.metrics)
```

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L2283-L2286">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>




<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1918-L1979">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    filepath, overwrite=(True), include_optimizer=(True), save_format=None,
    signatures=None, options=None
)
</code></pre>

Saves the model to Tensorflow SavedModel or a single HDF5 file.


#### The savefile includes:



- The model architecture, allowing to re-instantiate the model.
- The model weights.
- The state of the optimizer, allowing to resume training
    exactly where you left off.

This allows you to save the entirety of the state of a model
in a single file.

Saved models can be reinstantiated via <a href="../../tf/keras/models/load_model.md"><code>keras.models.load_model</code></a>.
The model returned by `load_model` is a compiled model ready to be used
(unless the saved model was never compiled in the first place).

Models built with the Sequential and Functional API can be saved to both the
HDF5 and SavedModel formats. Subclassed models can only be saved with the
SavedModel format.

Note that the model weights may have different scoped names after being
loaded. Scoped names include the model/layer names, such as
`"dense_1/kernel:0"`. It is recommended that you use the layer properties to
 access specific variables, e.g. `model.get_layer("dense_1").kernel`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`filepath`
</td>
<td>
String, PathLike, path to SavedModel or H5 file to save the
model.
</td>
</tr><tr>
<td>
`overwrite`
</td>
<td>
Whether to silently overwrite any existing file at the
target location, or provide the user with a manual prompt.
</td>
</tr><tr>
<td>
`include_optimizer`
</td>
<td>
If True, save optimizer's state together.
</td>
</tr><tr>
<td>
`save_format`
</td>
<td>
Either `'tf'` or `'h5'`, indicating whether to save the
model to Tensorflow SavedModel or HDF5. Defaults to 'tf' in TF 2.X,
and 'h5' in TF 1.X.
</td>
</tr><tr>
<td>
`signatures`
</td>
<td>
Signatures to save with the SavedModel. Applicable to the
'tf' format only. Please see the `signatures` argument in
<a href="../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> for details.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional <a href="../../tf/saved_model/SaveOptions.md"><code>tf.saved_model.SaveOptions</code></a> object that specifies
options for saving to SavedModel.
</td>
</tr>
</table>



#### Example:



```python
from keras.models import load_model

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')
```

<h3 id="save_weights"><code>save_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1981-L2107">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save_weights(
    filepath, overwrite=(True), save_format=None, options=None
)
</code></pre>

Saves all layer weights.

Either saves in HDF5 or in TensorFlow format based on the `save_format`
argument.

When saving in HDF5 format, the weight file has:
  - `layer_names` (attribute), a list of strings
      (ordered names of model layers).
  - For every layer, a `group` named `layer.name`
      - For every such layer group, a group attribute `weight_names`,
          a list of strings
          (ordered names of weights tensor of the layer).
      - For every weight in the layer, a dataset
          storing the weight value, named after the weight tensor.

When saving in TensorFlow format, all objects referenced by the network are
saved in the same format as <a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>, including any `Layer`
instances or `Optimizer` instances assigned to object attributes. For
networks constructed from inputs and outputs using `tf.keras.Model(inputs,
outputs)`, `Layer` instances used by the network are tracked/saved
automatically. For user-defined classes which inherit from <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a>,
`Layer` instances must be assigned to object attributes, typically in the
constructor. See the documentation of <a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> and
<a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a> for details.

While the formats are the same, do not mix `save_weights` and
<a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>. Checkpoints saved by <a href="../../tf/keras/Model.md#save_weights"><code>Model.save_weights</code></a> should be
loaded using <a href="../../tf/keras/Model.md#load_weights"><code>Model.load_weights</code></a>. Checkpoints saved using
<a href="../../tf/train/Checkpoint.md#save"><code>tf.train.Checkpoint.save</code></a> should be restored using the corresponding
<a href="../../tf/train/Checkpoint.md#restore"><code>tf.train.Checkpoint.restore</code></a>. Prefer <a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> over
`save_weights` for training checkpoints.

The TensorFlow format matches objects and variables by starting at a root
object, `self` for `save_weights`, and greedily matching attribute
names. For <a href="../../tf/keras/Model.md#save"><code>Model.save</code></a> this is the `Model`, and for <a href="../../tf/train/Checkpoint.md#save"><code>Checkpoint.save</code></a> this
is the `Checkpoint` even if the `Checkpoint` has a model attached. This
means saving a <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a> using `save_weights` and loading into a
<a href="../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a> with a `Model` attached (or vice versa) will not match
the `Model`'s variables. See the [guide to training
checkpoints](https://www.tensorflow.org/guide/checkpoint) for details
on the TensorFlow format.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`filepath`
</td>
<td>
String or PathLike, path to the file to save the weights to.
When saving in TensorFlow format, this is the prefix used for
checkpoint files (multiple files are generated). Note that the '.h5'
suffix causes weights to be saved in HDF5 format.
</td>
</tr><tr>
<td>
`overwrite`
</td>
<td>
Whether to silently overwrite any existing file at the
target location, or provide the user with a manual prompt.
</td>
</tr><tr>
<td>
`save_format`
</td>
<td>
Either 'tf' or 'h5'. A `filepath` ending in '.h5' or
'.keras' will default to HDF5 if `save_format` is `None`. Otherwise
`None` defaults to 'tf'.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional <a href="../../tf/train/CheckpointOptions.md"><code>tf.train.CheckpointOptions</code></a> object that specifies
options for saving weights.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
If h5py is not available when attempting to save in HDF5
format.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
For invalid/unknown format arguments.
</td>
</tr>
</table>



<h3 id="summary"><code>summary</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L2332-L2359">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>summary(
    line_length=None, positions=None, print_fn=None
)
</code></pre>

Prints a string summary of the network.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`line_length`
</td>
<td>
Total length of printed lines
(e.g. set this to adapt the display to different
terminal window sizes).
</td>
</tr><tr>
<td>
`positions`
</td>
<td>
Relative or absolute positions of log elements
in each line. If not provided,
defaults to `[.33, .55, .67, 1.]`.
</td>
</tr><tr>
<td>
`print_fn`
</td>
<td>
Print function to use. Defaults to `print`.
It will be called on each line of the summary.
You can set it to a custom function
in order to capture the string summary.
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
if `summary()` is called before the model is built.
</td>
</tr>
</table>



<h3 id="test_on_batch"><code>test_on_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1708-L1765">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>test_on_batch(
    x, y=None, sample_weight=None, reset_metrics=(True), return_dict=(False)
)
</code></pre>

Test the model on a single batch of samples.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
Input data. It could be: - A Numpy array (or array-like), or a list
of arrays (in case the model has multiple inputs). - A TensorFlow
tensor, or a list of tensors (in case the model has multiple inputs).
- A dict mapping input names to the corresponding array/tensors, if
the model has named inputs.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Target data. Like the input data `x`, it could be either Numpy
array(s) or TensorFlow tensor(s). It should be consistent with `x`
(you cannot have Numpy inputs and tensor targets, or inversely).
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional array of the same length as x, containing
weights to apply to the model's loss for each sample. In the case of
temporal data, you can pass a 2D array with shape (samples,
sequence_length), to apply a different weight to every timestep of
every sample.
</td>
</tr><tr>
<td>
`reset_metrics`
</td>
<td>
If `True`, the metrics returned will be only for this
batch. If `False`, the metrics will be statefully accumulated across
batches.
</td>
</tr><tr>
<td>
`return_dict`
</td>
<td>
If `True`, loss and metric results are returned as a dict,
with each key being the name of the metric. If `False`, they are
returned as a list.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Scalar test loss (if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.
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
If `model.test_on_batch` is wrapped in <a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case of invalid user-provided arguments.
</td>
</tr>
</table>



<h3 id="test_step"><code>test_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1148-L1180">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>test_step(
    data
)
</code></pre>

The logic for one evaluation step.

This method can be overridden to support custom evaluation logic.
This method is called by <a href="../../tf/keras/Model.md#make_test_function"><code>Model.make_test_function</code></a>.

This function should contain the mathemetical logic for one step of
evaluation.
This typically includes the forward pass, loss calculation, and metrics
updates.

Configuration details for *how* this logic is run (e.g. <a href="../../tf/function.md"><code>tf.function</code></a> and
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> settings), should be left to
<a href="../../tf/keras/Model.md#make_test_function"><code>Model.make_test_function</code></a>, which can also be overridden.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
A nested structure of `Tensor`s.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `dict` containing values that will be passed to
<a href="../../tf/keras/callbacks/CallbackList.md#on_train_batch_end"><code>tf.keras.callbacks.CallbackList.on_train_batch_end</code></a>. Typically, the
values of the `Model`'s metrics are returned.
</td>
</tr>

</table>



<h3 id="to_json"><code>to_json</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L2241-L2256">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_json(
    **kwargs
)
</code></pre>

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use
<a href="../../tf/keras/models/model_from_json.md"><code>keras.models.model_from_json(json_string, custom_objects={})</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
Additional keyword arguments
to be passed to `json.dumps()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A JSON string.
</td>
</tr>

</table>



<h3 id="to_yaml"><code>to_yaml</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L2258-L2281">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_yaml(
    **kwargs
)
</code></pre>

Returns a yaml string containing the network configuration.

To load a network from a yaml save file, use
<a href="../../tf/keras/models/model_from_yaml.md"><code>keras.models.model_from_yaml(yaml_string, custom_objects={})</code></a>.

`custom_objects` should be a dictionary mapping
the names of custom losses / layers / etc to the corresponding
functions / classes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
Additional keyword arguments
to be passed to `yaml.dump()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A YAML string.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
if yaml module is not found.
</td>
</tr>
</table>



<h3 id="train_on_batch"><code>train_on_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L1639-L1706">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>train_on_batch(
    x, y=None, sample_weight=None, class_weight=None, reset_metrics=(True),
    return_dict=(False)
)
</code></pre>

Runs a single gradient update on a single batch of data.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
Input data. It could be:
- A Numpy array (or array-like), or a list of arrays
(in case the model has multiple inputs).
- A TensorFlow tensor, or a list of tensors
(in case the model has multiple inputs).
- A dict mapping input names to the corresponding array/tensors,
if the model has named inputs.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Target data. Like the input data `x`, it could be either Numpy
array(s) or TensorFlow tensor(s). It should be consistent with `x`
(you cannot have Numpy inputs and tensor targets, or inversely).
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional array of the same length as x, containing
weights to apply to the model's loss for each sample. In the case of
temporal data, you can pass a 2D array with shape (samples,
sequence_length), to apply a different weight to every timestep of
every sample.
</td>
</tr><tr>
<td>
`class_weight`
</td>
<td>
Optional dictionary mapping class indices (integers) to a
weight (float) to apply to the model's loss for the samples from this
class during training. This can be useful to tell the model to "pay
more attention" to samples from an under-represented class.
</td>
</tr><tr>
<td>
`reset_metrics`
</td>
<td>
If `True`, the metrics returned will be only for this
batch. If `False`, the metrics will be statefully accumulated across
batches.
</td>
</tr><tr>
<td>
`return_dict`
</td>
<td>
If `True`, loss and metric results are returned as a dict,
with each key being the name of the metric. If `False`, they are
returned as a list.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Scalar training loss
(if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.
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
If `model.train_on_batch` is wrapped in <a href="../../tf/function.md"><code>tf.function</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
In case of invalid user-provided arguments.
</td>
</tr>
</table>



<h3 id="train_step"><code>train_step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/training.py#L716-L760">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>train_step(
    data
)
</code></pre>

The logic for one training step.

This method can be overridden to support custom training logic.
This method is called by <a href="../../tf/keras/Model.md#make_train_function"><code>Model.make_train_function</code></a>.

This method should contain the mathemetical logic for one step of training.
This typically includes the forward pass, loss calculation, backpropagation,
and metric updates.

Configuration details for *how* this logic is run (e.g. <a href="../../tf/function.md"><code>tf.function</code></a> and
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> settings), should be left to
<a href="../../tf/keras/Model.md#make_train_function"><code>Model.make_train_function</code></a>, which can also be overridden.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
A nested structure of `Tensor`s.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `dict` containing values that will be passed to
<a href="../../tf/keras/callbacks/CallbackList.md#on_train_batch_end"><code>tf.keras.callbacks.CallbackList.on_train_batch_end</code></a>. Typically, the
values of the `Model`'s metrics are returned. Example:
`{'loss': 0.2, 'accuracy': 0.7}`.
</td>
</tr>

</table>





