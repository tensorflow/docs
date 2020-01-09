page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ctc_batch_cost


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5707-L5736">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Runs CTC loss algorithm on each batch element.

### Aliases:

* `tf.compat.v1.keras.backend.ctc_batch_cost`
* `tf.compat.v2.keras.backend.ctc_batch_cost`


``` python
tf.keras.backend.ctc_batch_cost(
    y_true,
    y_pred,
    input_length,
    label_length
)
```



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
