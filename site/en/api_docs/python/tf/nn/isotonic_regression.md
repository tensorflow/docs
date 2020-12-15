description: Solves isotonic regression problems along the given axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.isotonic_regression" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.isotonic_regression

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L5759-L5831">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Solves isotonic regression problems along the given axis.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.isotonic_regression(
    inputs, decreasing=(True), axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->

For each vector x, the problem solved is

$$\argmin_{y_1 >= y_2 >= ... >= y_n} \sum_i (x_i - y_i)^2.$$

As the solution is component-wise constant, a second tensor is returned that
encodes the segments. The problems are solved over the given axis.

Consider the following example, where we solve a batch of two problems. The
first input is [3, 1, 2], while the second [1, 3, 4] (as the axis is 1).
>>> x = tf.constant([[3, 1, 2], [1, 3, 4]], dtype=tf.float32)
>>> y, segments = tf.nn.isotonic_regression(x, axis=1)
>>> y  # The solution.
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[3.       , 1.5      , 1.5      ],
       [2.6666667, 2.6666667, 2.6666667]], dtype=float32)>

Note that the first solution has two blocks [2] and [1.5, 1.5]. The second
solution is constant, and thus has a single segment. These segments are
exactly what the second returned tensor encodes:

```
>>> segments
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[0, 1, 1],
       [0, 0, 0]], dtype=int32)>
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A tensor holding the inputs.
</td>
</tr><tr>
<td>
`decreasing`
</td>
<td>
If set to False, the inequalities in the optimizing constrained
are flipped.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis along which the problems should be solved.
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
The solutions, same shape as type as the input.
</td>
</tr><tr>
<td>
`segments`
</td>
<td>
An int32 tensor, same shape as the input indicating the segments
that have the same value. Specifically, those positions that have the same
value correspond to the same segment. These values start at zero, and are
monotonously increasing for each solution.
</td>
</tr>
</table>

