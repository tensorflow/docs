page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.Interpreter

## Class `Interpreter`

Interpreter interface for TensorFlow Lite Models.



### Aliases:

* Class `tf.compat.v1.lite.Interpreter`
* Class `tf.compat.v2.lite.Interpreter`
* Class `tf.lite.Interpreter`



Defined in [`lite/python/interpreter.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/python/interpreter.py).

<!-- Placeholder for "Used in" -->

This makes the TensorFlow Lite interpreter accessible in Python.
It is possible to use this interpreter in a multithreaded Python environment,
but you must be sure to call functions of a particular instance from only
one thread at a time. So if you want to have 4 threads running different
inferences simultaneously, create  an interpreter for each one as thread-local
data. Similarly, if you are calling invoke() in one thread on a single
interpreter but you want to use tensor() on another thread once it is done,
you must use a synchronization primitive between the threads to ensure invoke
has returned before calling tensor().

<h2 id="__init__"><code>__init__</code></h2>

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



## Methods

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

Gets the value of the input tensor (get a copy).

If you wish to avoid the copy, use `tensor()`. This function cannot be used
to read intermediate results.

#### Args:


* <b>`tensor_index`</b>: Tensor index of tensor to get. This value can be gotten from
              the 'index' field in get_output_details.


#### Returns:

a numpy array.


<h3 id="get_tensor_details"><code>get_tensor_details</code></h3>

``` python
get_tensor_details()
```

Gets tensor details for every tensor with valid tensor details.

Tensors where required information about the tensor is not found are not
added to the list. This includes temporary tensors without a name.

#### Returns:

A list of dictionaries containing tensor information.


<h3 id="invoke"><code>invoke</code></h3>

``` python
invoke()
```

Invoke the interpreter.

Be sure to set the input sizes, allocate tensors and fill values before
calling this. Also, note that this function releases the GIL so heavy
computation can be done in the background while the Python interpreter
continues. No other function on this object should be called while the
invoke() call has not finished.

#### Raises:


* <b>`ValueError`</b>: When the underlying interpreter fails raise ValueError.

<h3 id="reset_all_variables"><code>reset_all_variables</code></h3>

``` python
reset_all_variables()
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

Sets the value of the input tensor. Note this copies data in `value`.

If you want to avoid copying, you can use the `tensor()` function to get a
numpy buffer pointing to the input buffer in the tflite interpreter.

#### Args:


* <b>`tensor_index`</b>: Tensor index of tensor to set. This value can be gotten from
              the 'index' field in get_input_details.
* <b>`value`</b>: Value of tensor to set.


#### Raises:


* <b>`ValueError`</b>: If the interpreter could not set the tensor.

<h3 id="tensor"><code>tensor</code></h3>

``` python
tensor(tensor_index)
```

Returns function that gives a numpy view of the current tensor buffer.

This allows reading and writing to this tensors w/o copies. This more
closely mirrors the C++ Interpreter class interface's tensor() member, hence
the name. Be careful to not hold these output references through calls
to `allocate_tensors()` and `invoke()`. This function cannot be used to read
intermediate results.

#### Usage:



```
interpreter.allocate_tensors()
input = interpreter.tensor(interpreter.get_input_details()[0]["index"])
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])
for i in range(10):
  input().fill(3.)
  interpreter.invoke()
  print("inference %s" % output())
```

Notice how this function avoids making a numpy array directly. This is
because it is important to not hold actual numpy views to the data longer
than necessary. If you do, then the interpreter can no longer be invoked,
because it is possible the interpreter would resize and invalidate the
referenced tensors. The NumPy API doesn't allow any mutability of the
the underlying buffers.

#### WRONG:



```
input = interpreter.tensor(interpreter.get_input_details()[0]["index"])()
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])()
interpreter.allocate_tensors()  # This will throw RuntimeError
for i in range(10):
  input.fill(3.)
  interpreter.invoke()  # this will throw RuntimeError since input,output
```

#### Args:


* <b>`tensor_index`</b>: Tensor index of tensor to get. This value can be gotten from
              the 'index' field in get_output_details.


#### Returns:

A function that can return a new numpy array pointing to the internal
TFLite tensor state at any point. It is safe to hold the function forever,
but it is not safe to hold the numpy array forever.




