page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.sigmoid_cross_entropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/losses/python/losses/loss_ops.py#L274-L322">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a cross-entropy loss using tf.nn.sigmoid_cross_entropy_with_logits. (deprecated)

``` python
tf.contrib.losses.sigmoid_cross_entropy(
    logits,
    multi_class_labels,
    weights=1.0,
    label_smoothing=0,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.sigmoid_cross_entropy instead. Note that the order of the predictions and labels arguments has been changed.

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of size [`batch_size`], then the loss weights apply to each
corresponding sample.

If `label_smoothing` is nonzero, smooth the labels towards 1/2:

    new_multiclass_labels = multiclass_labels * (1 - label_smoothing)
                            + 0.5 * label_smoothing

#### Args:


* <b>`logits`</b>: [batch_size, num_classes] logits outputs of the network .
* <b>`multi_class_labels`</b>: [batch_size, num_classes] labels in (0, 1).
* <b>`weights`</b>: Coefficients for the loss. The tensor must be a scalar, a tensor of
  shape [batch_size] or shape [batch_size, num_classes].
* <b>`label_smoothing`</b>: If greater than 0 then smooth the labels.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.


#### Returns:

A scalar `Tensor` representing the loss value.



#### Raises:


* <b>`ValueError`</b>: If the shape of `logits` doesn't match that of
  `multi_class_labels` or if the shape of `weights` is invalid, or if
  `weights` is None.
