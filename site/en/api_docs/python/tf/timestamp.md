page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.timestamp

Provides the time since epoch in seconds.

### Aliases:

* `tf.compat.v1.timestamp`
* `tf.compat.v2.timestamp`
* `tf.timestamp`

``` python
tf.timestamp(name=None)
```



Defined in generated file: `python/ops/gen_logging_ops.py`.

<!-- Placeholder for "Used in" -->

Returns the timestamp as a `float64` for seconds since the Unix epoch.

Note: the timestamp is computed when the op is executed, not when it is added
to the graph.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float64`.
