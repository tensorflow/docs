page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.sobel_edges


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/sobel_edges">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L3496-L3534">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a tensor holding Sobel edge maps.

### Aliases:

* <a href="/api_docs/python/tf/image/sobel_edges"><code>tf.compat.v1.image.sobel_edges</code></a>
* <a href="/api_docs/python/tf/image/sobel_edges"><code>tf.compat.v2.image.sobel_edges</code></a>


``` python
tf.image.sobel_edges(image)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`image`</b>: Image tensor with shape [batch_size, h, w, d] and type float32 or
  float64.  The image(s) must be 2x2 or larger.


#### Returns:

Tensor holding edge maps for each channel. Returns a tensor with shape
[batch_size, h, w, d, 2] where the last two dimensions hold [[dy[0], dx[0]],
[dy[1], dx[1]], ..., [dy[d-1], dx[d-1]]] calculated using the Sobel filter.
