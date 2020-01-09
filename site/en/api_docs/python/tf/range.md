page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.range


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/range">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L1358-L1427">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a sequence of numbers.

### Aliases:

* <a href="/api_docs/python/tf/range"><code>tf.compat.v1.range</code></a>
* <a href="/api_docs/python/tf/range"><code>tf.compat.v2.range</code></a>


``` python
tf.range(limit, delta=1, dtype=None, name='range')
tf.range(start, limit, delta=1, dtype=None, name='range')
```



<!-- Placeholder for "Used in" -->

Creates a sequence of numbers that begins at `start` and extends by
increments of `delta` up to but not including `limit`.

The dtype of the resulting tensor is inferred from the inputs unless
it is provided explicitly.

Like the Python builtin `range`, `start` defaults to 0, so that
`range(n) = range(0, n)`.

#### For example:



```python
start = 3
limit = 18
delta = 3
tf.range(start, limit, delta)  # [3, 6, 9, 12, 15]

start = 3
limit = 1
delta = -0.5
tf.range(start, limit, delta)  # [3, 2.5, 2, 1.5]

limit = 5
tf.range(limit)  # [0, 1, 2, 3, 4]
```

#### Args:


* <b>`start`</b>: A 0-D `Tensor` (scalar). Acts as first entry in the range if `limit`
  is not None; otherwise, acts as range limit and first entry defaults to 0.
* <b>`limit`</b>: A 0-D `Tensor` (scalar). Upper limit of sequence, exclusive. If None,
  defaults to the value of `start` while the first entry of the range
  defaults to 0.
* <b>`delta`</b>: A 0-D `Tensor` (scalar). Number that increments `start`. Defaults to
  1.
* <b>`dtype`</b>: The type of the elements of the resulting tensor.
* <b>`name`</b>: A name for the operation. Defaults to "range".


#### Returns:

An 1-D `Tensor` of type `dtype`.




#### Numpy Compatibility
Equivalent to np.arange
