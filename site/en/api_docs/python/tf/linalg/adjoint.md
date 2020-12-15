description: Transposes the last two dimensions of and conjugates tensor matrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.adjoint" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.adjoint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linalg_impl.py#L102-L128">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transposes the last two dimensions of and conjugates tensor `matrix`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.adjoint`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.adjoint(
    matrix, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```python
x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.adjoint(x)  # [[1 - 1j, 4 - 4j],
                      #  [2 - 2j, 5 - 5j],
                      #  [3 - 3j, 6 - 6j]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`matrix`
</td>
<td>
A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`,
or `complex128` with shape `[..., M, M]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name to give this `Op` (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The adjoint (a.k.a. Hermitian transpose a.k.a. conjugate transpose) of
matrix.
</td>
</tr>

</table>

