page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.text


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/text/summary_v2.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Write a text summary.

### Aliases:

* `tf.compat.v2.summary.text`


``` python
tf.summary.text(
    name,
    data,
    step=None,
    description=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`name`</b>: A name for this summary. The summary tag used for TensorBoard will
  be this name prefixed by any active name scopes.
* <b>`data`</b>: A UTF-8 string tensor value.
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to <a href="../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a>, which must
  not be None.
* <b>`description`</b>: Optional long-form description for this summary, as a
  constant `str`. Markdown is supported. Defaults to empty.


#### Returns:

True on success, or false if no summary was emitted because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  <a href="../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a> is None.
