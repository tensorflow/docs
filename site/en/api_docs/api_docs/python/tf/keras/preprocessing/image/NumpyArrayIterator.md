

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.image.NumpyArrayIterator

## Class `NumpyArrayIterator`

Inherits From: [`Iterator`](../../../../tf/keras/preprocessing/image/Iterator)



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Iterator yielding data from a Numpy array.

#### Arguments:

* <b>`x`</b>: Numpy array of input data.
* <b>`y`</b>: Numpy array of targets data.
* <b>`image_data_generator`</b>: Instance of `ImageDataGenerator`
        to use for random transformations and normalization.
* <b>`batch_size`</b>: Integer, size of a batch.
* <b>`shuffle`</b>: Boolean, whether to shuffle the data between epochs.
* <b>`seed`</b>: Random seed for data shuffling.
* <b>`data_format`</b>: String, one of `channels_first`, `channels_last`.
* <b>`save_to_dir`</b>: Optional directory where to save the pictures
        being yielded, in a viewable format. This is useful
        for visualizing the random transformations being
        applied, for debugging purposes.
* <b>`save_prefix`</b>: String prefix to use for saving sample
        images (if `save_to_dir` is set).
* <b>`save_format`</b>: Format to use for saving sample images
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
    save_format='png'
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





