page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.CycleGANModel

## Class `CycleGANModel`

An CycleGANModel contains all the pieces needed for CycleGAN training.





Defined in [`contrib/gan/python/namedtuples.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/namedtuples.py).

<!-- Placeholder for "Used in" -->

The model `model_x2y` generator F maps data set X to Y, while the model
`model_y2x` generator G maps data set Y to X.

See https://arxiv.org/abs/1703.10593 for more details.

#### Args:


* <b>`model_x2y`</b>: A `GANModel` namedtuple whose generator maps data set X to Y.
* <b>`model_y2x`</b>: A `GANModel` namedtuple whose generator maps data set Y to X.
* <b>`reconstructed_x`</b>: A `Tensor` of reconstructed data X which is G(F(X)).
* <b>`reconstructed_y`</b>: A `Tensor` of reconstructed data Y which is F(G(Y)).

## Properties

<h3 id="model_x2y"><code>model_x2y</code></h3>




<h3 id="model_y2x"><code>model_y2x</code></h3>




<h3 id="reconstructed_x"><code>reconstructed_x</code></h3>




<h3 id="reconstructed_y"><code>reconstructed_y</code></h3>






