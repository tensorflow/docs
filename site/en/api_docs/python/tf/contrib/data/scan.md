

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.scan

``` python
tf.contrib.data.scan(
    initial_state,
    scan_func
)
```



Defined in [`tensorflow/contrib/data/python/ops/scan_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/data/python/ops/scan_ops.py).

See the guide: [Dataset Input Pipeline > Transformations on existing datasets](../../../../../api_guides/python/input_dataset#Transformations_on_existing_datasets)

A transformation that scans a function across an input dataset.

This transformation is a stateful relative of <a href="../../../tf/data/Dataset#map"><code>tf.data.Dataset.map</code></a>.
In addition to mapping `scan_func` across the elements of the input dataset,
`scan()` accumulates one or more state tensors, whose initial values are
`initial_state`.

#### Args:

* <b>`initial_state`</b>: A nested structure of tensors, representing the initial state
    of the accumulator.
* <b>`scan_func`</b>: A function that maps `(old_state, input_element)` to
    `(new_state, output_element). It must take two arguments and return a
    pair of nested structures of tensors. The `new_state` must match the
    structure of `initial_state`.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.