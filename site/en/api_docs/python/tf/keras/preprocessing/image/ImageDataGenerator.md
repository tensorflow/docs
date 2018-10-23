

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.ImageDataGenerator

## Class `ImageDataGenerator`





Defined in [`tensorflow/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/preprocessing/image.py).

Generates batches of tensor image data with real-time data augmentation.
The data will be looped over (in batches).

#### Arguments:

* <b>`featurewise_center`</b>: boolean, set input mean to 0 over the dataset,
        feature-wise.
* <b>`samplewise_center`</b>: boolean, set each sample mean to 0.
* <b>`featurewise_std_normalization`</b>: boolean, divide inputs by std
        of the dataset, feature-wise.
* <b>`samplewise_std_normalization`</b>: boolean, divide each input by its std.
* <b>`zca_epsilon`</b>: epsilon for ZCA whitening. Default is 1e-6.
* <b>`zca_whitening`</b>: boolean, apply ZCA whitening.
* <b>`rotation_range`</b>: int, degree range for random rotations.
* <b>`width_shift_range`</b>: float, 1-D array-like or int
        float: fraction of total width, if < 1, or pixels if >= 1.
        1-D array-like: random elements from the array.
        int: integer number of pixels from interval
            `(-width_shift_range, +width_shift_range)`
        With `width_shift_range=2` possible values are integers [-1, 0, +1],
        same as with `width_shift_range=[-1, 0, +1]`,
        while with `width_shift_range=1.0` possible values are floats in
        the interval [-1.0, +1.0).
* <b>`shear_range`</b>: float, shear Intensity
        (Shear angle in counter-clockwise direction in degrees)
* <b>`zoom_range`</b>: float or [lower, upper], Range for random zoom.
        If a float, `[lower, upper] = [1-zoom_range, 1+zoom_range]`.
* <b>`channel_shift_range`</b>: float, range for random channel shifts.
* <b>`fill_mode`</b>: One of {"constant", "nearest", "reflect" or "wrap"}.
        Default is 'nearest'. Points outside the boundaries of the input
        are filled according to the given mode:
            'constant': kkkkkkkk|abcd|kkkkkkkk (cval=k)
            'nearest':  aaaaaaaa|abcd|dddddddd
            'reflect':  abcddcba|abcd|dcbaabcd
            'wrap':  abcdabcd|abcd|abcdabcd
* <b>`cval`</b>: float or int, value used for points outside the boundaries
        when `fill_mode = "constant"`.
* <b>`horizontal_flip`</b>: boolean, randomly flip inputs horizontally.
* <b>`vertical_flip`</b>: boolean, randomly flip inputs vertically.
* <b>`rescale`</b>: rescaling factor. Defaults to None. If None or 0, no rescaling
        is applied, otherwise we multiply the data by the value provided
        (before applying any other transformation).
* <b>`preprocessing_function`</b>: function that will be implied on each input.
        The function will run after the image is resized and augmented.
        The function should take one argument:
        one image (Numpy tensor with rank 3),
        and should output a Numpy tensor with the same shape.
* <b>`data_format`</b>: One of {"channels_first", "channels_last"}.
        "channels_last" mode means that the images should have shape
            `(samples, height, width, channels)`,
        "channels_first" mode means that the images should have shape
            `(samples, channels, height, width)`.
        It defaults to the `image_data_format` value found in your
            Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".
* <b>`validation_split`</b>: float, fraction of images reserved for validation
        (strictly between 0 and 1).

Examples:
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
                         rotation_range=90.,
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

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-06,
    rotation_range=0.0,
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
    validation_split=0.0
)
```



<h3 id="fit"><code>fit</code></h3>

``` python
fit(
    x,
    augment=False,
    rounds=1,
    seed=None
)
```

Computes the internal data statistics based on an array of sample data.

These are statistics related to the data-dependent transformations.
Only required if featurewise_center or featurewise_std_normalization or
zca_whitening.

#### Arguments:

* <b>`x`</b>: sample data. Should have rank 4.
        In case of grayscale data, the channels axis should have value 1
        and in case of RGB data, it should have value 3.
* <b>`augment`</b>: Boolean (default: False). Whether to fit on randomly
        augmented samples.
* <b>`rounds`</b>: int (default: 1). If augment, how many augmentation passes
        over the data to use.
* <b>`seed`</b>: int (default: None). Random seed.


#### Raises:

* <b>`ValueError`</b>: If input rank is not 4.
* <b>`ImportError`</b>: If scipy is not imported.

<h3 id="flow"><code>flow</code></h3>

``` python
flow(
    x,
    y=None,
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    subset=None
)
```

Generates batches of augmented/normalized data with given numpy arrays.

#### Arguments:

* <b>`x`</b>: data. Should have rank 4.
        In case of grayscale data, the channels axis should have value 1
        and in case of RGB data, it should have value 3.
* <b>`y`</b>: labels.
* <b>`batch_size`</b>: int (default: 32).
* <b>`shuffle`</b>: boolean (default: True).
* <b>`seed`</b>: int (default: None).
* <b>`save_to_dir`</b>: None or str (default: None).
        This allows you to optionally specify a directory
        to which to save the augmented pictures being generated
        (useful for visualizing what you are doing).
* <b>`save_prefix`</b>: str (default: `''`). Prefix to use for filenames of
        saved pictures (only relevant if `save_to_dir` is set).
* <b>`save_format`</b>: one of "png", "jpeg". Default: "png".
        (only relevant if `save_to_dir` is set)
* <b>`subset`</b>: Subset of data (`"training"` or `"validation"`) if
        `validation_split` is set in `ImageDataGenerator`.


#### Returns:

An Iterator yielding tuples of `(x, y)` where `x` is a numpy array of
  image data and `y` is a numpy array of corresponding labels.

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

Generates batches of augmented/normalized data given directory path.

#### Arguments:

* <b>`directory`</b>: path to the target directory. It should contain one
        subdirectory per class. Any PNG, JPG, BMP, PPM or TIF images
        inside each of the subdirectories directory tree will be included
        in the generator. See [this script]
        (https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d)
        for more details.
* <b>`target_size`</b>: tuple of integers `(height, width)`, default: `(256,
        256)`. The dimensions to which all images found will be resized.
* <b>`color_mode`</b>: one of "grayscale", "rbg". Default: "rgb". Whether the
        images will be converted to have 1 or 3 color channels.
* <b>`classes`</b>: optional list of class subdirectories (e.g. `['dogs',
        'cats']`). Default: None. If not provided, the list of classes
        will be automatically inferred from the subdirectory
        names/structure under `directory`, where each subdirectory will be
        treated as a different class (and the order of the classes, which
        will map to the label indices, will be alphanumeric). The
        dictionary containing the mapping from class names to class
        indices can be obtained via the attribute `class_indices`.
* <b>`class_mode`</b>: one of "categorical", "binary", "sparse", "input" or
        None. Default: "categorical". Determines the type of label arrays
        that are returned: "categorical" will be 2D one-hot encoded
        labels, "binary" will be 1D binary labels, "sparse" will be 1D
        integer labels, "input" will be images identical to input images
        (mainly used to work with autoencoders). If None, no labels are
        returned (the generator will only yield batches of image data,
        which is useful to use `model.predict_generator()`,
        `model.evaluate_generator()`, etc.). Please note that in case of
        class_mode None, the data still needs to reside in a subdirectory
        of `directory` for it to work correctly.
* <b>`batch_size`</b>: size of the batches of data (default: 32).
* <b>`shuffle`</b>: whether to shuffle the data (default: True)
* <b>`seed`</b>: optional random seed for shuffling and transformations.
* <b>`save_to_dir`</b>: None or str (default: None). This allows you to
        optionally specify a directory to which to save the augmented
        pictures being generated (useful for visualizing what you are doing)
* <b>`save_prefix`</b>: str. Prefix to use for filenames of saved pictures
        (only relevant if `save_to_dir` is set).
* <b>`save_format`</b>: one of "png", "jpeg" (only relevant if `save_to_dir` is
        set). Default: "png".
* <b>`follow_links`</b>: whether to follow symlinks inside class subdirectories
        (default: False).
* <b>`subset`</b>: Subset of data (`"training"` or `"validation"`) if
      ` validation_split` is set in `ImageDataGenerator`.
* <b>`interpolation`</b>: Interpolation method used to resample the image if
        the target size is different from that of the loaded image.
        Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`.
        If PIL version 1.1.3 or newer is installed, `"lanczos"` is also
        supported. If PIL version 3.4.0 or newer is installed, `"box"` and
        `"hamming"` are also supported. By default, `"nearest"` is used.


#### Returns:

A DirectoryIterator yielding tuples of `(x, y)` where `x` is a
numpy array containing a batch of images with shape
`(batch_size, *target_size, channels)` and `y` is a numpy
array of corresponding labels.

<h3 id="random_transform"><code>random_transform</code></h3>

``` python
random_transform(
    x,
    seed=None
)
```

Randomly augment a single image tensor.

#### Arguments:

* <b>`x`</b>: 3D tensor, single image.
* <b>`seed`</b>: random seed.


#### Returns:

A randomly transformed version of the input (same shape).


#### Raises:

* <b>`ImportError`</b>: if Scipy is not available.

<h3 id="standardize"><code>standardize</code></h3>

``` python
standardize(x)
```

Apply the normalization configuration to a batch of inputs.

#### Arguments:

* <b>`x`</b>: batch of inputs to be normalized.


#### Returns:

The inputs, normalized.



