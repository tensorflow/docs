page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.add_check_numerics_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/numerics.py#L72-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Connect a <a href="../../../tf/debugging/check_numerics"><code>tf.debugging.check_numerics</code></a> to every floating point tensor.

``` python
tf.compat.v1.add_check_numerics_ops()
```



<!-- Placeholder for "Used in" -->

`check_numerics` operations themselves are added for each `half`, `float`,
or `double` tensor in the current default graph. For all ops in the graph, the
`check_numerics` op for all of its (`half`, `float`, or `double`) inputs
is guaranteed to run before the `check_numerics` op on any of its outputs.

Note: This API is not compatible with the use of <a href="../../../tf/cond"><code>tf.cond</code></a> or
<a href="../../../tf/while_loop"><code>tf.while_loop</code></a>, and will raise a `ValueError` if you attempt to call it
in such a graph.

#### Returns:

A `group` op depending on all `check_numerics` ops added.



#### Raises:


* <b>`ValueError`</b>: If the graph contains any numeric operations in a control flow
  structure.
* <b>`RuntimeError`</b>: If called with eager execution enabled.



#### Eager Compatibility
Not compatible with eager execution. To check for `Inf`s and `NaN`s under
eager execution, call `tfe.seterr(inf_or_nan='raise')` once before executing
the checked operations.
