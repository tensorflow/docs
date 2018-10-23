

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.assert_proper_iterable

``` python
tf.assert_proper_iterable(values)
```



Defined in [`tensorflow/python/ops/check_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/check_ops.py).

See the guide: [Asserts and boolean checks](../../../api_guides/python/check_ops)

Static assert that values is a "proper" iterable.

`Ops` that expect iterables of `Tensor` can call this to validate input.
Useful since `Tensor`, `ndarray`, byte/text type are all iterables themselves.

#### Args:

* <b>`values`</b>:  Object to be checked.


#### Raises:

* <b>`TypeError`</b>:  If `values` is not iterable or is one of
    `Tensor`, `SparseTensor`, `np.array`, <a href="../tf/compat/bytes_or_text_types"><code>tf.compat.bytes_or_text_types</code></a>.