

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.datasets.cifar100.load_data

### `tf.contrib.keras.datasets.cifar100.load_data`

``` python
load_data(label_mode='fine')
```



Defined in [`tensorflow/contrib/keras/python/keras/datasets/cifar100.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/datasets/cifar100.py).

Loads CIFAR100 dataset.

#### Arguments:

    label_mode: one of "fine", "coarse".


#### Returns:

    Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.


#### Raises:

    ValueError: in case of invalid `label_mode`.