page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.AdditiveAttention


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/AdditiveAttention">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/dense_attention.py#L317-L455">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AdditiveAttention`

Additive attention layer, a.k.a. Bahdanau-style attention.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/AdditiveAttention"><code>tf.compat.v1.keras.layers.AdditiveAttention</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/AdditiveAttention"><code>tf.compat.v2.keras.layers.AdditiveAttention</code></a>


<!-- Placeholder for "Used in" -->

Inputs are `query` tensor of shape `[batch_size, Tq, dim]`, `value` tensor of
shape `[batch_size, Tv, dim]` and `key` tensor of shape
`[batch_size, Tv, dim]`. The calculation follows the steps:

1. Reshape `query` and `value` into shapes `[batch_size, Tq, 1, dim]`
   and `[batch_size, 1, Tv, dim]` respectively.
2. Calculate scores with shape `[batch_size, Tq, Tv]` as a non-linear
   sum: `scores = tf.reduce_sum(tf.tanh(query + value), axis=-1)`
3. Use scores to calculate a distribution with shape
   `[batch_size, Tq, Tv]`: `distribution = tf.nn.softmax(scores)`.
4. Use `distribution` to create a linear combination of `value` with
   shape `batch_size, Tq, dim]`:
   `return tf.matmul(distribution, value)`.

#### Args:


* <b>`use_scale`</b>: If `True`, will create a variable to scale the attention scores.
* <b>`causal`</b>: Boolean. Set to `True` for decoder self-attention. Adds a mask such
  that position `i` cannot attend to positions `j > i`. This prevents the
  flow of information from the future towards the past.


#### Call Arguments:



* <b>`inputs`</b>: List of the following tensors:
  * query: Query `Tensor` of shape `[batch_size, Tq, dim]`.
  * value: Value `Tensor` of shape `[batch_size, Tv, dim]`.
  * key: Optional key `Tensor` of shape `[batch_size, Tv, dim]`. If not
    given, will use `value` for both `key` and `value`, which is the
    most common case.
* <b>`mask`</b>: List of the following tensors:
  * query_mask: A boolean mask `Tensor` of shape `[batch_size, Tq]`.
    If given, the output will be zero at the positions where
    `mask==False`.
  * value_mask: A boolean mask `Tensor` of shape `[batch_size, Tv]`.
    If given, will apply the mask such that values at positions where
    `mask==False` do not contribute to the result.


#### Output shape:


Attention outputs of shape `[batch_size, Tq, dim]`.


The meaning of `query`, `value` and `key` depend on the application. In the
case of text similarity, for example, `query` is the sequence embeddings of
the first piece of text and `value` is the sequence embeddings of the second
piece of text. `key` is usually the same tensor as `value`.

Here is a code example for using `AdditiveAttention` in a CNN+Attention
network:

```python
# Variable-length int sequences.
query_input = tf.keras.Input(shape=(None,), dtype='int32')
value_input = tf.keras.Input(shape=(None,), dtype='int32')

# Embedding lookup.
token_embedding = tf.keras.layers.Embedding(max_tokens, dimension)
# Query embeddings of shape [batch_size, Tq, dimension].
query_embeddings = token_embedding(query_input)
# Value embeddings of shape [batch_size, Tv, dimension].
value_embeddings = token_embedding(query_input)

# CNN layer.
cnn_layer = tf.keras.layers.Conv1D(
    filters=100,
    kernel_size=4,
    # Use 'same' padding so outputs have the same shape as inputs.
    padding='same')
# Query encoding of shape [batch_size, Tq, filters].
query_seq_encoding = cnn_layer(query_embeddings)
# Value encoding of shape [batch_size, Tv, filters].
value_seq_encoding = cnn_layer(value_embeddings)

# Query-value attention of shape [batch_size, Tq, filters].
query_value_attention_seq = tf.keras.layers.AdditiveAttention()(
    [query_seq_encoding, value_seq_encoding])

# Reduce over the sequence axis to produce encodings of shape
# [batch_size, filters].
query_encoding = tf.keras.layers.GlobalAveragePooling1D()(
    query_seq_encoding)
query_value_attention = tf.keras.layers.GlobalAveragePooling1D()(
    query_value_attention_seq)

# Concatenate query and document encodings to produce a DNN input layer.
input_layer = tf.keras.layers.Concatenate()(
    [query_encoding, query_value_attention])

# Add DNN layers, and create Model.
# ...
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/dense_attention.py#L411-L413">View source</a>

``` python
__init__(
    use_scale=True,
    **kwargs
)
```
