page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.cosine_distance


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/losses/python/losses/loss_ops.py#L607-L652">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds a cosine-distance loss to the training procedure. (deprecated arguments) (deprecated)

``` python
tf.contrib.losses.cosine_distance(
    predictions,
    labels=None,
    axis=None,
    weights=1.0,
    scope=None,
    dim=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.cosine_distance instead.

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead

Note that the function assumes that `predictions` and `labels` are already
unit-normalized.

#### Args:


* <b>`predictions`</b>: An arbitrary matrix.
* <b>`labels`</b>: A `Tensor` whose shape matches 'predictions'
* <b>`axis`</b>: The dimension along which the cosine distance is computed.
* <b>`weights`</b>: Coefficients for the loss a scalar, a tensor of shape
  [batch_size] or a tensor whose shape matches `predictions`.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`dim`</b>: The old (deprecated) name for `axis`.


#### Returns:

A scalar `Tensor` representing the loss value.



#### Raises:


* <b>`ValueError`</b>: If `predictions` shape doesn't match `labels` shape, or
  `weights` is `None`.
