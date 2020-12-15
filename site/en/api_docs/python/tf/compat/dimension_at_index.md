description: Compatibility utility required to allow for both V1 and V2 behavior in TF.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.dimension_at_index" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.dimension_at_index

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/tensor_shape.py#L132-L178">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compatibility utility required to allow for both V1 and V2 behavior in TF.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.compat.dimension_at_index`, `tf.compat.v1.dimension_at_index`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.dimension_at_index(
    shape, index
)
</code></pre>



<!-- Placeholder for "Used in" -->

Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to
coexist with the new behavior. This utility is a bridge between the two.

If you want to retrieve the Dimension instance corresponding to a certain
index in a TensorShape instance, use this utility, like this:

```
# If you had this in your V1 code:
dim = tensor_shape[i]

# Use `dimension_at_index` as direct replacement compatible with both V1 & V2:
dim = dimension_at_index(tensor_shape, i)

# Another possibility would be this, but WARNING: it only works if the
# tensor_shape instance has a defined rank.
dim = tensor_shape.dims[i]  # `dims` may be None if the rank is undefined!

# In native V2 code, we recommend instead being more explicit:
if tensor_shape.rank is None:
  dim = Dimension(None)
else:
  dim = tensor_shape.dims[i]

# Being more explicit will save you from the following trap (present in V1):
# you might do in-place modifications to `dim` and expect them to be reflected
# in `tensor_shape[i]`, but they would not be (as the Dimension object was
# instantiated on the fly.
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A TensorShape instance.
</td>
</tr><tr>
<td>
`index`
</td>
<td>
An integer index.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dimension object.
</td>
</tr>

</table>

