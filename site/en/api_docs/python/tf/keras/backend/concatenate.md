page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.concatenate


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2676-L2708">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Concatenates a list of tensors alongside the specified axis.

### Aliases:

* `tf.compat.v1.keras.backend.concatenate`
* `tf.compat.v2.keras.backend.concatenate`


``` python
tf.keras.backend.concatenate(
    tensors,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensors`</b>: list of tensors to concatenate.
* <b>`axis`</b>: concatenation axis.


#### Returns:

A tensor.



#### Example:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}b = tf.constant([[10, 20, 30], [40, 50, 60], [70, 80, 90]]){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}tf.keras.backend.concatenate((a, b), axis=-1){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}<tf.Tensor: id=14, shape=(3, 6), dtype=int32, numpy={% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}array([[ 1,  2,  3, 10, 20, 30],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [ 4,  5,  6, 40, 50, 60],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [ 7,  8,  9, 70, 80, 90]], dtype=int32)>{% endhtmlescape %}</code>
</pre>
