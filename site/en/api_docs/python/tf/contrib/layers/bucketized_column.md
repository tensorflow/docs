page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.bucketized_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/feature_column.py#L2210-L2224">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a _BucketizedColumn for discretizing dense input.

``` python
tf.contrib.layers.bucketized_column(
    source_column,
    boundaries
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`source_column`</b>: A _RealValuedColumn defining dense column.
* <b>`boundaries`</b>: A list or tuple of floats specifying the boundaries. It has to
  be sorted.


#### Returns:

A _BucketizedColumn.



#### Raises:


* <b>`ValueError`</b>: if 'boundaries' is empty or not sorted.
