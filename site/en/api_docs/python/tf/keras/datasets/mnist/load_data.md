page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.mnist.load_data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/datasets/mnist/load_data">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/datasets/mnist.py#L27-L55">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads the MNIST dataset.

### Aliases:

* <a href="/api_docs/python/tf/keras/datasets/mnist/load_data"><code>tf.compat.v1.keras.datasets.mnist.load_data</code></a>
* <a href="/api_docs/python/tf/keras/datasets/mnist/load_data"><code>tf.compat.v2.keras.datasets.mnist.load_data</code></a>


``` python
tf.keras.datasets.mnist.load_data(path='mnist.npz')
```



<!-- Placeholder for "Used in" -->


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
