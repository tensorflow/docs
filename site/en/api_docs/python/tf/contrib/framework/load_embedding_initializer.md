

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.load_embedding_initializer

``` python
tf.contrib.framework.load_embedding_initializer(
    ckpt_path,
    embedding_tensor_name,
    new_vocab_size,
    embedding_dim,
    old_vocab_file,
    new_vocab_file,
    old_vocab_size=-1,
    num_oov_buckets=0,
    initializer=None,
    max_rows_in_memory=-1
)
```



Defined in [`tensorflow/python/training/checkpoint_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/training/checkpoint_ops.py).

Returns a variable initializer for loading pre-trained embeddings.

Wrapper around `load_and_remap_matrix_initializer()` specialized for loading
embedding weights and remapping according to the provided vocab files. See
docs for `load_and_remap_matrix_initializer()` for more details.

NOTE: Only for use with div-partitioned variables / vocabularies.

#### Args:

* <b>`ckpt_path`</b>: Path to the TensorFlow checkpoint (version 2, `TensorBundle`)
    from which the old matrix `Tensor` will be loaded.
* <b>`embedding_tensor_name`</b>: Name of the 2-D `Tensor` to load from checkpoint.
* <b>`new_vocab_size`</b>: Number of entries in the new vocab.
* <b>`embedding_dim`</b>: `int` specifying the dimension of the embedding vectors from
    the checkpoint. Must match the number of columns in the old embedding
    matrix.
* <b>`old_vocab_file`</b>: A scalar `Tensor` of type `string` containing the
    path to the old vocabulary file.
* <b>`new_vocab_file`</b>: A scalar `Tensor` of type `string` containing the
    path to the new vocabulary file.
* <b>`old_vocab_size`</b>: The number of entries to consider in the old vocabulary.
    With the default value of -1, the entire old row vocabulary file will be
    used.  Otherwise, only the first `old_vocab_size` entries will be
    considered for remapping.Must be smaller than the length of
    `old_row_vocab_file`.
* <b>`num_oov_buckets`</b>: `int` specifying the number of out-of-vocabulary
    buckets to use. Must be >= 0.
* <b>`initializer`</b>: Initializer function that accepts a 1-D tensor as the arg to
    specify the shape of the returned tensor. If `None`, defaults to using
    `truncated_normal_initializer()`.
* <b>`max_rows_in_memory`</b>: `int` specifying the maximum number of rows to load from
    the checkpoint at once. If less than or equal to 0, the entire matrix will
    be loaded into memory. Setting this arg trades increased disk reads for
    lower memory usage.


#### Returns:

A variable initializer function.