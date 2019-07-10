page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.assert_element_shape

Assert the shape of this `Dataset`.

``` python
tf.contrib.data.assert_element_shape(expected_shapes)
```



Defined in [`contrib/data/python/ops/batching.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/batching.py).

<!-- Placeholder for "Used in" -->

```python
shapes = [tf.TensorShape([16, 256]), tf.TensorShape([None, 2])]
result = dataset.apply(tf.data.experimental.assert_element_shape(shapes))
print(result.output_shapes)  # ==> "((16, 256), (<unknown>, 2))"
```

If dataset shapes and expected_shape, are fully defined, assert they match.
Otherwise, add assert op that will validate the shapes when tensors are
evaluated, and set shapes on tensors, respectively.

Note that unknown dimension in `expected_shapes` will be ignored.

#### Args:


* <b>`expected_shapes`</b>: A nested structure of <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> objects.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>
