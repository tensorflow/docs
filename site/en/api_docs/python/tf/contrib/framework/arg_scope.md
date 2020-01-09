page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.arg_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/arg_scope.py#L110-L162">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stores the default arguments for the given set of list_ops.

``` python
tf.contrib.framework.arg_scope(
    list_ops_or_scope,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

For usage, please see examples at top of the file.

#### Args:


* <b>`list_ops_or_scope`</b>: List or tuple of operations to set argument scope for or
  a dictionary containing the current scope. When list_ops_or_scope is a
  dict, kwargs must be empty. When list_ops_or_scope is a list or tuple,
  then every op in it need to be decorated with @add_arg_scope to work.
* <b>`**kwargs`</b>: keyword=value that will define the defaults for each op in
          list_ops. All the ops need to accept the given set of arguments.


#### Yields:

the current_scope, which is a dictionary of {op: {arg: value}}


#### Raises:


* <b>`TypeError`</b>: if list_ops is not a list or a tuple.
* <b>`ValueError`</b>: if any op in list_ops has not be decorated with @add_arg_scope.
