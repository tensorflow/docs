page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.normalize


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/np_utils.py#L55-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Normalizes a Numpy array.

### Aliases:

* `tf.compat.v1.keras.utils.normalize`
* `tf.compat.v2.keras.utils.normalize`


``` python
tf.keras.utils.normalize(
    x,
    axis=-1,
    order=2
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Numpy array to normalize.
* <b>`axis`</b>: axis along which to normalize.
* <b>`order`</b>: Normalization order (e.g. 2 for L2 norm).


#### Returns:

A normalized copy of the array.
