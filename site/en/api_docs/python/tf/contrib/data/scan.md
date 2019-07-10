page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.scan

A transformation that scans a function across an input dataset. (deprecated)

``` python
tf.contrib.data.scan(
    initial_state,
    scan_func
)
```



Defined in [`contrib/data/python/ops/scan_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/scan_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/scan"><code>tf.data.experimental.scan(...)</code></a>.

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
