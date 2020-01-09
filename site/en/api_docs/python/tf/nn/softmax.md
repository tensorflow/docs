page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.softmax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L2961-L2985">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes softmax activations.

### Aliases:

* `tf.compat.v2.math.softmax`
* `tf.compat.v2.nn.softmax`
* `tf.math.softmax`


``` python
tf.nn.softmax(
    logits,
    axis=None,
    name=None
)
```



### Used in the tutorials:

* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



This function performs the equivalent of

    softmax = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis)

#### Args:


* <b>`logits`</b>: A non-empty `Tensor`. Must be one of the following types: `half`,
  `float32`, `float64`.
* <b>`axis`</b>: The dimension softmax would be performed on. The default is -1 which
  indicates the last dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type and shape as `logits`.



#### Raises:


* <b>`InvalidArgumentError`</b>: if `logits` is empty or `axis` is beyond the last
  dimension of `logits`.
