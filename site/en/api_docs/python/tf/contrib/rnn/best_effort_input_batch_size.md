page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.best_effort_input_batch_size

``` python
tf.contrib.rnn.best_effort_input_batch_size(flat_input)
```



Defined in [`tensorflow/python/ops/rnn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/rnn.py).

Get static input batch size if available, with fallback to the dynamic one.

#### Args:

* <b>`flat_input`</b>: An iterable of time major input Tensors of shape
    `[max_time, batch_size, ...]`.
  All inputs should have compatible batch sizes.


#### Returns:

The batch size in Python integer if available, or a scalar Tensor otherwise.


#### Raises:

* <b>`ValueError`</b>: if there is any input with an invalid shape.