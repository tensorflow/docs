page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.compose_transforms


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/image/python/ops/image_ops.py#L311-L331">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Composes the transforms tensors.

``` python
tf.contrib.image.compose_transforms(*transforms)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`*transforms`</b>: List of image projective transforms to be composed. Each
    transform is length 8 (single transform) or shape (N, 8) (batched
    transforms). The shapes of all inputs must be equal, and at least one
    input must be given.


#### Returns:

A composed transform tensor. When passed to <a href="../../../tf/contrib/image/transform"><code>tf.contrib.image.transform</code></a>,
    equivalent to applying each of the given transforms to the image in
    order.
