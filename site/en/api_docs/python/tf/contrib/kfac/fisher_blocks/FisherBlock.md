

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_blocks.FisherBlock

## Class `FisherBlock`





Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

Abstract base class for objects modeling approximate Fisher matrix blocks.

Subclasses must implement register_matpower, multiply_matpower,
instantiate_factors, tensors_to_compute_grads, and num_registered_towers
methods.

## Properties

<h3 id="num_registered_towers"><code>num_registered_towers</code></h3>

Number of towers registered for this FisherBlock.

Typically equal to the number of towers in a multi-tower setup.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(layer_collection)
```



<h3 id="instantiate_factors"><code>instantiate_factors</code></h3>

``` python
instantiate_factors(
    grads_list,
    damping
)
```

Creates and registers the component factors of this Fisher block.

#### Args:

* <b>`grads_list`</b>: A list gradients (each a Tensor or tuple of Tensors) with
      respect to the tensors returned by tensors_to_compute_grads() that
      are to be used to estimate the block.
* <b>`damping`</b>: The damping factor (float or Tensor).

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

Multiplies the vector by the (damped) matrix-power of the block.

#### Args:

* <b>`vector`</b>: The vector (a Tensor or tuple of Tensors) to be multiplied.
* <b>`exp`</b>: A float representing the power to raise the block by before
    multiplying it by the vector.


#### Returns:

The vector left-multiplied by the (damped) matrix-power of the block.

<h3 id="register_inverse"><code>register_inverse</code></h3>

``` python
register_inverse()
```

Registers a matrix inverse to be computed by the block.

<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(exp)
```

Registers a matrix power to be computed by the block.

#### Args:

* <b>`exp`</b>: A float representing the power to raise the block by.

<h3 id="tensors_to_compute_grads"><code>tensors_to_compute_grads</code></h3>

``` python
tensors_to_compute_grads()
```

Returns the Tensor(s) with respect to which this FisherBlock needs grads.
    



