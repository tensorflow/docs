page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.constraints.RadialConstraint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/constraints/RadialConstraint">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L176-L249">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RadialConstraint`

Constrains `Conv2D` kernel weights to be the same for each radius.

Inherits From: [`Constraint`](../../../tf/keras/constraints/Constraint)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/constraints/RadialConstraint"><code>tf.compat.v1.keras.constraints.RadialConstraint</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/RadialConstraint"><code>tf.compat.v1.keras.constraints.radial_constraint</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/RadialConstraint"><code>tf.compat.v2.keras.constraints.RadialConstraint</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/RadialConstraint"><code>tf.compat.v2.keras.constraints.radial_constraint</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/RadialConstraint"><code>tf.keras.constraints.radial_constraint</code></a>


<!-- Placeholder for "Used in" -->

For example, the desired output for the following 4-by-4 kernel::

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

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L203-L217">View source</a>

``` python
__call__(w)
```

Call self as a function.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L40-L41">View source</a>

``` python
get_config()
```
