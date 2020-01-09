page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.translations_to_projective_transforms


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/image/python/ops/image_ops.py#L176-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns projective transform(s) for the given translation(s).

``` python
tf.contrib.image.translations_to_projective_transforms(
    translations,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`translations`</b>: A 2-element list representing [dx, dy] or a matrix of
    2-element lists representing [dx, dy] to translate for each image
    (for a batch of images). The rank must be statically known (the shape
    is not `TensorShape(None)`.
* <b>`name`</b>: The name of the op.


#### Returns:

A tensor of shape (num_images, 8) projective transforms which can be given
    to <a href="../../../tf/contrib/image/transform"><code>tf.contrib.image.transform</code></a>.
