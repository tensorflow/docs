page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.smart_cond

``` python
tf.contrib.framework.smart_cond(
    pred,
    true_fn=None,
    false_fn=None,
    name=None
)
```



Defined in [`tensorflow/python/framework/smart_cond.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/framework/smart_cond.py).

Return either `true_fn()` if predicate `pred` is true else `false_fn()`.

If `pred` is a bool or has a constant value, we return either `true_fn()`
or `false_fn()`, otherwise we use <a href="../../../tf/cond"><code>tf.cond</code></a> to dynamically route to both.

#### Arguments:

* <b>`pred`</b>: A scalar determining whether to return the result of `true_fn` or
    `false_fn`.
* <b>`true_fn`</b>: The callable to be performed if pred is true.
* <b>`false_fn`</b>: The callable to be performed if pred is false.
* <b>`name`</b>: Optional name prefix when using <a href="../../../tf/cond"><code>tf.cond</code></a>.


#### Returns:

Tensors returned by the call to either `true_fn` or `false_fn`.


#### Raises:

* <b>`TypeError`</b>: If `true_fn` or `false_fn` is not callable.