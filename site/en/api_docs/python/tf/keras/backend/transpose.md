page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.transpose


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/transpose">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1793-L1826">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Transposes a tensor and returns it.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/transpose"><code>tf.compat.v1.keras.backend.transpose</code></a>
* <a href="/api_docs/python/tf/keras/backend/transpose"><code>tf.compat.v2.keras.backend.transpose</code></a>


``` python
tf.keras.backend.transpose(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

A tensor.



#### Examples:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}var = K.variable([[1, 2, 3], [4, 5, 6]]){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}K.eval(var){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}array([[ 1.,  2.,  3.],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [ 4.,  5.,  6.]], dtype=float32){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}var_transposed = K.transpose(var){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}K.eval(var_transposed){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}array([[ 1.,  4.],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [ 2.,  5.],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [ 3.,  6.]], dtype=float32){% endhtmlescape %}</code>
</pre>

```python
>>> input = K.placeholder((2, 3))
>>> input
<tf.Tensor 'Placeholder_11:0' shape=(2, 3) dtype=float32>
>>> input_transposed = K.transpose(input)
>>> input_transposed
<tf.Tensor 'transpose_4:0' shape=(3, 2) dtype=float32>

```
