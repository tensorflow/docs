page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.filter_ops_from_regex

Get all the operations that match the given regex.

``` python
tf.contrib.graph_editor.filter_ops_from_regex(
    ops,
    regex
)
```



Defined in [`contrib/graph_editor/select.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/select.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
* <b>`regex`</b>: a regular expression matching the operation's name.
  For example, `"^foo(/.*)?$"` will match all the operations in the "foo"
  scope.

#### Returns:

A list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.


#### Raises:


* <b>`TypeError`</b>: if ops cannot be converted to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.