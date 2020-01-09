page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.normal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/random_ops.py#L42-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs random values from a normal distribution.

### Aliases:

* `tf.compat.v1.random.normal`
* `tf.compat.v1.random_normal`
* `tf.compat.v2.random.normal`


``` python
tf.random.normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)

### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)
* [Custom training: basics](https://www.tensorflow.org/tutorials/customization/custom_training)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)




#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output tensor.
* <b>`mean`</b>: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
  distribution.
* <b>`stddev`</b>: A 0-D Tensor or Python value of type `dtype`. The standard deviation
  of the normal distribution.
* <b>`dtype`</b>: The type of the output.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
  See
  <a href="../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random normal values.
