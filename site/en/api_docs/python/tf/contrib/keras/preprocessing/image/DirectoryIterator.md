

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.preprocessing.image.DirectoryIterator

### `class tf.contrib.keras.preprocessing.image.DirectoryIterator`



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/preprocessing/image.py).

Iterator capable of reading images from a directory on disk.

#### Arguments:

    directory: Path to the directory to read images from.
        Each subdirectory in this directory will be
        considered to contain images from one class,
        or alternatively you could specify class subdirectories
        via the `classes` argument.
    image_data_generator: Instance of `ImageDataGenerator`
        to use for random transformations and normalization.
    target_size: tuple of integers, dimensions to resize input images to.
    color_mode: One of `"rgb"`, `"grayscale"`. Color mode to read images.
    classes: Optional list of strings, names of sudirectories
        containing images from each class (e.g. `["dogs", "cats"]`).
        It will be computed automatically if not set.
    class_mode: Mode for yielding the targets:
        `"binary"`: binary targets (if there are only two classes),
        `"categorical"`: categorical targets,
        `"sparse"`: integer targets,
        `None`: no targets get yielded (only input images are yielded).
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
    save_format='jpeg',
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





