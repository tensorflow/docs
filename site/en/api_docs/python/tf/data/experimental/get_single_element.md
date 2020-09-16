description: Returns the single element in dataset as a nested structure of tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.get_single_element" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.get_single_element

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/get_single_element.py#L26-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the single element in `dataset` as a nested structure of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.get_single_element`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.get_single_element(
    dataset
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function enables you to use a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> in a stateless
"tensor-in tensor-out" expression, without creating an iterator.
This can be useful when your preprocessing transformations are expressed
as a `Dataset`, and you want to use the transformation at serving time.

#### For example:



```python
def preprocessing_fn(input_str):
  # ...
  return image, label

input_batch = ...  # input batch of BATCH_SIZE elements
dataset = (tf.data.Dataset.from_tensor_slices(input_batch)
           .map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)
           .batch(BATCH_SIZE))

image_batch, label_batch = tf.data.experimental.get_single_element(dataset)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset`
</td>
<td>
A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object containing a single element.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a> objects, corresponding to the single
element of `dataset`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if `dataset` is not a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object.
InvalidArgumentError (at runtime): if `dataset` does not contain exactly
one element.
</td>
</tr>
</table>

