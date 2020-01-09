page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/is_tensor">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_util.py#L934-L949">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Checks whether `x` is a tensor or "tensor-like".

### Aliases:

* <a href="/api_docs/python/tf/is_tensor"><code>tf.compat.v1.is_tensor</code></a>
* <a href="/api_docs/python/tf/is_tensor"><code>tf.compat.v2.is_tensor</code></a>
* <a href="/api_docs/python/tf/is_tensor"><code>tf.contrib.framework.is_tensor</code></a>


``` python
tf.is_tensor(x)
```



<!-- Placeholder for "Used in" -->

If `is_tensor(x)` returns `True`, it is safe to assume that `x` is a tensor or
can be converted to a tensor using `ops.convert_to_tensor(x)`.

#### Args:


* <b>`x`</b>: A python object to check.


#### Returns:

`True` if `x` is a tensor or "tensor-like", `False` if not.
