description: Computes and returns the theoretical and numerical Jacobian. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.test.compute_gradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.test.compute_gradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/gradient_checker.py#L271-L335">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes and returns the theoretical and numerical Jacobian. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.test.compute_gradient(
    x, x_shape, y, y_shape, x_init_value=None, delta=0.001, init_targets=None,
    extra_feed_dict=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.test.compute_gradient in 2.0, which has better support for functions. Note that the two versions have different usage, so code change is needed.

If `x` or `y` is complex, the Jacobian will still be real but the
corresponding Jacobian dimension(s) will be twice as large.  This is required
even if both input and output is complex since TensorFlow graphs are not
necessarily holomorphic, and may have gradients not expressible as complex
numbers.  For example, if `x` is complex with shape `[m]` and `y` is complex
with shape `[n]`, each Jacobian `J` will have shape `[m * 2, n * 2]` with

    J[:m, :n] = d(Re y)/d(Re x)
    J[:m, n:] = d(Im y)/d(Re x)
    J[m:, :n] = d(Re y)/d(Im x)
    J[m:, n:] = d(Im y)/d(Im x)

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
Two 2-d numpy arrays representing the theoretical and numerical
Jacobian for dy/dx. Each has "x_size" rows and "y_size" columns
where "x_size" is the number of elements in x and "y_size" is the
number of elements in y. If x is a list, returns a list of two numpy arrays.
</td>
</tr>

</table>

