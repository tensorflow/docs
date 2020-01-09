page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.swish


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L502-L535">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the Swish activation function: `x * sigmoid(x)`.

### Aliases:

* <a href="/api_docs/python/tf/nn/swish"><code>tf.compat.v1.nn.swish</code></a>
* <a href="/api_docs/python/tf/nn/swish"><code>tf.compat.v2.nn.swish</code></a>


``` python
tf.nn.swish(features)
```



<!-- Placeholder for "Used in" -->

Source: "Searching for Activation Functions" (Ramachandran et al. 2017)
https://arxiv.org/abs/1710.05941

#### Args:


* <b>`features`</b>: A `Tensor` representing preactivation values.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The activation value.
