page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.repeat_elements


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2866-L2924">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Repeats the elements of a tensor along an axis, like `np.repeat`.

### Aliases:

* `tf.compat.v1.keras.backend.repeat_elements`
* `tf.compat.v2.keras.backend.repeat_elements`


``` python
tf.keras.backend.repeat_elements(
    x,
    rep,
    axis
)
```



<!-- Placeholder for "Used in" -->

If `x` has shape `(s1, s2, s3)` and `axis` is `1`, the output
will have shape `(s1, s2 * rep, s3)`.

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`rep`</b>: Python integer, number of times to repeat.
* <b>`axis`</b>: Axis along which to repeat.


#### Returns:

A tensor.



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}b = tf.constant([1, 2, 3]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> tf.keras.backend.repeat_elements(b, rep=2, axis=0){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=70, shape=(6,), dtype=int32,{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}      numpy=array([1, 1, 2, 2, 3, 3], dtype=int32)>{% endhtmlescape %}</code>
  </pre>
