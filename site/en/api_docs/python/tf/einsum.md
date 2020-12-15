description: Tensor contraction over specified indices and outer product.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.einsum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.einsum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/special_math_ops.py#L606-L751">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tensor contraction over specified indices and outer product.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.linalg.einsum`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.einsum`, `tf.compat.v1.linalg.einsum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.einsum(
    equation, *inputs, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Einsum allows defining Tensors by defining their element-wise computation.
This computation is defined by `equation`, a shorthand form based on Einstein
summation. As an example, consider multiplying two matrices A and B to form a
matrix C.  The elements of C are given by:

$$ C_{i,k} = \sum_j A_{i,j} B_{j,k} $$

or

```
C[i,k] = sum_j A[i,j] * B[j,k]
```

The corresponding einsum `equation` is:

```
ij,jk->ik
```

In general, to convert the element-wise equation into the `equation` string,
use the following procedure (intermediate strings for matrix multiplication
example provided in parentheses):

1. remove variable names, brackets, and commas, (`ik = sum_j ij * jk`)
2. replace "*" with ",", (`ik = sum_j ij , jk`)
3. drop summation signs, and (`ik = ij, jk`)
4. move the output to the right, while replacing "=" with "->". (`ij,jk->ik`)

Note: If the output indices are not specified repeated indices are summed.
So `ij,jk->ik` can be simplified to `ij,jk`.

Many common operations can be expressed in this way.  For example:

**Matrix multiplication**

```
>>> m0 = tf.random.normal(shape=[2, 3])
>>> m1 = tf.random.normal(shape=[3, 5])
>>> e = tf.einsum('ij,jk->ik', m0, m1)
>>> # output[i,k] = sum_j m0[i,j] * m1[j, k]
>>> print(e.shape)
(2, 5)
```

Repeated indices are summed if the output indices are not specified.

```
>>> e = tf.einsum('ij,jk', m0, m1)  # output[i,k] = sum_j m0[i,j] * m1[j, k]
>>> print(e.shape)
(2, 5)
```


**Dot product**

```
>>> u = tf.random.normal(shape=[5])
>>> v = tf.random.normal(shape=[5])
>>> e = tf.einsum('i,i->', u, v)  # output = sum_i u[i]*v[i]
>>> print(e.shape)
()
```

**Outer product**

```
>>> u = tf.random.normal(shape=[3])
>>> v = tf.random.normal(shape=[5])
>>> e = tf.einsum('i,j->ij', u, v)  # output[i,j] = u[i]*v[j]
>>> print(e.shape)
(3, 5)
```

**Transpose**

```
>>> m = tf.ones(2,3)
>>> e = tf.einsum('ij->ji', m0)  # output[j,i] = m0[i,j]
>>> print(e.shape)
(3, 2)
```

**Diag**

```
>>> m = tf.reshape(tf.range(9), [3,3])
>>> diag = tf.einsum('ii->i', m)
>>> print(diag.shape)
(3,)
```

**Trace**

```
>>> # Repeated indices are summed.
>>> trace = tf.einsum('ii', m)  # output[j,i] = trace(m) = sum_i m[i, i]
>>> assert trace == sum(diag)
>>> print(trace.shape)
()
```

**Batch matrix multiplication**

```
>>> s = tf.random.normal(shape=[7,5,3])
>>> t = tf.random.normal(shape=[7,3,2])
>>> e = tf.einsum('bij,bjk->bik', s, t)
>>> # output[a,i,k] = sum_j s[a,i,j] * t[a, j, k]
>>> print(e.shape)
(7, 5, 2)
```

This method does not support broadcasting on named-axes. All axes with
matching labels should have the same length. If you have length-1 axes,
use `tf.squeseze` or <a href="../tf/reshape.md"><code>tf.reshape</code></a> to eliminate them.

To write code that is agnostic to the number of indices in the input
use an ellipsis. The ellipsis is a placeholder for "whatever other indices
fit here".

For example, to perform a NumPy-style broadcasting-batch-matrix multiplication
where the matrix multiply acts on the last two axes of the input, use:

```
>>> s = tf.random.normal(shape=[11, 7, 5, 3])
>>> t = tf.random.normal(shape=[11, 7, 3, 2])
>>> e =  tf.einsum('...ij,...jk->...ik', s, t)
>>> print(e.shape)
(11, 7, 5, 2)
```

Einsum **will** broadcast over axes covered by the ellipsis.

```
>>> s = tf.random.normal(shape=[11, 1, 5, 3])
>>> t = tf.random.normal(shape=[1, 7, 3, 2])
>>> e =  tf.einsum('...ij,...jk->...ik', s, t)
>>> print(e.shape)
(11, 7, 5, 2)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`equation`
</td>
<td>
a `str` describing the contraction, in the same format as
`numpy.einsum`.
</td>
</tr><tr>
<td>
`*inputs`
</td>
<td>
the inputs to contract (each one a `Tensor`), whose shapes should
be consistent with `equation`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
- optimize: Optimization strategy to use to find contraction path using
opt_einsum. Must be 'greedy', 'optimal', 'branch-2', 'branch-all' or
'auto'. (optional, default: 'greedy').
- name: A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The contracted `Tensor`, with shape determined by `equation`.
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
If
- the format of `equation` is incorrect,
- number of inputs or their shapes are inconsistent with `equation`.
</td>
</tr>
</table>

