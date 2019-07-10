page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.sparsemax.sparsemax_loss

Computes sparsemax loss function [1].

``` python
tf.contrib.sparsemax.sparsemax_loss(
    logits,
    sparsemax,
    labels,
    name=None
)
```



Defined in [`contrib/sparsemax/python/ops/sparsemax_loss.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/sparsemax/python/ops/sparsemax_loss.py).

<!-- Placeholder for "Used in" -->

[1]: https://arxiv.org/abs/1602.02068

#### Args:


* <b>`logits`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`,
  `float64`.
* <b>`sparsemax`</b>: A `Tensor`. Must have the same type as `logits`.
* <b>`labels`</b>: A `Tensor`. Must have the same type as `logits`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `logits`.
