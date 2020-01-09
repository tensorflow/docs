page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.arange


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L2962-L2997">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a 1D tensor containing a sequence of integers.

### Aliases:

* `tf.compat.v1.keras.backend.arange`
* `tf.compat.v2.keras.backend.arange`


``` python
tf.keras.backend.arange(
    start,
    stop=None,
    step=1,
    dtype='int32'
)
```



<!-- Placeholder for "Used in" -->

The function arguments use the same convention as
Theano's arange: if only one argument is provided,
it is in fact the "stop" argument and "start" is 0.

The default type of the returned tensor is `'int32'` to
match TensorFlow's default.

#### Arguments:


* <b>`start`</b>: Start value.
* <b>`stop`</b>: Stop value.
* <b>`step`</b>: Difference between two successive values.
* <b>`dtype`</b>: Integer dtype to use.


#### Returns:

An integer tensor.



#### Example:

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}tf.keras.backend.arange(start=0, stop=10, step=1.5){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  <tf.Tensor: id=96, shape=(7,), dtype=float32,{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}      numpy=array([0. , 1.5, 3. , 4.5, 6. , 7.5, 9. ], dtype=float32)>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  </pre>
