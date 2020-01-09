page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_proper_iterable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_proper_iterable">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L374-L402">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Static assert that values is a "proper" iterable.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_proper_iterable"><code>tf.assert_proper_iterable</code></a>
* <a href="/api_docs/python/tf/debugging/assert_proper_iterable"><code>tf.compat.v1.assert_proper_iterable</code></a>
* <a href="/api_docs/python/tf/debugging/assert_proper_iterable"><code>tf.compat.v1.debugging.assert_proper_iterable</code></a>
* <a href="/api_docs/python/tf/debugging/assert_proper_iterable"><code>tf.compat.v2.debugging.assert_proper_iterable</code></a>


``` python
tf.debugging.assert_proper_iterable(values)
```



<!-- Placeholder for "Used in" -->

`Ops` that expect iterables of `Tensor` can call this to validate input.
Useful since `Tensor`, `ndarray`, byte/text type are all iterables themselves.

#### Args:


* <b>`values`</b>:  Object to be checked.


#### Raises:


* <b>`TypeError`</b>:  If `values` is not iterable or is one of
  `Tensor`, `SparseTensor`, `np.array`, <a href="../../tf/compat#bytes_or_text_types"><code>tf.compat.bytes_or_text_types</code></a>.
