

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.spectral.dct

``` python
tf.spectral.dct(
    input,
    type=2,
    n=None,
    axis=-1,
    norm=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/spectral_ops.py).

See the guide: [Spectral Functions > Discrete Cosine Transforms](../../../../api_guides/python/spectral_ops#Discrete_Cosine_Transforms)

Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

Currently only Type II is supported. Implemented using a length `2N` padded
<a href="../../tf/spectral/rfft"><code>tf.spectral.rfft</code></a>, as described here: https://dsp.stackexchange.com/a/10606



#### Args:

* <b>`input`</b>: A `[..., samples]` `float32` `Tensor` containing the signals to
    take the DCT of.
* <b>`type`</b>: The DCT type to perform. Must be 2.
* <b>`n`</b>: For future expansion. The length of the transform. Must be `None`.
* <b>`axis`</b>: For future expansion. The axis to compute the DCT along. Must be `-1`.
* <b>`norm`</b>: The normalization to apply. `None` for no normalization or `'ortho'`
    for orthonormal normalization.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `[..., samples]` `float32` `Tensor` containing the DCT of `input`.


#### Raises:

* <b>`ValueError`</b>: If `type` is not `2`, `n` is not `None, `axis` is not `-1`, or
    `norm` is not `None` or `'ortho'`.

[dct]: https://en.wikipedia.org/wiki/Discrete_cosine_transform

#### Scipy Compatibility
Equivalent to scipy.fftpack.dct for the Type-II DCT.
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.fftpack.dct.html

