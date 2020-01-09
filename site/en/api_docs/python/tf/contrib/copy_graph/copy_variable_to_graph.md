page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.copy_graph.copy_variable_to_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/copy_graph/python/util/copy_elements.py#L41-L98">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Given a `Variable` instance from one `Graph`, initializes and returns

``` python
tf.contrib.copy_graph.copy_variable_to_graph(
    org_instance,
    to_graph,
    scope=''
)
```



<!-- Placeholder for "Used in" -->
a copy of it from another `Graph`, under the specified scope
(default `""`).

#### Args:


* <b>`org_instance`</b>: A `Variable` from some `Graph`.
* <b>`to_graph`</b>: The `Graph` to copy the `Variable` to.
* <b>`scope`</b>: A scope for the new `Variable` (default `""`).


#### Returns:

The copied `Variable` from `to_graph`.



#### Raises:


* <b>`TypeError`</b>: If `org_instance` is not a `Variable`.
