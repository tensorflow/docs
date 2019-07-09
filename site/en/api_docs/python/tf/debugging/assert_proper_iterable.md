page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_proper_iterable

### Aliases:

* `tf.assert_proper_iterable`
* `tf.debugging.assert_proper_iterable`

``` python
tf.debugging.assert_proper_iterable(values)
```



Defined in [`tensorflow/python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/check_ops.py).

Static assert that values is a "proper" iterable.

`Ops` that expect iterables of `Tensor` can call this to validate input.
Useful since `Tensor`, `ndarray`, byte/text type are all iterables themselves.

#### Args:

* <b>`values`</b>:  Object to be checked.


#### Raises:

* <b>`TypeError`</b>:  If `values` is not iterable or is one of
    `Tensor`, `SparseTensor`, `np.array`, <a href="../../tf/compat#bytes_or_text_types"><code>tf.compat.bytes_or_text_types</code></a>.