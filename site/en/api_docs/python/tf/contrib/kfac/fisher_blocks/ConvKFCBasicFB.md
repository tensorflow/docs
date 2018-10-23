

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_blocks.ConvKFCBasicFB

## Class `ConvKFCBasicFB`

Inherits From: [`KroneckerProductFB`](../../../../tf/contrib/kfac/fisher_blocks/KroneckerProductFB)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for 2D convolutional layers using the basic KFC approx.

Estimates the Fisher Information matrix's blog for a convolutional
layer.

Consider a convoluational layer in this model with (unshared) filter matrix
'w'. For a minibatch that produces inputs 'a' and output preactivations 's',
this FisherBlock estimates,

  F(w) = #locations * kronecker(E[flat(a) flat(a)^T],
                                E[flat(ds) flat(ds)^T])

where

  ds = (d / ds) log p(y | x, w)
  #locations = number of (x, y) locations where 'w' is applied.

where the expectation is taken over all examples and locations and flat()
concatenates an array's leading dimensions.

See equation 23 in https://arxiv.org/abs/1602.01407 for details.

## Properties

<h3 id="num_registered_minibatches"><code>num_registered_minibatches</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    params,
    strides,
    padding
)
```

Creates a ConvKFCBasicFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`params`</b>: The parameters (Tensor or tuple of Tensors) of this layer. If
    kernel alone, a Tensor of shape [kernel_height, kernel_width,
    in_channels, out_channels]. If kernel and bias, a tuple of 2 elements
    containing the previous and a Tensor of shape [out_channels].
* <b>`strides`</b>: The stride size in this layer (1-D Tensor of length 4).
* <b>`padding`</b>: The padding in this layer (1-D of Tensor length 4).

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



<h3 id="multiply_inverse"><code>multiply_inverse</code></h3>

``` python
multiply_inverse(vector)
```



<h3 id="register_additional_minibatch"><code>register_additional_minibatch</code></h3>

``` python
register_additional_minibatch(
    inputs,
    outputs
)
```

Registers an additional minibatch to the FisherBlock.

#### Args:

* <b>`inputs`</b>: Tensor of shape [batch_size, height, width, input_size]. Inputs to
    the convolution.
* <b>`outputs`</b>: Tensor of shape [batch_size, height, width, output_size]. Layer
    preactivations.

<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```





