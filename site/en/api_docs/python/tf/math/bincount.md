page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.bincount


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L3156-L3228">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Counts the number of occurrences of each value in an integer array.

### Aliases:

* `tf.compat.v2.math.bincount`


``` python
tf.math.bincount(
    arr,
    weights=None,
    minlength=None,
    maxlength=None,
    dtype=tf.dtypes.int32,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If `minlength` and `maxlength` are not given, returns a vector with length
`tf.reduce_max(arr) + 1` if `arr` is non-empty, and length 0 otherwise.
If `weights` are non-None, then index `i` of the output stores the sum of the
value in `weights` at each index where the corresponding value in `arr` is
`i`.

```python
values = tf.constant([1,1,2,3,2,4,4,5])
tf.math.bincount(values) #[0 2 2 1 2 1]
```
Vector length = Maximum element in vector `values` is 5. Adding 1, which is 6
                will be the vector length.

Each bin value in the output indicates number of occurrences of the particular
index. Here, index 1 in output has a value 2. This indicates value 1 occurs
two times in `values`.

```python
values = tf.constant([1,1,2,3,2,4,4,5])
weights = tf.constant([1,5,0,1,0,5,4,5])
tf.math.bincount(values, weights=weights) #[0 6 0 1 9 5]
```
Bin will be incremented by the corresponding weight instead of 1.
Here, index 1 in output has a value 6. This is the summation of weights
corresponding to the value in `values`.

#### Args:


* <b>`arr`</b>: An int32 tensor of non-negative values.
* <b>`weights`</b>: If non-None, must be the same shape as arr. For each value in
  `arr`, the bin will be incremented by the corresponding weight instead of
  1.
* <b>`minlength`</b>: If given, ensures the output has length at least `minlength`,
  padding with zeros at the end if necessary.
* <b>`maxlength`</b>: If given, skips values in `arr` that are equal or greater than
  `maxlength`, ensuring that the output has length at most `maxlength`.
* <b>`dtype`</b>: If `weights` is None, determines the type of the output bins.
* <b>`name`</b>: A name scope for the associated operations (optional).


#### Returns:

A vector with the same dtype as `weights` or the given `dtype`. The bin
values.



#### Raises:

`InvalidArgumentError` if negative values are provided as an input.
