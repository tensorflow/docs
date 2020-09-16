description: MaxNorm weight constraint.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.constraints.MaxNorm" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.constraints.MaxNorm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/constraints.py#L45-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



MaxNorm weight constraint.

Inherits From: [`Constraint`](../../../tf/keras/constraints/Constraint.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.constraints.max_norm`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.constraints.MaxNorm`, `tf.compat.v1.keras.constraints.max_norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.constraints.MaxNorm(
    max_value=2, axis=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

Constrains the weights incident to each hidden unit
to have a norm less than or equal to a desired value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`m`
</td>
<td>
the maximum norm for the incoming weights.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
integer, axis along which to calculate weight norms.
For instance, in a `Dense` layer the weight matrix
has shape `(input_dim, output_dim)`,
set `axis` to `0` to constrain each weight vector
of length `(input_dim,)`.
In a `Conv2D` layer with `data_format="channels_last"`,
the weight tensor has shape
`(rows, cols, input_depth, output_depth)`,
set `axis` to `[0, 1, 2]`
to constrain the weights of each filter tensor of size
`(rows, cols, input_depth)`.
</td>
</tr>
</table>



## Methods

<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/constraints.py#L77-L78">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>




<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/constraints.py#L71-L75">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    w
)
</code></pre>

Call self as a function.




