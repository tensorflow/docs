page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.tf_decorator.make_decorator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_decorator.py#L67-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Make a decorator from a wrapper and a target.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.make_decorator`


``` python
tf.compat.v1.flags.tf_decorator.make_decorator(
    target,
    decorator_func,
    decorator_name=None,
    decorator_doc='',
    decorator_argspec=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`target`</b>: The final callable to be wrapped.
* <b>`decorator_func`</b>: The wrapper function.
* <b>`decorator_name`</b>: The name of the decorator. If `None`, the name of the
  function calling make_decorator.
* <b>`decorator_doc`</b>: Documentation specific to this application of
  `decorator_func` to `target`.
* <b>`decorator_argspec`</b>: The new callable signature of this decorator.


#### Returns:

The `decorator_func` argument with new metadata attached.
