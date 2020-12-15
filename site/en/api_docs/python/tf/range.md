description: Creates a sequence of numbers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.range" />
<meta itemprop="path" content="Stable" />
</div>

# tf.range

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1796-L1877">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a sequence of numbers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.range`</p>
</p>
</section>


```python
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



```
>>> start = 3
>>> limit = 18
>>> delta = 3
>>> tf.range(start, limit, delta)
<tf.Tensor: shape=(5,), dtype=int32,
numpy=array([ 3,  6,  9, 12, 15], dtype=int32)>
```

```
>>> start = 3
>>> limit = 1
>>> delta = -0.5
>>> tf.range(start, limit, delta)
<tf.Tensor: shape=(4,), dtype=float32,
numpy=array([3. , 2.5, 2. , 1.5], dtype=float32)>
```

```
>>> limit = 5
>>> tf.range(limit)
<tf.Tensor: shape=(5,), dtype=int32,
numpy=array([0, 1, 2, 3, 4], dtype=int32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`start`
</td>
<td>
A 0-D `Tensor` (scalar). Acts as first entry in the range if `limit`
is not None; otherwise, acts as range limit and first entry defaults to 0.
</td>
</tr><tr>
<td>
`limit`
</td>
<td>
A 0-D `Tensor` (scalar). Upper limit of sequence, exclusive. If None,
defaults to the value of `start` while the first entry of the range
defaults to 0.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
A 0-D `Tensor` (scalar). Number that increments `start`. Defaults to
1.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the elements of the resulting tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation. Defaults to "range".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An 1-D `Tensor` of type `dtype`.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to np.arange

