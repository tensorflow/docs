description: Loads an image into PIL format.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.load_img" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.image.load_img

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Loads an image into PIL format.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.load_img`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.load_img(
    path, grayscale=(False), color_mode='rgb', target_size=None,
    interpolation='nearest'
)
</code></pre>



<!-- Placeholder for "Used in" -->

# Arguments
    path: Path to image file.
    grayscale: DEPRECATED use `color_mode="grayscale"`.
    color_mode: The desired image format. One of "grayscale", "rgb", "rgba".
        "grayscale" supports 8-bit images and 32-bit signed integer images.
        Default: "rgb".
    target_size: Either `None` (default to original size)
        or tuple of ints `(img_height, img_width)`.
    interpolation: Interpolation method used to resample the image if the
        target size is different from that of the loaded image.
        Supported methods are "nearest", "bilinear", and "bicubic".
        If PIL version 1.1.3 or newer is installed, "lanczos" is also
        supported. If PIL version 3.4.0 or newer is installed, "box" and
        "hamming" are also supported.
        Default: "nearest".

# Returns
    A PIL Image instance.

# Raises
    ImportError: if PIL is not available.
    ValueError: if interpolation method is not supported.