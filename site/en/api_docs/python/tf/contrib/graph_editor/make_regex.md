page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_regex


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L62-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return a compiled regular expression.

``` python
tf.contrib.graph_editor.make_regex(obj)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`obj`</b>: a string or a regular expression.

#### Returns:

A compiled regular expression.


#### Raises:


* <b>`ValueError`</b>: if obj could not be converted to a regular expression.
