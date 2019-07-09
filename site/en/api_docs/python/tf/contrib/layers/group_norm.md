page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.group_norm

``` python
tf.contrib.layers.group_norm(
    inputs,
    groups=32,
    channels_axis=-1,
    reduction_axes=(-3, -2),
    center=True,
    scale=True,
    epsilon=1e-06,
    activation_fn=None,
    param_initializers=None,
    reuse=None,
    variables_collections=None,
    outputs_collections=None,
    trainable=True,
    scope=None,
    mean_close_to_zero=False
)
```



Defined in [`tensorflow/contrib/layers/python/layers/normalization.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/layers/python/layers/normalization.py).

Functional interface for the group normalization layer.

Reference: https://arxiv.org/abs/1803.08494.

  "Group Normalization", Yuxin Wu, Kaiming He

#### Args:

* <b>`inputs`</b>: A Tensor with at least 2 dimensions one which is channels. All
   shape dimensions must be fully defined.
* <b>`groups`</b>: Integer. Divide the channels into this number of groups over which
    normalization statistics are computed. This number must be commensurate
    with the number of channels in `inputs`.
* <b>`channels_axis`</b>: An integer. Specifies index of channels axis which will be
    broken into `groups`, each of which whose statistics will be computed
    across. Must be mutually exclusive with `reduction_axes`. Preferred usage
    is to specify negative integers to be agnostic as to whether a batch
    dimension is included.
* <b>`reduction_axes`</b>: Tuple of integers. Specifies dimensions over which
     statistics will be accumulated. Must be mutually exclusive with
     `channels_axis`. Statistics will not be accumulated across axes not
     specified in `reduction_axes` nor `channel_axis`. Preferred usage is to
     specify negative integers to be agnostic to whether a batch dimension is
     included.

    Some sample usage cases:
      NHWC format: channels_axis=-1, reduction_axes=[-3, -2]
      NCHW format: channels_axis=-3, reduction_axes=[-2, -1]

* <b>`center`</b>: If True, add offset of `beta` to normalized tensor. If False, `beta`
    is ignored.
* <b>`scale`</b>: If True, multiply by `gamma`. If False, `gamma` is
    not used. When the next layer is linear (also e.g. `nn.relu`), this can be
    disabled since the scaling can be done by the next layer.
* <b>`epsilon`</b>: Small float added to variance to avoid dividing by zero.
* <b>`activation_fn`</b>: Activation function, default set to None to skip it and
    maintain a linear activation.
* <b>`param_initializers`</b>: Optional initializers for beta, gamma, moving mean and
    moving variance.
* <b>`reuse`</b>: Whether or not the layer and its variables should be reused. To be
    able to reuse the layer scope must be given.
* <b>`variables_collections`</b>: Optional collections for the variables.
* <b>`outputs_collections`</b>: Collections to add the outputs.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`scope`</b>: Optional scope for `variable_scope`.
* <b>`mean_close_to_zero`</b>: The mean of `input` before ReLU will be close to zero
    when batch size >= 4k for Resnet-50 on TPU. If `True`, use
    `nn.sufficient_statistics` and `nn.normalize_moments` to calculate the
    variance. This is the same behavior as `fused` equals `True` in batch
    normalization. If `False`, use `nn.moments` to calculate the variance.
    When `mean` is close to zero, like 1e-4, use `mean` to calculate the
    variance may have poor result due to repeated roundoff error and
    denormalization in `mean`.  When `mean` is large, like 1e2,
    sum(`input`^2) is so large that only the high-order digits of the elements
    are being accumulated. Thus, use sum(`input` - `mean`)^2/n to calculate
    the variance has better accuracy compared to (sum(`input`^2)/n - `mean`^2)
    when `mean` is large.



#### Returns:

A `Tensor` representing the output of the operation.


#### Raises:

* <b>`ValueError`</b>: If the rank of `inputs` is undefined.
* <b>`ValueError`</b>: If rank or channels dimension of `inputs` is undefined.
* <b>`ValueError`</b>: If number of groups is not commensurate with number of channels.
* <b>`ValueError`</b>: If reduction_axes or channels_axis are out of bounds.
* <b>`ValueError`</b>: If reduction_axes are not mutually exclusive with channels_axis.