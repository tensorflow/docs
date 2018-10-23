

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.sdca_optimizer

### `tf.train.sdca_optimizer`

``` python
sdca_optimizer(
    sparse_example_indices,
    sparse_feature_indices,
    sparse_feature_values,
    dense_features,
    example_weights,
    example_labels,
    sparse_indices,
    sparse_weights,
    dense_weights,
    example_state_data,
    loss_type,
    l1,
    l2,
    num_loss_partitions,
    num_inner_iterations,
    adaptative=None,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_sdca_ops.py`.

Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

linear models with L1 + L2 regularization. As global optimization objective is
strongly-convex, the optimizer optimizes the dual objective at each step. The
optimizer applies each update one example at a time. Examples are sampled
uniformly, and the optimizer is learning rate free and enjoys linear convergence
rate.

[Proximal Stochastic Dual Coordinate Ascent](http://arxiv.org/pdf/1211.2717v1.pdf).<br>
Shai Shalev-Shwartz, Tong Zhang. 2012

<div> $$Loss Objective = \sum f_{i} (wx_{i}) + (l2 / 2) * |w|^2 + l1 * |w|$$ </div>

[Adding vs. Averaging in Distributed Primal-Dual Optimization](http://arxiv.org/abs/1502.03508).<br>
Chenxin Ma, Virginia Smith, Martin Jaggi, Michael I. Jordan,
Peter Richtarik, Martin Takac. 2015

[Stochastic Dual Coordinate Ascent with Adaptive Probabilities](https://arxiv.org/abs/1502.08053).<br>
Dominik Csiba, Zheng Qu, Peter Richtarik. 2015

#### Args:

* <b>`sparse_example_indices`</b>: A list of `Tensor` objects with type `int64`.
    a list of vectors which contain example indices.
* <b>`sparse_feature_indices`</b>: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
    a list of vectors which contain feature indices.
* <b>`sparse_feature_values`</b>: A list of `Tensor` objects with type `float32`.
    a list of vectors which contains feature value
    associated with each feature group.
* <b>`dense_features`</b>: A list of `Tensor` objects with type `float32`.
    a list of matrices which contains the dense feature values.
* <b>`example_weights`</b>: A `Tensor` of type `float32`.
    a vector which contains the weight associated with each
    example.
* <b>`example_labels`</b>: A `Tensor` of type `float32`.
    a vector which contains the label/target associated with each
    example.
* <b>`sparse_indices`</b>: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `int64`.
    a list of vectors where each value is the indices which has
    corresponding weights in sparse_weights. This field maybe omitted for the
    dense approach.
* <b>`sparse_weights`</b>: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`.
    a list of vectors where each value is the weight associated with
    a sparse feature group.
* <b>`dense_weights`</b>: A list with the same length as `dense_features` of `Tensor` objects with type `float32`.
    a list of vectors where the values are the weights associated
    with a dense feature group.
* <b>`example_state_data`</b>: A `Tensor` of type `float32`.
    a list of vectors containing the example state data.
* <b>`loss_type`</b>: A `string` from: `"logistic_loss", "squared_loss", "hinge_loss", "smooth_hinge_loss"`.
    Type of the primal loss. Currently SdcaSolver supports logistic,
    squared and hinge losses.
* <b>`l1`</b>: A `float`. Symmetric l1 regularization strength.
* <b>`l2`</b>: A `float`. Symmetric l2 regularization strength.
* <b>`num_loss_partitions`</b>: An `int` that is `>= 1`.
    Number of partitions of the global loss function.
* <b>`num_inner_iterations`</b>: An `int` that is `>= 1`.
    Number of iterations per mini-batch.
* <b>`adaptative`</b>: An optional `bool`. Defaults to `False`.
    Whether to use Adapative SDCA for the inner loop.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A tuple of `Tensor` objects (out_example_state_data, out_delta_sparse_weights, out_delta_dense_weights).

* <b>`out_example_state_data`</b>: A `Tensor` of type `float32`. a list of vectors containing the updated example state
    data.
* <b>`out_delta_sparse_weights`</b>: A list with the same length as `sparse_example_indices` of `Tensor` objects with type `float32`. a list of vectors where each value is the delta
    weights associated with a sparse feature group.
* <b>`out_delta_dense_weights`</b>: A list with the same length as `dense_features` of `Tensor` objects with type `float32`. a list of vectors where the values are the delta
    weights associated with a dense feature group.