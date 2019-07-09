

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.transpose_batch_time

``` python
tf.contrib.rnn.transpose_batch_time(x)
```



Defined in [`tensorflow/python/ops/rnn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/rnn.py).

Transposes the batch and time dimensions of a Tensor.

If the input tensor has rank < 2 it returns the original tensor. Retains as
much of the static shape information as possible.

#### Args:

* <b>`x`</b>: A Tensor.


#### Returns:

x transposed along the first two dimensions.