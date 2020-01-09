page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.batch_gather


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L3994-L4007">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gather slices from params according to indices with leading batch dims. (deprecated)

``` python
tf.compat.v1.batch_gather(
    params,
    indices,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2017-10-25.
Instructions for updating:
`tf.batch_gather` is deprecated, please use <a href="../../../tf/gather"><code>tf.gather</code></a> with `batch_dims=-1` instead.
