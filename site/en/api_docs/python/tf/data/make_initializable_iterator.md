page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.make_initializable_iterator

``` python
tf.data.make_initializable_iterator(dataset)
```



Defined in [`tensorflow/python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/ops/dataset_ops.py).

Creates a <a href="../../tf/data/Iterator"><code>tf.data.Iterator</code></a> for enumerating the elements of a dataset.

Note: The returned iterator will be in an uninitialized state,
and you must run the `iterator.initializer` operation before using it:

```python
dataset = ...
iterator = dataset.make_initializable_iterator()
# ...
sess.run(iterator.initializer)
```

#### Args:

* <b>`dataset`</b>: A <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.


#### Returns:

A <a href="../../tf/data/Iterator"><code>tf.data.Iterator</code></a> over the elements of `dataset`.


#### Raises:

* <b>`RuntimeError`</b>: If eager execution is enabled.