

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.load_variable_slot_initializer

``` python
load_variable_slot_initializer(
    ckpt_path,
    old_tensor_name,
    primary_partition_info,
    new_row_vocab_size,
    new_col_vocab_size,
    old_row_vocab_file=None,
    new_row_vocab_file=None,
    old_col_vocab_file=None,
    new_col_vocab_file=None,
    num_row_oov_buckets=0,
    num_col_oov_buckets=0,
    initializer=None,
    max_rows_in_memory=-1
)
```



Defined in [`tensorflow/contrib/framework/python/ops/checkpoint_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/framework/python/ops/checkpoint_ops.py).

Loads pre-trained multi-class slots for linear models from checkpoint.

Wrapper around `load_and_remap_matrix_initializer()` specialized for loading
multi-class slots (such as optimizer accumulators) and remapping them
according to the provided vocab files. See docs for
`load_and_remap_matrix_initializer()` for more details.  Takes in a
`variable_scope._PartitionInfo` representing the slot's primary `Variable`'s
partitioning.  This is necessary since accumulator `Variable` creation ignores
primary scoping and partitioning information.

#### Args:

* <b>`ckpt_path`</b>: Path to the TensorFlow checkpoint (version 2, `TensorBundle`)
    from which the old matrix `Tensor` will be loaded.
* <b>`old_tensor_name`</b>: Name of the 2-D `Tensor` to load from checkpoint.
* <b>`primary_partition_info`</b>: A `variable_scope._PartitionInfo` containing this
    slot's primary `Variable`'s partitioning information.  This is used to
    calculate the offset and override the partition_info passed to the call to
    _initialize.
* <b>`new_row_vocab_size`</b>: `int` specifying the number of entries in
    `new_row_vocab_file`. If no row remapping is needed (no row vocab
    provided), this should be equal to the number of rows to load from the old
    matrix (which can theoretically be smaller than the number of rows in the
    old matrix).
* <b>`new_col_vocab_size`</b>: `int` specifying the number of entries in
    `new_col_vocab_file`. If no column remapping is needed (no column vocab
    provided), this should be equal to the number of columns in the old
    matrix.
* <b>`old_row_vocab_file`</b>: A scalar `Tensor` of type `string` containing the
    path to the old row vocabulary file. Can be None, which represents no
    remapping on the row axis.
* <b>`new_row_vocab_file`</b>: A scalar `Tensor` of type `string` containing the path
    to the new row vocabulary file. Can be None, which represents no remapping
    on the row axis.
* <b>`old_col_vocab_file`</b>: A scalar `Tensor` of type `string` containing the
    path to the old column vocabulary file. Can be None, which represents no
    remapping on the column axis.
* <b>`new_col_vocab_file`</b>: A scalar `Tensor` of type `string` containing the path
    to the new column vocabulary file. Can be None, which represents no
    remapping on the column axis.
* <b>`num_row_oov_buckets`</b>: `int` specifying the number of out-of-vocabulary rows
    to append. Must be >= 0.
* <b>`num_col_oov_buckets`</b>: `int` specifying the number of out-of-vocabulary
    columns to append. Must be >= 0.
* <b>`initializer`</b>: Initializer function to initialize missing values. Accepts a
    1-D tensor as the arg to specify the shape of the returned tensor. If
    `None`, defaults to using `zeros_initializer()`.
* <b>`max_rows_in_memory`</b>: `int` specifying the maximum number of rows to load from
    the checkpoint at once. If less than or equal to 0, the entire matrix will
    be loaded into memory. Setting this arg trades increased disk reads for
    lower memory usage.


#### Returns:

A variable initializer function that should be used to initialize a
(potentially partitioned) `Variable` whose complete shape is
`[new_row_vocab_size + num_row_oov_buckets, new_col_vocab_size +
num_col_oov_buckets]`.


#### Raises:

* <b>`TypeError`</b>: If `initializer` is specified but not callable.