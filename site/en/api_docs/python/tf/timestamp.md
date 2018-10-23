

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.timestamp

``` python
tf.timestamp(name=None)
```



Defined in `tensorflow/python/ops/gen_logging_ops.py`.

Provides the time since epoch in seconds.

Returns the timestamp as a `float64` for seconds since the Unix epoch.

Note: the timestamp is computed when the op is executed, not when it is added
to the graph.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float64`.