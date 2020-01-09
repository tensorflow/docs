page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.permute_dimensions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2740-L2768">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Permutes axes in a tensor.

### Aliases:

* `tf.compat.v1.keras.backend.permute_dimensions`
* `tf.compat.v2.keras.backend.permute_dimensions`


``` python
tf.keras.backend.permute_dimensions(
    x,
    pattern
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`pattern`</b>: A tuple of
    dimension indices, e.g. `(0, 2, 1)`.


#### Returns:

A tensor.



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> a{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=49, shape=(4, 3), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[ 1,  2,  3],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 4,  5,  6],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 7,  8,  9],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [10, 11, 12]], dtype=int32)>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> tf.keras.backend.permute_dimensions(a, pattern=(1, 0)){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=52, shape=(3, 4), dtype=int32, numpy={% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  array([[ 1,  4,  7, 10],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 2,  5,  8, 11],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}         [ 3,  6,  9, 12]], dtype=int32)>{% endhtmlescape %}</code>
  </pre>
