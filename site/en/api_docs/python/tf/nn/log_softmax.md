page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.log_softmax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L3018-L3042">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes log softmax activations.

### Aliases:

* `tf.compat.v2.math.log_softmax`
* `tf.compat.v2.nn.log_softmax`
* `tf.math.log_softmax`


``` python
tf.nn.log_softmax(
    logits,
    axis=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

For each batch `i` and class `j` we have

    logsoftmax = logits - log(reduce_sum(exp(logits), axis))

#### Args:


* <b>`logits`</b>: A non-empty `Tensor`. Must be one of the following types: `half`,
  `float32`, `float64`.
* <b>`axis`</b>: The dimension softmax would be performed on. The default is -1 which
  indicates the last dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `logits`. Same shape as `logits`.



#### Raises:


* <b>`InvalidArgumentError`</b>: if `logits` is empty or `axis` is beyond the last
  dimension of `logits`.
