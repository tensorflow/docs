page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.broadcast_to


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/broadcast_to">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Broadcast an array for a compatible shape.

### Aliases:

* <a href="/api_docs/python/tf/broadcast_to"><code>tf.compat.v1.broadcast_to</code></a>
* <a href="/api_docs/python/tf/broadcast_to"><code>tf.compat.v2.broadcast_to</code></a>


``` python
tf.broadcast_to(
    input,
    shape,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Broadcasting is the process of making arrays to have compatible shapes
for arithmetic operations. Two shapes are compatible if for each
dimension pair they are either equal or one of them is one. When trying
to broadcast a Tensor to a shape, it starts with the trailing dimensions,
and works its way forward.

For example,

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}x = tf.constant([1, 2, 3]){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}y = tf.broadcast_to(x, [3, 3]){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}sess.run(y){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}array([[1, 2, 3],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [1, 2, 3],{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}       [1, 2, 3]], dtype=int32){% endhtmlescape %}</code>
</pre>

In the above example, the input Tensor with the shape of `[1, 3]`
is broadcasted to output Tensor with shape of `[3, 3]`.

#### Args:


* <b>`input`</b>: A `Tensor`. A Tensor to broadcast.
* <b>`shape`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  An 1-D `int` Tensor. The shape of the desired output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
