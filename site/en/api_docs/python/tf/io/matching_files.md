page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.matching_files

### Aliases:

* `tf.io.matching_files`
* `tf.matching_files`

``` python
tf.io.matching_files(
    pattern,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_io_ops.py`.

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