

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.rnn.transpose_batch_time

``` python
tf.contrib.rnn.transpose_batch_time(x)
```



Defined in [`tensorflow/python/ops/rnn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/rnn.py).

Transpose the batch and time dimensions of a Tensor.

Retains as much of the static shape information as possible.

#### Args:

* <b>`x`</b>: A tensor of rank 2 or higher.


#### Returns:

x transposed along the first two dimensions.


#### Raises:

* <b>`ValueError`</b>: if `x` is rank 1 or lower.