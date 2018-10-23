

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.Sequential

## Class `Sequential`

Inherits From: [`Model`](../../tf/keras/Model)

### Aliases:

* Class `tf.keras.Sequential`
* Class `tf.keras.models.Sequential`



Defined in [`tensorflow/python/keras/_impl/keras/engine/sequential.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/engine/sequential.py).

Linear stack of layers.

#### Arguments:

* <b>`layers`</b>: list of layers to add to the model.

# Note
    The first layer passed to a Sequential model
    should have a defined input shape. What that
    means is that it should have received an `input_shape`
    or `batch_input_shape` argument,
    or for some type of layers (recurrent, Dense...)
    an `input_dim` argument.

Example:

    ```python
        model = Sequential()
        # first layer must have a defined input shape
        model.add(Dense(32, input_dim=500))
        # afterwards, Keras does automatic shape inference
        model.add(Dense(32))

        # also possible (equivalent to the above):
        model = Sequential()
        model.add(Dense(32, input_shape=(500,)))
        model.add(Dense(32))

        # also possible (equivalent to the above):
        model = Sequential()
        # here the batch dimension is None,
        # which means any batch size will be accepted by the model.
        model.add(Dense(32, batch_input_shape=(None, 500)))
        model.add(Dense(32))
    ```

## Properties

<h3 id="activity_regularizer"><code>activity_regularizer</code></h3>

Optional regularizer function for the output of this layer.

<h3 id="dtype"><code>dtype</code></h3>



<h3 id="graph"><code>graph</code></h3>



<h3 id="input"><code>input</code></h3>

Retrieves the input tensor(s) of a layer.

Only applicable if the layer has exactly one input,
i.e. if it is connected to one incoming layer.

#### Returns:

Input tensor or list of input tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to
    more than one incoming layers.


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.
* <b>`AttributeError`</b>: If no inbound nodes are found.

<h3 id="input_mask"><code>input_mask</code></h3>

Retrieves the input mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

Input mask tensor (potentially None) or list of input
mask tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to
    more than one incoming layers.

<h3 id="input_shape"><code>input_shape</code></h3>

Retrieves the input shape(s) of a layer.

Only applicable if the layer has exactly one input,
i.e. if it is connected to one incoming layer, or if all inputs
have the same shape.

#### Returns:

Input shape, as an integer shape tuple
(or list of shape tuples, one tuple per input tensor).


#### Raises:

* <b>`AttributeError`</b>: if the layer has no defined input_shape.
* <b>`RuntimeError`</b>: if called in Eager mode.

<h3 id="input_spec"><code>input_spec</code></h3>

Gets the network's input specs.

#### Returns:

A list of `InputSpec` instances (one per input to the model)
    or a single instance if the model has only one input.

<h3 id="layers"><code>layers</code></h3>



<h3 id="losses"><code>losses</code></h3>

Retrieve the network's losses.

Will only include losses that are either
unconditional, or conditional on inputs to this model
(e.g. will not include losses that depend on tensors
that aren't inputs to this model).

#### Returns:

A list of loss tensors.

<h3 id="name"><code>name</code></h3>



<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="output"><code>output</code></h3>

Retrieves the output tensor(s) of a layer.

Only applicable if the layer has exactly one output,
i.e. if it is connected to one incoming layer.

#### Returns:

Output tensor or list of output tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to more than one incoming
    layers.
* <b>`RuntimeError`</b>: if called in Eager mode.

<h3 id="output_mask"><code>output_mask</code></h3>

Retrieves the output mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

Output mask tensor (potentially None) or list of output
mask tensors.


#### Raises:

* <b>`AttributeError`</b>: if the layer is connected to
    more than one incoming layers.

<h3 id="output_shape"><code>output_shape</code></h3>

Retrieves the output shape(s) of a layer.

Only applicable if the layer has one output,
or if all outputs have the same shape.

#### Returns:

Output shape, as an integer shape tuple
(or list of shape tuples, one tuple per output tensor).


#### Raises:

* <b>`AttributeError`</b>: if the layer has no defined output shape.
* <b>`RuntimeError`</b>: if called in Eager mode.

<h3 id="regularizers"><code>regularizers</code></h3>



<h3 id="scope_name"><code>scope_name</code></h3>



<h3 id="state_updates"><code>state_updates</code></h3>

Returns the `updates` from all layers that are stateful.

This is useful for separating training updates and
state updates, e.g. when we need to update a layer's internal state
during prediction.

#### Returns:

A list of update ops.

<h3 id="stateful"><code>stateful</code></h3>



<h3 id="trainable"><code>trainable</code></h3>



<h3 id="trainable_variables"><code>trainable_variables</code></h3>



<h3 id="trainable_weights"><code>trainable_weights</code></h3>



<h3 id="updates"><code>updates</code></h3>

Retrieve the network's updates.

Will only include updates that are either
unconditional, or conditional on inputs to this model
(e.g. will not include updates that were created by layers of this model
outside of the model).

Effectively, `network.updates` behaves like `layer.updates`.

Concrete example:

```python
  bn = keras.layers.BatchNormalization()
  x1 = keras.layers.Input(shape=(10,))
  _ = bn(x1)  # This creates 2 updates.

  x2 = keras.layers.Input(shape=(10,))
  y2 = bn(x2)  # This creates 2 more updates.

  # The BN layer has now 4 updates.
  self.assertEqual(len(bn.updates), 4)

  # Let's create a model from x2 to y2.
  model = keras.models.Model(x2, y2)

  # The model does not list all updates from its underlying layers,
  # but only the updates that are relevant to it. Updates created by layers
  # outside of the model are discarded.
  self.assertEqual(len(model.updates), 2)

  # If you keep calling the model, you append to its updates, just like
  # what happens for a layer.
  x3 = keras.layers.Input(shape=(10,))
  y3 = model(x3)
  self.assertEqual(len(model.updates), 4)

  # But if you call the inner BN layer independently, you don't affect
  # the model's updates.
  x4 = keras.layers.Input(shape=(10,))
  _ = bn(x4)
  self.assertEqual(len(model.updates), 4)
```

#### Returns:

A list of update ops.

<h3 id="uses_learning_phase"><code>uses_learning_phase</code></h3>



<h3 id="variables"><code>variables</code></h3>

Returns the list of all layer variables/weights.

#### Returns:

A list of variables.

<h3 id="weights"><code>weights</code></h3>

Returns the list of all layer variables/weights.

#### Returns:

A list of variables.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layers=None,
    name=None
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    **kwargs
)
```

Wrapper around self.call(), for handling internal references.

If a Keras tensor is passed:
    - We call self._add_inbound_node().
    - If necessary, we `build` the layer to match
        the shape of the input(s).
    - We update the _keras_history of the output tensor(s)
        with the current layer.
        This is done as part of _add_inbound_node().

#### Arguments:

* <b>`inputs`</b>: Can be a tensor or list/tuple of tensors.
* <b>`**kwargs`</b>: Additional keyword arguments to be passed to `call()`.


#### Returns:

Output of the layer's `call` method.


#### Raises:

* <b>`ValueError`</b>: in case the layer is missing shape information
        for its `build` call.

<h3 id="__deepcopy__"><code>__deepcopy__</code></h3>

``` python
__deepcopy__(memo)
```



<h3 id="__setattr__"><code>__setattr__</code></h3>

``` python
__setattr__(
    name,
    value
)
```



<h3 id="add"><code>add</code></h3>

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

<h3 id="add_loss"><code>add_loss</code></h3>

``` python
add_loss(
    *args,
    **kwargs
)
```



<h3 id="add_update"><code>add_update</code></h3>

``` python
add_update(
    updates,
    inputs=None
)
```

Add update op(s), potentially dependent on layer inputs.

Weight updates (for instance, the updates of the moving mean and variance
in a BatchNormalization layer) may be dependent on the inputs passed
when calling a layer. Hence, when reusing the same layer on
different inputs `a` and `b`, some entries in `layer.updates` may be
dependent on `a` and some on `b`. This method automatically keeps track
of dependencies.

The `get_updates_for` method allows to retrieve the updates relevant to a
specific set of inputs.

This call is ignored in Eager mode.

#### Arguments:

* <b>`updates`</b>: Update op, or list/tuple of update ops.
* <b>`inputs`</b>: If anything other than None is passed, it signals the updates
    are conditional on some of the layer's inputs,
    and thus they should only be run where these inputs are available.
    This is the case for BatchNormalization updates, for instance.
    If None, the updates will be taken into account unconditionally,
    and you are responsible for making sure that any dependency they might
    have is available at runtime.
    A step counter might fall into this category.

<h3 id="add_variable"><code>add_variable</code></h3>

``` python
add_variable(
    name,
    shape,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True,
    constraint=None
)
```



<h3 id="add_weight"><code>add_weight</code></h3>

``` python
add_weight(
    name,
    shape,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True,
    constraint=None
)
```

Adds a weight variable to the layer.

#### Arguments:

* <b>`name`</b>: String, the name for the weight variable.
* <b>`shape`</b>: The shape tuple of the weight.
* <b>`dtype`</b>: The dtype of the weight.
* <b>`initializer`</b>: An Initializer instance (callable).
* <b>`regularizer`</b>: An optional Regularizer instance.
* <b>`trainable`</b>: A boolean, whether the weight should
        be trained via backprop or not (assuming
        that the layer itself is also trainable).
* <b>`constraint`</b>: An optional Constraint instance.


#### Returns:

The created weight variable.

<h3 id="apply"><code>apply</code></h3>

``` python
apply(
    inputs,
    *args,
    **kwargs
)
```

Apply the layer on a input.

This simply wraps `self.__call__`.

#### Arguments:

* <b>`inputs`</b>: Input tensor(s).
* <b>`*args`</b>: additional positional arguments to be passed to `self.call`.
* <b>`**kwargs`</b>: additional keyword arguments to be passed to `self.call`.


#### Returns:

Output tensor(s).

<h3 id="build"><code>build</code></h3>

``` python
build(input_shape=None)
```



<h3 id="call"><code>call</code></h3>

``` python
call(
    inputs,
    **kwargs
)
```



<h3 id="compile"><code>compile</code></h3>

``` python
compile(
    optimizer,
    loss,
    metrics=None,
    sample_weight_mode=None,
    weighted_metrics=None,
    target_tensors=None,
    **kwargs
)
```

Configures the model for training.

#### Arguments:

* <b>`optimizer`</b>: String (name of optimizer) or optimizer object.
        See [optimizers](/optimizers).
* <b>`loss`</b>: String (name of objective function) or objective function.
        See [losses](/losses).
        If the model has multiple outputs, you can use a different loss
        on each output by passing a dictionary or a list of losses.
        The loss value that will be minimized by the model
        will then be the sum of all individual losses.
* <b>`metrics`</b>: List of metrics to be evaluated by the model
        during training and testing.
        Typically you will use `metrics=['accuracy']`.
        To specify different metrics for different outputs of a
        multi-output model, you could also pass a dictionary,
        such as `metrics={'output_a': 'accuracy'}`.
* <b>`sample_weight_mode`</b>: If you need to do timestep-wise
        sample weighting (2D weights), set this to `"temporal"`.
        `None` defaults to sample-wise weights (1D).
        If the model has multiple outputs, you can use a different
        `sample_weight_mode` on each output by passing a
        dictionary or a list of modes.
* <b>`weighted_metrics`</b>: list of metrics to be evaluated and weighted
         by `sample_weight` or `class_weight` during training and testing.
* <b>`target_tensors`</b>: By default, Keras will create a placeholder for the
        model's target, which will be fed with the target data during
        training. If instead you would like to use your own
        target tensor (in turn, Keras will not expect external
        Numpy data for these targets at training time), you
        can specify them via the `target_tensors` argument.
        It should be a single tensor
        (for a single-output `Sequential` model).
* <b>`**kwargs`</b>: These arguments are passed into `tf.Session.run`.

Example:

    ```python
        model = Sequential()
        model.add(Dense(32, input_shape=(500,)))
        model.add(Dense(10, activation='softmax'))
        model.compile(optimizer='rmsprop',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
    ```

<h3 id="compute_mask"><code>compute_mask</code></h3>

``` python
compute_mask(
    inputs,
    mask
)
```



<h3 id="compute_output_shape"><code>compute_output_shape</code></h3>

``` python
compute_output_shape(input_shape)
```



<h3 id="count_params"><code>count_params</code></h3>

``` python
count_params()
```

Count the total number of scalars composing the weights.

#### Returns:

An integer count.


#### Raises:

* <b>`ValueError`</b>: if the layer isn't yet built
      (in which case its weights aren't yet defined).

<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(
    x,
    y,
    batch_size=32,
    verbose=1,
    sample_weight=None
)
```

Computes the loss on some input data, batch by batch.

#### Arguments:

* <b>`x`</b>: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
* <b>`y`</b>: labels, as a Numpy array.
* <b>`batch_size`</b>: integer. Number of samples per gradient update.
* <b>`verbose`</b>: verbosity mode, 0 or 1.
* <b>`sample_weight`</b>: sample weights, as a Numpy array.


#### Returns:

Scalar test loss (if the model has no metrics)
or list of scalars (if the model computes other metrics).
The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.


#### Raises:

* <b>`RuntimeError`</b>: if the model was never compiled.

<h3 id="evaluate_generator"><code>evaluate_generator</code></h3>

``` python
evaluate_generator(
    generator,
    steps=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    **kwargs
)
```

Evaluates the model on a data generator.

The generator should return the same kind of data
as accepted by `test_on_batch`.

#### Arguments:

* <b>`generator`</b>: Generator yielding tuples (inputs, targets)
        or (inputs, targets, sample_weights)
* <b>`steps`</b>: Total number of steps (batches of samples)
        to yield from `generator` before stopping.
        Optional for `Sequence`: if unspecified, will use
        the `len(generator)` as a number of steps.
* <b>`max_queue_size`</b>: maximum size for the generator queue
* <b>`workers`</b>: maximum number of processes to spin up
* <b>`use_multiprocessing`</b>: if True, use process based threading.
        Note that because this implementation
        relies on multiprocessing, you should not pass
        non picklable arguments to the generator
        as they can't be passed easily to children processes.
* <b>`**kwargs`</b>: support for legacy arguments.


#### Returns:

Scalar test loss (if the model has no metrics)
or list of scalars (if the model computes other metrics).
The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.


#### Raises:

* <b>`RuntimeError`</b>: if the model was never compiled.
* <b>`ValueError`</b>: In case the generator yields
        data in an invalid format.

<h3 id="fit"><code>fit</code></h3>

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
    **kwargs
)
```

Trains the model for a fixed number of epochs.

#### Arguments:

* <b>`x`</b>: Numpy array of training data.
        If the input layer in the model is named, you can also pass a
        dictionary mapping the input name to a Numpy array.
        `x` can be `None` (default) if feeding from
        TensorFlow data tensors.
* <b>`y`</b>: Numpy array of target (label) data.
        If the output layer in the model is named, you can also pass a
        dictionary mapping the output name to a Numpy array.
        `y` can be `None` (default) if feeding from
        TensorFlow data tensors.
* <b>`batch_size`</b>: Integer or `None`.
        Number of samples per gradient update.
        If unspecified, it will default to 32.
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
* <b>`callbacks`</b>: List of `keras.callbacks.Callback` instances.
        List of callbacks to apply during training.
        See [callbacks](/callbacks).
* <b>`validation_split`</b>: Float between 0 and 1:
        Fraction of the training data to be used as validation data.
        The model will set apart this fraction of the training data,
        will not train on it, and will evaluate
        the loss and any model metrics
        on this data at the end of each epoch.
        The validation data is selected from the last samples
        in the `x` and `y` data provided, before shuffling.
* <b>`validation_data`</b>: tuple `(x_val, y_val)` or tuple
        `(x_val, y_val, val_sample_weights)` on which to evaluate
        the loss and any model metrics at the end of each epoch.
        The model will not be trained on this data.
        This will override `validation_split`.
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
        `sample_weight_mode="temporal"` in `compile()`.
* <b>`initial_epoch`</b>: Epoch at which to start training
        (useful for resuming a previous training run).
* <b>`steps_per_epoch`</b>: Total number of steps (batches of samples)
        before declaring one epoch finished and starting the
        next epoch. When training with input tensors such as
        TensorFlow data tensors, the default `None` is equal to
        the number of unique samples in your dataset divided by
        the batch size, or 1 if that cannot be determined.
* <b>`validation_steps`</b>: Only relevant if `steps_per_epoch`
        is specified. Total number of steps (batches of samples)
        to validate before stopping.
* <b>`**kwargs`</b>: Used for backwards compatibility support.


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

``` python
fit_generator(
    generator,
    steps_per_epoch=None,
    epochs=1,
    verbose=1,
    callbacks=None,
    validation_data=None,
    validation_steps=None,
    class_weight=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    shuffle=True,
    initial_epoch=0,
    **kwargs
)
```

Fits the model on data generated batch-by-batch by a Python generator.

The generator is run in parallel to the model, for efficiency.
For instance, this allows you to do real-time data augmentation
on images on CPU in parallel to training your model on GPU.

#### Arguments:

* <b>`generator`</b>: A generator.
        The output of the generator must be either
        - a tuple (inputs, targets)
        - a tuple (inputs, targets, sample_weights).
        All arrays should contain the same number of samples.
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
        Note that in conjunction with initial_epoch, the parameter
        epochs is to be understood as "final epoch". The model is
        not trained for n steps given by epochs, but until the
        epoch epochs is reached.
* <b>`verbose`</b>: Verbosity mode, 0, 1, or 2.
* <b>`callbacks`</b>: List of callbacks to be called during training.
* <b>`validation_data`</b>: This can be either
        - A generator for the validation data
        - A tuple (inputs, targets)
        - A tuple (inputs, targets, sample_weights).
* <b>`validation_steps`</b>: Only relevant if `validation_data`
        is a generator.
        Number of steps to yield from validation generator
        at the end of every epoch. It should typically
        be equal to the number of samples of your
        validation dataset divided by the batch size.
        Optional for `Sequence`: if unspecified, will use
        the `len(validation_data)` as a number of steps.
* <b>`class_weight`</b>: Dictionary mapping class indices to a weight
        for the class.
* <b>`max_queue_size`</b>: Maximum size for the generator queue
* <b>`workers`</b>: Maximum number of processes to spin up
* <b>`use_multiprocessing`</b>: If True, use process based threading.
        Note that because
        this implementation relies on multiprocessing,
        you should not pass
        non picklable arguments to the generator
        as they can't be passed
        easily to children processes.
* <b>`shuffle`</b>: Whether to shuffle the order of the batches at
          the beginning of each epoch. Only used with instances
          of `Sequence` (keras.utils.Sequence).
* <b>`initial_epoch`</b>: Epoch at which to start training
        (useful for resuming a previous training run)
* <b>`**kwargs`</b>: support for legacy arguments.


#### Returns:

A `History` object.


#### Raises:

* <b>`RuntimeError`</b>: if the model was never compiled.
* <b>`ValueError`</b>: In case the generator yields
        data in an invalid format.

Example:

```python
    def generate_arrays_from_file(path):
        while 1:
            f = open(path)
            for line in f:
                # create Numpy arrays of input data
                # and labels, from each line in the file
                x, y = process_line(line)
                yield (x, y)
                f.close()

    model.fit_generator(generate_arrays_from_file('/my_file.txt'),
                        steps_per_epoch=1000, epochs=10)
```

<h3 id="from_config"><code>from_config</code></h3>

``` python
@classmethod
from_config(
    cls,
    config,
    custom_objects=None
)
```



<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```



<h3 id="get_input_at"><code>get_input_at</code></h3>

``` python
get_input_at(node_index)
```

Retrieves the input tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A tensor (or list of tensors if the layer has multiple inputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_input_mask_at"><code>get_input_mask_at</code></h3>

``` python
get_input_mask_at(node_index)
```

Retrieves the input mask tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A mask tensor
(or list of tensors if the layer has multiple inputs).

<h3 id="get_input_shape_at"><code>get_input_shape_at</code></h3>

``` python
get_input_shape_at(node_index)
```

Retrieves the input shape(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A shape tuple
(or list of shape tuples if the layer has multiple inputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_layer"><code>get_layer</code></h3>

``` python
get_layer(
    name=None,
    index=None
)
```

Retrieve a layer that is part of the model.

Returns a layer based on either its name (unique)
or its index in the graph. Indices are based on
order of horizontal graph traversal (bottom-up).

#### Arguments:

* <b>`name`</b>: string, name of layer.
* <b>`index`</b>: integer, index of layer.


#### Returns:

A layer instance.

<h3 id="get_losses_for"><code>get_losses_for</code></h3>

``` python
get_losses_for(inputs)
```

Retrieves losses relevant to a specific set of inputs.

#### Arguments:

* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.


#### Returns:

List of loss tensors of the layer that depend on `inputs`.


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_output_at"><code>get_output_at</code></h3>

``` python
get_output_at(node_index)
```

Retrieves the output tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A tensor (or list of tensors if the layer has multiple outputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_output_mask_at"><code>get_output_mask_at</code></h3>

``` python
get_output_mask_at(node_index)
```

Retrieves the output mask tensor(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A mask tensor
(or list of tensors if the layer has multiple outputs).

<h3 id="get_output_shape_at"><code>get_output_shape_at</code></h3>

``` python
get_output_shape_at(node_index)
```

Retrieves the output shape(s) of a layer at a given node.

#### Arguments:

* <b>`node_index`</b>: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

A shape tuple
(or list of shape tuples if the layer has multiple outputs).


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_updates_for"><code>get_updates_for</code></h3>

``` python
get_updates_for(inputs)
```

Retrieves updates relevant to a specific set of inputs.

#### Arguments:

* <b>`inputs`</b>: Input tensor or list/tuple of input tensors.


#### Returns:

List of update ops of the layer that depend on `inputs`.


#### Raises:

* <b>`RuntimeError`</b>: If called in Eager mode.

<h3 id="get_weights"><code>get_weights</code></h3>

``` python
get_weights()
```

Retrieves the weights of the model.

#### Returns:

A flat list of Numpy arrays
(one array per model weight).

<h3 id="load_weights"><code>load_weights</code></h3>

``` python
load_weights(
    filepath,
    by_name=False
)
```



<h3 id="pop"><code>pop</code></h3>

``` python
pop()
```

Removes the last layer in the model.

#### Raises:

* <b>`TypeError`</b>: if there are no layers in the model.

<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    x,
    batch_size=32,
    verbose=0
)
```

Generates output predictions for the input samples.

The input samples are processed batch by batch.

#### Arguments:

* <b>`x`</b>: the input data, as a Numpy array.
* <b>`batch_size`</b>: integer.
* <b>`verbose`</b>: verbosity mode, 0 or 1.


#### Returns:

A Numpy array of predictions.

<h3 id="predict_classes"><code>predict_classes</code></h3>

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

``` python
predict_generator(
    generator,
    steps=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    verbose=0,
    **kwargs
)
```

Generates predictions for the input samples from a data generator.

The generator should return the same kind of data as accepted by
`predict_on_batch`.

#### Arguments:

* <b>`generator`</b>: generator yielding batches of input samples.
* <b>`steps`</b>: Total number of steps (batches of samples)
        to yield from `generator` before stopping.
        Optional for `Sequence`: if unspecified, will use
        the `len(generator)` as a number of steps.
* <b>`max_queue_size`</b>: maximum size for the generator queue
* <b>`workers`</b>: maximum number of processes to spin up
* <b>`use_multiprocessing`</b>: if True, use process based threading.
        Note that because this implementation
        relies on multiprocessing, you should not pass
        non picklable arguments to the generator
        as they can't be passed easily to children processes.
* <b>`verbose`</b>: verbosity mode, 0 or 1.
* <b>`**kwargs`</b>: support for legacy arguments.


#### Returns:

A Numpy array of predictions.


#### Raises:

* <b>`ValueError`</b>: In case the generator yields
        data in an invalid format.

<h3 id="predict_on_batch"><code>predict_on_batch</code></h3>

``` python
predict_on_batch(x)
```

Returns predictions for a single batch of samples.

#### Arguments:

* <b>`x`</b>: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).


#### Returns:

A Numpy array of predictions.

<h3 id="predict_proba"><code>predict_proba</code></h3>

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

<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states()
```



<h3 id="save"><code>save</code></h3>

``` python
save(
    filepath,
    overwrite=True,
    include_optimizer=True
)
```

Save the model to a single HDF5 file.

The savefile includes:
    - The model architecture, allowing to re-instantiate the model.
    - The model weights.
    - The state of the optimizer, allowing to resume training
        exactly where you left off.

This allows you to save the entirety of the state of a model
in a single file.

Saved models can be reinstantiated via `keras.models.load_model`.
The model returned by `load_model`
is a compiled model ready to be used (unless the saved model
was never compiled in the first place).

#### Arguments:

* <b>`filepath`</b>: String, path to the file to save the weights to.
* <b>`overwrite`</b>: Whether to silently overwrite any existing file at the
        target location, or provide the user with a manual prompt.
* <b>`include_optimizer`</b>: If True, save optimizer's state together.

Example:

```python
from keras.models import load_model

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')
```

<h3 id="save_weights"><code>save_weights</code></h3>

``` python
save_weights(
    filepath,
    overwrite=True
)
```



<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```

Sets the weights of the model.

#### Arguments:

* <b>`weights`</b>: Should be a list
        of Numpy arrays with shapes and types matching
        the output of `model.get_weights()`.

<h3 id="summary"><code>summary</code></h3>

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

<h3 id="test_on_batch"><code>test_on_batch</code></h3>

``` python
test_on_batch(
    x,
    y,
    sample_weight=None
)
```

Evaluates the model over a single batch of samples.

#### Arguments:

* <b>`x`</b>: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
* <b>`y`</b>: labels, as a Numpy array.
* <b>`sample_weight`</b>: sample weights, as a Numpy array.


#### Returns:

Scalar test loss (if the model has no metrics)
or list of scalars (if the model computes other metrics).
The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.


#### Raises:

* <b>`RuntimeError`</b>: if the model was never compiled.

<h3 id="to_json"><code>to_json</code></h3>

``` python
to_json(**kwargs)
```

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use
`keras.models.model_from_json(json_string, custom_objects={})`.

#### Arguments:

* <b>`**kwargs`</b>: Additional keyword arguments
        to be passed to `json.dumps()`.


#### Returns:

A JSON string.

<h3 id="to_yaml"><code>to_yaml</code></h3>

``` python
to_yaml(**kwargs)
```

Returns a yaml string containing the network configuration.

To load a network from a yaml save file, use
`keras.models.model_from_yaml(yaml_string, custom_objects={})`.

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

``` python
train_on_batch(
    x,
    y,
    class_weight=None,
    sample_weight=None
)
```

Single gradient update over one batch of samples.

#### Arguments:

* <b>`x`</b>: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
* <b>`y`</b>: labels, as a Numpy array.
* <b>`class_weight`</b>: dictionary mapping classes to a weight value,
        used for scaling the loss function (during training only).
* <b>`sample_weight`</b>: sample weights, as a Numpy array.


#### Returns:

Scalar training loss (if the model has no metrics)
or list of scalars (if the model computes other metrics).
The attribute `model.metrics_names` will give you
the display labels for the scalar outputs.


#### Raises:

* <b>`RuntimeError`</b>: if the model was never compiled.



