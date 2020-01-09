page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.rgb_to_grayscale


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/rgb_to_grayscale">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L1821-L1848">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts one or more images from RGB to Grayscale.

### Aliases:

* <a href="/api_docs/python/tf/image/rgb_to_grayscale"><code>tf.compat.v1.image.rgb_to_grayscale</code></a>
* <a href="/api_docs/python/tf/image/rgb_to_grayscale"><code>tf.compat.v2.image.rgb_to_grayscale</code></a>


``` python
tf.image.rgb_to_grayscale(
    images,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Outputs a tensor of the same `DType` and rank as `images`.  The size of the
last dimension of the output is 1, containing the Grayscale value of the
pixels.

#### Args:


* <b>`images`</b>: The RGB tensor to convert. Last dimension must have size 3 and
  should contain RGB values.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The converted grayscale image(s).
