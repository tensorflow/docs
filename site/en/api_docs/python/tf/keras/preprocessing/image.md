description: Set of tools for real-time data augmentation on image data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.keras.preprocessing.image

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Set of tools for real-time data augmentation on image data.



## Classes

[`class DirectoryIterator`](../../../tf/keras/preprocessing/image/DirectoryIterator.md): Iterator capable of reading images from a directory on disk.

[`class ImageDataGenerator`](../../../tf/keras/preprocessing/image/ImageDataGenerator.md): Generate batches of tensor image data with real-time data augmentation.

[`class Iterator`](../../../tf/keras/preprocessing/image/Iterator.md): Base class for image data iterators.

[`class NumpyArrayIterator`](../../../tf/keras/preprocessing/image/NumpyArrayIterator.md): Iterator yielding data from a Numpy array.

## Functions

[`apply_affine_transform(...)`](../../../tf/keras/preprocessing/image/apply_affine_transform.md): Applies an affine transformation specified by the parameters given.

[`apply_brightness_shift(...)`](../../../tf/keras/preprocessing/image/apply_brightness_shift.md): Performs a brightness shift.

[`apply_channel_shift(...)`](../../../tf/keras/preprocessing/image/apply_channel_shift.md): Performs a channel shift.

[`array_to_img(...)`](../../../tf/keras/preprocessing/image/array_to_img.md): Converts a 3D Numpy array to a PIL Image instance.

[`img_to_array(...)`](../../../tf/keras/preprocessing/image/img_to_array.md): Converts a PIL Image instance to a Numpy array.

[`load_img(...)`](../../../tf/keras/preprocessing/image/load_img.md): Loads an image into PIL format.

[`random_brightness(...)`](../../../tf/keras/preprocessing/image/random_brightness.md): Performs a random brightness shift.

[`random_channel_shift(...)`](../../../tf/keras/preprocessing/image/random_channel_shift.md): Performs a random channel shift.

[`random_rotation(...)`](../../../tf/keras/preprocessing/image/random_rotation.md): Performs a random rotation of a Numpy image tensor.

[`random_shear(...)`](../../../tf/keras/preprocessing/image/random_shear.md): Performs a random spatial shear of a Numpy image tensor.

[`random_shift(...)`](../../../tf/keras/preprocessing/image/random_shift.md): Performs a random spatial shift of a Numpy image tensor.

[`random_zoom(...)`](../../../tf/keras/preprocessing/image/random_zoom.md): Performs a random spatial zoom of a Numpy image tensor.

[`save_img(...)`](../../../tf/keras/preprocessing/image/save_img.md): Saves an image stored as a Numpy array to a path or file object.

[`smart_resize(...)`](../../../tf/keras/preprocessing/image/smart_resize.md): Resize images to a target size without aspect ratio distortion.

