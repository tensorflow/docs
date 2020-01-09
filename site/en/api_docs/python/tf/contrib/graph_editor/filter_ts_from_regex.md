page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.filter_ts_from_regex


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L139-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get all the tensors linked to ops that match the given regex.

``` python
tf.contrib.graph_editor.filter_ts_from_regex(
    ops,
    regex
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of tf.Operation.
* <b>`regex`</b>: a regular expression matching the tensors' name.
  For example, "^foo(/.*)?:\d+$" will match all the tensors in the "foo"
  scope.

#### Returns:

A list of tf.Tensor.


#### Raises:


* <b>`TypeError`</b>: if ops cannot be converted to a list of tf.Operation.
