description: Constrains Conv2D kernel weights to be the same for each radius.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.constraints.RadialConstraint" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.constraints.RadialConstraint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/constraints.py#L191-L268">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Constrains `Conv2D` kernel weights to be the same for each radius.

Inherits From: [`Constraint`](../../../tf/keras/constraints/Constraint.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.constraints.radial_constraint`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.constraints.RadialConstraint`, `tf.compat.v1.keras.constraints.radial_constraint`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

Also available via the shortcut function
<a href="../../../tf/keras/constraints/RadialConstraint.md"><code>tf.keras.constraints.radial_constraint</code></a>.

For example, the desired output for the following 4-by-4 kernel:

```
    kernel = [[v_00, v_01, v_02, v_03],
              [v_10, v_11, v_12, v_13],
              [v_20, v_21, v_22, v_23],
              [v_30, v_31, v_32, v_33]]
```

is this::

```
    kernel = [[v_11, v_11, v_11, v_11],
              [v_11, v_33, v_33, v_11],
              [v_11, v_33, v_33, v_11],
              [v_11, v_11, v_11, v_11]]
```

This constraint can be applied to any `Conv2D` layer version, including
`Conv2DTranspose` and `SeparableConv2D`, and with either `"channels_last"` or
`"channels_first"` data format. The method assumes the weight tensor is of
shape `(rows, cols, input_depth, output_depth)`.

## Methods

<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/constraints.py#L41-L42">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>






