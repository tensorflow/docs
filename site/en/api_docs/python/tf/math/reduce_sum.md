description: Computes the sum of elements across dimensions of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.reduce_sum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.reduce_sum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L1921-L1984">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the sum of elements across dimensions of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.reduce_sum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.reduce_sum(
    input_tensor, axis=None, keepdims=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### For example:



```
>>> # x has a shape of (2, 3) (two rows and three columns):
>>> x = tf.constant([[1, 1, 1], [1, 1, 1]])
>>> x.numpy()
array([[1, 1, 1],
       [1, 1, 1]], dtype=int32)
>>> # sum all the elements
>>> # 1 + 1 + 1 + 1 + 1+ 1 = 6
>>> tf.reduce_sum(x).numpy()
6
>>> # reduce along the first dimension
>>> # the result is [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
>>> tf.reduce_sum(x, 0).numpy()
array([2, 2, 2], dtype=int32)
>>> # reduce along the second dimension
>>> # the result is [1, 1] + [1, 1] + [1, 1] = [3, 3]
>>> tf.reduce_sum(x, 1).numpy()
array([3, 3], dtype=int32)
>>> # keep the original dimensions
>>> tf.reduce_sum(x, 1, keepdims=True).numpy()
array([[3],
       [3]], dtype=int32)
>>> # reduce along both dimensions
>>> # the result is 1 + 1 + 1 + 1 + 1 + 1 = 6
>>> # or, equivalently, reduce along rows, then reduce the resultant array
>>> # [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
>>> # 2 + 2 + 2 = 6
>>> tf.reduce_sum(x, [0, 1]).numpy()
6
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_tensor`
</td>
<td>
The tensor to reduce. Should have numeric type.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The dimensions to reduce. If `None` (the default), reduces all
dimensions. Must be in the range `[-rank(input_tensor),
rank(input_tensor)]`.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
If true, retains reduced dimensions with length 1.
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
The reduced tensor, of the same dtype as the input_tensor.
</td>
</tr>

</table>




#### Numpy Compatibility
Equivalent to np.sum apart the fact that numpy upcast uint8 and int32 to
int64 while tensorflow returns the same dtype as the input.

