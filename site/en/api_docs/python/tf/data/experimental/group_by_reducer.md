page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.group_by_reducer

``` python
tf.data.experimental.group_by_reducer(
    key_func,
    reducer
)
```



Defined in [`tensorflow/python/data/experimental/ops/grouping.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/experimental/ops/grouping.py).

A transformation that groups elements and performs a reduction.

This transformation maps element of a dataset to a key using `key_func` and
groups the elements by key. The `reducer` is used to process each group; its
`init_func` is used to initialize state for each group when it is created, the
`reduce_func` is used to update the state every time an element is mapped to
the matching group, and the `finalize_func` is used to map the final state to
an output value.

#### Args:

* <b>`key_func`</b>: A function mapping a nested structure of tensors
    (having shapes and types defined by `self.output_shapes` and
    `self.output_types`) to a scalar <a href="../../../tf/dtypes#int64"><code>tf.int64</code></a> tensor.
* <b>`reducer`</b>: An instance of `Reducer`, which captures the reduction logic using
    the `init_func`, `reduce_func`, and `finalize_func` functions.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.