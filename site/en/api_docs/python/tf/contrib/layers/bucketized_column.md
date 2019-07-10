page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.bucketized_column

Creates a _BucketizedColumn for discretizing dense input.

``` python
tf.contrib.layers.bucketized_column(
    source_column,
    boundaries
)
```



Defined in [`contrib/layers/python/layers/feature_column.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/feature_column.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`source_column`</b>: A _RealValuedColumn defining dense column.
* <b>`boundaries`</b>: A list or tuple of floats specifying the boundaries. It has to
  be sorted.


#### Returns:

A _BucketizedColumn.



#### Raises:


* <b>`ValueError`</b>: if 'boundaries' is empty or not sorted.