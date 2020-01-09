page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.make_ndarray


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/make_ndarray">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_util.py#L562-L629">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create a numpy ndarray from a tensor.

### Aliases:

* <a href="/api_docs/python/tf/make_ndarray"><code>tf.compat.v1.make_ndarray</code></a>
* <a href="/api_docs/python/tf/make_ndarray"><code>tf.compat.v2.make_ndarray</code></a>
* <a href="/api_docs/python/tf/make_ndarray"><code>tf.contrib.util.make_ndarray</code></a>


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
