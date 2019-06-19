page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.spatial_softmax

``` python
tf.contrib.layers.spatial_softmax(
    features,
    temperature=None,
    name=None,
    variables_collections=None,
    trainable=True,
    data_format='NHWC'
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/layers/python/layers/layers.py).

Computes the spatial softmax of a convolutional feature map.

First computes the softmax over the spatial extent of each channel of a
convolutional feature map. Then computes the expected 2D position of the
points of maximal activation for each channel, resulting in a set of
feature keypoints [x1, y1, ... xN, yN] for all N channels.

Read more here:
"Learning visual feature spaces for robotic manipulation with
deep spatial autoencoders." Finn et al., http://arxiv.org/abs/1509.06113.

#### Args:

* <b>`features`</b>: A `Tensor` of size [batch_size, W, H, num_channels]; the
    convolutional feature map.
* <b>`temperature`</b>: Softmax temperature (optional). If None, a learnable
    temperature is created.
* <b>`name`</b>: A name for this operation (optional).
* <b>`variables_collections`</b>: Collections for the temperature variable.
* <b>`trainable`</b>: If `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see <a href="../../../tf/Variable"><code>tf.Variable</code></a>).
* <b>`data_format`</b>: A string. `NHWC` (default) and `NCHW` are supported.

#### Returns:

* <b>`feature_keypoints`</b>: A `Tensor` with size [batch_size, num_channels * 2];
    the expected 2D locations of each channel's feature keypoint (normalized
    to the range (-1,1)). The inner dimension is arranged as
    [x1, y1, ... xN, yN].

#### Raises:

* <b>`ValueError`</b>: If unexpected data_format specified.
* <b>`ValueError`</b>: If num_channels dimension is unspecified.