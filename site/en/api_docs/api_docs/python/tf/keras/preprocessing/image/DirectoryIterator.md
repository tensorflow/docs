

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.image.DirectoryIterator

## Class `DirectoryIterator`

Inherits From: [`Iterator`](../../../../tf/keras/preprocessing/image/Iterator)



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Iterator capable of reading images from a directory on disk.

#### Arguments:

* <b>`directory`</b>: Path to the directory to read images from.
        Each subdirectory in this directory will be
        considered to contain images from one class,
        or alternatively you could specify class subdirectories
        via the `classes` argument.
* <b>`image_data_generator`</b>: Instance of `ImageDataGenerator`
        to use for random transformations and normalization.
* <b>`target_size`</b>: tuple of integers, dimensions to resize input images to.
* <b>`color_mode`</b>: One of `"rgb"`, `"grayscale"`. Color mode to read images.
* <b>`classes`</b>: Optional list of strings, names of sudirectories
        containing images from each class (e.g. `["dogs", "cats"]`).
        It will be computed automatically if not set.
* <b>`class_mode`</b>: Mode for yielding the targets:
        `"binary"`: binary targets (if there are only two classes),
        `"categorical"`: categorical targets,
        `"sparse"`: integer targets,
        `"input"`: targets are images identical to input images (mainly
            used to work with autoencoders),
        `None`: no targets get yielded (only input images are yielded).
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
    directory,
    image_data_generator,
    target_size=(256, 256),
    color_mode='rgb',
    classes=None,
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=None,
    data_format=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    follow_links=False
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





