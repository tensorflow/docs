page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.prefetch_to_device


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/prefetching_ops.py#L36-L56">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A transformation that prefetches dataset values to the given `device`.

### Aliases:

* `tf.compat.v1.data.experimental.prefetch_to_device`
* `tf.compat.v2.data.experimental.prefetch_to_device`


``` python
tf.data.experimental.prefetch_to_device(
    device,
    buffer_size=None
)
```



<!-- Placeholder for "Used in" -->

NOTE: Although the transformation creates a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>, the
transformation must be the final `Dataset` in the input pipeline.

#### Args:


* <b>`device`</b>: A string. The name of a device to which elements will be prefetched.
* <b>`buffer_size`</b>: (Optional.) The number of elements to buffer on `device`.
  Defaults to an automatically chosen value.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
