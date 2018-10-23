

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.matching_files

``` python
matching_files(
    pattern,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_io_ops.py`.

See the guide: [Inputs and Readers > Dealing with the filesystem](../../../api_guides/python/io_ops#Dealing_with_the_filesystem)

Returns the set of files matching one or more glob patterns.

Note that this routine only supports wildcard characters in the
basename portion of the pattern, not in the directory portion.

#### Args:

* <b>`pattern`</b>: A `Tensor` of type `string`.
    Shell wildcard pattern(s). Scalar or vector of type string.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`. A vector of matching filenames.