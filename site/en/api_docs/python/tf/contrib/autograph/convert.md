page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.convert

Decorator that compiles a function to use TensorFlow ops.

``` python
tf.contrib.autograph.convert(
    recursive=False,
    optional_features=None
)
```



Defined in [`python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/impl/api.py).

<!-- Placeholder for "Used in" -->

The decorator is dynamic - it recompiles the target whenever the decorated
function is called. This means the parameter values are known at conversion.
It also means that repeated calls with different types of parameters will be
correctly processed.

#### Args:


* <b>`recursive`</b>: bool, whether to recursively convert any functions or classes
  that the converted function may use.
* <b>`optional_features`</b>: converted.Feature, allows toggling optional or
  experimental features. When set to None, only the core features are
  enabled.


#### Returns:

Callable, a decorator that converts the given function into an equivalent
function that uses TensorFlow ops.
