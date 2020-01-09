page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.flatten


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3017-L3039">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Flatten a tensor.

### Aliases:

* `tf.compat.v1.keras.backend.flatten`
* `tf.compat.v2.keras.backend.flatten`


``` python
tf.keras.backend.flatten(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.


#### Returns:

A tensor, reshaped into 1-D



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}b = tf.constant([[1, 2], [3, 4]]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> b{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=102, shape=(2, 2), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[1, 2],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [3, 4]], dtype=int32)>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> tf.keras.backend.flatten(b){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=105, shape=(4,), dtype=int32,{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}      numpy=array([1, 2, 3, 4], dtype=int32)>{% endhtmlescape %}</code>
  </pre>
