page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.reshape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2711-L2737">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reshapes a tensor to the specified shape.

### Aliases:

* `tf.compat.v1.keras.backend.reshape`
* `tf.compat.v2.keras.backend.reshape`


``` python
tf.keras.backend.reshape(
    x,
    shape
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`shape`</b>: Target shape tuple.


#### Returns:

A tensor.



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> a{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=32, shape=(4, 3), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[ 1,  2,  3],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 4,  5,  6],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 7,  8,  9],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [10, 11, 12]], dtype=int32)>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> tf.keras.backend.reshape(a, shape=(2, 6)){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=35, shape=(2, 6), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[ 1,  2,  3,  4,  5,  6],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 7,  8,  9, 10, 11, 12]], dtype=int32)>{% endhtmlescape %}</code>
  </pre>
