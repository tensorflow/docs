

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_blocks.ConvKFCBasicFB

## Class `ConvKFCBasicFB`

Inherits From: [`KroneckerProductFB`](../../../../tf/contrib/kfac/fisher_blocks/KroneckerProductFB)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for convolutional layers using the basic KFC approx.

Estimates the Fisher Information matrix's blog for a convolutional
layer.

Consider a convoluational layer in this model with (unshared) filter matrix
'w'. For a minibatch that produces inputs 'a' and output preactivations 's',
this FisherBlock estimates,

<div>   $$F(w) = \#locations * kronecker(E[flat(a) flat(a)^T],
                                E[flat(ds) flat(ds)^T])$$</div>

where

<div>   $$ds = (d / ds) log p(y | x, w)$$ </div>
  #locations = number of (x, y) locations where 'w' is applied.

where the expectation is taken over all examples and locations and flat()
concatenates an array's leading dimensions.

See equation 23 in https://arxiv.org/abs/1602.01407 for details.

## Properties

<h3 id="num_registered_towers"><code>num_registered_towers</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    params,
    padding,
    strides=None,
    dilation_rate=None,
    data_format=None,
    extract_patches_fn=None
)
```

Creates a ConvKFCBasicFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`params`</b>: The parameters (Tensor or tuple of Tensors) of this layer. If
    kernel alone, a Tensor of shape [..spatial_filter_shape..,
    in_channels, out_channels]. If kernel and bias, a tuple of 2 elements
    containing the previous and a Tensor of shape [out_channels].
* <b>`padding`</b>: str. Padding method.
* <b>`strides`</b>: List of ints or None. Contains [..spatial_filter_strides..] if
    'extract_patches_fn' is compatible with tf.nn.convolution(), else
    [1, ..spatial_filter_strides, 1].
* <b>`dilation_rate`</b>: List of ints or None. Rate for dilation along each spatial
    dimension if 'extract_patches_fn' is compatible with
    tf.nn.convolution(), else [1, ..spatial_dilation_rates.., 1].
* <b>`data_format`</b>: str or None. Format of input data.
* <b>`extract_patches_fn`</b>: str or None. Name of function that extracts image
    patches. One of "extract_convolution_patches", "extract_image_patches",
    "extract_pointwise_conv2d_patches".

<h3 id="full_fisher_block"><code>full_fisher_block</code></h3>

``` python
full_fisher_block()
```

Explicitly constructs the full Fisher block.

Used for testing purposes. (In general, the result may be very large.)

#### Returns:

The full Fisher block.

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



