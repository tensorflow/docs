page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.copy_graph.get_copied_op


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/copy_graph/python/util/copy_elements.py#L233-L257">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Given an `Operation` instance from some `Graph`, returns

``` python
tf.contrib.copy_graph.get_copied_op(
    org_instance,
    graph,
    scope=''
)
```



<!-- Placeholder for "Used in" -->
its namesake from `graph`, under the specified scope
(default `""`).

If a copy of `org_instance` is present in `graph` under the given
`scope`, it will be returned.

#### Args:


* <b>`org_instance`</b>: An `Operation` from some `Graph`.
* <b>`graph`</b>: The `Graph` to be searched for a copr of `org_instance`.
* <b>`scope`</b>: The scope `org_instance` is present in.


#### Returns:

The `Operation` copy from `graph`.
