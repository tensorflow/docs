description: Bitcasts a tensor from one type to another without copying data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.bitcast" />
<meta itemprop="path" content="Stable" />
</div>

# tf.bitcast

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Bitcasts a tensor from one type to another without copying data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.bitcast`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.bitcast(
    input, type, name=None
)
</code></pre>



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



```
>>> a = [1., 2., 3.]
>>> equality_bitcast = tf.bitcast(a, tf.complex128)
Traceback (most recent call last):
...
InvalidArgumentError: Cannot bitcast from 1 to 18 [Op:Bitcast]
>>> equality_cast = tf.cast(a, tf.complex128)
>>> print(equality_cast)
tf.Tensor([1.+0.j 2.+0.j 3.+0.j], shape=(3,), dtype=complex128)
```

#### Example 2:



```
>>> tf.bitcast(tf.constant(0xffffffff, dtype=tf.uint32), tf.uint8)
<tf.Tensor: shape=(4,), dtype=uint8, numpy=array([255, 255, 255, 255], dtype=uint8)>
```

#### Example 3:



```
>>> x = [1., 2., 3.]
>>> y = [0., 2., 3.]
>>> equality= tf.equal(x,y)
>>> equality_cast = tf.cast(equality,tf.float32)
>>> equality_bitcast = tf.bitcast(equality_cast,tf.uint8)
>>> print(equality)
tf.Tensor([False True True], shape=(3,), dtype=bool)
>>> print(equality_cast)
tf.Tensor([0. 1. 1.], shape=(3,), dtype=float32)
>>> print(equality_bitcast)
tf.Tensor(
    [[  0   0   0   0]
     [  0   0 128  63]
     [  0   0 128  63]], shape=(3, 4), dtype=uint8)
```

*NOTE*: Bitcast is implemented as a low-level cast, so machines with different
endian orderings will give different results.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `complex64`, `complex128`, `qint8`, `quint8`, `qint16`, `quint16`, `qint32`.
</td>
</tr><tr>
<td>
`type`
</td>
<td>
A <a href="../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.bfloat16, tf.half, tf.float32, tf.float64, tf.int64, tf.int32, tf.uint8, tf.uint16, tf.uint32, tf.uint64, tf.int8, tf.int16, tf.complex64, tf.complex128, tf.qint8, tf.quint8, tf.qint16, tf.quint16, tf.qint32`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `type`.
</td>
</tr>

</table>

