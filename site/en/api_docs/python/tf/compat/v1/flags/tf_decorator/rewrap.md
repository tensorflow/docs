description: Injects a new target into a function built by make_decorator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.tf_decorator.rewrap" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.tf_decorator.rewrap

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/util/tf_decorator.py#L128-L197">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Injects a new target into a function built by make_decorator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.tf_decorator.rewrap`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.tf_decorator.rewrap(
    decorator_func, previous_target, new_target
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function allows replacing a function wrapped by `decorator_func`,
assuming the decorator that wraps the function is written as described below.

The decorator function must use `<decorator name>.__wrapped__` instead of the
wrapped function that is normally used:

#### Example:


# Instead of this:
def simple_parametrized_wrapper(*args, **kwds):
  return wrapped_fn(*args, **kwds)

tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)

# Write this:
def simple_parametrized_wrapper(*args, **kwds):
  return simple_parametrized_wrapper.__wrapped__(*args, **kwds)

tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)


Note that this process modifies decorator_func.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`decorator_func`
</td>
<td>
Callable returned by `wrap`.
</td>
</tr><tr>
<td>
`previous_target`
</td>
<td>
Callable that needs to be replaced.
</td>
</tr><tr>
<td>
`new_target`
</td>
<td>
Callable to replace previous_target with.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The updated decorator. If decorator_func is not a tf_decorator, new_target
is returned.
</td>
</tr>

</table>

