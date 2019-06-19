

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.Variable.SaveSliceInfo

## Class `SaveSliceInfo`



### Aliases:

* Class `tf.Variable.SaveSliceInfo`
* Class `tf.contrib.eager.Variable.SaveSliceInfo`



Defined in [`tensorflow/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/variables.py).

Information on how to save this Variable as a slice.

Provides internal support for saving variables as slices of a larger
variable.  This API is not public and is subject to change.

Available properties:

* full_name
* full_shape
* var_offset
* var_shape

## Properties

<h3 id="spec"><code>spec</code></h3>

Computes the spec string used for saving.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    full_name=None,
    full_shape=None,
    var_offset=None,
    var_shape=None,
    save_slice_info_def=None,
    import_scope=None
)
```

Create a `SaveSliceInfo`.

#### Args:

* <b>`full_name`</b>: Name of the full variable of which this `Variable` is a
      slice.
* <b>`full_shape`</b>: Shape of the full variable, as a list of int.
* <b>`var_offset`</b>: Offset of this `Variable` into the full variable, as a
      list of int.
* <b>`var_shape`</b>: Shape of this `Variable`, as a list of int.
* <b>`save_slice_info_def`</b>: `SaveSliceInfoDef` protocol buffer. If not `None`,
    recreates the SaveSliceInfo object its contents.
    `save_slice_info_def` and other arguments are mutually
    exclusive.
* <b>`import_scope`</b>: Optional `string`. Name scope to add. Only used
    when initializing from protocol buffer.

<h3 id="to_proto"><code>to_proto</code></h3>

``` python
to_proto(export_scope=None)
```

Returns a SaveSliceInfoDef() proto.

#### Args:

* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

A `SaveSliceInfoDef` protocol buffer, or None if the `Variable` is not
in the specified name scope.



