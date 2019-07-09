

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.sparsemax.sparsemax_loss

``` python
tf.contrib.sparsemax.sparsemax_loss(
    logits,
    sparsemax,
    labels,
    name=None
)
```



Defined in [`tensorflow/contrib/sparsemax/python/ops/sparsemax_loss.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/sparsemax/python/ops/sparsemax_loss.py).

Computes sparsemax loss function [1].

[1]: https://arxiv.org/abs/1602.02068

#### Args:

* <b>`logits`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`,
    `float64`.
* <b>`sparsemax`</b>: A `Tensor`. Must have the same type as `logits`.
* <b>`labels`</b>: A `Tensor`. Must have the same type as `logits`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `logits`.