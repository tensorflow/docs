description: Repeat elements of input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.repeat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.repeat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L5767-L5818">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Repeat elements of `input`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.repeat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.repeat(
    input, repeats, axis=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/concat.md"><code>tf.concat</code></a>, <a href="../tf/stack.md"><code>tf.stack</code></a>, <a href="../tf/tile.md"><code>tf.tile</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
An `N`-dimensional Tensor.
</td>
</tr><tr>
<td>
`repeats`
</td>
<td>
An 1-D `int` Tensor. The number of repetitions for each element.
repeats is broadcasted to fit the shape of the given axis. `len(repeats)`
must equal `input.shape[axis]` if axis is not None.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An int. The axis along which to repeat values. By default (axis=None),
use the flattened input array, and return a flat output array.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Tensor which has the same shape as `input`, except along the given axis.
If axis is None then the output array is flattened to match the flattened
input array.
</td>
</tr>

</table>



#### Example usage:



```
>>> repeat(['a', 'b', 'c'], repeats=[3, 0, 2], axis=0)
<tf.Tensor: shape=(5,), dtype=string,
numpy=array([b'a', b'a', b'a', b'c', b'c'], dtype=object)>
```

```
>>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=0)
<tf.Tensor: shape=(5, 2), dtype=int32, numpy=
array([[1, 2],
       [1, 2],
       [3, 4],
       [3, 4],
       [3, 4]], dtype=int32)>
```

```
>>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=1)
<tf.Tensor: shape=(2, 5), dtype=int32, numpy=
array([[1, 1, 2, 2, 2],
       [3, 3, 4, 4, 4]], dtype=int32)>
```

```
>>> repeat(3, repeats=4)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([3, 3, 3, 3], dtype=int32)>
```

```
>>> repeat([[1,2], [3,4]], repeats=2)
<tf.Tensor: shape=(8,), dtype=int32,
numpy=array([1, 1, 2, 2, 3, 3, 4, 4], dtype=int32)>
```