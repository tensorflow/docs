page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.mnist.load_data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/datasets/mnist.py#L27-L55">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads the MNIST dataset.

### Aliases:

* `tf.compat.v1.keras.datasets.mnist.load_data`
* `tf.compat.v2.keras.datasets.mnist.load_data`


``` python
tf.keras.datasets.mnist.load_data(path='mnist.npz')
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Keras custom callbacks](https://www.tensorflow.org/guide/keras/custom_callback)
* [Save and serialize models with Keras](https://www.tensorflow.org/guide/keras/save_and_serialize)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)




#### Arguments:


* <b>`path`</b>: path where to cache the dataset locally
    (relative to ~/.keras/datasets).


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.



#### License:

Yann LeCun and Corinna Cortes hold the copyright of MNIST dataset,
which is a derivative work from original NIST datasets.
MNIST dataset is made available under the terms of the
[Creative Commons Attribution-Share Alike 3.0 license.](
https://creativecommons.org/licenses/by-sa/3.0/)
