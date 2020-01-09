page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.bow_encoder

``` python
tf.contrib.layers.bow_encoder(
    ids,
    vocab_size,
    embed_dim,
    sparse_lookup=True,
    initializer=None,
    regularizer=None,
    trainable=True,
    scope=None,
    reuse=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/encoders.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/layers/python/layers/encoders.py).

Maps a sequence of symbols to a vector per example by averaging embeddings.

#### Args:

* <b>`ids`</b>: `[batch_size, doc_length]` `Tensor` or `SparseTensor` of type
    `int32` or `int64` with symbol ids.
* <b>`vocab_size`</b>: Integer number of symbols in vocabulary.
* <b>`embed_dim`</b>: Integer number of dimensions for embedding matrix.
* <b>`sparse_lookup`</b>: `bool`, if `True`, converts ids to a `SparseTensor`
      and performs a sparse embedding lookup. This is usually faster,
      but not desirable if padding tokens should have an embedding. Empty rows
      are assigned a special embedding.
* <b>`initializer`</b>: An initializer for the embeddings, if `None` default for
      current scope is used.
* <b>`regularizer`</b>: Optional regularizer for the embeddings.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`scope`</b>: Optional string specifying the variable scope for the op, required
      if `reuse=True`.
* <b>`reuse`</b>: If `True`, variables inside the op will be reused.


#### Returns:

Encoding `Tensor` `[batch_size, embed_dim]` produced by
averaging embeddings.


#### Raises:

* <b>`ValueError`</b>: If `embed_dim` or `vocab_size` are not specified.