

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.nest.flatten

``` python
flatten(nest)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/util/nest.py).

Returns a flat sequence from a given nested structure.

If `nest` is not a sequence, tuple, or dict, then returns a single-element
list: `[nest]`.

#### Args:

* <b>`nest`</b>: an arbitrarily nested structure or a scalar object. Note, numpy
      arrays are considered scalars.


#### Returns:

  A Python list, the flattened version of the input.