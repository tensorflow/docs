description: Returns input function that would feed Pandas DataFrame into the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.inputs.pandas_input_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.estimator.inputs.pandas_input_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/inputs/pandas_io.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns input function that would feed Pandas DataFrame into the model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.inputs.pandas_input_fn(
    x, y=None, batch_size=128, num_epochs=1, shuffle=None, queue_capacity=1000,
    num_threads=1, target_column='target'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: `y`'s index must match `x`'s index.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
pandas `DataFrame` object.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
pandas `Series` object or `DataFrame`. `None` if absent.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
int, size of batches to return.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
int, number of epochs to iterate over data. If not `None`, read
attempts that would exceed this value will raise `OutOfRangeError`.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
bool, whether to read the records in random order.
</td>
</tr><tr>
<td>
`queue_capacity`
</td>
<td>
int, size of the read queue. If `None`, it will be set
roughly to the size of `x`.
</td>
</tr><tr>
<td>
`num_threads`
</td>
<td>
Integer, number of threads used for reading and enqueueing. In
order to have predicted and repeatable order of reading and enqueueing,
such as in prediction and evaluation mode, `num_threads` should be 1.
</td>
</tr><tr>
<td>
`target_column`
</td>
<td>
str, name to give the target column `y`. This parameter is
not used when `y` is a `DataFrame`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Function, that has signature of ()->(dict of `features`, `target`)
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `x` already contains a column with the same name as `y`, or
if the indexes of `x` and `y` don't match.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if 'shuffle' is not provided or a bool.
</td>
</tr>
</table>

