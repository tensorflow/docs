page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.create_partitioned_variables

``` python
tf.create_partitioned_variables(
    shape,
    slicing,
    initializer,
    dtype=tf.float32,
    trainable=True,
    collections=None,
    name=None,
    reuse=None
)
```



Defined in [`tensorflow/python/ops/partitioned_variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/partitioned_variables.py).

Create a list of partitioned variables according to the given `slicing`.

Currently only one dimension of the full variable can be sliced, and the
full variable can be reconstructed by the concatenation of the returned
list along that dimension.

#### Args:

* <b>`shape`</b>: List of integers.  The shape of the full variable.
* <b>`slicing`</b>: List of integers.  How to partition the variable.
    Must be of the same length as `shape`.  Each value
    indicate how many slices to create in the corresponding
    dimension.  Presently only one of the values can be more than 1;
    that is, the variable can only be sliced along one dimension.

    For convenience, The requested number of partitions does not have to
    divide the corresponding dimension evenly.  If it does not, the
    shapes of the partitions are incremented by 1 starting from partition
    0 until all slack is absorbed.  The adjustment rules may change in the
    future, but as you can save/restore these variables with different
    slicing specifications this should not be a problem.
* <b>`initializer`</b>: A `Tensor` of shape `shape` or a variable initializer
    function.  If a function, it will be called once for each slice,
    passing the shape and data type of the slice as parameters.  The
    function must return a tensor with the same shape as the slice.
* <b>`dtype`</b>: Type of the variables. Ignored if `initializer` is a `Tensor`.
* <b>`trainable`</b>: If True also add all the variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`collections`</b>: List of graph collections keys to add the variables to.
    Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
* <b>`name`</b>: Optional name for the full variable.  Defaults to
    `"PartitionedVariable"` and gets uniquified automatically.
* <b>`reuse`</b>: Boolean or `None`; if `True` and name is set, it would reuse
    previously created variables. if `False` it will create new variables.
    if `None`, it would inherit the parent scope reuse.


#### Returns:

A list of Variables corresponding to the slicing.


#### Raises:

* <b>`ValueError`</b>: If any of the arguments is malformed.