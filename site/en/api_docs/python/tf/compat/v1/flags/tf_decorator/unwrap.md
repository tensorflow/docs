page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.tf_decorator.unwrap


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_decorator.py#L200-L226">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Unwraps an object into a list of TFDecorators and a final target.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.unwrap`


``` python
tf.compat.v1.flags.tf_decorator.unwrap(maybe_tf_decorator)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`maybe_tf_decorator`</b>: Any callable object.


#### Returns:

A tuple whose first element is an list of TFDecorator-derived objects that
were applied to the final callable target, and whose second element is the
final undecorated callable target. If the `maybe_tf_decorator` parameter is
not decorated by any TFDecorators, the first tuple element will be an empty
list. The `TFDecorator` list is ordered from outermost to innermost
decorators.
