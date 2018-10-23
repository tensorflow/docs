

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.bincount

``` python
tf.bincount(
    arr,
    weights=None,
    minlength=None,
    maxlength=None,
    dtype=tf.int32
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/math_ops.py).

Counts the number of occurrences of each value in an integer array.

If `minlength` and `maxlength` are not given, returns a vector with length
`tf.reduce_max(arr) + 1` if `arr` is non-empty, and length 0 otherwise.
If `weights` are non-None, then index `i` of the output stores the sum of the
value in `weights` at each index where the corresponding value in `arr` is
`i`.

#### Args:

* <b>`arr`</b>: An int32 tensor of non-negative values.
* <b>`weights`</b>: If non-None, must be the same shape as arr. For each value in
      `arr`, the bin will be incremented by the corresponding weight instead
      of 1.
* <b>`minlength`</b>: If given, ensures the output has length at least `minlength`,
      padding with zeros at the end if necessary.
* <b>`maxlength`</b>: If given, skips values in `arr` that are equal or greater than
      `maxlength`, ensuring that the output has length at most `maxlength`.
* <b>`dtype`</b>: If `weights` is None, determines the type of the output bins.


#### Returns:

A vector with the same dtype as `weights` or the given `dtype`. The bin
values.