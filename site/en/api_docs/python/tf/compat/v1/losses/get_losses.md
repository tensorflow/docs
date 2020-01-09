page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.losses.get_losses


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/losses/util.py#L197-L208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the list of losses from the loss_collection.

``` python
tf.compat.v1.losses.get_losses(
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: An optional scope name for filtering the losses to return.
* <b>`loss_collection`</b>: Optional losses collection.


#### Returns:

a list of loss tensors.
