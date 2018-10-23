

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_blocks.ConvKFCBasicFB

## Class `ConvKFCBasicFB`

Inherits From: [`KroneckerProductFB`](../../../../tf/contrib/kfac/fisher_blocks/KroneckerProductFB)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for 2D convolutional layers using the basic KFC approx.

See https://arxiv.org/abs/1602.01407 for details.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    params,
    inputs,
    outputs,
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
* <b>`inputs`</b>: A Tensor of shape [batch_size, height, width, in_channels].
    Input activations to this layer.
* <b>`outputs`</b>: A Tensor of shape [batch_size, height, width, out_channels].
    Output pre-activations from this layer.
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



<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```





