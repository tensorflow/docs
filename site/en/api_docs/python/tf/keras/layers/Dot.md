page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Dot


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Dot">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/merge.py#L447-L558">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Dot`

Layer that computes a dot product between samples in two tensors.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Dot"><code>tf.compat.v1.keras.layers.Dot</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Dot"><code>tf.compat.v2.keras.layers.Dot</code></a>


<!-- Placeholder for "Used in" -->

E.g. if applied to a list of two tensors `a` and `b` of shape
`(batch_size, n)`, the output will be a tensor of shape `(batch_size, 1)`
where each entry `i` will be the dot product between
`a[i]` and `b[i]`.

#### Arguments:


* <b>`axes`</b>: Integer or tuple of integers,
    axis or axes along which to take the dot product.
* <b>`normalize`</b>: Whether to L2-normalize samples along the
    dot product axis before taking the dot product.
    If set to True, then the output of the dot product
    is the cosine proximity between the two samples.
* <b>`**kwargs`</b>: Standard layer keyword arguments.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/merge.py#L465-L480">View source</a>

``` python
__init__(
    axes,
    normalize=False,
    **kwargs
)
```
