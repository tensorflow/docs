description: MinMaxNorm weight constraint.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.constraints.MinMaxNorm" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.constraints.MinMaxNorm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/constraints.py#L133-L186">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



MinMaxNorm weight constraint.

Inherits From: [`Constraint`](../../../tf/keras/constraints/Constraint.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.constraints.min_max_norm`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.constraints.MinMaxNorm`, `tf.compat.v1.keras.constraints.min_max_norm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.constraints.MinMaxNorm(
    min_value=0.0, max_value=1.0, rate=1.0, axis=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

Constrains the weights incident to each hidden unit
to have the norm between a lower bound and an upper bound.

Also available via the shortcut function <a href="../../../tf/keras/constraints/MinMaxNorm.md"><code>tf.keras.constraints.min_max_norm</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`min_value`
</td>
<td>
the minimum norm for the incoming weights.
</td>
</tr><tr>
<td>
`max_value`
</td>
<td>
the maximum norm for the incoming weights.
</td>
</tr><tr>
<td>
`rate`
</td>
<td>
rate for enforcing the constraint: weights will be
rescaled to yield
`(1 - rate) * norm + rate * norm.clip(min_value, max_value)`.
Effectively, this means that rate=1.0 stands for strict
enforcement of the constraint, while rate<1.0 means that
weights will be rescaled at each step to slowly move
towards a value inside the desired interval.
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



