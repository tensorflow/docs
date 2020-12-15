description: Transposes a, where a is a Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L2057-L2135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transposes `a`, where `a` is a Tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.transpose(
    a, perm=None, conjugate=(False), name='transpose'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Permutes the dimensions according to the value of `perm`.

The returned tensor's dimension `i` will correspond to the input dimension
`perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is the rank
of the input tensor. Hence by default, this operation performs a regular
matrix transpose on 2-D input Tensors.

If conjugate is `True` and `a.dtype` is either `complex64` or `complex128`
then the values of `a` are conjugated and transposed.



#### For example:



```
>>> x = tf.constant([[1, 2, 3], [4, 5, 6]])
>>> tf.transpose(x)
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
array([[1, 4],
       [2, 5],
       [3, 6]], dtype=int32)>
```

Equivalently, you could call `tf.transpose(x, perm=[1, 0])`.

If `x` is complex, setting conjugate=True gives the conjugate transpose:

```
>>> x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
...                  [4 + 4j, 5 + 5j, 6 + 6j]])
>>> tf.transpose(x, conjugate=True)
<tf.Tensor: shape=(3, 2), dtype=complex128, numpy=
array([[1.-1.j, 4.-4.j],
       [2.-2.j, 5.-5.j],
       [3.-3.j, 6.-6.j]])>
```

'perm' is more useful for n-dimensional tensors where n > 2:

```
>>> x = tf.constant([[[ 1,  2,  3],
...                   [ 4,  5,  6]],
...                  [[ 7,  8,  9],
...                   [10, 11, 12]]])
```

As above, simply calling <a href="../tf/transpose.md"><code>tf.transpose</code></a> will default to `perm=[2,1,0]`.

To take the transpose of the matrices in dimension-0 (such as when you are
transposing matrices where 0 is the batch dimesnion), you would set
`perm=[0,2,1]`.

```
>>> tf.transpose(x, perm=[0, 2, 1])
<tf.Tensor: shape=(2, 3, 2), dtype=int32, numpy=
array([[[ 1,  4],
        [ 2,  5],
        [ 3,  6]],
        [[ 7, 10],
        [ 8, 11],
        [ 9, 12]]], dtype=int32)>
```

Note: This has a shorthand <a href="../tf/linalg/matrix_transpose.md"><code>linalg.matrix_transpose</code></a>):

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`perm`
</td>
<td>
A permutation of the dimensions of `a`.  This should be a vector.
</td>
</tr><tr>
<td>
`conjugate`
</td>
<td>
Optional bool. Setting it to `True` is mathematically equivalent
to tf.math.conj(tf.transpose(input)).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A transposed `Tensor`.
</td>
</tr>

</table>



#### Numpy Compatibility
In `numpy` transposes are memory-efficient constant time operations as they
simply return a new view of the same data with adjusted `strides`.

TensorFlow does not support strides, so `transpose` returns a new tensor with
the items permuted.

