page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.boston_housing.load_data

Loads the Boston Housing dataset.

### Aliases:

* `tf.compat.v1.keras.datasets.boston_housing.load_data`
* `tf.compat.v2.keras.datasets.boston_housing.load_data`
* `tf.keras.datasets.boston_housing.load_data`

``` python
tf.keras.datasets.boston_housing.load_data(
    path='boston_housing.npz',
    test_split=0.2,
    seed=113
)
```



Defined in [`python/keras/datasets/boston_housing.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/datasets/boston_housing.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`path`</b>: path where to cache the dataset locally
    (relative to ~/.keras/datasets).
* <b>`test_split`</b>: fraction of the data to reserve as test set.
* <b>`seed`</b>: Random seed for shuffling the data
    before computing the test split.


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
