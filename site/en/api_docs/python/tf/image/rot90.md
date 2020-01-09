page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.rot90


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L484-L521">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Rotate image(s) counter-clockwise by 90 degrees.

### Aliases:

* `tf.compat.v1.image.rot90`
* `tf.compat.v2.image.rot90`


``` python
tf.image.rot90(
    image,
    k=1,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### For example:


```python
a=tf.constant([[[1],[2]],[[3],[4]]])
# rotating `a` counter clockwise by 90 degrees
a_rot=tf.image.rot90(a,k=1) #rotated `a`
print(a_rot) # [[[2],[4]],[[1],[3]]]
```
Args:
  image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
    of shape `[height, width, channels]`.
  k: A scalar integer. The number of times the image is rotated by 90 degrees.
  name: A name for this operation (optional).

#### Returns:

A rotated tensor of the same type and shape as `image`.



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.
