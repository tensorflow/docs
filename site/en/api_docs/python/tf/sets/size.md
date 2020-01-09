page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sets.size


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sets/size">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sets_impl.py#L34-L58">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute number of unique elements along last dimension of `a`.

### Aliases:

* <a href="/api_docs/python/tf/sets/size"><code>tf.compat.v1.sets.set_size</code></a>
* <a href="/api_docs/python/tf/sets/size"><code>tf.compat.v1.sets.size</code></a>
* <a href="/api_docs/python/tf/sets/size"><code>tf.compat.v2.sets.size</code></a>
* <a href="/api_docs/python/tf/sets/size"><code>tf.contrib.metrics.set_size</code></a>
* <a href="/api_docs/python/tf/sets/size"><code>tf.sets.set_size</code></a>


``` python
tf.sets.size(
    a,
    validate_indices=True
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`a`</b>: `SparseTensor`, with indices sorted in row-major order.
* <b>`validate_indices`</b>: Whether to validate the order and range of sparse indices
   in `a`.


#### Returns:

`int32` `Tensor` of set sizes. For `a` ranked `n`, this is a `Tensor` with
rank `n-1`, and the same 1st `n-1` dimensions as `a`. Each value is the
number of unique elements in the corresponding `[0...n-1]` dimension of `a`.



#### Raises:


* <b>`TypeError`</b>: If `a` is an invalid types.
