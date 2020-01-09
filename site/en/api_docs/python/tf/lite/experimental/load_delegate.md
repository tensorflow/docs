page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.experimental.load_delegate


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/lite/python/interpreter.py#L140-L169">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns loaded Delegate object.

### Aliases:

* `tf.compat.v1.lite.experimental.load_delegate`
* `tf.compat.v2.lite.experimental.load_delegate`


``` python
tf.lite.experimental.load_delegate(
    library,
    options=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`library`</b>: Name of shared library containing the
  [TfLiteDelegate](https://www.tensorflow.org/lite/performance/delegates).
* <b>`options`</b>: Dictionary of options that are required to load the delegate. All
  keys and values in the dictionary should be convertible to str. Consult
  the documentation of the specific delegate for required and legal options.
  (default None)


#### Returns:

Delegate object.



#### Raises:


* <b>`ValueError`</b>: Delegate failed to load.
* <b>`RuntimeError`</b>: If delegate loading is used on unsupported platform.
