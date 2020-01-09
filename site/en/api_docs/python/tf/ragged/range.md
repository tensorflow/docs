page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.range


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/ragged/range">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_math_ops.py#L41-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a `RaggedTensor` containing the specified sequences of numbers.

### Aliases:

* <a href="/api_docs/python/tf/ragged/range"><code>tf.compat.v1.ragged.range</code></a>
* <a href="/api_docs/python/tf/ragged/range"><code>tf.compat.v2.ragged.range</code></a>


``` python
tf.ragged.range(
    starts,
    limits=None,
    deltas=1,
    dtype=None,
    name=None,
    row_splits_dtype=tf.dtypes.int64
)
```



<!-- Placeholder for "Used in" -->

Each row of the returned `RaggedTensor` contains a single sequence:

```python
ragged.range(starts, limits, deltas)[i] ==
    tf.range(starts[i], limits[i], deltas[i])
```

If `start[i] < limits[i] and deltas[i] > 0`, then `output[i]` will be an
empty list.  Similarly, if `start[i] > limits[i] and deltas[i] < 0`, then
`output[i]` will be an empty list.  This behavior is consistent with the
Python `range` function, but differs from the <a href="../../tf/range"><code>tf.range</code></a> op, which returns
an error for these cases.

#### Examples:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}ragged.range([3, 5, 2]).eval().tolist(){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}[[0, 1, 2], [0, 1, 2, 3, 4], [0, 1]]{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}ragged.range([0, 5, 8], [3, 3, 12]).eval().tolist(){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}[[0, 1, 2], [], [8, 9, 10, 11]]{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}ragged.range([0, 5, 8], [3, 3, 12], 2).eval().tolist(){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}[[0, 2], [], [8, 10]]{% endhtmlescape %}</code>
</pre>

The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors.
The vector inputs must all have the same size.  Scalar inputs are broadcast
to match the size of the vector inputs.

#### Args:


* <b>`starts`</b>: Vector or scalar `Tensor`.  Specifies the first entry for each range
  if `limits` is not `None`; otherwise, specifies the range limits, and the
  first entries default to `0`.
* <b>`limits`</b>: Vector or scalar `Tensor`.  Specifies the exclusive upper limits for
  each range.
* <b>`deltas`</b>: Vector or scalar `Tensor`.  Specifies the increment for each range.
  Defaults to `1`.
* <b>`dtype`</b>: The type of the elements of the resulting tensor.  If not specified,
  then a value is chosen based on the other args.
* <b>`name`</b>: A name for the operation.
* <b>`row_splits_dtype`</b>: `dtype` for the returned `RaggedTensor`'s `row_splits`
  tensor.  One of <a href="../../tf#int32"><code>tf.int32</code></a> or <a href="../../tf#int64"><code>tf.int64</code></a>.


#### Returns:

A `RaggedTensor` of type `dtype` with `ragged_rank=1`.
