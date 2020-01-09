page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/tensor_util.py#L934-L949">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Checks whether `x` is a tensor or "tensor-like".

### Aliases:

* `tf.compat.v1.is_tensor`
* `tf.compat.v2.is_tensor`


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
