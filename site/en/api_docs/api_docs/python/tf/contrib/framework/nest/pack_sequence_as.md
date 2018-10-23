

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.nest.pack_sequence_as

``` python
pack_sequence_as(
    structure,
    flat_sequence
)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/util/nest.py).

Returns a given flattened sequence packed into a nest.

If `structure` is a scalar, `flat_sequence` must be a single-element list;
in this case the return value is `flat_sequence[0]`.

#### Args:

* <b>`structure`</b>: Nested structure, whose structure is given by nested lists,
      tuples, and dicts. Note: numpy arrays and strings are considered
      scalars.
* <b>`flat_sequence`</b>: flat sequence to pack.


#### Returns:

* <b>`packed`</b>: `flat_sequence` converted to have the same recursive structure as
    `structure`.


#### Raises:

* <b>`ValueError`</b>: If nest and structure have different element counts.