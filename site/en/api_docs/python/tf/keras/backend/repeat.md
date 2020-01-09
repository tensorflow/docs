page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.repeat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2927-L2959">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Repeats a 2D tensor.

### Aliases:

* `tf.compat.v1.keras.backend.repeat`
* `tf.compat.v2.keras.backend.repeat`


``` python
tf.keras.backend.repeat(
    x,
    n
)
```



<!-- Placeholder for "Used in" -->

if `x` has shape (samples, dim) and `n` is `2`,
the output will have shape `(samples, 2, dim)`.

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`n`</b>: Python integer, number of times to repeat.


#### Returns:

A tensor.



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}b = tf.constant([[1, 2], [3, 4]]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> b{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=78, shape=(2, 2), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[1, 2],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [3, 4]], dtype=int32)>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> tf.keras.backend.repeat(b, n=2){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=82, shape=(2, 2, 2), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[[1, 2],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}          [1, 2]],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [[3, 4],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}          [3, 4]]], dtype=int32)>{% endhtmlescape %}</code>
  </pre>
