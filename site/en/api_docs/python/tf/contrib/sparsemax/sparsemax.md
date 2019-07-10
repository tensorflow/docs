page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.sparsemax.sparsemax

``` python
tf.contrib.sparsemax.sparsemax(
    logits,
    name=None
)
```



Defined in [`tensorflow/contrib/sparsemax/python/ops/sparsemax.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/sparsemax/python/ops/sparsemax.py).

Computes sparsemax activations [1].

For each batch `i` and class `j` we have
<div>   $$sparsemax[i, j] = max(logits[i, j] - tau(logits[i, :]), 0)$$ </div>

[1]: https://arxiv.org/abs/1602.02068

#### Args:

* <b>`logits`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`,
    `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `logits`.