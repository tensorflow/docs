

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.layers.Cropping2D

### `class tf.contrib.keras.layers.Cropping2D`



Defined in [`tensorflow/contrib/keras/python/keras/layers/convolutional.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/layers/convolutional.py).

Cropping layer for 2D input (e.g. picture).

It crops along spatial dimensions, i.e. width and height.

#### Arguments:

    cropping: int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
        - If int: the same symmetric cropping
            is applied to width and height.
        - If tuple of 2 ints:
            interpreted as two different
            symmetric cropping values for height and width:
            `(symmetric_height_crop, symmetrc_width_crop)`.
        - If tuple of 2 tuples of 2 ints:
            interpreted as
            `((top_crop, bottom_crop), (left_crop, right_crop))`
    data_format: A string,
        one of `channels_last` (default) or `channels_first`.
        The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, width, height, channels)` while `channels_first`
        corresponds to inputs with shape
        `(batch, channels, width, height)`.
        It defaults to the `image_data_format` value found in your
        Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".

Input shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch, rows, cols, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch, channels, rows, cols)`

Output shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch, cropped_rows, cropped_cols, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch, channels, cropped_rows, cropped_cols)`

Examples:

```python
    # Crop the input 2D images or feature maps
    model = Sequential()
    model.add(Cropping2D(cropping=((2, 2), (4, 4)),
                         input_shape=(28, 28, 3)))
    # now model.output_shape == (None, 24, 20, 3)
    model.add(Conv2D(64, (3, 3), padding='same))
    model.add(Cropping2D(cropping=((2, 2), (2, 2))))
    # now model.output_shape == (None, 20, 16. 64)
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

<h3 id="trainable_weights"><code>trainable_weights</code></h3>



<h3 id="updates"><code>updates</code></h3>



<h3 id="weights"><code>weights</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cropping=((0, 0), (0, 0)),
    data_format=None,
    **kwargs
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
build(input_shape)
```

Creates the layer weights.

Must be implemented on all layers that have weights.

#### Arguments:

    input_shape: Keras tensor (future input to layer)
        or list/tuple of Keras tensors to reference
        for weight shape computations.

<h3 id="call"><code>call</code></h3>

``` python
call(inputs)
```



<h3 id="compute_mask"><code>compute_mask</code></h3>

``` python
compute_mask(
    inputs,
    mask=None
)
```

Computes an output mask tensor.

#### Arguments:

    inputs: Tensor or list of tensors.
    mask: Tensor or list of tensors.


#### Returns:

    None or a tensor (or list of tensors,
        one per output tensor of the layer).

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

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Container), nor weights (handled by `set_weights`).

#### Arguments:

    config: A Python dictionary, typically the
        output of get_config.


#### Returns:

    A layer instance.

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

Returns the current weights of the layer.

#### Returns:

    Weights values as a list of numpy arrays.

<h3 id="set_weights"><code>set_weights</code></h3>

``` python
set_weights(weights)
```

Sets the weights of the layer, from Numpy arrays.

#### Arguments:

    weights: a list of Numpy arrays. The number
        of arrays and their shape must match
        number of the dimensions of the weights
        of the layer (i.e. it should match the
        output of `get_weights`).


#### Raises:

    ValueError: If the provided weights list does not match the
        layer's specifications.



