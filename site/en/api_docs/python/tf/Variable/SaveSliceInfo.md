page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.Variable.SaveSliceInfo


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/Variable/SaveSliceInfo">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L1279-L1358">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SaveSliceInfo`

Information on how to save this Variable as a slice.



### Aliases:

* Class <a href="/api_docs/python/tf/Variable/SaveSliceInfo"><code>tf.compat.v1.Variable.SaveSliceInfo</code></a>
* Class <a href="/api_docs/python/tf/Variable/SaveSliceInfo"><code>tf.compat.v2.Variable.SaveSliceInfo</code></a>
* Class <a href="/api_docs/python/tf/Variable/SaveSliceInfo"><code>tf.contrib.eager.Variable.SaveSliceInfo</code></a>


<!-- Placeholder for "Used in" -->

Provides internal support for saving variables as slices of a larger
variable.  This API is not public and is subject to change.

#### Available properties:



* full_name
* full_shape
* var_offset
* var_shape

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L1293-L1326">View source</a>

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
* <b>`var_offset`</b>: Offset of this `Variable` into the full variable, as a list
  of int.
* <b>`var_shape`</b>: Shape of this `Variable`, as a list of int.
* <b>`save_slice_info_def`</b>: `SaveSliceInfoDef` protocol buffer. If not `None`,
  recreates the SaveSliceInfo object its contents. `save_slice_info_def`
  and other arguments are mutually exclusive.
* <b>`import_scope`</b>: Optional `string`. Name scope to add. Only used when
  initializing from protocol buffer.



## Properties

<h3 id="spec"><code>spec</code></h3>

Computes the spec string used for saving.




## Methods

<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L1336-L1358">View source</a>

``` python
to_proto(export_scope=None)
```

Returns a SaveSliceInfoDef() proto.


#### Args:


* <b>`export_scope`</b>: Optional `string`. Name scope to remove.


#### Returns:

A `SaveSliceInfoDef` protocol buffer, or None if the `Variable` is not
in the specified name scope.
