page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.get_losses


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/losses/util.py#L197-L208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the list of losses from the loss_collection.

### Aliases:

* <a href="/api_docs/python/tf/losses/get_losses"><code>tf.compat.v1.losses.get_losses</code></a>


``` python
tf.losses.get_losses(
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
