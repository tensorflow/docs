page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.converted_call


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L365-L546">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compiles a function call inline.

``` python
tf.contrib.autograph.converted_call(
    f,
    options,
    args,
    kwargs,
    caller_fn_scope=None
)
```



<!-- Placeholder for "Used in" -->

For internal use only.

#### Args:


* <b>`f`</b>: The function to convert.
* <b>`options`</b>: converter.ConversionOptions
* <b>`args`</b>: Tuple, the original positional arguments of f
* <b>`kwargs`</b>: Dict, the original keyword arguments of f
* <b>`caller_fn_scope`</b>: Optional[function_wrappers.FunctionScope], the function
  scope of the converted function in which this call was originally made.


#### Returns:

Any, the result of executing a possibly-converted `f` with the given
  arguments.
