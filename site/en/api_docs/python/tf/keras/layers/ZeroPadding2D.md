page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ZeroPadding2D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional.py#L2114-L2212">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ZeroPadding2D`

Zero-padding layer for 2D input (e.g. picture).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.ZeroPadding2D`
* Class `tf.compat.v2.keras.layers.ZeroPadding2D`


### Used in the tutorials:

* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)



This layer can add rows and columns of zeros
at the top, bottom, left and right side of an image tensor.

#### Arguments:


* <b>`padding`</b>: Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
  - If int: the same symmetric padding
    is applied to height and width.
  - If tuple of 2 ints:
    interpreted as two different
    symmetric padding values for height and width:
    `(symmetric_height_pad, symmetric_width_pad)`.
  - If tuple of 2 tuples of 2 ints:
    interpreted as
    `((top_pad, bottom_pad), (left_pad, right_pad))`
* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, height, width, channels)` while `channels_first`
  corresponds to inputs with shape
  `(batch, channels, height, width)`.
  It defaults to the `image_data_format` value found in your
  Keras config file at `~/.keras/keras.json`.
  If you never set it, then it will be "channels_last".


#### Input shape:

4D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch, rows, cols, channels)`
- If `data_format` is `"channels_first"`:
    `(batch, channels, rows, cols)`



#### Output shape:

4D tensor with shape:
- If `data_format` is `"channels_last"`:
    `(batch, padded_rows, padded_cols, channels)`
- If `data_format` is `"channels_first"`:
    `(batch, channels, padded_rows, padded_cols)`


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/convolutional.py#L2157-L2178">View source</a>

``` python
__init__(
    padding=(1, 1),
    data_format=None,
    **kwargs
)
```
