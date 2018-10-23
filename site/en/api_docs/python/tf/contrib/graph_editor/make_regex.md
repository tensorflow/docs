

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_regex

``` python
tf.contrib.graph_editor.make_regex(obj)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/graph_editor/select.py).

Return a compiled regular expression.

#### Args:

* <b>`obj`</b>: a string or a regular expression.

#### Returns:

A compiled regular expression.

#### Raises:

* <b>`ValueError`</b>: if obj could not be converted to a regular expression.