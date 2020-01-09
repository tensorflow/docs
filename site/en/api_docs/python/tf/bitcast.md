page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.bitcast


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Bitcasts a tensor from one type to another without copying data.

### Aliases:

* `tf.compat.v1.bitcast`
* `tf.compat.v2.bitcast`


``` python
tf.bitcast(
    input,
    type,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation returns a tensor that has the same buffer
data as `input` with datatype `type`.

If the input datatype `T` is larger than the output datatype `type` then the
shape changes from [...] to [..., sizeof(`T`)/sizeof(`type`)].

If `T` is smaller than `type`, the operator requires that the rightmost
dimension be equal to sizeof(`type`)/sizeof(`T`). The shape then goes from
[..., sizeof(`type`)/sizeof(`T`)] to [...].

tf.bitcast() and tf.cast() work differently when real dtype is casted as a complex dtype
(e.g. tf.complex64 or tf.complex128) as tf.cast() make imaginary part 0 while tf.bitcast()
gives module error.
For example,

#### Example 1:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}a = [1., 2., 3.]{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}equality_bitcast = tf.bitcast(a,tf.complex128){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}tensorflow.python.framework.errors_impl.InvalidArgumentError: Cannot bitcast from float to complex128: shape [3] [Op:Bitcast]{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}equality_cast = tf.cast(a,tf.complex128){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}print(equality_cast){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}tf.Tensor([1.+0.j 2.+0.j 3.+0.j], shape=(3,), dtype=complex128){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}```{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}Example 2:{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}```python{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}tf.bitcast(tf.constant(0xffffffff, dtype=tf.uint32), tf.uint8){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}<tf.Tensor: ... shape=(4,), dtype=uint8, numpy=array([255, 255, 255, 255], dtype=uint8)>{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}```{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}Example 3:{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}```python{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}x = [1., 2., 3.]{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}y = [0., 2., 3.]{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}equality= tf.equal(x,y){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}equality_cast = tf.cast(equality,tf.float32){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}equality_bitcast = tf.bitcast(equality_cast,tf.uint8){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}print(equality){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}tf.Tensor([False True True], shape=(3,), dtype=bool){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}print(equality_cast){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}tf.Tensor([0. 1. 1.], shape=(3,), dtype=float32){% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}print(equality_bitcast){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}tf.Tensor({% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}[[ 0 0 0 0]{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %} [ 0 0 128 63]{% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %} [ 0 0 128 63]], shape=(3, 4), dtype=uint8){% endhtmlescape %}</code>
</pre>

*NOTE*: Bitcast is implemented as a low-level cast, so machines with different
endian orderings will give different results.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `complex64`, `complex128`, `qint8`, `quint8`, `qint16`, `quint16`, `qint32`.
* <b>`type`</b>: A <a href="../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.bfloat16, tf.half, tf.float32, tf.float64, tf.int64, tf.int32, tf.uint8, tf.uint16, tf.uint32, tf.uint64, tf.int8, tf.int16, tf.complex64, tf.complex128, tf.qint8, tf.quint8, tf.qint16, tf.quint16, tf.qint32`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `type`.
