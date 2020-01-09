page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.zero_fraction


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_impl.py#L677-L715">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the fraction of zeros in `value`.

### Aliases:

* `tf.compat.v1.math.zero_fraction`
* `tf.compat.v1.nn.zero_fraction`
* `tf.compat.v2.math.zero_fraction`
* `tf.compat.v2.nn.zero_fraction`
* `tf.nn.zero_fraction`


``` python
tf.math.zero_fraction(
    value,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If `value` is empty, the result is `nan`.

This is useful in summaries to measure and report sparsity.  For example,

```python
    z = tf.nn.relu(...)
    summ = tf.compat.v1.summary.scalar('sparsity', tf.nn.zero_fraction(z))
```

#### Args:


* <b>`value`</b>: A tensor of numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The fraction of zeros in `value`, with type `float32`.
