

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.preprocessing.image.NumpyArrayIterator

### `class tf.contrib.keras.preprocessing.image.NumpyArrayIterator`



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/preprocessing/image.py).

Iterator yielding data from a Numpy array.

#### Arguments:

    x: Numpy array of input data.
    y: Numpy array of targets data.
    image_data_generator: Instance of `ImageDataGenerator`
        to use for random transformations and normalization.
    batch_size: Integer, size of a batch.
    shuffle: Boolean, whether to shuffle the data between epochs.
    seed: Random seed for data shuffling.
    data_format: String, one of `channels_first`, `channels_last`.
    save_to_dir: Optional directory where to save the pictures
        being yielded, in a viewable format. This is useful
        for visualizing the random transformations being
        applied, for debugging purposes.
    save_prefix: String prefix to use for saving sample
        images (if `save_to_dir` is set).
    save_format: Format to use for saving sample images
        (if `save_to_dir` is set).

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    x,
    y,
    image_data_generator,
    batch_size=32,
    shuffle=False,
    seed=None,
    data_format=None,
    save_to_dir=None,
    save_prefix='',
    save_format='jpeg'
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



<h3 id="next"><code>next</code></h3>

``` python
next()
```

For python 2.x.

#### Returns:

    The next batch.

<h3 id="reset"><code>reset</code></h3>

``` python
reset()
```





