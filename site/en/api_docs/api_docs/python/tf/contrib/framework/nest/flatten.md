

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.nest.flatten

``` python
flatten(nest)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/util/nest.py).

Returns a flat list from a given nested structure.

If `nest` is not a sequence, tuple, or dict, then returns a single-element
list: `[nest]`.

In the case of dict instances, the sequence consists of the values, sorted by
key to ensure deterministic behavior. This is true also for `OrderedDict`
instances: their sequence order is ignored, the sorting order of keys is
used instead. The same convention is followed in `pack_sequence_as`. This
correctly repacks dicts and `OrderedDict`s after they have been flattened,
and also allows flattening an `OrderedDict` and then repacking it back using
a correponding plain dict, or vice-versa.
Dictionaries with non-sortable keys cannot be flattened.

#### Args:

* <b>`nest`</b>: an arbitrarily nested structure or a scalar object. Note, numpy
      arrays are considered scalars.


#### Returns:

A Python list, the flattened version of the input.


#### Raises:

* <b>`TypeError`</b>: The nest is or contains a dict with non-sortable keys.