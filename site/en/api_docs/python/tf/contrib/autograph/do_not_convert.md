page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.do_not_convert

``` python
tf.contrib.autograph.do_not_convert(
    run_as=tf.contrib.autograph.RunMode.GRAPH,
    return_dtypes=None
)
```



Defined in [`tensorflow/python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/impl/api.py).

Decorator that suppresses the conversion of a function.

See also: docs/pyfunc_dtypes.md

#### Args:

* <b>`run_as`</b>: RunMode, specifies how to use the function in TensorFlow.
* <b>`return_dtypes`</b>: Optional[Iterable[ Union[tf.DType,
    utils.py_func.MatchDType]]], the return data types of the converted
    function, if run_as is RunMode.PY_FUNC. Ignored otherwise. May be set to
    None if the function has no return values.


#### Returns:

Callable, a decorator that wraps the original function.