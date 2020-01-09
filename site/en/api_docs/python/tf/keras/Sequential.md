page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.Sequential


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/Sequential">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/sequential.py#L40-L382">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Sequential`

Linear stack of layers.

Inherits From: [`Model`](../../tf/keras/Model)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/Sequential"><code>tf.compat.v1.keras.Sequential</code></a>
* Class <a href="/api_docs/python/tf/keras/Sequential"><code>tf.compat.v1.keras.models.Sequential</code></a>
* Class <a href="/api_docs/python/tf/keras/Sequential"><code>tf.compat.v2.keras.Sequential</code></a>
* Class <a href="/api_docs/python/tf/keras/Sequential"><code>tf.compat.v2.keras.models.Sequential</code></a>
* Class <a href="/api_docs/python/tf/keras/Sequential"><code>tf.keras.models.Sequential</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`layers`</b>: list of layers to add to the model.


#### Example:



```python
# Optionally, the first layer can receive an `input_shape` argument:
model = Sequential()
model.add(Dense(32, input_shape=(500,)))
# Afterwards, we do automatic shape inference:
model.add(Dense(32))

# This is identical to the following:
model = Sequential()
model.add(Dense(32, input_dim=500))

# And to the following:
model = Sequential()
model.add(Dense(32, batch_input_shape=(None, 500)))

# Note that you can also omit the `input_shape` argument:
# In that case the model gets built the first time you call `fit` (or other
# training and evaluation methods).
model = Sequential()
model.add(Dense(32))
model.add(Dense(32))
model.compile(optimizer=optimizer, loss=loss)
# This builds the model for the first time:
model.fit(x, y, batch_size=32, epochs=10)

# Note that when using this delayed-build pattern (no input shape specified),
# the model doesn't have any weights until the first call
# to a training/evaluation method (since it isn't yet built):
model = Sequential()
model.add(Dense(32))
model.add(Dense(32))
model.weights  # returns []

# Whereas if you specify the input shape, the model gets built continuously
# as you are adding layers:
model = Sequential()
model.add(Dense(32, input_shape=(500,)))
model.add(Dense(32))
model.weights  # returns list of length 4

# When using the delayed-build pattern (no input shape specified), you can
# choose to manually build your model by calling `build(batch_input_shape)`:
model = Sequential()
model.add(Dense(32))
model.add(Dense(32))
model.build((None, 500))
model.weights  # returns list of length 4
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/sequential.py#L98-L113">View source</a>

``` python
__init__(
    layers=None,
    name=None
)
```






## Properties

<h3 id="layers"><code>layers</code></h3>




<h3 id="metrics_names"><code>metrics_names</code></h3>

Returns the model's display labels for all outputs.


<h3 id="run_eagerly"><code>run_eagerly</code></h3>

Settable attribute indicating whether the model should run eagerly.

Running eagerly means that your model will be run step by step,
like Python code. Your model might run slower, but it should become easier
for you to debug it by stepping into individual layer calls.

By default, we will attempt to compile your model to a static graph to
deliver the best execution performance.

#### Returns:

Boolean, whether the model should run eagerly.


<h3 id="sample_weights"><code>sample_weights</code></h3>




<h3 id="state_updates"><code>state_updates</code></h3>

Returns the `updates` from all layers that are stateful.

This is useful for separating training updates and
state updates, e.g. when we need to update a layer's internal state
during prediction.

#### Returns:

A list of update ops.


<h3 id="stateful"><code>stateful</code></h3>






## Methods

<h3 id="add"><code>add</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/sequential.py#L131-L215">View source</a>

``` python
add(layer)
```

Adds a layer instance on top of the layer stack.


#### Arguments:


* <b>`layer`</b>: layer instance.


#### Raises:


* <b>`TypeError`</b>: If `layer` is not a layer instance.
* <b>`ValueError`</b>: In case the `layer` argument does not
    know its input shape.
* <b>`ValueError`</b>: In case the `layer` argument has
    multiple output tensors, or is already connected
    somewhere else (forbidden in `Sequential` models).

<h3 id="compile"><code>compile</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L184-L400">View source</a>

``` python
compile(
    optimizer='rmsprop',
    loss=None,
    metrics=None,
    loss_weights=None,
    sample_weight_mode=None,
    weighted_metrics=None,
    target_tensors=None,
    distribute=None,
    **kwargs
)
```

Configures the model for training.


#### Arguments:


* <b>`optimizer`</b>: String (name of optimizer) or optimizer instance.
    See <a href="../../tf/keras/optimizers"><code>tf.keras.optimizers</code></a>.
* <b>`loss`</b>: String (name of objective function), objective function or
    `tf.losses.Loss` instance. See <a href="../../tf/losses"><code>tf.losses</code></a>. If the model has
    multiple outputs, you can use a different loss on each output by
    passing a dictionary or a list of losses. The loss value that will
    be minimized by the model will then be the sum of all individual
    losses.
* <b>`metrics`</b>: List of metrics to be evaluated by the model during training
    and testing. Typically you will use `metrics=['accuracy']`.
    To specify different metrics for different outputs of a
    multi-output model, you could also pass a dictionary, such as
    `metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}`.
    You can also pass a list (len = len(outputs)) of lists of metrics
    such as `metrics=[['accuracy'], ['accuracy', 'mse']]` or
    `metrics=['accuracy', ['accuracy', 'mse']]`.
* <b>`loss_weights`</b>: Optional list or dictionary specifying scalar
    coefficients (Python floats) to weight the loss contributions
    of different model outputs.
    The loss value that will be minimized by the model
    will then be the *weighted sum* of all individual losses,
    weighted by the `loss_weights` coefficients.
    If a list, it is expected to have a 1:1 mapping
    to the model's outputs. If a tensor, it is expected to map
    output names (strings) to scalar coefficients.
* <b>`sample_weight_mode`</b>: If you need to do timestep-wise
    sample weighting (2D weights), set this to `"temporal"`.
    `None` defaults to sample-wise weights (1D).
    If the model has multiple outputs, you can use a different
    `sample_weight_mode` on each output by passing a
    dictionary or a list of modes.
* <b>`weighted_metrics`</b>: List of metrics to be evaluated and weighted
    by sample_weight or class_weight during training and testing.
* <b>`target_tensors`</b>: By default, Keras will create placeholders for the
    model's target, which will be fed with the target data during
    training. If instead you would like to use your own
    target tensors (in turn, Keras will not expect external
    Numpy data for these targets at training time), you
    can specify them via the `target_tensors` argument. It can be
    a single tensor (for a single-output model), a list of tensors,
    or a dict mapping output names to target tensors.
* <b>`distribute`</b>: NOT SUPPORTED IN TF 2.0, please create and compile the
    model under distribution strategy scope instead of passing it to
    compile.
* <b>`**kwargs`</b>: Any additional arguments.


#### Raises:


* <b>`ValueError`</b>: In case of invalid arguments for
    `optimizer`, `loss`, `metrics` or `sample_weight_mode`.

<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L729-L832">View source</a>

``` python
evaluate(
    x=None,
    y=None,
    batch_size=None,
    verbose=1,
    sample_weight=None,
    steps=None,
    callbacks=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False
)
```

Returns the loss value & metrics values for the model in test mode.

Computation is done in batches.

#### Arguments:


* <b>`x`</b>: Input data. It could be:
  - A Numpy array (or array-like), or a list of arrays
    (in case the model has multiple inputs).
  - A TensorFlow tensor, or a list of tensors
    (in case the model has multiple inputs).
  - A dict mapping input names to the corresponding array/tensors,
    if the model has named inputs.
  - A <a href="../../tf/data"><code>tf.data</code></a> dataset.
  - A generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instance.
* <b>`y`</b>: Target data. Like the input data `x`,
  it could be either Numpy array(s) or TensorFlow tensor(s).
  It should be consistent with `x` (you cannot have Numpy inputs and
  tensor targets, or inversely).
  If `x` is a dataset, generator or
  <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instance, `y` should not be specified (since
  targets will be obtained from the iterator/dataset).
* <b>`batch_size`</b>: Integer or `None`.
    Number of samples per gradient update.
    If unspecified, `batch_size` will default to 32.
    Do not specify the `batch_size` is your data is in the
    form of symbolic tensors, dataset,
    generators, or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instances (since they generate
    batches).
* <b>`verbose`</b>: 0 or 1. Verbosity mode.
    0 = silent, 1 = progress bar.
* <b>`sample_weight`</b>: Optional Numpy array of weights for
    the test samples, used for weighting the loss function.
    You can either pass a flat (1D)
    Numpy array with the same length as the input samples
    (1:1 mapping between weights and samples),
    or in the case of temporal data,
    you can pass a 2D array with shape
    `(samples, sequence_length)`,
    to apply a different weight to every timestep of every sample.
    In this case you should make sure to specify
    `sample_weight_mode="temporal"` in `compile()`. This argument is not
    supported when `x` is a dataset, instead pass
    sample weights as the third element of `x`.
* <b>`steps`</b>: Integer or `None`.
    Total number of steps (batches of samples)
    before declaring the evaluation round finished.
    Ignored with the default value of `None`.
    If x is a <a href="../../tf/data"><code>tf.data</code></a> dataset and `steps` is
    None, 'evaluate' will run until the dataset is exhausted.
    This argument is not supported with array inputs.
* <b>`callbacks`</b>: List of <a href="../../tf/keras/callbacks/Callback"><code>keras.callbacks.Callback</code></a> instances.
    List of callbacks to apply during evaluation.
    See [callbacks](/api_docs/python/tf/keras/callbacks).
* <b>`max_queue_size`</b>: Integer. Used for generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a>
    input only. Maximum size for the generator queue.
    If unspecified, `max_queue_size` will default to 10.
* <b>`workers`</b>: Integer. Used for generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> input
    only. Maximum number of processes to spin up when using
    process-based threading. If unspecified, `workers` will default
    to 1. If 0, will execute the generator on the main thread.
* <b>`use_multiprocessing`</b>: Boolean. Used for generator or
    <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> input only. If `True`, use process-based
    threading. If unspecified, `use_multiprocessing` will default to
    `False`. Note that because this implementation relies on
    multiprocessing, you should not pass non-picklable arguments to
    the generator as they can't be passed easily to children processes.


#### Returns:

Scalar test loss (if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.



#### Raises:


* <b>`ValueError`</b>: in case of invalid arguments.

<h3 id="evaluate_generator"><code>evaluate_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L1298-L1363">View source</a>

``` python
evaluate_generator(
    generator,
    steps=None,
    callbacks=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    verbose=0
)
```

Evaluates the model on a data generator.

The generator should return the same kind of data
as accepted by `test_on_batch`.

#### Arguments:


* <b>`generator`</b>: Generator yielding tuples (inputs, targets)
    or (inputs, targets, sample_weights)
    or an instance of <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a>
    object in order to avoid duplicate data
    when using multiprocessing.
* <b>`steps`</b>: Total number of steps (batches of samples)
    to yield from `generator` before stopping.
    Optional for `Sequence`: if unspecified, will use
    the `len(generator)` as a number of steps.
* <b>`callbacks`</b>: List of <a href="../../tf/keras/callbacks/Callback"><code>keras.callbacks.Callback</code></a> instances.
    List of callbacks to apply during evaluation.
    See [callbacks](/api_docs/python/tf/keras/callbacks).
* <b>`max_queue_size`</b>: maximum size for the generator queue
* <b>`workers`</b>: Integer. Maximum number of processes to spin up
    when using process-based threading.
    If unspecified, `workers` will default to 1. If 0, will
    execute the generator on the main thread.
* <b>`use_multiprocessing`</b>: Boolean.
    If `True`, use process-based threading.
    If unspecified, `use_multiprocessing` will default to `False`.
    Note that because this implementation relies on multiprocessing,
    you should not pass non-picklable arguments to the generator
    as they can't be passed easily to children processes.
* <b>`verbose`</b>: Verbosity mode, 0 or 1.


#### Returns:

Scalar test loss (if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.



#### Raises:


* <b>`ValueError`</b>: in case of invalid arguments.


#### Raises:


* <b>`ValueError`</b>: In case the generator yields data in an invalid format.

<h3 id="fit"><code>fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L534-L727">View source</a>

``` python
fit(
    x=None,
    y=None,
    batch_size=None,
    epochs=1,
    verbose=1,
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0,
    steps_per_epoch=None,
    validation_steps=None,
    validation_freq=1,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    **kwargs
)
```

Trains the model for a fixed number of epochs (iterations on a dataset).


#### Arguments:


* <b>`x`</b>: Input data. It could be:
  - A Numpy array (or array-like), or a list of arrays
    (in case the model has multiple inputs).
  - A TensorFlow tensor, or a list of tensors
    (in case the model has multiple inputs).
  - A dict mapping input names to the corresponding array/tensors,
    if the model has named inputs.
  - A <a href="../../tf/data"><code>tf.data</code></a> dataset. Should return a tuple
    of either `(inputs, targets)` or
    `(inputs, targets, sample_weights)`.
  - A generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> returning `(inputs, targets)`
    or `(inputs, targets, sample weights)`.
* <b>`y`</b>: Target data. Like the input data `x`,
  it could be either Numpy array(s) or TensorFlow tensor(s).
  It should be consistent with `x` (you cannot have Numpy inputs and
  tensor targets, or inversely). If `x` is a dataset, generator,
  or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instance, `y` should
  not be specified (since targets will be obtained from `x`).
* <b>`batch_size`</b>: Integer or `None`.
    Number of samples per gradient update.
    If unspecified, `batch_size` will default to 32.
    Do not specify the `batch_size` if your data is in the
    form of symbolic tensors, datasets,
    generators, or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instances (since they generate
    batches).
* <b>`epochs`</b>: Integer. Number of epochs to train the model.
    An epoch is an iteration over the entire `x` and `y`
    data provided.
    Note that in conjunction with `initial_epoch`,
    `epochs` is to be understood as "final epoch".
    The model is not trained for a number of iterations
    given by `epochs`, but merely until the epoch
    of index `epochs` is reached.
* <b>`verbose`</b>: 0, 1, or 2. Verbosity mode.
    0 = silent, 1 = progress bar, 2 = one line per epoch.
    Note that the progress bar is not particularly useful when
    logged to a file, so verbose=2 is recommended when not running
    interactively (eg, in a production environment).
* <b>`callbacks`</b>: List of <a href="../../tf/keras/callbacks/Callback"><code>keras.callbacks.Callback</code></a> instances.
    List of callbacks to apply during training.
    See <a href="../../tf/keras/callbacks"><code>tf.keras.callbacks</code></a>.
* <b>`validation_split`</b>: Float between 0 and 1.
    Fraction of the training data to be used as validation data.
    The model will set apart this fraction of the training data,
    will not train on it, and will evaluate
    the loss and any model metrics
    on this data at the end of each epoch.
    The validation data is selected from the last samples
    in the `x` and `y` data provided, before shuffling. This argument is
    not supported when `x` is a dataset, generator or
   <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instance.
* <b>`validation_data`</b>: Data on which to evaluate
    the loss and any model metrics at the end of each epoch.
    The model will not be trained on this data.
    `validation_data` will override `validation_split`.
    `validation_data` could be:
      - tuple `(x_val, y_val)` of Numpy arrays or tensors
      - tuple `(x_val, y_val, val_sample_weights)` of Numpy arrays
      - dataset
    For the first two cases, `batch_size` must be provided.
    For the last case, `validation_steps` must be provided.
* <b>`shuffle`</b>: Boolean (whether to shuffle the training data
    before each epoch) or str (for 'batch').
    'batch' is a special option for dealing with the
    limitations of HDF5 data; it shuffles in batch-sized chunks.
    Has no effect when `steps_per_epoch` is not `None`.
* <b>`class_weight`</b>: Optional dictionary mapping class indices (integers)
    to a weight (float) value, used for weighting the loss function
    (during training only).
    This can be useful to tell the model to
    "pay more attention" to samples from
    an under-represented class.
* <b>`sample_weight`</b>: Optional Numpy array of weights for
    the training samples, used for weighting the loss function
    (during training only). You can either pass a flat (1D)
    Numpy array with the same length as the input samples
    (1:1 mapping between weights and samples),
    or in the case of temporal data,
    you can pass a 2D array with shape
    `(samples, sequence_length)`,
    to apply a different weight to every timestep of every sample.
    In this case you should make sure to specify
    `sample_weight_mode="temporal"` in `compile()`. This argument is not
    supported when `x` is a dataset, generator, or
   <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instance, instead provide the sample_weights
    as the third element of `x`.
* <b>`initial_epoch`</b>: Integer.
    Epoch at which to start training
    (useful for resuming a previous training run).
* <b>`steps_per_epoch`</b>: Integer or `None`.
    Total number of steps (batches of samples)
    before declaring one epoch finished and starting the
    next epoch. When training with input tensors such as
    TensorFlow data tensors, the default `None` is equal to
    the number of samples in your dataset divided by
    the batch size, or 1 if that cannot be determined. If x is a
    <a href="../../tf/data"><code>tf.data</code></a> dataset, and 'steps_per_epoch'
    is None, the epoch will run until the input dataset is exhausted.
    This argument is not supported with array inputs.
* <b>`validation_steps`</b>: Only relevant if `validation_data` is provided and
    is a <a href="../../tf/data"><code>tf.data</code></a> dataset. Total number of steps (batches of
    samples) to draw before stopping when performing validation
    at the end of every epoch. If validation_data is a <a href="../../tf/data"><code>tf.data</code></a> dataset
    and 'validation_steps' is None, validation
    will run until the `validation_data` dataset is exhausted.
* <b>`validation_freq`</b>: Only relevant if validation data is provided. Integer
    or `collections_abc.Container` instance (e.g. list, tuple, etc.).
    If an integer, specifies how many training epochs to run before a
    new validation run is performed, e.g. `validation_freq=2` runs
    validation every 2 epochs. If a Container, specifies the epochs on
    which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
    validation at the end of the 1st, 2nd, and 10th epochs.
* <b>`max_queue_size`</b>: Integer. Used for generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a>
    input only. Maximum size for the generator queue.
    If unspecified, `max_queue_size` will default to 10.
* <b>`workers`</b>: Integer. Used for generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> input
    only. Maximum number of processes to spin up
    when using process-based threading. If unspecified, `workers`
    will default to 1. If 0, will execute the generator on the main
    thread.
* <b>`use_multiprocessing`</b>: Boolean. Used for generator or
    <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> input only. If `True`, use process-based
    threading. If unspecified, `use_multiprocessing` will default to
    `False`. Note that because this implementation relies on
    multiprocessing, you should not pass non-picklable arguments to
    the generator as they can't be passed easily to children processes.
* <b>`**kwargs`</b>: Used for backwards compatibility.


#### Returns:

A `History` object. Its `History.history` attribute is
a record of training loss values and metrics values
at successive epochs, as well as validation loss values
and validation metrics values (if applicable).



#### Raises:


* <b>`RuntimeError`</b>: If the model was never compiled.
* <b>`ValueError`</b>: In case of mismatch between the provided input data
    and what the model expects.

<h3 id="fit_generator"><code>fit_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L1162-L1296">View source</a>

``` python
fit_generator(
    generator,
    steps_per_epoch=None,
    epochs=1,
    verbose=1,
    callbacks=None,
    validation_data=None,
    validation_steps=None,
    validation_freq=1,
    class_weight=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    shuffle=True,
    initial_epoch=0
)
```

Fits the model on data yielded batch-by-batch by a Python generator.

The generator is run in parallel to the model, for efficiency.
For instance, this allows you to do real-time data augmentation
on images on CPU in parallel to training your model on GPU.

The use of <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> guarantees the ordering
and guarantees the single use of every input per epoch when
using `use_multiprocessing=True`.

#### Arguments:


* <b>`generator`</b>: A generator or an instance of `Sequence`
  (<a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a>)
    object in order to avoid duplicate data
    when using multiprocessing.
    The output of the generator must be either
    - a tuple `(inputs, targets)`
    - a tuple `(inputs, targets, sample_weights)`.
    This tuple (a single output of the generator) makes a single batch.
    Therefore, all arrays in this tuple must have the same length (equal
    to the size of this batch). Different batches may have different
      sizes.
    For example, the last batch of the epoch is commonly smaller than
      the
    others, if the size of the dataset is not divisible by the batch
      size.
    The generator is expected to loop over its data
    indefinitely. An epoch finishes when `steps_per_epoch`
    batches have been seen by the model.
* <b>`steps_per_epoch`</b>: Total number of steps (batches of samples)
    to yield from `generator` before declaring one epoch
    finished and starting the next epoch. It should typically
    be equal to the number of samples of your dataset
    divided by the batch size.
    Optional for `Sequence`: if unspecified, will use
    the `len(generator)` as a number of steps.
* <b>`epochs`</b>: Integer, total number of iterations on the data.
* <b>`verbose`</b>: Verbosity mode, 0, 1, or 2.
* <b>`callbacks`</b>: List of callbacks to be called during training.
* <b>`validation_data`</b>: This can be either
    - a generator for the validation data
    - a tuple (inputs, targets)
    - a tuple (inputs, targets, sample_weights).
* <b>`validation_steps`</b>: Only relevant if `validation_data`
    is a generator. Total number of steps (batches of samples)
    to yield from `generator` before stopping.
    Optional for `Sequence`: if unspecified, will use
    the `len(validation_data)` as a number of steps.
* <b>`validation_freq`</b>: Only relevant if validation data is provided. Integer
    or `collections_abc.Container` instance (e.g. list, tuple, etc.).
    If an integer, specifies how many training epochs to run before a
    new validation run is performed, e.g. `validation_freq=2` runs
    validation every 2 epochs. If a Container, specifies the epochs on
    which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
    validation at the end of the 1st, 2nd, and 10th epochs.
* <b>`class_weight`</b>: Dictionary mapping class indices to a weight
    for the class.
* <b>`max_queue_size`</b>: Integer. Maximum size for the generator queue.
    If unspecified, `max_queue_size` will default to 10.
* <b>`workers`</b>: Integer. Maximum number of processes to spin up
    when using process-based threading.
    If unspecified, `workers` will default to 1. If 0, will
    execute the generator on the main thread.
* <b>`use_multiprocessing`</b>: Boolean.
    If `True`, use process-based threading.
    If unspecified, `use_multiprocessing` will default to `False`.
    Note that because this implementation relies on multiprocessing,
    you should not pass non-picklable arguments to the generator
    as they can't be passed easily to children processes.
* <b>`shuffle`</b>: Boolean. Whether to shuffle the order of the batches at
    the beginning of each epoch. Only used with instances
    of `Sequence` (<a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a>).
    Has no effect when `steps_per_epoch` is not `None`.
* <b>`initial_epoch`</b>: Epoch at which to start training
    (useful for resuming a previous training run)


#### Returns:

A `History` object.



#### Example:



```python
    def generate_arrays_from_file(path):
        while 1:
            f = open(path)
            for line in f:
                # create numpy arrays of input data
                # and labels, from each line in the file
                x1, x2, y = process_line(line)
                yield ({'input_1': x1, 'input_2': x2}, {'output': y})
            f.close()

    model.fit_generator(generate_arrays_from_file('/my_file.txt'),
                        steps_per_epoch=10000, epochs=10)
```
Raises:
    ValueError: In case the generator yields data in an invalid format.

<h3 id="get_layer"><code>get_layer</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L500-L531">View source</a>

``` python
get_layer(
    name=None,
    index=None
)
```

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence.
Indices are based on order of horizontal graph traversal (bottom-up).

#### Arguments:


* <b>`name`</b>: String, name of layer.
* <b>`index`</b>: Integer, index of layer.


#### Returns:

A layer instance.



#### Raises:


* <b>`ValueError`</b>: In case of invalid layer name or index.

<h3 id="load_weights"><code>load_weights</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L175-L182">View source</a>

``` python
load_weights(
    filepath,
    by_name=False
)
```

Loads all layer weights, either from a TensorFlow or an HDF5 file.


<h3 id="pop"><code>pop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/sequential.py#L217-L237">View source</a>

``` python
pop()
```

Removes the last layer in the model.


#### Raises:


* <b>`TypeError`</b>: if there are no layers in the model.

<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L834-L908">View source</a>

``` python
predict(
    x,
    batch_size=None,
    verbose=0,
    steps=None,
    callbacks=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False
)
```

Generates output predictions for the input samples.

Computation is done in batches.

#### Arguments:


* <b>`x`</b>: Input samples. It could be:
  - A Numpy array (or array-like), or a list of arrays
    (in case the model has multiple inputs).
  - A TensorFlow tensor, or a list of tensors
    (in case the model has multiple inputs).
  - A <a href="../../tf/data"><code>tf.data</code></a> dataset.
  - A generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instance.
* <b>`batch_size`</b>: Integer or `None`.
    Number of samples per gradient update.
    If unspecified, `batch_size` will default to 32.
    Do not specify the `batch_size` is your data is in the
    form of symbolic tensors, dataset,
    generators, or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> instances (since they generate
    batches).
* <b>`verbose`</b>: Verbosity mode, 0 or 1.
* <b>`steps`</b>: Total number of steps (batches of samples)
    before declaring the prediction round finished.
    Ignored with the default value of `None`. If x is a <a href="../../tf/data"><code>tf.data</code></a>
    dataset and `steps` is None, `predict` will
    run until the input dataset is exhausted.
* <b>`callbacks`</b>: List of <a href="../../tf/keras/callbacks/Callback"><code>keras.callbacks.Callback</code></a> instances.
    List of callbacks to apply during prediction.
    See [callbacks](/api_docs/python/tf/keras/callbacks).
* <b>`max_queue_size`</b>: Integer. Used for generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a>
    input only. Maximum size for the generator queue.
    If unspecified, `max_queue_size` will default to 10.
* <b>`workers`</b>: Integer. Used for generator or <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> input
    only. Maximum number of processes to spin up when using
    process-based threading. If unspecified, `workers` will default
    to 1. If 0, will execute the generator on the main thread.
* <b>`use_multiprocessing`</b>: Boolean. Used for generator or
    <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> input only. If `True`, use process-based
    threading. If unspecified, `use_multiprocessing` will default to
    `False`. Note that because this implementation relies on
    multiprocessing, you should not pass non-picklable arguments to
    the generator as they can't be passed easily to children processes.



#### Returns:

Numpy array(s) of predictions.



#### Raises:


* <b>`ValueError`</b>: In case of mismatch between the provided
    input data and the model's expectations,
    or in case a stateful model receives a number of samples
    that is not a multiple of the batch size.

<h3 id="predict_classes"><code>predict_classes</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/sequential.py#L312-L330">View source</a>

``` python
predict_classes(
    x,
    batch_size=32,
    verbose=0
)
```

Generate class predictions for the input samples.

The input samples are processed batch by batch.

#### Arguments:


* <b>`x`</b>: input data, as a Numpy array or list of Numpy arrays
    (if the model has multiple inputs).
* <b>`batch_size`</b>: integer.
* <b>`verbose`</b>: verbosity mode, 0 or 1.


#### Returns:

A numpy array of class predictions.


<h3 id="predict_generator"><code>predict_generator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L1365-L1420">View source</a>

``` python
predict_generator(
    generator,
    steps=None,
    callbacks=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    verbose=0
)
```

Generates predictions for the input samples from a data generator.

The generator should return the same kind of data as accepted by
`predict_on_batch`.

#### Arguments:


* <b>`generator`</b>: Generator yielding batches of input samples
    or an instance of <a href="../../tf/keras/utils/Sequence"><code>keras.utils.Sequence</code></a> object in order to
    avoid duplicate data when using multiprocessing.
* <b>`steps`</b>: Total number of steps (batches of samples)
    to yield from `generator` before stopping.
    Optional for `Sequence`: if unspecified, will use
    the `len(generator)` as a number of steps.
* <b>`callbacks`</b>: List of <a href="../../tf/keras/callbacks/Callback"><code>keras.callbacks.Callback</code></a> instances.
    List of callbacks to apply during prediction.
    See [callbacks](/api_docs/python/tf/keras/callbacks).
* <b>`max_queue_size`</b>: Maximum size for the generator queue.
* <b>`workers`</b>: Integer. Maximum number of processes to spin up
    when using process-based threading.
    If unspecified, `workers` will default to 1. If 0, will
    execute the generator on the main thread.
* <b>`use_multiprocessing`</b>: Boolean.
    If `True`, use process-based threading.
    If unspecified, `use_multiprocessing` will default to `False`.
    Note that because this implementation relies on multiprocessing,
    you should not pass non-picklable arguments to the generator
    as they can't be passed easily to children processes.
* <b>`verbose`</b>: verbosity mode, 0 or 1.


#### Returns:

Numpy array(s) of predictions.



#### Raises:


* <b>`ValueError`</b>: In case the generator yields data in an invalid format.

<h3 id="predict_on_batch"><code>predict_on_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L1114-L1160">View source</a>

``` python
predict_on_batch(x)
```

Returns predictions for a single batch of samples.


#### Arguments:


* <b>`x`</b>: Input data. It could be:
  - A Numpy array (or array-like), or a list of arrays
    (in case the model has multiple inputs).
  - A TensorFlow tensor, or a list of tensors
    (in case the model has multiple inputs).
  - A <a href="../../tf/data"><code>tf.data</code></a> dataset.


#### Returns:

Numpy array(s) of predictions.



#### Raises:


* <b>`ValueError`</b>: In case of mismatch between given number of inputs and
  expectations of the model.

<h3 id="predict_proba"><code>predict_proba</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/sequential.py#L290-L310">View source</a>

``` python
predict_proba(
    x,
    batch_size=32,
    verbose=0
)
```

Generates class probability predictions for the input samples.

The input samples are processed batch by batch.

#### Arguments:


* <b>`x`</b>: input data, as a Numpy array or list of Numpy arrays
    (if the model has multiple inputs).
* <b>`batch_size`</b>: integer.
* <b>`verbose`</b>: verbosity mode, 0 or 1.


#### Returns:

A Numpy array of probability predictions.


<h3 id="reset_metrics"><code>reset_metrics</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L910-L918">View source</a>

``` python
reset_metrics()
```

Resets the state of metrics.


<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L443-L446">View source</a>

``` python
reset_states()
```




<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L1122-L1171">View source</a>

``` python
save(
    filepath,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None
)
```

Saves the model to Tensorflow SavedModel or a single HDF5 file.


#### The savefile includes:

- The model architecture, allowing to re-instantiate the model.
- The model weights.
- The state of the optimizer, allowing to resume training
    exactly where you left off.


This allows you to save the entirety of the state of a model
in a single file.

Saved models can be reinstantiated via <a href="../../tf/keras/models/load_model"><code>keras.models.load_model</code></a>.
The model returned by `load_model`
is a compiled model ready to be used (unless the saved model
was never compiled in the first place).

#### Arguments:

filepath: String, path to SavedModel or H5 file to save the model.
overwrite: Whether to silently overwrite any existing file at the
    target location, or provide the user with a manual prompt.
include_optimizer: If True, save optimizer's state together.
save_format: Either 'tf' or 'h5', indicating whether to save the model
  to Tensorflow SavedModel or HDF5. The default is currently 'h5', but
  will switch to 'tf' in TensorFlow 2.0. The 'tf' option is currently
  disabled (use <a href="../../tf/keras/experimental/export_saved_model"><code>tf.keras.experimental.export_saved_model</code></a> instead).

* <b>`signatures`</b>: Signatures to save with the SavedModel. Applicable to the 'tf'
  format only. Please see the `signatures` argument in
  <a href="../../tf/saved_model/save"><code>tf.saved_model.save</code></a> for details.


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L1173-L1292">View source</a>

``` python
save_weights(
    filepath,
    overwrite=True,
    save_format=None
)
```

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
saved in the same format as <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>, including any `Layer`
instances or `Optimizer` instances assigned to object attributes. For
networks constructed from inputs and outputs using `tf.keras.Model(inputs,
outputs)`, `Layer` instances used by the network are tracked/saved
automatically. For user-defined classes which inherit from <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a>,
`Layer` instances must be assigned to object attributes, typically in the
constructor. See the documentation of <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a> and
<a href="../../tf/keras/Model"><code>tf.keras.Model</code></a> for details.

While the formats are the same, do not mix `save_weights` and
<a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>. Checkpoints saved by <a href="../../tf/keras/Model#save_weights"><code>Model.save_weights</code></a> should be
loaded using <a href="../../tf/keras/Model#load_weights"><code>Model.load_weights</code></a>. Checkpoints saved using
<a href="../../tf/train/Checkpoint#save"><code>tf.train.Checkpoint.save</code></a> should be restored using the corresponding
<a href="../../tf/train/Checkpoint#restore"><code>tf.train.Checkpoint.restore</code></a>. Prefer <a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a> over
`save_weights` for training checkpoints.

The TensorFlow format matches objects and variables by starting at a root
object, `self` for `save_weights`, and greedily matching attribute
names. For <a href="../../tf/keras/Model#save"><code>Model.save</code></a> this is the `Model`, and for <a href="../../tf/train/Checkpoint#save"><code>Checkpoint.save</code></a> this
is the `Checkpoint` even if the `Checkpoint` has a model attached. This
means saving a <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a> using `save_weights` and loading into a
<a href="../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a> with a `Model` attached (or vice versa) will not match
the `Model`'s variables. See the [guide to training
checkpoints](https://www.tensorflow.org/alpha/guide/checkpoints) for details
on the TensorFlow format.

#### Arguments:


* <b>`filepath`</b>: String, path to the file to save the weights to. When saving
    in TensorFlow format, this is the prefix used for checkpoint files
    (multiple files are generated). Note that the '.h5' suffix causes
    weights to be saved in HDF5 format.
* <b>`overwrite`</b>: Whether to silently overwrite any existing file at the
    target location, or provide the user with a manual prompt.
* <b>`save_format`</b>: Either 'tf' or 'h5'. A `filepath` ending in '.h5' or
    '.keras' will default to HDF5 if `save_format` is `None`. Otherwise
    `None` defaults to 'tf'.


#### Raises:


* <b>`ImportError`</b>: If h5py is not available when attempting to save in HDF5
    format.
* <b>`ValueError`</b>: For invalid/unknown format arguments.

<h3 id="summary"><code>summary</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L1434-L1461">View source</a>

``` python
summary(
    line_length=None,
    positions=None,
    print_fn=None
)
```

Prints a string summary of the network.


#### Arguments:


* <b>`line_length`</b>: Total length of printed lines
    (e.g. set this to adapt the display to different
    terminal window sizes).
* <b>`positions`</b>: Relative or absolute positions of log elements
    in each line. If not provided,
    defaults to `[.33, .55, .67, 1.]`.
* <b>`print_fn`</b>: Print function to use. Defaults to `print`.
    It will be called on each line of the summary.
    You can set it to a custom function
    in order to capture the string summary.


#### Raises:


* <b>`ValueError`</b>: if `summary()` is called before the model is built.

<h3 id="test_on_batch"><code>test_on_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L1026-L1112">View source</a>

``` python
test_on_batch(
    x,
    y=None,
    sample_weight=None,
    reset_metrics=True
)
```

Test the model on a single batch of samples.


#### Arguments:


* <b>`x`</b>: Input data. It could be:
  - A Numpy array (or array-like), or a list of arrays
    (in case the model has multiple inputs).
  - A TensorFlow tensor, or a list of tensors
    (in case the model has multiple inputs).
  - A dict mapping input names to the corresponding array/tensors,
    if the model has named inputs.
  - A <a href="../../tf/data"><code>tf.data</code></a> dataset.
* <b>`y`</b>: Target data. Like the input data `x`,
  it could be either Numpy array(s) or TensorFlow tensor(s).
  It should be consistent with `x` (you cannot have Numpy inputs and
  tensor targets, or inversely). If `x` is a dataset `y` should
  not be specified (since targets will be obtained from the iterator).
* <b>`sample_weight`</b>: Optional array of the same length as x, containing
    weights to apply to the model's loss for each sample.
    In the case of temporal data, you can pass a 2D array
    with shape (samples, sequence_length),
    to apply a different weight to every timestep of every sample.
    In this case you should make sure to specify
    sample_weight_mode="temporal" in compile(). This argument is not
    supported when `x` is a dataset.
* <b>`reset_metrics`</b>: If `True`, the metrics returned will be only for this
  batch. If `False`, the metrics will be statefully accumulated across
  batches.


#### Returns:

Scalar test loss (if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.



#### Raises:


* <b>`ValueError`</b>: In case of invalid user-provided arguments.

<h3 id="to_json"><code>to_json</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L1392-L1407">View source</a>

``` python
to_json(**kwargs)
```

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use
<a href="../../tf/keras/models/model_from_json"><code>keras.models.model_from_json(json_string, custom_objects={})</code></a>.

#### Arguments:


* <b>`**kwargs`</b>: Additional keyword arguments
    to be passed to `json.dumps()`.


#### Returns:

A JSON string.


<h3 id="to_yaml"><code>to_yaml</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/network.py#L1409-L1432">View source</a>

``` python
to_yaml(**kwargs)
```

Returns a yaml string containing the network configuration.

To load a network from a yaml save file, use
<a href="../../tf/keras/models/model_from_yaml"><code>keras.models.model_from_yaml(yaml_string, custom_objects={})</code></a>.

`custom_objects` should be a dictionary mapping
the names of custom losses / layers / etc to the corresponding
functions / classes.

#### Arguments:


* <b>`**kwargs`</b>: Additional keyword arguments
    to be passed to `yaml.dump()`.


#### Returns:

A YAML string.



#### Raises:


* <b>`ImportError`</b>: if yaml module is not found.

<h3 id="train_on_batch"><code>train_on_batch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/engine/training.py#L920-L1024">View source</a>

``` python
train_on_batch(
    x,
    y=None,
    sample_weight=None,
    class_weight=None,
    reset_metrics=True
)
```

Runs a single gradient update on a single batch of data.


#### Arguments:


* <b>`x`</b>: Input data. It could be:
  - A Numpy array (or array-like), or a list of arrays
      (in case the model has multiple inputs).
  - A TensorFlow tensor, or a list of tensors
      (in case the model has multiple inputs).
  - A dict mapping input names to the corresponding array/tensors,
      if the model has named inputs.
  - A <a href="../../tf/data"><code>tf.data</code></a> dataset.
* <b>`y`</b>: Target data. Like the input data `x`, it could be either Numpy
  array(s) or TensorFlow tensor(s). It should be consistent with `x`
  (you cannot have Numpy inputs and tensor targets, or inversely). If
  `x` is a dataset, `y` should not be specified
  (since targets will be obtained from the iterator).
* <b>`sample_weight`</b>: Optional array of the same length as x, containing
  weights to apply to the model's loss for each sample. In the case of
  temporal data, you can pass a 2D array with shape (samples,
  sequence_length), to apply a different weight to every timestep of
  every sample. In this case you should make sure to specify
  sample_weight_mode="temporal" in compile(). This argument is not
  supported when `x` is a dataset.
* <b>`class_weight`</b>: Optional dictionary mapping class indices (integers) to a
  weight (float) to apply to the model's loss for the samples from this
  class during training. This can be useful to tell the model to "pay
  more attention" to samples from an under-represented class.
* <b>`reset_metrics`</b>: If `True`, the metrics returned will be only for this
  batch. If `False`, the metrics will be statefully accumulated across
  batches.


#### Returns:

Scalar training loss
(if the model has a single output and no metrics)
or list of scalars (if the model has multiple outputs
and/or metrics). The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.



#### Raises:


* <b>`ValueError`</b>: In case of invalid user-provided arguments.
