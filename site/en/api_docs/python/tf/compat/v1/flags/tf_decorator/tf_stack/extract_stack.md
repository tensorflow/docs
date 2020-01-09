page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_stack.py#L141-L201">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A lightweight, extensible re-implementation of traceback.extract_stack.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.tf_stack.extract_stack`


``` python
tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack(limit=None)
```



<!-- Placeholder for "Used in" -->

NOTE(mrry): traceback.extract_stack eagerly retrieves the line of code for
    each stack frame using linecache, which results in an abundance of stat()
    calls. This implementation does not retrieve the code, and any consumer
    should apply _convert_stack to the result to obtain a traceback that can
    be formatted etc. using traceback methods.

#### Args:


* <b>`limit`</b>: A limit on the number of frames to return.


#### Returns:

A list of 5-tuples
    (filename, lineno, name, frame_globals, func_start_lineno)
corresponding to the call stack of the current thread.  The returned tuples
have the innermost stack frame at the end, unlike the Python inspect
module's stack() function.
