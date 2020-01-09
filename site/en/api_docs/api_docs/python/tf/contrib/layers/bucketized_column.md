

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.bucketized_column

``` python
tf.contrib.layers.bucketized_column(
    source_column,
    boundaries
)
```



Defined in [`tensorflow/contrib/layers/python/layers/feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/layers/python/layers/feature_column.py).

See the guide: [Layers (contrib) > Feature columns](../../../../../api_guides/python/contrib.layers#Feature_columns)

Creates a _BucketizedColumn for discretizing dense input.

#### Args:

* <b>`source_column`</b>: A _RealValuedColumn defining dense column.
* <b>`boundaries`</b>: A list or tuple of floats specifying the boundaries. It has to
    be sorted.


#### Returns:

A _BucketizedColumn.


#### Raises:

* <b>`ValueError`</b>: if 'boundaries' is empty or not sorted.