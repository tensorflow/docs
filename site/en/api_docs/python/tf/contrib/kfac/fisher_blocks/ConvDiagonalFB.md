

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_blocks.ConvDiagonalFB

## Class `ConvDiagonalFB`

Inherits From: [`FisherBlock`](../../../../tf/contrib/kfac/fisher_blocks/FisherBlock)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

FisherBlock for convolutional layers using a diagonal approx.

Estimates the Fisher Information matrix's diagonal entries for a convolutional
layer. Unlike NaiveDiagonalFB this uses the low-variance "sum of squares"
estimator.

Let 'params' be a vector parameterizing a model and 'i' an arbitrary index
into it. We are interested in Fisher(params)[i, i]. This is,

  Fisher(params)[i, i] = E[ v(x, y, params) v(x, y, params)^T ][i, i]
                       = E[ v(x, y, params)[i] ^ 2 ]

Consider a convoluational layer in this model with (unshared) filter matrix
'w'. For an example image 'x' that produces layer inputs 'a' and output
preactivations 's',

  v(x, y, w) = vec( sum_{loc} a_{loc} (d loss / d s_{loc})^T )

where 'loc' is a single (x, y) location in an image.

This FisherBlock tracks Fisher(params)[i, i] for all indices 'i' corresponding
to the layer's parameters 'w'.

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





