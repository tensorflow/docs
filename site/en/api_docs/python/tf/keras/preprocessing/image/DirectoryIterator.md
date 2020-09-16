description: Iterator capable of reading images from a directory on disk.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.DirectoryIterator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="next"/>
<meta itemprop="property" content="on_epoch_end"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="set_processing_attrs"/>
<meta itemprop="property" content="allowed_class_modes"/>
<meta itemprop="property" content="white_list_formats"/>
</div>

# tf.keras.preprocessing.image.DirectoryIterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/preprocessing/image.py#L167-L254">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Iterator capable of reading images from a directory on disk.

Inherits From: [`Iterator`](../../../../tf/keras/preprocessing/image/Iterator.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.DirectoryIterator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.DirectoryIterator(
    directory, image_data_generator, target_size=(256, 256), color_mode='rgb',
    classes=None, class_mode='categorical', batch_size=32, shuffle=(True),
    seed=None, data_format=None, save_to_dir=None, save_prefix='',
    save_format='png', follow_links=(False), subset=None, interpolation='nearest',
    dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`directory`
</td>
<td>
Path to the directory to read images from.
Each subdirectory in this directory will be
considered to contain images from one class,
or alternatively you could specify class subdirectories
via the `classes` argument.
</td>
</tr><tr>
<td>
`image_data_generator`
</td>
<td>
Instance of `ImageDataGenerator`
to use for random transformations and normalization.
</td>
</tr><tr>
<td>
`target_size`
</td>
<td>
tuple of integers, dimensions to resize input images to.
</td>
</tr><tr>
<td>
`color_mode`
</td>
<td>
One of `"rgb"`, `"rgba"`, `"grayscale"`.
Color mode to read images.
</td>
</tr><tr>
<td>
`classes`
</td>
<td>
Optional list of strings, names of subdirectories
containing images from each class (e.g. `["dogs", "cats"]`).
It will be computed automatically if not set.
</td>
</tr><tr>
<td>
`class_mode`
</td>
<td>
Mode for yielding the targets:
`"binary"`: binary targets (if there are only two classes),
`"categorical"`: categorical targets,
`"sparse"`: integer targets,
`"input"`: targets are images identical to input images (mainly
used to work with autoencoders),
`None`: no targets get yielded (only input images are yielded).
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Integer, size of a batch.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Boolean, whether to shuffle the data between epochs.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Random seed for data shuffling.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
String, one of `channels_first`, `channels_last`.
</td>
</tr><tr>
<td>
`save_to_dir`
</td>
<td>
Optional directory where to save the pictures
being yielded, in a viewable format. This is useful
for visualizing the random transformations being
applied, for debugging purposes.
</td>
</tr><tr>
<td>
`save_prefix`
</td>
<td>
String prefix to use for saving sample
images (if `save_to_dir` is set).
</td>
</tr><tr>
<td>
`save_format`
</td>
<td>
Format to use for saving sample images
(if `save_to_dir` is set).
</td>
</tr><tr>
<td>
`subset`
</td>
<td>
Subset of data (`"training"` or `"validation"`) if
validation_split is set in ImageDataGenerator.
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
Interpolation method used to resample the image if the
target size is different from that of the loaded image.
Supported methods are "nearest", "bilinear", and "bicubic".
If PIL version 1.1.3 or newer is installed, "lanczos" is also
supported. If PIL version 3.4.0 or newer is installed, "box" and
"hamming" are also supported. By default, "nearest" is used.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Dtype to use for generated arrays.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`filepaths`
</td>
<td>
List of absolute paths to image files
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
Class labels of every observation
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="next"><code>next</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>next()
</code></pre>

For python 2.x.

# Returns
    The next batch.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_epoch_end()
</code></pre>




<h3 id="reset"><code>reset</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>




<h3 id="set_processing_attrs"><code>set_processing_attrs</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_processing_attrs(
    image_data_generator, target_size, color_mode, data_format, save_to_dir,
    save_prefix, save_format, subset, interpolation
)
</code></pre>

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

<h3 id="__getitem__"><code>__getitem__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    idx
)
</code></pre>




<h3 id="__iter__"><code>__iter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>






## Class Variables

* `allowed_class_modes` <a id="allowed_class_modes"></a>
* `white_list_formats` <a id="white_list_formats"></a>
