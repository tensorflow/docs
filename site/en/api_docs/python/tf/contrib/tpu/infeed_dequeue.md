page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.infeed_dequeue


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/ops/tpu_ops.py#L196-L216">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A placeholder op for a value that will be fed into the computation.

``` python
tf.contrib.tpu.infeed_dequeue(
    dtype,
    shape,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dtype`</b>: A <a href="../../../tf/dtypes/DType"><code>tf.DType</code></a>. The type of elements in the tensor.
* <b>`shape`</b>: A <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `ints`. The shape of the tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`.
A tensor that will be provided using the infeed mechanism.



#### Raises:


* <b>`TypeError`</b>: If 'dtype` is not a supported infeed type.
