page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.image

Write an image summary.

``` python
tf.compat.v2.summary.image(
    name,
    data,
    step=None,
    max_outputs=3,
    description=None
)
```



Defined in [`plugins/image/summary_v2.py`](https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/image/summary_v2.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`name`</b>: A name for this summary. The summary tag used for TensorBoard will
  be this name prefixed by any active name scopes.
* <b>`data`</b>: A `Tensor` representing pixel data with shape `[k, h, w, c]`,
  where `k` is the number of images, `h` and `w` are the height and
  width of the images, and `c` is the number of channels, which
  should be 1, 2, 3, or 4 (grayscale, grayscale with alpha, RGB, RGBA).
  Any of the dimensions may be statically unknown (i.e., `None`).
  Floating point data will be clipped to the range [0,1).
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to `tf.summary.experimental.get_step()`, which must
  not be None.
* <b>`max_outputs`</b>: Optional `int` or rank-0 integer `Tensor`. At most this
  many images will be emitted at each step. When more than
  `max_outputs` many images are provided, the first `max_outputs` many
  images will be used and the rest silently discarded.
* <b>`description`</b>: Optional long-form description for this summary, as a
  constant `str`. Markdown is supported. Defaults to empty.


#### Returns:

True on success, or false if no summary was emitted because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  `tf.summary.experimental.get_step()` is None.