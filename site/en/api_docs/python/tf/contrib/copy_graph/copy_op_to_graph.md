page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.copy_graph.copy_op_to_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/copy_graph/python/util/copy_elements.py#L101-L230">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a copy of an operation from another Graph under a specified scope.

``` python
tf.contrib.copy_graph.copy_op_to_graph(
    org_instance,
    to_graph,
    variables,
    scope=''
)
```



<!-- Placeholder for "Used in" -->

Given an `Operation` `org_instance` from one `Graph`,
initializes and returns a copy of it from another `Graph`,
under the specified scope (default `""`).

The copying is done recursively, so any `Operation` whose output
is required to evaluate the `org_instance`, is also copied (unless
already done).

Since `Variable` instances are copied separately, those required
to evaluate `org_instance` must be provided as input.

#### Args:


* <b>`org_instance`</b>: An `Operation` from some `Graph`. Could be a
  `Placeholder` as well.
* <b>`to_graph`</b>: The `Graph` to copy `org_instance` to.
* <b>`variables`</b>: An iterable of `Variable` instances to copy `org_instance` to.
* <b>`scope`</b>: A scope for the new `Variable` (default `""`).


#### Returns:

The copied `Operation` from `to_graph`.



#### Raises:


* <b>`TypeError`</b>: If `org_instance` is not an `Operation` or `Tensor`.
