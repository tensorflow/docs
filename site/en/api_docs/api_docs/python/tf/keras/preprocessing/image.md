

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.keras.preprocessing.image



Defined in [`tensorflow/keras/preprocessing/image/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/keras/preprocessing/image/__init__.py).

Fairly basic set of tools for real-time data augmentation on image data.

Can easily be extended to include new transformations,
new preprocessing methods, etc...

## Classes

[`class DirectoryIterator`](../../../tf/keras/preprocessing/image/DirectoryIterator): Iterator capable of reading images from a directory on disk.

[`class ImageDataGenerator`](../../../tf/keras/preprocessing/image/ImageDataGenerator): Generates batches of tensor image data with real-time data augmentation.

[`class Iterator`](../../../tf/keras/preprocessing/image/Iterator): Base class for image data iterators.

[`class NumpyArrayIterator`](../../../tf/keras/preprocessing/image/NumpyArrayIterator): Iterator yielding data from a Numpy array.

## Functions

[`apply_transform(...)`](../../../tf/keras/preprocessing/image/apply_transform): Apply the image transformation specified by a matrix.

[`array_to_img(...)`](../../../tf/keras/preprocessing/image/array_to_img): Converts a 3D Numpy array to a PIL Image instance.

[`flip_axis(...)`](../../../tf/keras/preprocessing/image/flip_axis)

[`img_to_array(...)`](../../../tf/keras/preprocessing/image/img_to_array): Converts a PIL Image instance to a Numpy array.

[`load_img(...)`](../../../tf/keras/preprocessing/image/load_img): Loads an image into PIL format.

[`random_brightness(...)`](../../../tf/keras/preprocessing/image/random_brightness): Performs a random adjustment of brightness of a Numpy image tensor.

[`random_channel_shift(...)`](../../../tf/keras/preprocessing/image/random_channel_shift): Perform a random channel shift.

[`random_rotation(...)`](../../../tf/keras/preprocessing/image/random_rotation): Performs a random rotation of a Numpy image tensor.

[`random_shear(...)`](../../../tf/keras/preprocessing/image/random_shear): Performs a random spatial shear of a Numpy image tensor.

[`random_shift(...)`](../../../tf/keras/preprocessing/image/random_shift): Performs a random spatial shift of a Numpy image tensor.

[`random_zoom(...)`](../../../tf/keras/preprocessing/image/random_zoom): Performs a random spatial zoom of a Numpy image tensor.

