description: Computes the gradient error. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.test.compute_gradient_error" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.test.compute_gradient_error

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/gradient_checker.py#L348-L395">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the gradient error. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.test.compute_gradient_error(
    x, x_shape, y, y_shape, x_init_value=None, delta=0.001, init_targets=None,
    extra_feed_dict=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.test.compute_gradient in 2.0, which has better support for functions. Note that the two versions have different usage, so code change is needed.

Computes the maximum error for dy/dx between the computed Jacobian and the
numerically estimated Jacobian.

This function will modify the tensors passed in as it adds more operations
and hence changing the consumers of the operations of the input tensors.

This function adds operations to the current session. To compute the error
using a particular device, such as a GPU, use the standard methods for
setting a device (e.g. using with sess.graph.device() or setting a device
function in the session constructor).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
a tensor or list of tensors
</td>
</tr><tr>
<td>
`x_shape`
</td>
<td>
the dimensions of x as a tuple or an array of ints. If x is a list,
then this is the list of shapes.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
a tensor
</td>
</tr><tr>
<td>
`y_shape`
</td>
<td>
the dimensions of y as a tuple or an array of ints.
</td>
</tr><tr>
<td>
`x_init_value`
</td>
<td>
(optional) a numpy array of the same shape as "x"
representing the initial value of x. If x is a list, this should be a list
of numpy arrays.  If this is none, the function will pick a random tensor
as the initial value.
</td>
</tr><tr>
<td>
`delta`
</td>
<td>
(optional) the amount of perturbation.
</td>
</tr><tr>
<td>
`init_targets`
</td>
<td>
list of targets to run to initialize model params.
</td>
</tr><tr>
<td>
`extra_feed_dict`
</td>
<td>
dict that allows fixing specified tensor values
during the Jacobian calculation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The maximum error in between the two Jacobians.
</td>
</tr>

</table>

