description: Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.sdca_optimizer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.sdca_optimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.sdca_optimizer(
    sparse_example_indices, sparse_feature_indices, sparse_feature_values,
    dense_features, example_weights, example_labels, sparse_indices, sparse_weights,
    dense_weights, example_state_data, loss_type, l1, l2, num_loss_partitions,
    num_inner_iterations, adaptative=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

linear models with L1 + L2 regularization. As global optimization objective is
strongly-convex, the optimizer optimizes the dual objective at each step. The
optimizer applies each update one example at a time. Examples are sampled
uniformly, and the optimizer is learning rate free and enjoys linear convergence
rate.

[Proximal Stochastic Dual Coordinate Ascent](http://arxiv.org/pdf/1211.2717v1.pdf).<br>
Shai Shalev-Shwartz, Tong Zhang. 2012

$$Loss Objective = \sum f_{i} (wx_{i}) + (l2 / 2) * |w|^2 + l1 * |w|$$

[Adding vs. Averaging in Distributed Primal-Dual Optimization](http://arxiv.org/abs/1502.03508).<br>
Chenxin Ma, Virginia Smith, Martin Jaggi, Michael I. Jordan,
Peter Richtarik, Martin Takac. 2015

[Stochastic Dual Coordinate Ascent with Adaptive Probabilities](https://arxiv.org/abs/1502.08053).<br>
Dominik Csiba, Zheng Qu, Peter Richtarik. 2015

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sparse_example_indices`
</td>
<td>
A list of `Tensor` objects with type `int64`.
a list of vectors which contain example indices.
</td>
</tr><tr>
<td>
`sparse_feature_indices`
</td>
<td>
A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
a list of vectors which contain feature indices.
</td>
</tr><tr>
<td>
`sparse_feature_values`
</td>
<td>
A list of `Tensor` objects with type `float32`.
a list of vectors which contains feature value
associated with each feature group.
</td>
</tr><tr>
<td>
`dense_features`
</td>
<td>
A list of `Tensor` objects with type `float32`.
a list of matrices which contains the dense feature values.
</td>
</tr><tr>
<td>
`example_weights`
</td>
<td>
A `Tensor` of type `float32`.
a vector which contains the weight associated with each
example.
</td>
</tr><tr>
<td>
`example_labels`
</td>
<td>
A `Tensor` of type `float32`.
a vector which contains the label/target associated with each
example.
</td>
</tr><tr>
<td>
`sparse_indices`
</td>
<td>
A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
a list of vectors where each value is the indices which has
corresponding weights in sparse_weights. This field maybe omitted for the
dense approach.
</td>
</tr><tr>
<td>
`sparse_weights`
</td>
<td>
A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
a list of vectors where each value is the weight associated with
a sparse feature group.
</td>
</tr><tr>
<td>
`dense_weights`
</td>
<td>
A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
a list of vectors where the values are the weights associated
with a dense feature group.
</td>
</tr><tr>
<td>
`example_state_data`
</td>
<td>
A `Tensor` of type `float32`.
a list of vectors containing the example state data.
</td>
</tr><tr>
<td>
`loss_type`
</td>
<td>
A `string` from: `"logistic_loss", "squared_loss", "hinge_loss", "smooth_hinge_loss", "poisson_loss"`.
Type of the primal loss. Currently SdcaSolver supports logistic,
squared and hinge losses.
</td>
</tr><tr>
<td>
`l1`
</td>
<td>
A `float`. Symmetric l1 regularization strength.
</td>
</tr><tr>
<td>
`l2`
</td>
<td>
A `float`. Symmetric l2 regularization strength.
</td>
</tr><tr>
<td>
`num_loss_partitions`
</td>
<td>
An `int` that is `>= 1`.
Number of partitions of the global loss function.
</td>
</tr><tr>
<td>
`num_inner_iterations`
</td>
<td>
An `int` that is `>= 1`.
Number of iterations per mini-batch.
</td>
</tr><tr>
<td>
`adaptative`
</td>
<td>
An optional `bool`. Defaults to `True`.
Whether to use Adaptive SDCA for the inner loop.
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
A tuple of `Tensor` objects (out_example_state_data, out_delta_sparse_weights, out_delta_dense_weights).
</td>
</tr>
<tr>
<td>
`out_example_state_data`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`out_delta_sparse_weights`
</td>
<td>
A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
</td>
</tr><tr>
<td>
`out_delta_dense_weights`
</td>
<td>
A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
</td>
</tr>
</table>

