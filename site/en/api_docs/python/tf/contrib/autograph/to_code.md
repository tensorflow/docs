page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.to_code

``` python
tf.contrib.autograph.to_code(
    e,
    recursive=True,
    arg_values=None,
    arg_types=None,
    partial_types=None,
    indentation='  '
)
```



Defined in [`tensorflow/python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/autograph/impl/api.py).

Returns the equivalent code that uses TensorFlow ops.

Also see: `to_graph`, `convert`

#### Args:

* <b>`e`</b>: Union[Callable, Type], the Python entity to convert.
* <b>`recursive`</b>: bool, whether to recursively convert any functions that the
      converted function may call.
* <b>`arg_values`</b>: Optional[Dict[Text, Any]], value hints for symbols including
      function arguments.
* <b>`arg_types`</b>: Optional[Dict[Text, Type]], type hints for symbols including
      function arguments.
* <b>`partial_types`</b>: Set[Type], reserved for internal use.
* <b>`indentation`</b>: Text, when to use for each level of indentation.


#### Returns:

Text, the converted code.