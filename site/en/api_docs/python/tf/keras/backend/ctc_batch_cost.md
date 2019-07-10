page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ctc_batch_cost

Runs CTC loss algorithm on each batch element.

### Aliases:

* `tf.compat.v1.keras.backend.ctc_batch_cost`
* `tf.compat.v2.keras.backend.ctc_batch_cost`
* `tf.keras.backend.ctc_batch_cost`

``` python
tf.keras.backend.ctc_batch_cost(
    y_true,
    y_pred,
    input_length,
    label_length
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`y_true`</b>: tensor `(samples, max_string_length)`
    containing the truth labels.
* <b>`y_pred`</b>: tensor `(samples, time_steps, num_categories)`
    containing the prediction, or output of the softmax.
* <b>`input_length`</b>: tensor `(samples, 1)` containing the sequence length for
    each batch item in `y_pred`.
* <b>`label_length`</b>: tensor `(samples, 1)` containing the sequence length for
    each batch item in `y_true`.


#### Returns:

Tensor with shape (samples,1) containing the
    CTC loss of each element.
