page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.keras.preprocessing.image


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/v2/keras/preprocessing/image">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Set of tools for real-time data augmentation on image data.

<!-- Placeholder for "Used in" -->


## Classes

[`class DirectoryIterator`](../../../../../tf/keras/preprocessing/image/DirectoryIterator): Iterator capable of reading images from a directory on disk.

[`class ImageDataGenerator`](../../../../../tf/keras/preprocessing/image/ImageDataGenerator): Generate batches of tensor image data with real-time data augmentation.

[`class Iterator`](../../../../../tf/keras/preprocessing/image/Iterator): Base class for image data iterators.

[`class NumpyArrayIterator`](../../../../../tf/keras/preprocessing/image/NumpyArrayIterator): Iterator yielding data from a Numpy array.

## Functions

[`apply_affine_transform(...)`](../../../../../tf/keras/preprocessing/image/apply_affine_transform): Applies an affine transformation specified by the parameters given.

[`apply_brightness_shift(...)`](../../../../../tf/keras/preprocessing/image/apply_brightness_shift): Performs a brightness shift.

[`apply_channel_shift(...)`](../../../../../tf/keras/preprocessing/image/apply_channel_shift): Performs a channel shift.

[`array_to_img(...)`](../../../../../tf/keras/preprocessing/image/array_to_img): Converts a 3D Numpy array to a PIL Image instance.

[`img_to_array(...)`](../../../../../tf/keras/preprocessing/image/img_to_array): Converts a PIL Image instance to a Numpy array.

[`load_img(...)`](../../../../../tf/keras/preprocessing/image/load_img): Loads an image into PIL format.

[`random_brightness(...)`](../../../../../tf/keras/preprocessing/image/random_brightness): Performs a random brightness shift.

[`random_channel_shift(...)`](../../../../../tf/keras/preprocessing/image/random_channel_shift): Performs a random channel shift.

[`random_rotation(...)`](../../../../../tf/keras/preprocessing/image/random_rotation): Performs a random rotation of a Numpy image tensor.

[`random_shear(...)`](../../../../../tf/keras/preprocessing/image/random_shear): Performs a random spatial shear of a Numpy image tensor.

[`random_shift(...)`](../../../../../tf/keras/preprocessing/image/random_shift): Performs a random spatial shift of a Numpy image tensor.

[`random_zoom(...)`](../../../../../tf/keras/preprocessing/image/random_zoom): Performs a random spatial zoom of a Numpy image tensor.

[`save_img(...)`](../../../../../tf/keras/preprocessing/image/save_img): Saves an image stored as a Numpy array to a path or file object.
