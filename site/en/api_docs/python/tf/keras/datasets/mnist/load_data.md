page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.mnist.load_data

Loads the MNIST dataset.

### Aliases:

* `tf.compat.v1.keras.datasets.mnist.load_data`
* `tf.compat.v2.keras.datasets.mnist.load_data`
* `tf.keras.datasets.mnist.load_data`

``` python
tf.keras.datasets.mnist.load_data(path='mnist.npz')
```



Defined in [`python/keras/datasets/mnist.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/datasets/mnist.py).

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
