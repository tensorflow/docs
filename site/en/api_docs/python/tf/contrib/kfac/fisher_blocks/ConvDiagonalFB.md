page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_blocks.ConvDiagonalFB

## Class `ConvDiagonalFB`





Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for 2-D convolutional layers using a diagonal approx.

Estimates the Fisher Information matrix's diagonal entries for a convolutional
layer. Unlike NaiveDiagonalFB this uses the low-variance "sum of squares"
estimator.

Let 'params' be a vector parameterizing a model and 'i' an arbitrary index
into it. We are interested in Fisher(params)[i, i]. This is,

<div>   $$Fisher(params)[i, i] = E[ v(x, y, params) v(x, y, params)^T ][i, i]
                       = E[ v(x, y, params)[i] ^ 2 ]$$</div>

Consider a convoluational layer in this model with (unshared) filter matrix
'w'. For an example image 'x' that produces layer inputs 'a' and output
preactivations 's',

<div>   $$v(x, y, w) = vec( sum_{loc} a_{loc} (d loss / d s_{loc})^T )$$ </div>

where 'loc' is a single (x, y) location in an image.

This FisherBlock tracks Fisher(params)[i, i] for all indices 'i' corresponding
to the layer's parameters 'w'.

## Properties

<h3 id="num_registered_towers"><code>num_registered_towers</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    params,
    strides,
    padding,
    data_format=None,
    dilations=None
)
```

Creates a ConvDiagonalFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`params`</b>: The parameters (Tensor or tuple of Tensors) of this layer. If
    kernel alone, a Tensor of shape [kernel_height, kernel_width,
    in_channels, out_channels]. If kernel and bias, a tuple of 2 elements
    containing the previous and a Tensor of shape [out_channels].
* <b>`strides`</b>: The stride size in this layer (1-D Tensor of length 4).
* <b>`padding`</b>: The padding in this layer (e.g. "SAME").
* <b>`data_format`</b>: str or None. Format of input data.
* <b>`dilations`</b>: List of 4 ints or None. Rate for dilation along all dimensions.


#### Raises:

* <b>`ValueError`</b>: if strides is not length-4.
* <b>`ValueError`</b>: if dilations is not length-4.
* <b>`ValueError`</b>: if channel is not last dimension.

<h3 id="full_fisher_block"><code>full_fisher_block</code></h3>

``` python
full_fisher_block()
```



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

Multiplies the vector by the (damped) block.

#### Args:

* <b>`vector`</b>: The vector (a Tensor or tuple of Tensors) to be multiplied.


#### Returns:

The vector left-multiplied by the (damped) block.

<h3 id="multiply_cholesky"><code>multiply_cholesky</code></h3>

``` python
multiply_cholesky(
    vector,
    transpose=False
)
```



<h3 id="multiply_cholesky_inverse"><code>multiply_cholesky_inverse</code></h3>

``` python
multiply_cholesky_inverse(
    vector,
    transpose=False
)
```



<h3 id="multiply_inverse"><code>multiply_inverse</code></h3>

``` python
multiply_inverse(vector)
```

Multiplies the vector by the (damped) inverse of the block.

#### Args:

* <b>`vector`</b>: The vector (a Tensor or tuple of Tensors) to be multiplied.


#### Returns:

The vector left-multiplied by the (damped) inverse of the block.

<h3 id="multiply_matpower"><code>multiply_matpower</code></h3>

``` python
multiply_matpower(
    vector,
    exp
)
```



<h3 id="register_additional_tower"><code>register_additional_tower</code></h3>

``` python
register_additional_tower(
    inputs,
    outputs
)
```



<h3 id="register_cholesky"><code>register_cholesky</code></h3>

``` python
register_cholesky()
```



<h3 id="register_cholesky_inverse"><code>register_cholesky_inverse</code></h3>

``` python
register_cholesky_inverse()
```



<h3 id="register_inverse"><code>register_inverse</code></h3>

``` python
register_inverse()
```

Registers a matrix inverse to be computed by the block.

<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(exp)
```



<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```

Tensors to compute derivative of loss with respect to.



