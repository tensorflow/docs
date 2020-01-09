page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.make_ndarray


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/tensor_util.py#L562-L629">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create a numpy ndarray from a tensor.

### Aliases:

* `tf.compat.v1.make_ndarray`
* `tf.compat.v2.make_ndarray`


``` python
tf.make_ndarray(tensor)
```



<!-- Placeholder for "Used in" -->

Create a numpy ndarray with the same shape and data as the tensor.

#### Args:


* <b>`tensor`</b>: A TensorProto.


#### Returns:

A numpy array with the tensor contents.



#### Raises:


* <b>`TypeError`</b>: if tensor has unsupported type.
