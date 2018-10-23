

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.utils.HDF5Matrix

### `class tf.contrib.keras.utils.HDF5Matrix`



Defined in [`tensorflow/contrib/keras/python/keras/utils/io_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/utils/io_utils.py).

Representation of HDF5 dataset to be used instead of a Numpy array.

Example:

```python
    x_data = HDF5Matrix('input/file.hdf5', 'data')
    model.predict(x_data)
```

Providing `start` and `end` allows use of a slice of the dataset.

Optionally, a normalizer function (or lambda) can be given. This will
be called on every slice of data retrieved.

#### Arguments:

    datapath: string, path to a HDF5 file
    dataset: string, name of the HDF5 dataset in the file specified
        in datapath
    start: int, start of desired slice of the specified dataset
    end: int, end of desired slice of the specified dataset
    normalizer: function to be called on data when retrieved


#### Returns:

    An array-like HDF5 dataset.

## Properties

<h3 id="shape"><code>shape</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    datapath,
    dataset,
    start=0,
    end=None,
    normalizer=None
)
```



<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(key)
```



<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```





## Class Members

<h3 id="refs"><code>refs</code></h3>

