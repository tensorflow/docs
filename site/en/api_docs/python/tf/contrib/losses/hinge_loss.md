page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.hinge_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/losses/python/losses/loss_ops.py#L452-L483">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Method that returns the loss tensor for hinge loss. (deprecated)

``` python
tf.contrib.losses.hinge_loss(
    logits,
    labels=None,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.hinge_loss instead. Note that the order of the logits and labels arguments has been changed, and to stay unweighted, reduction=Reduction.NONE

#### Args:


* <b>`logits`</b>: The logits, a float tensor. Note that logits are assumed to be
  unbounded and 0-centered. A value > 0 (resp. < 0) is considered a positive
  (resp. negative) binary prediction.
* <b>`labels`</b>: The ground truth output tensor. Its shape should match the shape of
  logits. The values of the tensor are expected to be 0.0 or 1.0. Internally
  the {0,1} labels are converted to {-1,1} when calculating the hinge loss.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.


#### Returns:

An unweighted `Tensor` of same shape as `logits` and `labels` representing
the
  loss values across the batch.



#### Raises:


* <b>`ValueError`</b>: If the shapes of `logits` and `labels` don't match.
