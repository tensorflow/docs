page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.in_top_k


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L4673-L4687">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns whether the `targets` are in the top `k` `predictions`.

### Aliases:

* `tf.compat.v1.keras.backend.in_top_k`
* `tf.compat.v2.keras.backend.in_top_k`


``` python
tf.keras.backend.in_top_k(
    predictions,
    targets,
    k
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`predictions`</b>: A tensor of shape `(batch_size, classes)` and type `float32`.
* <b>`targets`</b>: A 1D tensor of length `batch_size` and type `int32` or `int64`.
* <b>`k`</b>: An `int`, number of top elements to consider.


#### Returns:

A 1D tensor of length `batch_size` and type `bool`.
`output[i]` is `True` if `predictions[i, targets[i]]` is within top-`k`
values of `predictions[i]`.
