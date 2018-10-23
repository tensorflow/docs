

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.csiszar_divergence.modified_gan

``` python
modified_gan(
    logu,
    self_normalized=False,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/bayesflow/python/ops/csiszar_divergence_impl.py).

The Modified-GAN Csiszar-function in log-space.

A Csiszar-function is a member of,

```none
F = { f:R_+ to R : f convex }.
```

When `self_normalized = True` the modified-GAN (Generative/Adversarial
Network) Csiszar-function is:

```none
f(u) = log(1 + u) - log(u) + 0.5 (u - 1)
```

When `self_normalized = False` the `0.5 (u - 1)` is omitted.

The unmodified GAN Csiszar-function is identical to Jensen-Shannon (with
`self_normalized = False`).

Warning: this function makes non-log-space calculations and may therefore be
numerically unstable for `|logu| >> 0`.

#### Args:

* <b>`logu`</b>: Floating-type `Tensor` representing `log(u)` from above.
* <b>`self_normalized`</b>: Python `bool` indicating whether `f'(u=1)=0`. When
    `f'(u=1)=0` the implied Csiszar f-Divergence remains non-negative even
    when `p, q` are unnormalized measures.
* <b>`name`</b>: Python `str` name prefixed to Ops created by this function.


#### Returns:

* <b>`chi_square_of_u`</b>: Floating-type `Tensor` of the Csiszar-function evaluated
    at `u = exp(logu)`.