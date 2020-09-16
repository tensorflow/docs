description: Computes the norm of vectors, matrices, and tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.norm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.norm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/linalg_ops.py#L544-L611">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the norm of vectors, matrices, and tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.linalg.norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.norm(
    tensor, ord='euclidean', axis=None, keepdims=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function can compute several different vector norms (the 1-norm, the
Euclidean or 2-norm, the inf-norm, and in general the p-norm for p > 0) and
matrix norms (Frobenius, 1-norm, 2-norm and inf-norm).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
`Tensor` of types `float32`, `float64`, `complex64`, `complex128`
</td>
</tr><tr>
<td>
`ord`
</td>
<td>
Order of the norm. Supported values are `'fro'`, `'euclidean'`,
`1`, `2`, `np.inf` and any positive real number yielding the corresponding
p-norm. Default is `'euclidean'` which is equivalent to Frobenius norm if
`tensor` is a matrix and equivalent to 2-norm for vectors.
Some restrictions apply:
a) The Frobenius norm `'fro'` is not defined for vectors,
b) If axis is a 2-tuple (matrix norm), only `'euclidean'`, '`fro'`, `1`,
`2`, `np.inf` are supported.
See the description of `axis` on how to compute norms for a batch of
vectors or matrices stored in a tensor.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
If `axis` is `None` (the default), the input is considered a vector
and a single vector norm is computed over the entire set of values in the
tensor, i.e. `norm(tensor, ord=ord)` is equivalent to
`norm(reshape(tensor, [-1]), ord=ord)`.
If `axis` is a Python integer, the input is considered a batch of vectors,
and `axis` determines the axis in `tensor` over which to compute vector
norms.
If `axis` is a 2-tuple of Python integers it is considered a batch of
matrices and `axis` determines the axes in `tensor` over which to compute
a matrix norm.
Negative indices are supported. Example: If you are passing a tensor that
can be either a matrix or a batch of matrices at runtime, pass
`axis=[-2,-1]` instead of `axis=None` to make sure that matrix norms are
computed.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
If True, the axis indicated in `axis` are kept with size 1.
Otherwise, the dimensions in `axis` are removed from the output shape.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`output`
</td>
<td>
A `Tensor` of the same type as tensor, containing the vector or
matrix norms. If `keepdims` is True then the rank of output is equal to
the rank of `tensor`. Otherwise, if `axis` is none the output is a scalar,
if `axis` is an integer, the rank of `output` is one less than the rank
of `tensor`, if `axis` is a 2-tuple the rank of `output` is two less
than the rank of `tensor`.
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
If `ord` or `axis` is invalid.
</td>
</tr>
</table>




#### Numpy Compatibility
Mostly equivalent to numpy.linalg.norm.
Not supported: ord <= 0, 2-norm for matrices, nuclear norm.
Other differences:
  a) If axis is `None`, treats the flattened `tensor` as a vector
   regardless of rank.
  b) Explicitly supports 'euclidean' norm as the default, including for
   higher order tensors.

