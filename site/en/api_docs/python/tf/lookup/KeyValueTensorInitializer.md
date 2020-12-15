description: Table initializers given keys and values tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lookup.KeyValueTensorInitializer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="initialize"/>
</div>

# tf.lookup.KeyValueTensorInitializer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/lookup_ops.py#L498-L562">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Table initializers given `keys` and `values` tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lookup.KeyValueTensorInitializer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lookup.KeyValueTensorInitializer(
    keys, values, key_dtype=None, value_dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

```
>>> keys_tensor = tf.constant(['a', 'b', 'c'])
>>> vals_tensor = tf.constant([7, 8, 9])
>>> input_tensor = tf.constant(['a', 'f'])
>>> init = tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor)
>>> table = tf.lookup.StaticHashTable(
...     init,
...     default_value=-1)
>>> table.lookup(input_tensor).numpy()
array([ 7, -1], dtype=int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`keys`
</td>
<td>
The tensor for the keys.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
The tensor for the values.
</td>
</tr><tr>
<td>
`key_dtype`
</td>
<td>
The `keys` data type. Used when `keys` is a python array.
</td>
</tr><tr>
<td>
`value_dtype`
</td>
<td>
The `values` data type. Used when `values` is a python array.
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
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`key_dtype`
</td>
<td>
The expected table key dtype.
</td>
</tr><tr>
<td>
`value_dtype`
</td>
<td>
The expected table value dtype.
</td>
</tr>
</table>



## Methods

<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/lookup_ops.py#L543-L562">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>initialize(
    table
)
</code></pre>

Initializes the given `table` with `keys` and `values` tensors.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`table`
</td>
<td>
The table to initialize.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The operation that initializes the table.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when the keys and values data types do not match the table
key and value data types.
</td>
</tr>
</table>





