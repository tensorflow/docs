description: Retrieves the elements of indices indices in the tensor reference.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.gather" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.gather

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1918-L1947">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Retrieves the elements of indices `indices` in the tensor `reference`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.gather`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.gather(
    reference, indices
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`reference`
</td>
<td>
A tensor.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
An integer tensor of indices.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor of same type as `reference`.
</td>
</tr>

</table>



#### Examples:



```
>>> var = tf.keras.backend.variable([[1, 2, 3], [4, 5, 6]])
>>> tf.keras.backend.eval(var)
array([[1., 2., 3.],
       [4., 5., 6.]], dtype=float32)
>>> var_gathered = tf.keras.backend.gather(var, [0])
>>> tf.keras.backend.eval(var_gathered)
array([[1., 2., 3.]], dtype=float32)
>>> var_gathered = tf.keras.backend.gather(var, [1])
>>> tf.keras.backend.eval(var_gathered)
array([[4., 5., 6.]], dtype=float32)
>>> var_gathered = tf.keras.backend.gather(var, [0,1,0])
>>> tf.keras.backend.eval(var_gathered)
array([[1., 2., 3.],
       [4., 5., 6.],
       [1., 2., 3.]], dtype=float32)
```