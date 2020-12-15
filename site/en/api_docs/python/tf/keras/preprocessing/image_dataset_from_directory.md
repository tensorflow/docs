description: Generates a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> from image files in a directory.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image_dataset_from_directory" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.image_dataset_from_directory

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/preprocessing/image_dataset.py#L34-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> from image files in a directory.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image_dataset_from_directory(
    directory, labels='inferred', label_mode='int', class_names=None,
    color_mode='rgb', batch_size=32, image_size=(256, 256), shuffle=(True),
    seed=None, validation_split=None, subset=None, interpolation='bilinear',
    follow_links=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

If your directory structure is:

```
main_directory/
...class_a/
......a_image_1.jpg
......a_image_2.jpg
...class_b/
......b_image_1.jpg
......b_image_2.jpg
```

Then calling `image_dataset_from_directory(main_directory, labels='inferred')`
will return a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> that yields batches of images from
the subdirectories `class_a` and `class_b`, together with labels
0 and 1 (0 corresponding to `class_a` and 1 corresponding to `class_b`).

Supported image formats: jpeg, png, bmp, gif.
Animated gifs are truncated to the first frame.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`directory`
</td>
<td>
Directory where the data is located.
If `labels` is "inferred", it should contain
subdirectories, each containing images for a class.
Otherwise, the directory structure is ignored.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
Either "inferred"
(labels are generated from the directory structure),
or a list/tuple of integer labels of the same size as the number of
image files found in the directory. Labels should be sorted according
to the alphanumeric order of the image file paths
(obtained via `os.walk(directory)` in Python).
</td>
</tr><tr>
<td>
`label_mode`
</td>
<td>
- 'int': means that the labels are encoded as integers
(e.g. for `sparse_categorical_crossentropy` loss).
- 'categorical' means that the labels are
encoded as a categorical vector
(e.g. for `categorical_crossentropy` loss).
- 'binary' means that the labels (there can be only 2)
are encoded as `float32` scalars with values 0 or 1
(e.g. for `binary_crossentropy`).
- None (no labels).
</td>
</tr><tr>
<td>
`class_names`
</td>
<td>
Only valid if "labels" is "inferred". This is the explict
list of class names (must match names of subdirectories). Used
to control the order of the classes
(otherwise alphanumerical order is used).
</td>
</tr><tr>
<td>
`color_mode`
</td>
<td>
One of "grayscale", "rgb", "rgba". Default: "rgb".
Whether the images will be converted to
have 1, 3, or 4 channels.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Size of the batches of data. Default: 32.
</td>
</tr><tr>
<td>
`image_size`
</td>
<td>
Size to resize images to after they are read from disk.
Defaults to `(256, 256)`.
Since the pipeline processes batches of images that must all have
the same size, this must be provided.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Whether to shuffle the data. Default: True.
If set to False, sorts the data in alphanumeric order.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Optional random seed for shuffling and transformations.
</td>
</tr><tr>
<td>
`validation_split`
</td>
<td>
Optional float between 0 and 1,
fraction of data to reserve for validation.
</td>
</tr><tr>
<td>
`subset`
</td>
<td>
One of "training" or "validation".
Only used if `validation_split` is set.
</td>
</tr><tr>
<td>
`interpolation`
</td>
<td>
String, the interpolation method used when resizing images.
Defaults to `bilinear`. Supports `bilinear`, `nearest`, `bicubic`,
`area`, `lanczos3`, `lanczos5`, `gaussian`, `mitchellcubic`.
</td>
</tr><tr>
<td>
`follow_links`
</td>
<td>
Whether to visits subdirectories pointed to by symlinks.
Defaults to False.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object.
- If `label_mode` is None, it yields `float32` tensors of shape
`(batch_size, image_size[0], image_size[1], num_channels)`,
encoding images (see below for rules regarding `num_channels`).
- Otherwise, it yields a tuple `(images, labels)`, where `images`
has shape `(batch_size, image_size[0], image_size[1], num_channels)`,
and `labels` follows the format described below.
</td>
</tr>

</table>


Rules regarding labels format:
  - if `label_mode` is `int`, the labels are an `int32` tensor of shape
    `(batch_size,)`.
  - if `label_mode` is `binary`, the labels are a `float32` tensor of
    1s and 0s of shape `(batch_size, 1)`.
  - if `label_mode` is `categorial`, the labels are a `float32` tensor
    of shape `(batch_size, num_classes)`, representing a one-hot
    encoding of the class index.

Rules regarding number of channels in the yielded images:
  - if `color_mode` is `grayscale`,
    there's 1 channel in the image tensors.
  - if `color_mode` is `rgb`,
    there are 3 channel in the image tensors.
  - if `color_mode` is `rgba`,
    there are 4 channel in the image tensors.