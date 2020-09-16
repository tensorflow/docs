description: Controls how gradient computation behaves when y does not depend on x.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.UnconnectedGradients" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="NONE"/>
<meta itemprop="property" content="ZERO"/>
</div>

# tf.UnconnectedGradients

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/unconnected_gradients.py#L27-L43">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Controls how gradient computation behaves when y does not depend on x.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.UnconnectedGradients`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

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

## Class Variables

* `NONE` <a id="NONE"></a>
* `ZERO` <a id="ZERO"></a>
