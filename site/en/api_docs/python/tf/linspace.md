description: Generates evenly-spaced values in an interval along a given axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linspace" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linspace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L109-L218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates evenly-spaced values in an interval along a given axis.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lin_space`, `tf.compat.v1.linspace`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linspace(
    start, stop, num, name=None, axis=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

A sequence of `num` evenly-spaced values are generated beginning at `start`
along a given `axis`.
If `num > 1`, the values in the sequence increase by `stop - start / num - 1`,
so that the last one is exactly `stop`. If `num <= 0`, `ValueError` is raised.

Matches
[np.linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)'s
behaviour
except when `num == 0`.

#### For example:



```
tf.linspace(10.0, 12.0, 3, name="linspace") => [ 10.0  11.0  12.0]
```

`Start` and `stop` can be tensors of arbitrary size:

```
>>> tf.linspace([0., 5.], [10., 40.], 5, axis=0)
<tf.Tensor: shape=(5, 2), dtype=float32, numpy=
array([[ 0.  ,  5.  ],
       [ 2.5 , 13.75],
       [ 5.  , 22.5 ],
       [ 7.5 , 31.25],
       [10.  , 40.  ]], dtype=float32)>
```

`Axis` is where the values will be generated (the dimension in the
returned tensor which corresponds to the axis will be equal to `num`)

```
>>> tf.linspace([0., 5.], [10., 40.], 5, axis=-1)
<tf.Tensor: shape=(2, 5), dtype=float32, numpy=
array([[ 0.  ,  2.5 ,  5.  ,  7.5 , 10.  ],
       [ 5.  , 13.75, 22.5 , 31.25, 40.  ]], dtype=float32)>
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`start`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`,
`float32`, `float64`. N-D tensor. First entry in the range.
</td>
</tr><tr>
<td>
`stop`
</td>
<td>
A `Tensor`. Must have the same type and shape as `start`. N-D tensor.
Last entry in the range.
</td>
</tr><tr>
<td>
`num`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`. 0-D
tensor. Number of values to generate.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Axis along which the operation is performed (used only when N-D
tensors are provided).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `start`.
</td>
</tr>

</table>

