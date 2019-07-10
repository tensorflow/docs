page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.list_objects

Traverse the object graph and list all accessible objects.

``` python
tf.contrib.checkpoint.list_objects(root_trackable)
```



Defined in [`python/training/tracking/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/tracking/util.py).

<!-- Placeholder for "Used in" -->

Looks for `Trackable` objects which are dependencies of
`root_trackable`. Includes slot variables only if the variable they are
slotting for and the optimizer are dependencies of `root_trackable`
(i.e. if they would be saved with a checkpoint).

#### Args:


* <b>`root_trackable`</b>: A `Trackable` object whose dependencies should be flattened.


#### Returns:

A flat list of objects.
