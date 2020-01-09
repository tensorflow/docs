page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.to_graph

``` python
tf.contrib.autograph.to_graph(
    e,
    recursive=True,
    verbose=False,
    arg_values=None,
    arg_types=None,
    partial_types=None,
    strip_decorators=None
)
```



Defined in [`tensorflow/python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/autograph/impl/api.py).

Converts a Python entity into equivalent code that uses TensorFlow ops.

Supported Python entities include:
  * functions
  * classes

Classes are converted by converting all their methods into a new class.

#### Args:

* <b>`e`</b>: Union[Callable, Type], the Python entity to convert.
* <b>`recursive`</b>: bool, whether to recursively convert any functions that the
      converted function may call.
* <b>`verbose`</b>: bool, whether to output the compiled code in the logs.
* <b>`arg_values`</b>: Optional[Dict[Text, Any]], value hints for symbols including
      function arguments.
* <b>`arg_types`</b>: Optional[Dict[Text, Type]], type hints for symbols including
      function arguments.
* <b>`partial_types`</b>: Set[Type], reserved for internal use.
* <b>`strip_decorators`</b>: Tuple[Callable], same as
      ConversionOptions.strip_decorators.


#### Returns:

Union[Callable, Type], the converted entity, which is the same kind as e
(that is, a function is e is a function, a class if e is a class, etc.) but
its code has been converted to use TF ops.


#### Raises:

* <b>`ValueError`</b>: If the entity could not be converted.