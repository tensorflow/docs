page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.Interpreter

## Class `Interpreter`





Defined in [`tensorflow/contrib/lite/python/interpreter.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/lite/python/interpreter.py).

Interpreter inferace for TF-Lite Models.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    model_path=None,
    model_content=None
)
```

Constructor.

#### Args:

* <b>`model_path`</b>: Path to TF-Lite Flatbuffer file.
* <b>`model_content`</b>: Content of model.


#### Raises:

* <b>`ValueError`</b>: If the interpreter was unable to create.

<h3 id="allocate_tensors"><code>allocate_tensors</code></h3>

``` python
allocate_tensors()
```



<h3 id="get_input_details"><code>get_input_details</code></h3>

``` python
get_input_details()
```

Gets model input details.

#### Returns:

A list of input details.

<h3 id="get_output_details"><code>get_output_details</code></h3>

``` python
get_output_details()
```

Gets model output details.

#### Returns:

A list of output details.

<h3 id="get_tensor"><code>get_tensor</code></h3>

``` python
get_tensor(tensor_index)
```

Sets the value of the input.

#### Args:

* <b>`tensor_index`</b>: Tensor index of tensor to get. This value can be gotten from
                the 'index' field in get_output_details.


#### Returns:

a numpy array.

<h3 id="invoke"><code>invoke</code></h3>

``` python
invoke()
```



<h3 id="resize_tensor_input"><code>resize_tensor_input</code></h3>

``` python
resize_tensor_input(
    input_index,
    tensor_size
)
```

Resizes an input tensor.

#### Args:

* <b>`input_index`</b>: Tensor index of input to set. This value can be gotten from
               the 'index' field in get_input_details.
* <b>`tensor_size`</b>: The tensor_shape to resize the input to.


#### Raises:

* <b>`ValueError`</b>: If the interpreter could not resize the input tensor.

<h3 id="set_tensor"><code>set_tensor</code></h3>

``` python
set_tensor(
    tensor_index,
    value
)
```

Sets the value of the input.

#### Args:

* <b>`tensor_index`</b>: Tensor index of tensor to set. This value can be gotten from
                the 'index' field in get_input_details.
* <b>`value`</b>: Value of tensor to set.


#### Raises:

* <b>`ValueError`</b>: If the interpreter could not set the tensor.



