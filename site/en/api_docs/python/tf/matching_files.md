


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.matching_files

### `tf.matching_files`

```
tf.matching_files(pattern, name=None)
```


See the guide: [Inputs and Readers > Dealing with the filesystem](../../../api_guides/python/io_ops#Dealing_with_the_filesystem)

Returns the set of files matching a pattern.

Note that this routine only supports wildcard characters in the
basename portion of the pattern, not in the directory portion.

#### Args:

* <b>`pattern`</b>: A `Tensor` of type `string`. A (scalar) shell wildcard pattern.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `string`. A vector of matching filenames.

Defined in `tensorflow/python/ops/gen_io_ops.py`.

