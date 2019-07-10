page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.instance_norm

Functional interface for the instance normalization layer.

``` python
tf.contrib.layers.instance_norm(
    inputs,
    center=True,
    scale=True,
    epsilon=1e-06,
    activation_fn=None,
    param_initializers=None,
    reuse=None,
    variables_collections=None,
    outputs_collections=None,
    trainable=True,
    data_format=DATA_FORMAT_NHWC,
    scope=None
)
```



Defined in [`contrib/layers/python/layers/normalization.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/normalization.py).

<!-- Placeholder for "Used in" -->

Reference: https://arxiv.org/abs/1607.08022.

  "Instance Normalization: The Missing Ingredient for Fast Stylization"
  Dmitry Ulyanov, Andrea Vedaldi, Victor Lempitsky

#### Args:


* <b>`inputs`</b>: A tensor with 2 or more dimensions, where the first dimension has
  `batch_size`. The normalization is over all but the last dimension if
  `data_format` is `NHWC` and the second dimension if `data_format` is
  `NCHW`.
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
* <b>`data_format`</b>: A string. `NHWC` (default) and `NCHW` are supported.
* <b>`scope`</b>: Optional scope for `variable_scope`.


#### Returns:

A `Tensor` representing the output of the operation.



#### Raises:


* <b>`ValueError`</b>: If `data_format` is neither `NHWC` nor `NCHW`.
* <b>`ValueError`</b>: If the rank of `inputs` is undefined.
* <b>`ValueError`</b>: If rank or channels dimension of `inputs` is undefined.