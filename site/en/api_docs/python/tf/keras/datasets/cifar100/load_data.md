page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.cifar100.load_data

``` python
tf.keras.datasets.cifar100.load_data(label_mode='fine')
```



Defined in [`tensorflow/python/keras/datasets/cifar100.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/datasets/cifar100.py).

Loads CIFAR100 dataset.

#### Arguments:

* <b>`label_mode`</b>: one of "fine", "coarse".


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.


#### Raises:

* <b>`ValueError`</b>: in case of invalid `label_mode`.