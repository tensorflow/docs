

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.matching_files

``` python
tf.matching_files(
    pattern,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_io_ops.py`.

See the guide: [Inputs and Readers > Dealing with the filesystem](../../../api_guides/python/io_ops#Dealing_with_the_filesystem)

Returns the set of files matching one or more glob patterns.

Note that this routine only supports wildcard characters in the
basename portion of the pattern, not in the directory portion.
Note also that the order of filenames returned can be non-deterministic.

#### Args:

* <b>`pattern`</b>: A `Tensor` of type `string`.
    Shell wildcard pattern(s). Scalar or vector of type string.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.