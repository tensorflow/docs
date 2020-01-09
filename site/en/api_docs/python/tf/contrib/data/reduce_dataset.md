page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.reduce_dataset


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/data/python/ops/get_single_element.py#L68-L87">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the result of reducing the `dataset` using `reducer`. (deprecated)

``` python
tf.contrib.data.reduce_dataset(
    dataset,
    reducer
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset#reduce"><code>tf.data.Dataset.reduce(...)</code></a>.

#### Args:


* <b>`dataset`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object.
* <b>`reducer`</b>: A <a href="../../../tf/data/experimental/Reducer"><code>tf.data.experimental.Reducer</code></a> object representing the reduce
  logic.


#### Returns:

A nested structure of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> objects, corresponding to the result
of reducing `dataset` using `reducer`.



#### Raises:


* <b>`TypeError`</b>: if `dataset` is not a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object.
