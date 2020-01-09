page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.ImageDataGenerator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L295-L519">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ImageDataGenerator`

Generate batches of tensor image data with real-time data augmentation.



### Aliases:

* Class `tf.compat.v1.keras.preprocessing.image.ImageDataGenerator`
* Class `tf.compat.v2.keras.preprocessing.image.ImageDataGenerator`


### Used in the guide:

* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Basic classification: Predict an image of clothing](https://www.tensorflow.org/tutorials/keras/classification)
* [Image classification](https://www.tensorflow.org/tutorials/images/classification)
* [Load images](https://www.tensorflow.org/tutorials/load_data/images)
* [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)



 The data will be looped over (in batches).

#### Arguments:


* <b>`featurewise_center`</b>: Boolean.
    Set input mean to 0 over the dataset, feature-wise.
* <b>`samplewise_center`</b>: Boolean. Set each sample mean to 0.
* <b>`featurewise_std_normalization`</b>: Boolean.
    Divide inputs by std of the dataset, feature-wise.
* <b>`samplewise_std_normalization`</b>: Boolean. Divide each input by its std.
* <b>`zca_epsilon`</b>: epsilon for ZCA whitening. Default is 1e-6.
* <b>`zca_whitening`</b>: Boolean. Apply ZCA whitening.
* <b>`rotation_range`</b>: Int. Degree range for random rotations.
* <b>`width_shift_range`</b>: Float, 1-D array-like or int
    - float: fraction of total width, if < 1, or pixels if >= 1.
    - 1-D array-like: random elements from the array.
    - int: integer number of pixels from interval
        `(-width_shift_range, +width_shift_range)`
    - With `width_shift_range=2` possible values
        are integers `[-1, 0, +1]`,
        same as with `width_shift_range=[-1, 0, +1]`,
        while with `width_shift_range=1.0` possible values are floats
        in the interval [-1.0, +1.0).
* <b>`height_shift_range`</b>: Float, 1-D array-like or int
    - float: fraction of total height, if < 1, or pixels if >= 1.
    - 1-D array-like: random elements from the array.
    - int: integer number of pixels from interval
        `(-height_shift_range, +height_shift_range)`
    - With `height_shift_range=2` possible values
        are integers `[-1, 0, +1]`,
        same as with `height_shift_range=[-1, 0, +1]`,
        while with `height_shift_range=1.0` possible values are floats
        in the interval [-1.0, +1.0).
* <b>`brightness_range`</b>: Tuple or list of two floats. Range for picking
    a brightness shift value from.
* <b>`shear_range`</b>: Float. Shear Intensity
    (Shear angle in counter-clockwise direction in degrees)
* <b>`zoom_range`</b>: Float or [lower, upper]. Range for random zoom.
    If a float, `[lower, upper] = [1-zoom_range, 1+zoom_range]`.
* <b>`channel_shift_range`</b>: Float. Range for random channel shifts.
* <b>`fill_mode`</b>: One of {"constant", "nearest", "reflect" or "wrap"}.
    Default is 'nearest'.
    Points outside the boundaries of the input are filled
    according to the given mode:
    - 'constant': kkkkkkkk|abcd|kkkkkkkk (cval=k)
    - 'nearest':  aaaaaaaa|abcd|dddddddd
    - 'reflect':  abcddcba|abcd|dcbaabcd
    - 'wrap':  abcdabcd|abcd|abcdabcd
* <b>`cval`</b>: Float or Int.
    Value used for points outside the boundaries
    when `fill_mode = "constant"`.
* <b>`horizontal_flip`</b>: Boolean. Randomly flip inputs horizontally.
* <b>`vertical_flip`</b>: Boolean. Randomly flip inputs vertically.
* <b>`rescale`</b>: rescaling factor. Defaults to None.
    If None or 0, no rescaling is applied,
    otherwise we multiply the data by the value provided
    (after applying all other transformations).
* <b>`preprocessing_function`</b>: function that will be implied on each input.
    The function will run after the image is resized and augmented.
    The function should take one argument:
    one image (Numpy tensor with rank 3),
    and should output a Numpy tensor with the same shape.
* <b>`data_format`</b>: Image data format,
    either "channels_first" or "channels_last".
    "channels_last" mode means that the images should have shape
    `(samples, height, width, channels)`,
    "channels_first" mode means that the images should have shape
    `(samples, channels, height, width)`.
    It defaults to the `image_data_format` value found in your
    Keras config file at `~/.keras/keras.json`.
    If you never set it, then it will be "channels_last".
* <b>`validation_split`</b>: Float. Fraction of images reserved for validation
    (strictly between 0 and 1).
* <b>`dtype`</b>: Dtype to use for the generated arrays.


#### Examples:



Example of using `.flow(x, y)`:

```python
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)
datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)
# compute quantities required for featurewise normalization
# (std, mean, and principal components if ZCA whitening is applied)
datagen.fit(x_train)
# fits the model on batches with real-time data augmentation:
model.fit_generator(datagen.flow(x_train, y_train, batch_size=32),
                    steps_per_epoch=len(x_train) / 32, epochs=epochs)
# here's a more "manual" example
for e in range(epochs):
    print('Epoch', e)
    batches = 0
    for x_batch, y_batch in datagen.flow(x_train, y_train, batch_size=32):
        model.fit(x_batch, y_batch)
        batches += 1
        if batches >= len(x_train) / 32:
            # we need to break the loop by hand because
            # the generator loops indefinitely
            break
```

Example of using `.flow_from_directory(directory)`:

```python
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        'data/train',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')
validation_generator = test_datagen.flow_from_directory(
        'data/validation',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')
model.fit_generator(
        train_generator,
        steps_per_epoch=2000,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=800)
```

Example of transforming images and masks together.

```python
# we create two instances with the same arguments
data_gen_args = dict(featurewise_center=True,
                     featurewise_std_normalization=True,
                     rotation_range=90,
                     width_shift_range=0.1,
                     height_shift_range=0.1,
                     zoom_range=0.2)
image_datagen = ImageDataGenerator(**data_gen_args)
mask_datagen = ImageDataGenerator(**data_gen_args)
# Provide the same seed and keyword arguments to the fit and flow methods
seed = 1
image_datagen.fit(images, augment=True, seed=seed)
mask_datagen.fit(masks, augment=True, seed=seed)
image_generator = image_datagen.flow_from_directory(
    'data/images',
    class_mode=None,
    seed=seed)
mask_generator = mask_datagen.flow_from_directory(
    'data/masks',
    class_mode=None,
    seed=seed)
# combine generators into one which yields image and masks
train_generator = zip(image_generator, mask_generator)
model.fit_generator(
    train_generator,
    steps_per_epoch=2000,
    epochs=50)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L466-L519">View source</a>

``` python
__init__(
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-06,
    rotation_range=0,
    width_shift_range=0.0,
    height_shift_range=0.0,
    brightness_range=None,
    shear_range=0.0,
    zoom_range=0.0,
    channel_shift_range=0.0,
    fill_mode='nearest',
    cval=0.0,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=None,
    validation_split=0.0,
    dtype=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="apply_transform"><code>apply_transform</code></h3>

``` python
apply_transform(
    x,
    transform_parameters
)
```

Applies a transformation to an image according to given parameters.

# Arguments
    x: 3D tensor, single image.
    transform_parameters: Dictionary with string - parameter pairs
        describing the transformation.
        Currently, the following parameters
        from the dictionary are used:
        - `'theta'`: Float. Rotation angle in degrees.
        - `'tx'`: Float. Shift in the x direction.
        - `'ty'`: Float. Shift in the y direction.
        - `'shear'`: Float. Shear angle in degrees.
        - `'zx'`: Float. Zoom in the x direction.
        - `'zy'`: Float. Zoom in the y direction.
        - `'flip_horizontal'`: Boolean. Horizontal flip.
        - `'flip_vertical'`: Boolean. Vertical flip.
        - `'channel_shift_intencity'`: Float. Channel shift intensity.
        - `'brightness'`: Float. Brightness shift intensity.

# Returns
    A transformed version of the input (same shape).

<h3 id="fit"><code>fit</code></h3>

``` python
fit(
    x,
    augment=False,
    rounds=1,
    seed=None
)
```

Fits the data generator to some sample data.

This computes the internal data stats related to the
data-dependent transformations, based on an array of sample data.

Only required if `featurewise_center` or
`featurewise_std_normalization` or `zca_whitening` are set to True.

# Arguments
    x: Sample data. Should have rank 4.
     In case of grayscale data,
     the channels axis should have value 1, in case
     of RGB data, it should have value 3, and in case
     of RGBA data, it should have value 4.
    augment: Boolean (default: False).
        Whether to fit on randomly augmented samples.
    rounds: Int (default: 1).
        If using data augmentation (`augment=True`),
        this is how many augmentation passes over the data to use.
    seed: Int (default: None). Random seed.

<h3 id="flow"><code>flow</code></h3>

``` python
flow(
    x,
    y=None,
    batch_size=32,
    shuffle=True,
    sample_weight=None,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    subset=None
)
```

Takes data & label arrays, generates batches of augmented data.

# Arguments
    x: Input data. Numpy array of rank 4 or a tuple.
        If tuple, the first element
        should contain the images and the second element
        another numpy array or a list of numpy arrays
        that gets passed to the output
        without any modifications.
        Can be used to feed the model miscellaneous data
        along with the images.
        In case of grayscale data, the channels axis of the image array
        should have value 1, in case
        of RGB data, it should have value 3, and in case
        of RGBA data, it should have value 4.
    y: Labels.
    batch_size: Int (default: 32).
    shuffle: Boolean (default: True).
    sample_weight: Sample weights.
    seed: Int (default: None).
    save_to_dir: None or str (default: None).
        This allows you to optionally specify a directory
        to which to save the augmented pictures being generated
        (useful for visualizing what you are doing).
    save_prefix: Str (default: `''`).
        Prefix to use for filenames of saved pictures
        (only relevant if `save_to_dir` is set).
    save_format: one of "png", "jpeg"
        (only relevant if `save_to_dir` is set). Default: "png".
    subset: Subset of data (`"training"` or `"validation"`) if
        `validation_split` is set in `ImageDataGenerator`.

# Returns
    An `Iterator` yielding tuples of `(x, y)`
        where `x` is a numpy array of image data
        (in the case of a single image input) or a list
        of numpy arrays (in the case with
        additional inputs) and `y` is a numpy array
        of corresponding labels. If 'sample_weight' is not None,
        the yielded tuples are of the form `(x, y, sample_weight)`.
        If `y` is None, only the numpy array `x` is returned.

<h3 id="flow_from_dataframe"><code>flow_from_dataframe</code></h3>

``` python
flow_from_dataframe(
    dataframe,
    directory=None,
    x_col='filename',
    y_col='class',
    weight_col=None,
    target_size=(256, 256),
    color_mode='rgb',
    classes=None,
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    subset=None,
    interpolation='nearest',
    validate_filenames=True,
    **kwargs
)
```

Takes the dataframe and the path to a directory
 and generates batches of augmented/normalized data.

**A simple tutorial can be found **[here](
                            http://bit.ly/keras_flow_from_dataframe).

# Arguments
    dataframe: Pandas dataframe containing the filepaths relative to
        `directory` (or absolute paths if `directory` is None) of the
        images in a string column. It should include other column/s
        depending on the `class_mode`:
        - if `class_mode` is `"categorical"` (default value) it must
            include the `y_col` column with the class/es of each image.
            Values in column can be string/list/tuple if a single class
            or list/tuple if multiple classes.
        - if `class_mode` is `"binary"` or `"sparse"` it must include
            the given `y_col` column with class values as strings.
        - if `class_mode` is `"raw"` or `"multi_output"` it should contain
        the columns specified in `y_col`.
        - if `class_mode` is `"input"` or `None` no extra column is needed.
    directory: string, path to the directory to read images from. If `None`,
        data in `x_col` column should be absolute paths.
    x_col: string, column in `dataframe` that contains the filenames (or
        absolute paths if `directory` is `None`).
    y_col: string or list, column/s in `dataframe` that has the target data.
    weight_col: string, column in `dataframe` that contains the sample
        weights. Default: `None`.
    target_size: tuple of integers `(height, width)`, default: `(256, 256)`.
        The dimensions to which all images found will be resized.
    color_mode: one of "grayscale", "rgb", "rgba". Default: "rgb".
        Whether the images will be converted to have 1 or 3 color channels.
    classes: optional list of classes (e.g. `['dogs', 'cats']`).
        Default: None. If not provided, the list of classes will be
        automatically inferred from the `y_col`,
        which will map to the label indices, will be alphanumeric).
        The dictionary containing the mapping from class names to class
        indices can be obtained via the attribute `class_indices`.
    class_mode: one of "binary", "categorical", "input", "multi_output",
        "raw", sparse" or None. Default: "categorical".
        Mode for yielding the targets:
        - `"binary"`: 1D numpy array of binary labels,
        - `"categorical"`: 2D numpy array of one-hot encoded labels.
            Supports multi-label output.
        - `"input"`: images identical to input images (mainly used to
            work with autoencoders),
        - `"multi_output"`: list with the values of the different columns,
        - `"raw"`: numpy array of values in `y_col` column(s),
        - `"sparse"`: 1D numpy array of integer labels,
        - `None`, no targets are returned (the generator will only yield
            batches of image data, which is useful to use in
            `model.predict_generator()`).
    batch_size: size of the batches of data (default: 32).
    shuffle: whether to shuffle the data (default: True)
    seed: optional random seed for shuffling and transformations.
    save_to_dir: None or str (default: None).
        This allows you to optionally specify a directory
        to which to save the augmented pictures being generated
        (useful for visualizing what you are doing).
    save_prefix: str. Prefix to use for filenames of saved pictures
        (only relevant if `save_to_dir` is set).
    save_format: one of "png", "jpeg"
        (only relevant if `save_to_dir` is set). Default: "png".
    follow_links: whether to follow symlinks inside class subdirectories
        (default: False).
    subset: Subset of data (`"training"` or `"validation"`) if
        `validation_split` is set in `ImageDataGenerator`.
    interpolation: Interpolation method used to resample the image if the
        target size is different from that of the loaded image.
        Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`.
        If PIL version 1.1.3 or newer is installed, `"lanczos"` is also
        supported. If PIL version 3.4.0 or newer is installed, `"box"` and
        `"hamming"` are also supported. By default, `"nearest"` is used.
    validate_filenames: Boolean, whether to validate image filenames in
        `x_col`. If `True`, invalid images will be ignored. Disabling this
        option can lead to speed-up in the execution of this function.
        Default: `True`.

# Returns
    A `DataFrameIterator` yielding tuples of `(x, y)`
    where `x` is a numpy array containing a batch
    of images with shape `(batch_size, *target_size, channels)`
    and `y` is a numpy array of corresponding labels.

<h3 id="flow_from_directory"><code>flow_from_directory</code></h3>

``` python
flow_from_directory(
    directory,
    target_size=(256, 256),
    color_mode='rgb',
    classes=None,
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    follow_links=False,
    subset=None,
    interpolation='nearest'
)
```

Takes the path to a directory & generates batches of augmented data.

# Arguments
    directory: string, path to the target directory.
        It should contain one subdirectory per class.
        Any PNG, JPG, BMP, PPM or TIF images
        inside each of the subdirectories directory tree
        will be included in the generator.
        See [this script](
        https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d)
        for more details.
    target_size: Tuple of integers `(height, width)`,
        default: `(256, 256)`.
        The dimensions to which all images found will be resized.
    color_mode: One of "grayscale", "rgb", "rgba". Default: "rgb".
        Whether the images will be converted to
        have 1, 3, or 4 channels.
    classes: Optional list of class subdirectories
        (e.g. `['dogs', 'cats']`). Default: None.
        If not provided, the list of classes will be automatically
        inferred from the subdirectory names/structure
        under `directory`, where each subdirectory will
        be treated as a different class
        (and the order of the classes, which will map to the label
        indices, will be alphanumeric).
        The dictionary containing the mapping from class names to class
        indices can be obtained via the attribute `class_indices`.
    class_mode: One of "categorical", "binary", "sparse",
        "input", or None. Default: "categorical".
        Determines the type of label arrays that are returned:
        - "categorical" will be 2D one-hot encoded labels,
        - "binary" will be 1D binary labels,
            "sparse" will be 1D integer labels,
        - "input" will be images identical
            to input images (mainly used to work with autoencoders).
        - If None, no labels are returned
          (the generator will only yield batches of image data,
          which is useful to use with `model.predict_generator()`).
          Please note that in case of class_mode None,
          the data still needs to reside in a subdirectory
          of `directory` for it to work correctly.
    batch_size: Size of the batches of data (default: 32).
    shuffle: Whether to shuffle the data (default: True)
        If set to False, sorts the data in alphanumeric order.
    seed: Optional random seed for shuffling and transformations.
    save_to_dir: None or str (default: None).
        This allows you to optionally specify
        a directory to which to save
        the augmented pictures being generated
        (useful for visualizing what you are doing).
    save_prefix: Str. Prefix to use for filenames of saved pictures
        (only relevant if `save_to_dir` is set).
    save_format: One of "png", "jpeg"
        (only relevant if `save_to_dir` is set). Default: "png".
    follow_links: Whether to follow symlinks inside
        class subdirectories (default: False).
    subset: Subset of data (`"training"` or `"validation"`) if
        `validation_split` is set in `ImageDataGenerator`.
    interpolation: Interpolation method used to
        resample the image if the
        target size is different from that of the loaded image.
        Supported methods are `"nearest"`, `"bilinear"`,
        and `"bicubic"`.
        If PIL version 1.1.3 or newer is installed, `"lanczos"` is also
        supported. If PIL version 3.4.0 or newer is installed,
        `"box"` and `"hamming"` are also supported.
        By default, `"nearest"` is used.

# Returns
    A `DirectoryIterator` yielding tuples of `(x, y)`
        where `x` is a numpy array containing a batch
        of images with shape `(batch_size, *target_size, channels)`
        and `y` is a numpy array of corresponding labels.

<h3 id="get_random_transform"><code>get_random_transform</code></h3>

``` python
get_random_transform(
    img_shape,
    seed=None
)
```

Generates random parameters for a transformation.

# Arguments
    seed: Random seed.
    img_shape: Tuple of integers.
        Shape of the image that is transformed.

# Returns
    A dictionary containing randomly chosen parameters describing the
    transformation.

<h3 id="random_transform"><code>random_transform</code></h3>

``` python
random_transform(
    x,
    seed=None
)
```

Applies a random transformation to an image.

# Arguments
    x: 3D tensor, single image.
    seed: Random seed.

# Returns
    A randomly transformed version of the input (same shape).

<h3 id="standardize"><code>standardize</code></h3>

``` python
standardize(x)
```

Applies the normalization configuration in-place to a batch of inputs.

`x` is changed in-place since the function is mainly used internally
to standarize images and feed them to your network. If a copy of `x`
would be created instead it would have a significant performance cost.
If you want to apply this method without changing the input in-place
you can call the method creating a copy before:

standarize(np.copy(x))

# Arguments
    x: Batch of inputs to be normalized.

# Returns
    The inputs, normalized.
