

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.make_template

``` python
tf.contrib.eager.make_template(
    name_,
    func_,
    create_scope_now_=False,
    unique_name_=None,
    custom_getter_=None,
    create_graph_function_=False,
    **kwargs
)
```



Defined in [`tensorflow/python/ops/template.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/template.py).

Make a template, optionally compiling func_ into a graph function.

See `make_template` for full documentation.

#### Args:

* <b>`name_`</b>: A name for the scope created by this template. If necessary, the name
    will be made unique by appending `_N` to the name.
* <b>`func_`</b>: The function to wrap.
* <b>`create_scope_now_`</b>: Boolean controlling whether the scope should be created
    when the template is constructed or when the template is called. Default
    is False, meaning the scope is created when the template is called.
* <b>`unique_name_`</b>: When used, it overrides name_ and is not made unique. If a
    template of the same scope/unique_name already exists and reuse is false,
    an error is raised. Defaults to None. If executing eagerly, must be None.
* <b>`custom_getter_`</b>: Optional custom getter for variables used in `func_`. See
    the <a href="../../../tf/get_variable"><code>tf.get_variable</code></a> `custom_getter` documentation for
    more information.
* <b>`create_graph_function_`</b>: When True, `func_` will be executed as a graph
    function. This implies that `func_` must satisfy the properties that
    `function.defun` requires of functions: See the documentation of
    `function.defun` for details. When executing eagerly, setting this flag to
    True can improve performance. Regardless of whether eager execution is
    enabled, enabling this flag gives the caller access to graph-function
    semantics, i.e., accesses to variables are totally ordered and
    side-effecting ops are not pruned.
* <b>`**kwargs`</b>: Keyword arguments to apply to `func_`.


#### Returns:

A function to encapsulate a set of variables which should be created once
and reused. An enclosing scope will be created either when `make_template`
is called or when the result is called, depending on the value of
`create_scope_now_`. Regardless of the value, the first time the template
is called it will enter the scope with no reuse, and call `func_` to create
variables, which are guaranteed to be unique. All subsequent calls will
re-enter the scope and reuse those variables.


#### Raises:

* <b>`ValueError`</b>: if `name_` is None.
* <b>`ValueError`</b>: if `unique_name_` is not None and eager execution is enabled.