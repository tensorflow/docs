

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.quantized_max_pool

``` python
quantized_max_pool(
    input,
    min_input,
    max_input,
    ksize,
    strides,
    padding,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_nn_ops.py`.

See the guide: [Neural Network > Candidate Sampling](../../../../api_guides/python/nn#Candidate_Sampling)

Produces the max pool of the input tensor for quantized types.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint16`, `quint16`, `qint32`.
    The 4D (batch x rows x cols x depth) Tensor to MaxReduce over.
* <b>`min_input`</b>: A `Tensor` of type `float32`.
    The float value that the lowest quantized input value represents.
* <b>`max_input`</b>: A `Tensor` of type `float32`.
    The float value that the highest quantized input value represents.
* <b>`ksize`</b>: A list of `ints`.
    The size of the window for each dimension of the input tensor.
    The length must be 4 to match the number of dimensions of the input.
* <b>`strides`</b>: A list of `ints`.
    The stride of the sliding window for each dimension of the input
    tensor. The length must be 4 to match the number of dimensions of the input.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
    The type of padding algorithm to use.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (output, min_output, max_output).

* <b>`output`</b>: A `Tensor`. Has the same type as `input`.
* <b>`min_output`</b>: A `Tensor` of type `float32`. The float value that the lowest quantized output value represents.
* <b>`max_output`</b>: A `Tensor` of type `float32`. The float value that the highest quantized output value represents.