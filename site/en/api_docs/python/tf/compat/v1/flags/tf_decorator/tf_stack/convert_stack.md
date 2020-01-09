page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.tf_decorator.tf_stack.convert_stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_stack.py#L238-L266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a stack extracted using extract_stack() to a traceback stack.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.tf_stack.convert_stack`


``` python
tf.compat.v1.flags.tf_decorator.tf_stack.convert_stack(
    stack,
    include_func_start_lineno=False
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`stack`</b>: A list of n 5-tuples,
  (filename, lineno, name, frame_globals, func_start_lineno).
* <b>`include_func_start_lineno`</b>: True if function start line number should be
  included as the 5th entry in return tuples.


#### Returns:

A tuple of n 4-tuples or 5-tuples
(filename, lineno, name, code, [optional: func_start_lineno]), where the
code tuple element is calculated from the corresponding elements of the
input tuple.
