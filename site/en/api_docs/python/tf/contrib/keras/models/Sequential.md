

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.models.Sequential

### `class tf.contrib.keras.models.Sequential`



Defined in [`tensorflow/contrib/keras/python/keras/models.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/models.py).

Linear stack of layers.

#### Arguments:

    layers: list of layers to add to the model.

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

<h3 id="built"><code>built</code></h3>



<h3 id="constraints"><code>constraints</code></h3>



<h3 id="input"><code>input</code></h3>

Retrieves the input tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Input tensor or list of input tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="input_mask"><code>input_mask</code></h3>

Retrieves the input mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Input mask tensor (potentially None) or list of input
    mask tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="input_shape"><code>input_shape</code></h3>

Retrieves the input shape tuple(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Input shape tuple
    (or list of input shape tuples, one tuple per input tensor).


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="input_spec"><code>input_spec</code></h3>

Gets the model's input specs.

#### Returns:

    A list of `InputSpec` instances (one per input to the model)
        or a single instance if the model has only one input.

<h3 id="losses"><code>losses</code></h3>



<h3 id="non_trainable_weights"><code>non_trainable_weights</code></h3>



<h3 id="output"><code>output</code></h3>

Retrieves the output tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Output tensor or list of output tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="output_mask"><code>output_mask</code></h3>

Retrieves the output mask tensor(s) of a layer.

Only applicable if the layer has exactly one inbound node,
i.e. if it is connected to one incoming layer.

#### Returns:

    Output mask tensor (potentially None) or list of output
    mask tensors.


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="output_shape"><code>output_shape</code></h3>

Retrieves the output shape tuple(s) of a layer.

Only applicable if the layer has one inbound node,
or if all inbound nodes have the same output shape.

#### Returns:

    Output shape tuple
    (or list of input shape tuples, one tuple per output tensor).


#### Raises:

    AttributeError: if the layer is connected to
    more than one incoming layers.

<h3 id="regularizers"><code>regularizers</code></h3>



<h3 id="state_updates"><code>state_updates</code></h3>



<h3 id="stateful"><code>stateful</code></h3>



<h3 id="trainable"><code>trainable</code></h3>



<h3 id="trainable_weights"><code>trainable_weights</code></h3>



<h3 id="updates"><code>updates</code></h3>



<h3 id="uses_learning_phase"><code>uses_learning_phase</code></h3>



<h3 id="weights"><code>weights</code></h3>





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

    inputs: Can be a tensor or list/tuple of tensors.
    **kwargs: Additional keyword arguments to be passed to `call()`.


#### Returns:

    Output of the layer's `call` method.


#### Raises:

    ValueError: in case the layer is missing shape information
        for its `build` call.

<h3 id="add"><code>add</code></h3>

``` python
add(layer)
```

Adds a layer instance on top of the layer stack.

#### Arguments:

    layer: layer instance.


#### Raises:

    TypeError: If `layer` is not a layer instance.
    ValueError: In case the `layer` argument does not
        know its input shape.
    ValueError: In case the `layer` argument has
        multiple output tensors, or is already connected
        somewhere else (forbidden in `Sequential` models).

<h3 id="add_loss"><code>add_loss</code></h3>

``` python
add_loss(
    losses,
    inputs=None
)
```

Add losses to the layer.

The loss may potentially be conditional on some inputs tensors,
for instance activity losses are conditional on the layer's inputs.

#### Arguments:

    losses: loss tensor or list of loss tensors
        to add to the layer.
    inputs: input tensor or list of inputs tensors to mark
        the losses as conditional on these inputs.
        If None is passed, the loss is assumed unconditional
        (e.g. L2 weight regularization, which only depends
        on the layer's weights variables, not on any inputs tensors).

<h3 id="add_update"><code>add_update</code></h3>

``` python
add_update(
    updates,
    inputs=None
)
```

Add updates to the layer.

The updates may potentially be conditional on some inputs tensors,
for instance batch norm updates are conditional on the layer's inputs.

#### Arguments:

    updates: update op or list of update ops
        to add to the layer.
    inputs: input tensor or list of inputs tensors to mark
        the updates as conditional on these inputs.
        If None is passed, the updates are assumed unconditional.

<h3 id="add_weight"><code>add_weight</code></h3>

``` python
add_weight(
    shape,
    initializer,
    name=None,
    trainable=True,
    regularizer=None,
    constraint=None
)
```

Adds a weight variable to the layer.

#### Arguments:

    shape: The shape tuple of the weight.
    initializer: An Initializer instance (callable).
    name: String, the name for the weight variable.
    trainable: A boolean, whether the weight should
        be trained via backprop or not (assuming
        that the layer itself is also trainable).
    regularizer: An optional Regularizer instance.
    constraint: An optional Constraint instance.


#### Returns:

    The created weight variable.

<h3 id="assert_input_compatibility"><code>assert_input_compatibility</code></h3>

``` python
assert_input_compatibility(inputs)
```

Checks compatibility between the layer and provided inputs.

This checks that the tensor(s) `input`
verify the input assumptions of the layer
(if any). If not, exceptions are raised.

#### Arguments:

    inputs: input tensor or list of input tensors.


#### Raises:

    ValueError: in case of mismatch between
        the provided inputs and the expectations of the layer.

<h3 id="build"><code>build</code></h3>

``` python
build(input_shape=None)
```



<h3 id="call"><code>call</code></h3>

``` python
call(
    inputs,
    mask=None
)
```



<h3 id="compile"><code>compile</code></h3>

``` python
compile(
    optimizer,
    loss,
    metrics=None,
    sample_weight_mode=None,
    **kwargs
)
```

Configures the learning process.

#### Arguments:

    optimizer: str (name of optimizer) or optimizer object.
        See [optimizers](/optimizers).
    loss: str (name of objective function) or objective function.
        See [objectives](/objectives).
    metrics: list of metrics to be evaluated by the model
        during training and testing.
        Typically you will use `metrics=['accuracy']`.
        See [metrics](/metrics).
    sample_weight_mode: if you need to do timestep-wise
        sample weighting (2D weights), set this to "temporal".
        "None" defaults to sample-wise weights (1D).
    **kwargs: for Theano backend, these are passed into K.function.
        Ignored for Tensorflow backend.

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



<h3 id="count_params"><code>count_params</code></h3>

``` python
count_params()
```

Count the total number of scalars composing the weights.

#### Returns:

    An integer count.


#### Raises:

    RuntimeError: if the layer isn't yet built
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

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
    y: labels, as a Numpy array.
    batch_size: integer. Number of samples per gradient update.
    verbose: verbosity mode, 0 or 1.
    sample_weight: sample weights, as a Numpy array.


#### Returns:

    Scalar test loss (if the model has no metrics)
    or list of scalars (if the model computes other metrics).
    The attribute `model.metrics_names` will give you
    the display labels for the scalar outputs.


#### Raises:

    RuntimeError: if the model was never compiled.

<h3 id="evaluate_generator"><code>evaluate_generator</code></h3>

``` python
evaluate_generator(
    generator,
    steps,
    max_q_size=10,
    workers=1,
    pickle_safe=False
)
```

Evaluates the model on a data generator.

The generator should return the same kind of data
as accepted by `test_on_batch`.

#### Arguments:

    generator: Generator yielding tuples (inputs, targets)
        or (inputs, targets, sample_weights)
    steps: Total number of steps (batches of samples)
        to yield from `generator` before stopping.
    max_q_size: maximum size for the generator queue
    workers: maximum number of processes to spin up
    pickle_safe: if True, use process based threading.
        Note that because this implementation
        relies on multiprocessing, you should not pass
        non picklable arguments to the generator
        as they can't be passed easily to children processes.


#### Returns:

    Scalar test loss (if the model has no metrics)
    or list of scalars (if the model computes other metrics).
    The attribute `model.metrics_names` will give you
    the display labels for the scalar outputs.


#### Raises:

    RuntimeError: if the model was never compiled.

<h3 id="fit"><code>fit</code></h3>

``` python
fit(
    x,
    y,
    batch_size=32,
    epochs=10,
    verbose=1,
    callbacks=None,
    validation_split=0.0,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0
)
```

Trains the model for a fixed number of epochs.

#### Arguments:

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
    y: labels, as a Numpy array.
    batch_size: integer. Number of samples per gradient update.
    epochs: integer, the number of epochs to train the model.
    verbose: 0 for no logging to stdout,
        1 for progress bar logging, 2 for one log line per epoch.
    callbacks: list of `keras.callbacks.Callback` instances.
        List of callbacks to apply during training.
        See [callbacks](/callbacks).
    validation_split: float (0. < x < 1).
        Fraction of the data to use as held-out validation data.
    validation_data: tuple (x_val, y_val) or tuple
        (x_val, y_val, val_sample_weights) to be used as held-out
        validation data. Will override validation_split.
    shuffle: boolean or str (for 'batch').
        Whether to shuffle the samples at each epoch.
        'batch' is a special option for dealing with the
        limitations of HDF5 data; it shuffles in batch-sized chunks.
    class_weight: dictionary mapping classes to a weight value,
        used for scaling the loss function (during training only).
    sample_weight: Numpy array of weights for
        the training samples, used for scaling the loss function
        (during training only). You can either pass a flat (1D)
        Numpy array with the same length as the input samples
        (1:1 mapping between weights and samples),
        or in the case of temporal data,
        you can pass a 2D array with shape (samples, sequence_length),
        to apply a different weight to every timestep of every sample.
        In this case you should make sure to specify
        sample_weight_mode="temporal" in compile().
    initial_epoch: epoch at which to start training
        (useful for resuming a previous training run)


#### Returns:

    A `History` object. Its `History.history` attribute is
    a record of training loss values and metrics values
    at successive epochs, as well as validation loss values
    and validation metrics values (if applicable).


#### Raises:

    RuntimeError: if the model was never compiled.

<h3 id="fit_generator"><code>fit_generator</code></h3>

``` python
fit_generator(
    generator,
    steps_per_epoch,
    epochs=1,
    verbose=1,
    callbacks=None,
    validation_data=None,
    validation_steps=None,
    class_weight=None,
    max_q_size=10,
    workers=1,
    pickle_safe=False,
    initial_epoch=0
)
```

Fits the model on data generated batch-by-batch by a Python generator.

The generator is run in parallel to the model, for efficiency.
For instance, this allows you to do real-time data augmentation
on images on CPU in parallel to training your model on GPU.

#### Arguments:

    generator: A generator.
        The output of the generator must be either
        - a tuple (inputs, targets)
        - a tuple (inputs, targets, sample_weights).
        All arrays should contain the same number of samples.
        The generator is expected to loop over its data
        indefinitely. An epoch finishes when `samples_per_epoch`
        samples have been seen by the model.
    steps_per_epoch: Total number of steps (batches of samples)
        to yield from `generator` before declaring one epoch
        finished and starting the next epoch. It should typically
        be equal to the number of unique samples if your dataset
        divided by the batch size.
    epochs: Integer, total number of iterations on the data.
    verbose: Verbosity mode, 0, 1, or 2.
    callbacks: List of callbacks to be called during training.
    validation_data: This can be either
        - A generator for the validation data
        - A tuple (inputs, targets)
        - A tuple (inputs, targets, sample_weights).
    validation_steps: Only relevant if `validation_data`
        is a generator.
        Number of samples to use from validation generator
        at the end of every epoch.
    class_weight: Dictionary mapping class indices to a weight
        for the class.
    max_q_size: Maximum size for the generator queue
    workers: Maximum number of processes to spin up
    pickle_safe: Ff True, use process based threading.
        Note that because
        this implementation relies on multiprocessing,
        you should not pass
        non picklable arguments to the generator
        as they can't be passed
        easily to children processes.
    initial_epoch: Epoch at which to start training
        (useful for resuming a previous training run)


#### Returns:

    A `History` object.


#### Raises:

    RuntimeError: if the model was never compiled.

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
                        samples_per_epoch=10000, epochs=10)
```

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
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

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A tensor (or list of tensors if the layer has multiple inputs).

<h3 id="get_input_mask_at"><code>get_input_mask_at</code></h3>

``` python
get_input_mask_at(node_index)
```

Retrieves the input mask tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
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

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A shape tuple
    (or list of shape tuples if the layer has multiple inputs).

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

    name: string, name of layer.
    index: integer, index of layer.


#### Returns:

    A layer instance.

<h3 id="get_losses_for"><code>get_losses_for</code></h3>

``` python
get_losses_for(inputs)
```



<h3 id="get_output_at"><code>get_output_at</code></h3>

``` python
get_output_at(node_index)
```

Retrieves the output tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A tensor (or list of tensors if the layer has multiple outputs).

<h3 id="get_output_mask_at"><code>get_output_mask_at</code></h3>

``` python
get_output_mask_at(node_index)
```

Retrieves the output mask tensor(s) of a layer at a given node.

#### Arguments:

    node_index: Integer, index of the node
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

    node_index: Integer, index of the node
        from which to retrieve the attribute.
        E.g. `node_index=0` will correspond to the
        first time the layer was called.


#### Returns:

    A shape tuple
    (or list of shape tuples if the layer has multiple outputs).

<h3 id="get_updates_for"><code>get_updates_for</code></h3>

``` python
get_updates_for(inputs)
```



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

    TypeError: if there are no layers in the model.

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

    x: the input data, as a Numpy array.
    batch_size: integer.
    verbose: verbosity mode, 0 or 1.


#### Returns:

    A Numpy array of predictions.

<h3 id="predict_classes"><code>predict_classes</code></h3>

``` python
predict_classes(
    x,
    batch_size=32,
    verbose=1
)
```

Generate class predictions for the input samples.

The input samples are processed batch by batch.

#### Arguments:

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
    batch_size: integer.
    verbose: verbosity mode, 0 or 1.


#### Returns:

    A numpy array of class predictions.

<h3 id="predict_generator"><code>predict_generator</code></h3>

``` python
predict_generator(
    generator,
    steps,
    max_q_size=10,
    workers=1,
    pickle_safe=False
)
```

Generates predictions for the input samples from a data generator.

The generator should return the same kind of data as accepted by
`predict_on_batch`.

#### Arguments:

    generator: generator yielding batches of input samples.
    steps: Total number of steps (batches of samples)
        to yield from `generator` before stopping.
    max_q_size: maximum size for the generator queue
    workers: maximum number of processes to spin up
    pickle_safe: if True, use process based threading.
        Note that because this implementation
        relies on multiprocessing, you should not pass
        non picklable arguments to the generator
        as they can't be passed easily to children processes.


#### Returns:

    A Numpy array of predictions.

<h3 id="predict_on_batch"><code>predict_on_batch</code></h3>

``` python
predict_on_batch(x)
```

Returns predictions for a single batch of samples.

#### Arguments:

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).


#### Returns:

    A Numpy array of predictions.

<h3 id="predict_proba"><code>predict_proba</code></h3>

``` python
predict_proba(
    x,
    batch_size=32,
    verbose=1
)
```

Generates class probability predictions for the input samples.

The input samples are processed batch by batch.

#### Arguments:

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
    batch_size: integer.
    verbose: verbosity mode, 0 or 1.


#### Returns:

    A Numpy array of probability predictions.

<h3 id="reset_states"><code>reset_states</code></h3>

``` python
reset_states()
```



<h3 id="run_internal_graph"><code>run_internal_graph</code></h3>

``` python
run_internal_graph(
    inputs,
    masks=None
)
```

Computes output tensors for new inputs.

# Note:
    - Expects `inputs` to be a list (potentially with 1 element).
    - Can be run on non-Keras tensors.

#### Arguments:

    inputs: List of tensors
    masks: List of masks (tensors or None).


#### Returns:

    Three lists: output_tensors, output_masks, output_shapes

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

    filepath: String, path to the file to save the weights to.
    overwrite: Whether to silently overwrite any existing file at the
        target location, or provide the user with a manual prompt.
    include_optimizer: If True, save optimizer's state together.

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

    weights: Should be a list
        of Numpy arrays with shapes and types matching
        the output of `model.get_weights()`.

<h3 id="summary"><code>summary</code></h3>

``` python
summary(
    line_length=None,
    positions=None
)
```



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

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
    y: labels, as a Numpy array.
    sample_weight: sample weights, as a Numpy array.


#### Returns:

    Scalar test loss (if the model has no metrics)
    or list of scalars (if the model computes other metrics).
    The attribute `model.metrics_names` will give you
    the display labels for the scalar outputs.


#### Raises:

    RuntimeError: if the model was never compiled.

<h3 id="to_json"><code>to_json</code></h3>

``` python
to_json(**kwargs)
```

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use
`keras.models.model_from_json(json_string, custom_objects={})`.

#### Arguments:

    **kwargs: Additional keyword arguments
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

    **kwargs: Additional keyword arguments
        to be passed to `yaml.dump()`.


#### Returns:

    A YAML string.


#### Raises:

    ImportError: if yaml module is not found.

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

    x: input data, as a Numpy array or list of Numpy arrays
        (if the model has multiple inputs).
    y: labels, as a Numpy array.
    class_weight: dictionary mapping classes to a weight value,
        used for scaling the loss function (during training only).
    sample_weight: sample weights, as a Numpy array.


#### Returns:

    Scalar training loss (if the model has no metrics)
    or list of scalars (if the model computes other metrics).
    The attribute `model.metrics_names` will give you
    the display labels for the scalar outputs.


#### Raises:

    RuntimeError: if the model was never compiled.



