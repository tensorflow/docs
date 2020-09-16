description: Return a Tensor with the same shape and contents as input.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.identity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.identity

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/array_ops.py#L239-L286">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return a Tensor with the same shape and contents as input.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.identity`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.identity(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The return value is not the same Tensor as the original, but contains the same
values.  This operation is fast when used on the same device.

#### For example:



```
>>> a = tf.constant([0.78])
>>> a_identity = tf.identity(a)
>>> a.numpy()
array([0.78], dtype=float32)
>>> a_identity.numpy()
array([0.78], dtype=float32)
```

Calling <a href="../tf/identity.md"><code>tf.identity</code></a> on a variable will make a Tensor that represents the
value of that variable at the time it is called. This is equivalent to calling
`<variable>.read_value()`.

```
>>> a = tf.Variable(5)
>>> a_identity = tf.identity(a)
>>> a.assign_add(1)
<tf.Variable ... shape=() dtype=int32, numpy=6>
>>> a.numpy()
6
>>> a_identity.numpy()
5
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

