page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.UnconnectedGradients

## Class `UnconnectedGradients`





Defined in [`tensorflow/python/ops/unconnected_gradients.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/unconnected_gradients.py).

Controls how gradient computation behaves when y does not depend on x.

The gradient of y with respect to x can be zero in two different ways: there
could be no differentiable path in the graph connecting x to y (and so we can
statically prove that the gradient is zero) or it could be that runtime values
of tensors in a particular execution lead to a gradient of zero (say, if a
relu unit happens to not be activated). To allow you to distinguish between
these two cases you can choose what value gets returned for the gradient when
there is no path in the graph from x to y:

* `NONE`: Indicates that [None] will be returned if there is no path from x
  to y
* `ZERO`: Indicates that a zero tensor will be returned in the shape of x.

## Class Members

<h3 id="NONE"><code>NONE</code></h3>

<h3 id="ZERO"><code>ZERO</code></h3>

<h3 id="__members__"><code>__members__</code></h3>

