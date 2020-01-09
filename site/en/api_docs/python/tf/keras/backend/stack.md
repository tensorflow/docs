page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3189-L3212">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stacks a list of rank `R` tensors into a rank `R+1` tensor.

### Aliases:

* `tf.compat.v1.keras.backend.stack`
* `tf.compat.v2.keras.backend.stack`


``` python
tf.keras.backend.stack(
    x,
    axis=0
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: List of tensors.
* <b>`axis`</b>: Axis along which to perform stacking.


#### Returns:

A tensor.



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}a = tf.constant([[1, 2],[3, 4]]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> b = tf.constant([[10, 20],[30, 40]]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> tf.keras.backend.stack((a, b)){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=146, shape=(2, 2, 2), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[[ 1,  2],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}          [ 3,  4]],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [[10, 20],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}          [30, 40]]], dtype=int32)>{% endhtmlescape %}</code>
  </pre>
