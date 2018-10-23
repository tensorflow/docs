

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.datasets.cifar100.load_data

``` python
load_data(label_mode='fine')
```



Defined in [`tensorflow/python/keras/_impl/keras/datasets/cifar100.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/datasets/cifar100.py).

Loads CIFAR100 dataset.

#### Arguments:

* <b>`label_mode`</b>: one of "fine", "coarse".


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.


#### Raises:

* <b>`ValueError`</b>: in case of invalid `label_mode`.