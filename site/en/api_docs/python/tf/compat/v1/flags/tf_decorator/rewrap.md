page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.tf_decorator.rewrap


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/tf_decorator.py#L128-L197">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Injects a new target into a function built by make_decorator.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.rewrap`


``` python
tf.compat.v1.flags.tf_decorator.rewrap(
    decorator_func,
    previous_target,
    new_target
)
```



<!-- Placeholder for "Used in" -->

This function allows replacing a function wrapped by `decorator_func`,
assuming the decorator that wraps the function is written as described below.

The decorator function must use `<decorator name>.__wrapped__` instead of the
wrapped function that is normally used:

#### Example:


# Instead of this:
def simple_parametrized_wrapper(*args, **kwds):
  return wrapped_fn(*args, **kwds)

tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)

# Write this:
def simple_parametrized_wrapper(*args, **kwds):
  return simple_parametrized_wrapper.__wrapped__(*args, **kwds)

tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)


Note that this process modifies decorator_func.

#### Args:


* <b>`decorator_func`</b>: Callable returned by `wrap`.
* <b>`previous_target`</b>: Callable that needs to be replaced.
* <b>`new_target`</b>: Callable to replace previous_target with.


#### Returns:

The updated decorator. If decorator_func is not a tf_decorator, new_target
is returned.
