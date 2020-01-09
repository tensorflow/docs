page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.identity


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L176-L218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return a tensor with the same shape and contents as input.

### Aliases:

* `tf.compat.v1.identity`
* `tf.compat.v2.identity`


``` python
tf.identity(
    input,
    name=None
)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)




#### For example:



```python
import tensorflow as tf
val0 = tf.ones((1,), dtype=tf.float32)
a = tf.atan2(val0, val0)
a_identity = tf.identity(a)
print(a.numpy())          #[0.7853982]
print(a_identity.numpy()) #[0.7853982]
```

#### Args:


* <b>`input`</b>: A `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
