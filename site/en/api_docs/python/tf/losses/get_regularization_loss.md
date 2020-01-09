page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.get_regularization_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/losses/util.py#L224-L239">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the total regularization loss.

### Aliases:

* <a href="/api_docs/python/tf/losses/get_regularization_loss"><code>tf.compat.v1.losses.get_regularization_loss</code></a>


``` python
tf.losses.get_regularization_loss(
    scope=None,
    name='total_regularization_loss'
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`scope`</b>: An optional scope name for filtering the losses to return.
* <b>`name`</b>: The name of the returned tensor.


#### Returns:

A scalar regularization loss.
