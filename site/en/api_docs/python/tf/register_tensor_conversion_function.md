page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.register_tensor_conversion_function


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/register_tensor_conversion_function">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_conversion_registry.py#L56-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Registers a function for converting objects of `base_type` to `Tensor`.

### Aliases:

* <a href="/api_docs/python/tf/register_tensor_conversion_function"><code>tf.compat.v1.register_tensor_conversion_function</code></a>
* <a href="/api_docs/python/tf/register_tensor_conversion_function"><code>tf.compat.v2.register_tensor_conversion_function</code></a>


``` python
tf.register_tensor_conversion_function(
    base_type,
    conversion_func,
    priority=100
)
```



<!-- Placeholder for "Used in" -->

The conversion function must have the following signature:

```python
    def conversion_func(value, dtype=None, name=None, as_ref=False):
      # ...
```

It must return a `Tensor` with the given `dtype` if specified. If the
conversion function creates a new `Tensor`, it should use the given
`name` if specified. All exceptions will be propagated to the caller.

The conversion function may return `NotImplemented` for some
inputs. In this case, the conversion process will continue to try
subsequent conversion functions.

If `as_ref` is true, the function must return a `Tensor` reference,
such as a `Variable`.

NOTE: The conversion functions will execute in order of priority,
followed by order of registration. To ensure that a conversion function
`F` runs before another conversion function `G`, ensure that `F` is
registered with a smaller priority than `G`.

#### Args:


* <b>`base_type`</b>: The base type or tuple of base types for all objects that
  `conversion_func` accepts.
* <b>`conversion_func`</b>: A function that converts instances of `base_type` to
  `Tensor`.
* <b>`priority`</b>: Optional integer that indicates the priority for applying this
  conversion function. Conversion functions with smaller priority values run
  earlier than conversion functions with larger priority values. Defaults to
  100.


#### Raises:


* <b>`TypeError`</b>: If the arguments do not have the appropriate type.
