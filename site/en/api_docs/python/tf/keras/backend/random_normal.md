page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.random_normal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5554-L5574">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a tensor with normal distribution of values.

### Aliases:

* `tf.compat.v1.keras.backend.random_normal`
* `tf.compat.v2.keras.backend.random_normal`


``` python
tf.keras.backend.random_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=None,
    seed=None
)
```



### Used in the guide:

* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)




#### Arguments:


* <b>`shape`</b>: A tuple of integers, the shape of tensor to create.
* <b>`mean`</b>: A float, mean of the normal distribution to draw samples.
* <b>`stddev`</b>: A float, standard deviation of the normal distribution
    to draw samples.
* <b>`dtype`</b>: String, dtype of returned tensor.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A tensor.
