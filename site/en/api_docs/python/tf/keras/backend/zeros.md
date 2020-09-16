description: Instantiates an all-zeros variable and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.zeros" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.zeros

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1293-L1334">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates an all-zeros variable and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.zeros`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.zeros(
    shape, dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
Tuple or list of integers, shape of returned Keras variable
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
data type of returned Keras variable
</td>
</tr><tr>
<td>
`name`
</td>
<td>
name of returned Keras variable
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A variable (including Keras metadata), filled with `0.0`.
Note that if `shape` was symbolic, we cannot return a variable,
and will return a dynamically-shaped tensor instead.
</td>
</tr>

</table>



#### Example:



```
>>> kvar = tf.keras.backend.zeros((3,4))
>>> tf.keras.backend.eval(kvar)
array([[0.,  0.,  0.,  0.],
       [0.,  0.,  0.,  0.],
       [0.,  0.,  0.,  0.]], dtype=float32)
>>> A = tf.constant([1,2,3])
>>> kvar2 = tf.keras.backend.zeros(A.shape) # [0., 0., 0.]
>>> tf.keras.backend.eval(kvar2)
array([0., 0., 0.], dtype=float32)
>>> kvar3 = tf.keras.backend.zeros(A.shape,dtype=tf.int32)
>>> tf.keras.backend.eval(kvar3)
array([0, 0, 0], dtype=int32)
>>> kvar4 = tf.keras.backend.zeros([2,3])
>>> tf.keras.backend.eval(kvar4)
array([[0., 0., 0.],
       [0., 0., 0.]], dtype=float32)
```