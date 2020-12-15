description: Instantiates the MobileNetV3Small architecture.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.MobileNetV3Small" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.applications.MobileNetV3Small

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/applications/mobilenet_v3.py#L354-L387">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates the MobileNetV3Small architecture.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.applications.MobileNetV3Small`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.applications.MobileNetV3Small(
    input_shape=None, alpha=1.0, minimalistic=(False), include_top=(True),
    weights='imagenet', input_tensor=None, classes=1000, pooling=None,
    dropout_rate=0.2, classifier_activation='softmax'
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Reference:


- [Searching for MobileNetV3](
    https://arxiv.org/pdf/1905.02244.pdf) (ICCV 2019)

The following table describes the performance of MobileNets:
------------------------------------------------------------------------
MACs stands for Multiply Adds

|Classification Checkpoint|MACs(M)|Parameters(M)|Top1 Accuracy|Pixel1 CPU(ms)|
|---|---|---|---|---|
| mobilenet_v3_large_1.0_224              | 217 | 5.4 |   75.6   |   51.2  |
| mobilenet_v3_large_0.75_224             | 155 | 4.0 |   73.3   |   39.8  |
| mobilenet_v3_large_minimalistic_1.0_224 | 209 | 3.9 |   72.3   |   44.1  |
| mobilenet_v3_small_1.0_224              | 66  | 2.9 |   68.1   |   15.8  |
| mobilenet_v3_small_0.75_224             | 44  | 2.4 |   65.4   |   12.8  |
| mobilenet_v3_small_minimalistic_1.0_224 | 65  | 2.0 |   61.9   |   12.2  |

The weights for all 6 models are obtained and translated from the Tensorflow
checkpoints from TensorFlow checkpoints found [here]
(https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet/README.md).

Optionally loads weights pre-trained on ImageNet.

Note: each Keras Application expects a specific kind of input preprocessing.
For MobileNetV3, call
<a href="../../../tf/keras/applications/mobilenet_v3/preprocess_input.md"><code>tf.keras.applications.mobilenet_v3.preprocess_input</code></a> on your
inputs before passing them to the model.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`input_shape`
</td>
<td>
Optional shape tuple, to be specified if you would
like to use a model with an input image resolution that is not
(224, 224, 3).
It should have exactly 3 inputs channels (224, 224, 3).
You can also omit this option if you would like
to infer input_shape from an input_tensor.
If you choose to include both input_tensor and input_shape then
input_shape will be used if they match, if the shapes
do not match then we will throw an error.
E.g. `(160, 160, 3)` would be one valid value.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
controls the width of the network. This is known as the
depth multiplier in the MobileNetV3 paper, but the name is kept for
consistency with MobileNetV1 in Keras.
- If `alpha` < 1.0, proportionally decreases the number
of filters in each layer.
- If `alpha` > 1.0, proportionally increases the number
of filters in each layer.
- If `alpha` = 1, default number of filters from the paper
are used at each layer.
</td>
</tr><tr>
<td>
`minimalistic`
</td>
<td>
In addition to large and small models this module also
contains so-called minimalistic models, these models have the same
per-layer dimensions characteristic as MobilenetV3 however, they don't
utilize any of the advanced blocks (squeeze-and-excite units, hard-swish,
and 5x5 convolutions). While these models are less efficient on CPU, they
are much more performant on GPU/DSP.
</td>
</tr><tr>
<td>
`include_top`
</td>
<td>
Boolean, whether to include the fully-connected
layer at the top of the network. Defaults to `True`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
String, one of `None` (random initialization),
'imagenet' (pre-training on ImageNet),
or the path to the weights file to be loaded.
</td>
</tr><tr>
<td>
`input_tensor`
</td>
<td>
Optional Keras tensor (i.e. output of
<a href="../../../tf/keras/Input.md"><code>layers.Input()</code></a>)
to use as image input for the model.
</td>
</tr><tr>
<td>
`pooling`
</td>
<td>
String, optional pooling mode for feature extraction
when `include_top` is `False`.
- `None` means that the output of the model
will be the 4D tensor output of the
last convolutional block.
- `avg` means that global average pooling
will be applied to the output of the
last convolutional block, and thus
the output of the model will be a
2D tensor.
- `max` means that global max pooling will
be applied.
</td>
</tr><tr>
<td>
`classes`
</td>
<td>
Integer, optional number of classes to classify images
into, only to be specified if `include_top` is True, and
if no `weights` argument is specified.
</td>
</tr><tr>
<td>
`dropout_rate`
</td>
<td>
fraction of the input units to drop on the last layer.
</td>
</tr><tr>
<td>
`classifier_activation`
</td>
<td>
A `str` or callable. The activation function to use
on the "top" layer. Ignored unless `include_top=True`. Set
`classifier_activation=None` to return the logits of the "top" layer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/keras/Model.md"><code>keras.Model</code></a> instance.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
in case of invalid argument for `weights`,
or invalid input shape or invalid alpha, rows when
weights='imagenet'
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `classifier_activation` is not `softmax` or `None` when
using a pretrained top layer.
</td>
</tr>
</table>

