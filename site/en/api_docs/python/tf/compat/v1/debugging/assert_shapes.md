description: Assert tensor shapes and dimension size relationships between tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.debugging.assert_shapes" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.debugging.assert_shapes

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L1694-L1947">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Assert tensor shapes and dimension size relationships between tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.debugging.assert_shapes(
    shapes, data=None, summarize=None, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op checks that a collection of tensors shape relationships
satisfies given constraints.

#### Example:



```
>>> n = 10
>>> q = 3
>>> d = 7
>>> x = tf.zeros([n,q])
>>> y = tf.ones([n,d])
>>> param = tf.Variable([1.0, 2.0, 3.0])
>>> scalar = 1.0
>>> tf.debugging.assert_shapes([
...  (x, ('N', 'Q')),
...  (y, ('N', 'D')),
...  (param, ('Q',)),
...  (scalar, ()),
... ])
```

```
>>> tf.debugging.assert_shapes([
...   (x, ('N', 'D')),
...   (y, ('N', 'D'))
... ])
Traceback (most recent call last):
...
ValueError: ...
```

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.assert_shapes(shapes)]):
  output = tf.matmul(x, y, transpose_a=True)
```

If `x`, `y`, `param` or `scalar` does not have a shape that satisfies
all specified constraints, `message`, as well as the first `summarize` entries
of the first encountered violating tensor are printed, and
`InvalidArgumentError` is raised.

Size entries in the specified shapes are checked against other entries by
their __hash__, except:
  - a size entry is interpreted as an explicit size if it can be parsed as an
    integer primitive.
  - a size entry is interpreted as *any* size if it is None or '.'.

If the first entry of a shape is `...` (type `Ellipsis`) or '*' that indicates
a variable number of outer dimensions of unspecified size, i.e. the constraint
applies to the inner-most dimensions only.

Scalar tensors and specified shapes of length zero (excluding the 'inner-most'
prefix) are both treated as having a single dimension of size one.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shapes`
</td>
<td>
A list of (`Tensor`, `shape`) tuples, wherein `shape` is the
expected shape of `Tensor`. See the example code above. The `shape` must
be an iterable. Each element of the iterable can be either a concrete
integer value or a string that abstractly represents the dimension.
For example,
- `('N', 'Q')` specifies a 2D shape wherein the first and second
dimensions of shape may or may not be equal.
- `('N', 'N', 'Q')` specifies a 3D shape wherein the first and second
dimensions are equal.
- `(1, 'N')` specifies a 2D shape wherein the first dimension is
exactly 1 and the second dimension can be any value.
Note that the abstract dimension letters take effect across different
tuple elements of the list. For example,
`tf.debugging.assert_shapes([(x, ('N', 'A')), (y, ('N', 'B'))]` asserts
that both `x` and `y` are rank-2 tensors and their first dimensions are
equal (`N`).
`shape` can also be a <a href="../../../../tf/TensorShape.md"><code>tf.TensorShape</code></a>.
</td>
</tr><tr>
<td>
`data`
</td>
<td>
The tensors to print out if the condition is False.  Defaults to error
message and first few entries of the violating tensor.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
Print this many entries of the tensor.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
A string to prefix to the default message.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).  Defaults to "assert_shapes".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op raising `InvalidArgumentError` unless all shape constraints are
satisfied.
If static checks determine all constraints are satisfied, a `no_op` is
returned.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If static checks determine any shape constraint is violated.
</td>
</tr>
</table>

