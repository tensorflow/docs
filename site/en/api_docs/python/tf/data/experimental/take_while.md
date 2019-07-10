page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.take_while

A transformation that stops dataset iteration based on a `predicate`.

### Aliases:

* `tf.compat.v1.data.experimental.take_while`
* `tf.compat.v2.data.experimental.take_while`
* `tf.data.experimental.take_while`

``` python
tf.data.experimental.take_while(predicate)
```



Defined in [`python/data/experimental/ops/take_while_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/take_while_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`predicate`</b>: A function that maps a nested structure of tensors (having shapes
  and types defined by `self.output_shapes` and `self.output_types`) to a
  scalar <a href="../../../tf#bool"><code>tf.bool</code></a> tensor.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
