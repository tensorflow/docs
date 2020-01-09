page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.DirectoryIterator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L140-L227">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `DirectoryIterator`

Iterator capable of reading images from a directory on disk.

Inherits From: [`Iterator`](../../../../tf/keras/preprocessing/image/Iterator)

### Aliases:

* Class `tf.compat.v1.keras.preprocessing.image.DirectoryIterator`
* Class `tf.compat.v2.keras.preprocessing.image.DirectoryIterator`


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`directory`</b>: Path to the directory to read images from.
    Each subdirectory in this directory will be
    considered to contain images from one class,
    or alternatively you could specify class subdirectories
    via the `classes` argument.
* <b>`image_data_generator`</b>: Instance of `ImageDataGenerator`
    to use for random transformations and normalization.
* <b>`target_size`</b>: tuple of integers, dimensions to resize input images to.
* <b>`color_mode`</b>: One of `"rgb"`, `"rgba"`, `"grayscale"`.
    Color mode to read images.
* <b>`classes`</b>: Optional list of strings, names of subdirectories
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
* <b>`subset`</b>: Subset of data (`"training"` or `"validation"`) if
    validation_split is set in ImageDataGenerator.
* <b>`interpolation`</b>: Interpolation method used to resample the image if the
    target size is different from that of the loaded image.
    Supported methods are "nearest", "bilinear", and "bicubic".
    If PIL version 1.1.3 or newer is installed, "lanczos" is also
    supported. If PIL version 3.4.0 or newer is installed, "box" and
    "hamming" are also supported. By default, "nearest" is used.
* <b>`dtype`</b>: Dtype to use for generated arrays.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L187-L227">View source</a>

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
    follow_links=False,
    subset=None,
    interpolation='nearest',
    dtype=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="filepaths"><code>filepaths</code></h3>

List of absolute paths to image files


<h3 id="labels"><code>labels</code></h3>

Class labels of every observation


<h3 id="sample_weight"><code>sample_weight</code></h3>






## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(idx)
```

Gets batch at position `index`.


#### Arguments:


* <b>`index`</b>: position of the batch in the Sequence.


#### Returns:

A batch


<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```

Create a generator that iterate over the Sequence.


<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```

Number of batch in the Sequence.


#### Returns:

The number of batches in the Sequence.


<h3 id="next"><code>next</code></h3>

``` python
next()
```

For python 2.x.

# Returns
    The next batch.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end()
```

Method called at the end of every epoch.
    

<h3 id="reset"><code>reset</code></h3>

``` python
reset()
```




<h3 id="set_processing_attrs"><code>set_processing_attrs</code></h3>

``` python
set_processing_attrs(
    image_data_generator,
    target_size,
    color_mode,
    data_format,
    save_to_dir,
    save_prefix,
    save_format,
    subset,
    interpolation
)
```

Sets attributes to use later for processing files into a batch.

# Arguments
    image_data_generator: Instance of `ImageDataGenerator`
        to use for random transformations and normalization.
    target_size: tuple of integers, dimensions to resize input images to.
    color_mode: One of `"rgb"`, `"rgba"`, `"grayscale"`.
        Color mode to read images.
    data_format: String, one of `channels_first`, `channels_last`.
    save_to_dir: Optional directory where to save the pictures
        being yielded, in a viewable format. This is useful
        for visualizing the random transformations being
        applied, for debugging purposes.
    save_prefix: String prefix to use for saving sample
        images (if `save_to_dir` is set).
    save_format: Format to use for saving sample images
        (if `save_to_dir` is set).
    subset: Subset of data (`"training"` or `"validation"`) if
        validation_split is set in ImageDataGenerator.
    interpolation: Interpolation method used to resample the image if the
        target size is different from that of the loaded image.
        Supported methods are "nearest", "bilinear", and "bicubic".
        If PIL version 1.1.3 or newer is installed, "lanczos" is also
        supported. If PIL version 3.4.0 or newer is installed, "box" and
        "hamming" are also supported. By default, "nearest" is used.



## Class Members

* `allowed_class_modes` <a id="allowed_class_modes"></a>
* `white_list_formats` <a id="white_list_formats"></a>
