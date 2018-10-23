

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_blocks.EmbeddingKFACFB

## Class `EmbeddingKFACFB`

Inherits From: [`KroneckerProductFB`](../../../../tf/contrib/kfac/fisher_blocks/KroneckerProductFB)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

K-FAC FisherBlock for embedding layers.

This FisherBlock is similar to EmbeddingKFACFB, except that its
input factor is approximated by a diagonal matrix. In the case that each
example references exactly one embedding, this approximation is exact.

Does not support bias parameters.

## Properties

<h3 id="num_registered_minibatches"><code>num_registered_minibatches</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    layer_collection,
    vocab_size
)
```

Creates a EmbeddingKFACFB block.

#### Args:

* <b>`layer_collection`</b>: The collection of all layers in the K-FAC approximate
      Fisher information matrix to which this FisherBlock belongs.
* <b>`vocab_size`</b>: int. Size of vocabulary for this embedding layer.

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

Instantiate Kronecker Factors for this FisherBlock.

#### Args:

* <b>`grads_list`</b>: List of list of Tensors. grads_list[i][j] is the
    gradient of the loss with respect to 'outputs' from source 'i' and
    tower 'j'. Each Tensor has shape [tower_minibatch_size, output_size].
* <b>`damping`</b>: 0-D Tensor or float. 'damping' * identity is approximately added
    to this FisherBlock's Fisher approximation.

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

* <b>`inputs`</b>: Tensor of shape [batch_size, input_size]. Inputs to the
    matrix-multiply.
* <b>`outputs`</b>: Tensor of shape [batch_size, output_size]. Layer preactivations.

<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```





