

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_blocks.FullyConnectedDiagonalFB

## Class `FullyConnectedDiagonalFB`

Inherits From: [`FisherBlock`](../../../../tf/contrib/kfac/fisher_blocks/FisherBlock)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for fully-connected (dense) layers using a diagonal approx.

Unlike NaiveDiagonalFB this uses the low-variance "sum of squares" estimator
that is computed using the well-known trick.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    inputs,
    outputs,
    has_bias=False
)
```

Creates a FullyConnectedDiagonalFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`inputs`</b>: The Tensor of input activations to this layer.
* <b>`outputs`</b>: The Tensor of output pre-activations from this layer.
* <b>`has_bias`</b>: Whether the component Kronecker factors have an additive bias.
      (Default: False)

<h3 id="instantiate_factors"><code>instantiate_factors</code></h3>

``` python
instantiate_factors(
    grads_list,
    damping
)
```



<h3 id="multiply"><code>multiply</code></h3>

``` python
multiply(vector)
```



<h3 id="multiply_inverse"><code>multiply_inverse</code></h3>

``` python
multiply_inverse(vector)
```



<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```





