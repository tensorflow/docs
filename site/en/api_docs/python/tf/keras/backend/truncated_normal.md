page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.truncated_normal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5627-L5651">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a tensor with truncated random normal distribution of values.

### Aliases:

* `tf.compat.v1.keras.backend.truncated_normal`
* `tf.compat.v2.keras.backend.truncated_normal`


``` python
tf.keras.backend.truncated_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=None,
    seed=None
)
```



<!-- Placeholder for "Used in" -->

The generated values follow a normal distribution
with specified mean and standard deviation,
except that values whose magnitude is more than
two standard deviations from the mean are dropped and re-picked.

#### Arguments:


* <b>`shape`</b>: A tuple of integers, the shape of tensor to create.
* <b>`mean`</b>: Mean of the values.
* <b>`stddev`</b>: Standard deviation of the values.
* <b>`dtype`</b>: String, dtype of returned tensor.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A tensor.
