

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.datasets.boston_housing.load_data

``` python
load_data(
    path='boston_housing.npz',
    seed=113,
    test_split=0.2
)
```



Defined in [`tensorflow/python/keras/_impl/keras/datasets/boston_housing.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/datasets/boston_housing.py).

Loads the Boston Housing dataset.

#### Arguments:

* <b>`path`</b>: path where to cache the dataset locally
        (relative to ~/.keras/datasets).
* <b>`seed`</b>: Random seed for shuffling the data
        before computing the test split.
* <b>`test_split`</b>: fraction of the data to reserve as test set.


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.