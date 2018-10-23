

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.preprocessing.image.Iterator

### `class tf.contrib.keras.preprocessing.image.Iterator`



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/preprocessing/image.py).

Abstract base class for image data iterators.

#### Arguments:

    n: Integer, total number of samples in the dataset to loop over.
    batch_size: Integer, size of a batch.
    shuffle: Boolean, whether to shuffle the data between epochs.
    seed: Random seeding for data shuffling.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    n,
    batch_size,
    shuffle,
    seed
)
```



<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```



<h3 id="__next__"><code>__next__</code></h3>

``` python
__next__(
    *args,
    **kwargs
)
```



<h3 id="reset"><code>reset</code></h3>

``` python
reset()
```





