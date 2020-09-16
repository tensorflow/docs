description: Keras layers API.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.keras.layers

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Keras layers API.



## Modules

[`experimental`](../../tf/keras/layers/experimental.md) module: Public API for tf.keras.layers.experimental namespace.

## Classes

[`class AbstractRNNCell`](../../tf/keras/layers/AbstractRNNCell.md): Abstract object representing an RNN cell.

[`class Activation`](../../tf/keras/layers/Activation.md): Applies an activation function to an output.

[`class ActivityRegularization`](../../tf/keras/layers/ActivityRegularization.md): Layer that applies an update to the cost function based input activity.

[`class Add`](../../tf/keras/layers/Add.md): Layer that adds a list of inputs.

[`class AdditiveAttention`](../../tf/keras/layers/AdditiveAttention.md): Additive attention layer, a.k.a. Bahdanau-style attention.

[`class AlphaDropout`](../../tf/keras/layers/AlphaDropout.md): Applies Alpha Dropout to the input.

[`class Attention`](../../tf/keras/layers/Attention.md): Dot-product attention layer, a.k.a. Luong-style attention.

[`class Average`](../../tf/keras/layers/Average.md): Layer that averages a list of inputs element-wise.

[`class AveragePooling1D`](../../tf/keras/layers/AveragePooling1D.md): Average pooling for temporal data.

[`class AveragePooling2D`](../../tf/keras/layers/AveragePooling2D.md): Average pooling operation for spatial data.

[`class AveragePooling3D`](../../tf/keras/layers/AveragePooling3D.md): Average pooling operation for 3D data (spatial or spatio-temporal).

[`class AvgPool1D`](../../tf/keras/layers/AveragePooling1D.md): Average pooling for temporal data.

[`class AvgPool2D`](../../tf/keras/layers/AveragePooling2D.md): Average pooling operation for spatial data.

[`class AvgPool3D`](../../tf/keras/layers/AveragePooling3D.md): Average pooling operation for 3D data (spatial or spatio-temporal).

[`class BatchNormalization`](../../tf/keras/layers/BatchNormalization.md): Normalize and scale inputs or activations. (Ioffe and Szegedy, 2014).

[`class Bidirectional`](../../tf/keras/layers/Bidirectional.md): Bidirectional wrapper for RNNs.

[`class Concatenate`](../../tf/keras/layers/Concatenate.md): Layer that concatenates a list of inputs.

[`class Conv1D`](../../tf/keras/layers/Conv1D.md): 1D convolution layer (e.g. temporal convolution).

[`class Conv2D`](../../tf/keras/layers/Conv2D.md): 2D convolution layer (e.g. spatial convolution over images).

[`class Conv2DTranspose`](../../tf/keras/layers/Conv2DTranspose.md): Transposed convolution layer (sometimes called Deconvolution).

[`class Conv3D`](../../tf/keras/layers/Conv3D.md): 3D convolution layer (e.g. spatial convolution over volumes).

[`class Conv3DTranspose`](../../tf/keras/layers/Conv3DTranspose.md): Transposed convolution layer (sometimes called Deconvolution).

[`class ConvLSTM2D`](../../tf/keras/layers/ConvLSTM2D.md): Convolutional LSTM.

[`class Convolution1D`](../../tf/keras/layers/Conv1D.md): 1D convolution layer (e.g. temporal convolution).

[`class Convolution2D`](../../tf/keras/layers/Conv2D.md): 2D convolution layer (e.g. spatial convolution over images).

[`class Convolution2DTranspose`](../../tf/keras/layers/Conv2DTranspose.md): Transposed convolution layer (sometimes called Deconvolution).

[`class Convolution3D`](../../tf/keras/layers/Conv3D.md): 3D convolution layer (e.g. spatial convolution over volumes).

[`class Convolution3DTranspose`](../../tf/keras/layers/Conv3DTranspose.md): Transposed convolution layer (sometimes called Deconvolution).

[`class Cropping1D`](../../tf/keras/layers/Cropping1D.md): Cropping layer for 1D input (e.g. temporal sequence).

[`class Cropping2D`](../../tf/keras/layers/Cropping2D.md): Cropping layer for 2D input (e.g. picture).

[`class Cropping3D`](../../tf/keras/layers/Cropping3D.md): Cropping layer for 3D data (e.g. spatial or spatio-temporal).

[`class Dense`](../../tf/keras/layers/Dense.md): Just your regular densely-connected NN layer.

[`class DenseFeatures`](../../tf/keras/layers/DenseFeatures.md): A layer that produces a dense `Tensor` based on given `feature_columns`.

[`class DepthwiseConv2D`](../../tf/keras/layers/DepthwiseConv2D.md): Depthwise separable 2D convolution.

[`class Dot`](../../tf/keras/layers/Dot.md): Layer that computes a dot product between samples in two tensors.

[`class Dropout`](../../tf/keras/layers/Dropout.md): Applies Dropout to the input.

[`class ELU`](../../tf/keras/layers/ELU.md): Exponential Linear Unit.

[`class Embedding`](../../tf/keras/layers/Embedding.md): Turns positive integers (indexes) into dense vectors of fixed size.

[`class Flatten`](../../tf/keras/layers/Flatten.md): Flattens the input. Does not affect the batch size.

[`class GRU`](../../tf/keras/layers/GRU.md): Gated Recurrent Unit - Cho et al. 2014.

[`class GRUCell`](../../tf/keras/layers/GRUCell.md): Cell class for the GRU layer.

[`class GaussianDropout`](../../tf/keras/layers/GaussianDropout.md): Apply multiplicative 1-centered Gaussian noise.

[`class GaussianNoise`](../../tf/keras/layers/GaussianNoise.md): Apply additive zero-centered Gaussian noise.

[`class GlobalAveragePooling1D`](../../tf/keras/layers/GlobalAveragePooling1D.md): Global average pooling operation for temporal data.

[`class GlobalAveragePooling2D`](../../tf/keras/layers/GlobalAveragePooling2D.md): Global average pooling operation for spatial data.

[`class GlobalAveragePooling3D`](../../tf/keras/layers/GlobalAveragePooling3D.md): Global Average pooling operation for 3D data.

[`class GlobalAvgPool1D`](../../tf/keras/layers/GlobalAveragePooling1D.md): Global average pooling operation for temporal data.

[`class GlobalAvgPool2D`](../../tf/keras/layers/GlobalAveragePooling2D.md): Global average pooling operation for spatial data.

[`class GlobalAvgPool3D`](../../tf/keras/layers/GlobalAveragePooling3D.md): Global Average pooling operation for 3D data.

[`class GlobalMaxPool1D`](../../tf/keras/layers/GlobalMaxPool1D.md): Global max pooling operation for 1D temporal data.

[`class GlobalMaxPool2D`](../../tf/keras/layers/GlobalMaxPool2D.md): Global max pooling operation for spatial data.

[`class GlobalMaxPool3D`](../../tf/keras/layers/GlobalMaxPool3D.md): Global Max pooling operation for 3D data.

[`class GlobalMaxPooling1D`](../../tf/keras/layers/GlobalMaxPool1D.md): Global max pooling operation for 1D temporal data.

[`class GlobalMaxPooling2D`](../../tf/keras/layers/GlobalMaxPool2D.md): Global max pooling operation for spatial data.

[`class GlobalMaxPooling3D`](../../tf/keras/layers/GlobalMaxPool3D.md): Global Max pooling operation for 3D data.

[`class InputLayer`](../../tf/keras/layers/InputLayer.md): Layer to be used as an entry point into a Network (a graph of layers).

[`class InputSpec`](../../tf/keras/layers/InputSpec.md): Specifies the rank, dtype and shape of every input to a layer.

[`class LSTM`](../../tf/keras/layers/LSTM.md): Long Short-Term Memory layer - Hochreiter 1997.

[`class LSTMCell`](../../tf/keras/layers/LSTMCell.md): Cell class for the LSTM layer.

[`class Lambda`](../../tf/keras/layers/Lambda.md): Wraps arbitrary expressions as a `Layer` object.

[`class Layer`](../../tf/keras/layers/Layer.md): This is the class from which all layers inherit.

[`class LayerNormalization`](../../tf/keras/layers/LayerNormalization.md): Layer normalization layer (Ba et al., 2016).

[`class LeakyReLU`](../../tf/keras/layers/LeakyReLU.md): Leaky version of a Rectified Linear Unit.

[`class LocallyConnected1D`](../../tf/keras/layers/LocallyConnected1D.md): Locally-connected layer for 1D inputs.

[`class LocallyConnected2D`](../../tf/keras/layers/LocallyConnected2D.md): Locally-connected layer for 2D inputs.

[`class Masking`](../../tf/keras/layers/Masking.md): Masks a sequence by using a mask value to skip timesteps.

[`class MaxPool1D`](../../tf/keras/layers/MaxPool1D.md): Max pooling operation for 1D temporal data.

[`class MaxPool2D`](../../tf/keras/layers/MaxPool2D.md): Max pooling operation for 2D spatial data.

[`class MaxPool3D`](../../tf/keras/layers/MaxPool3D.md): Max pooling operation for 3D data (spatial or spatio-temporal).

[`class MaxPooling1D`](../../tf/keras/layers/MaxPool1D.md): Max pooling operation for 1D temporal data.

[`class MaxPooling2D`](../../tf/keras/layers/MaxPool2D.md): Max pooling operation for 2D spatial data.

[`class MaxPooling3D`](../../tf/keras/layers/MaxPool3D.md): Max pooling operation for 3D data (spatial or spatio-temporal).

[`class Maximum`](../../tf/keras/layers/Maximum.md): Layer that computes the maximum (element-wise) a list of inputs.

[`class Minimum`](../../tf/keras/layers/Minimum.md): Layer that computes the minimum (element-wise) a list of inputs.

[`class Multiply`](../../tf/keras/layers/Multiply.md): Layer that multiplies (element-wise) a list of inputs.

[`class PReLU`](../../tf/keras/layers/PReLU.md): Parametric Rectified Linear Unit.

[`class Permute`](../../tf/keras/layers/Permute.md): Permutes the dimensions of the input according to a given pattern.

[`class RNN`](../../tf/keras/layers/RNN.md): Base class for recurrent layers.

[`class ReLU`](../../tf/keras/layers/ReLU.md): Rectified Linear Unit activation function.

[`class RepeatVector`](../../tf/keras/layers/RepeatVector.md): Repeats the input n times.

[`class Reshape`](../../tf/keras/layers/Reshape.md): Layer that reshapes inputs into the given shape.

[`class SeparableConv1D`](../../tf/keras/layers/SeparableConv1D.md): Depthwise separable 1D convolution.

[`class SeparableConv2D`](../../tf/keras/layers/SeparableConv2D.md): Depthwise separable 2D convolution.

[`class SeparableConvolution1D`](../../tf/keras/layers/SeparableConv1D.md): Depthwise separable 1D convolution.

[`class SeparableConvolution2D`](../../tf/keras/layers/SeparableConv2D.md): Depthwise separable 2D convolution.

[`class SimpleRNN`](../../tf/keras/layers/SimpleRNN.md): Fully-connected RNN where the output is to be fed back to input.

[`class SimpleRNNCell`](../../tf/keras/layers/SimpleRNNCell.md): Cell class for SimpleRNN.

[`class Softmax`](../../tf/keras/layers/Softmax.md): Softmax activation function.

[`class SpatialDropout1D`](../../tf/keras/layers/SpatialDropout1D.md): Spatial 1D version of Dropout.

[`class SpatialDropout2D`](../../tf/keras/layers/SpatialDropout2D.md): Spatial 2D version of Dropout.

[`class SpatialDropout3D`](../../tf/keras/layers/SpatialDropout3D.md): Spatial 3D version of Dropout.

[`class StackedRNNCells`](../../tf/keras/layers/StackedRNNCells.md): Wrapper allowing a stack of RNN cells to behave as a single cell.

[`class Subtract`](../../tf/keras/layers/Subtract.md): Layer that subtracts two inputs.

[`class ThresholdedReLU`](../../tf/keras/layers/ThresholdedReLU.md): Thresholded Rectified Linear Unit.

[`class TimeDistributed`](../../tf/keras/layers/TimeDistributed.md): This wrapper allows to apply a layer to every temporal slice of an input.

[`class UpSampling1D`](../../tf/keras/layers/UpSampling1D.md): Upsampling layer for 1D inputs.

[`class UpSampling2D`](../../tf/keras/layers/UpSampling2D.md): Upsampling layer for 2D inputs.

[`class UpSampling3D`](../../tf/keras/layers/UpSampling3D.md): Upsampling layer for 3D inputs.

[`class Wrapper`](../../tf/keras/layers/Wrapper.md): Abstract wrapper base class.

[`class ZeroPadding1D`](../../tf/keras/layers/ZeroPadding1D.md): Zero-padding layer for 1D input (e.g. temporal sequence).

[`class ZeroPadding2D`](../../tf/keras/layers/ZeroPadding2D.md): Zero-padding layer for 2D input (e.g. picture).

[`class ZeroPadding3D`](../../tf/keras/layers/ZeroPadding3D.md): Zero-padding layer for 3D data (spatial or spatio-temporal).

## Functions

[`Input(...)`](../../tf/keras/Input.md): `Input()` is used to instantiate a Keras tensor.

[`add(...)`](../../tf/keras/layers/add.md): Functional interface to the <a href="../../tf/keras/layers/Add.md"><code>tf.keras.layers.Add</code></a> layer.

[`average(...)`](../../tf/keras/layers/average.md): Functional interface to the <a href="../../tf/keras/layers/Average.md"><code>tf.keras.layers.Average</code></a> layer.

[`concatenate(...)`](../../tf/keras/layers/concatenate.md): Functional interface to the `Concatenate` layer.

[`deserialize(...)`](../../tf/keras/layers/deserialize.md): Instantiates a layer from a config dictionary.

[`dot(...)`](../../tf/keras/layers/dot.md): Functional interface to the `Dot` layer.

[`maximum(...)`](../../tf/keras/layers/maximum.md): Functional interface to compute maximum (element-wise) list of `inputs`.

[`minimum(...)`](../../tf/keras/layers/minimum.md): Functional interface to the `Minimum` layer.

[`multiply(...)`](../../tf/keras/layers/multiply.md): Functional interface to the `Multiply` layer.

[`serialize(...)`](../../tf/keras/layers/serialize.md)

[`subtract(...)`](../../tf/keras/layers/subtract.md): Functional interface to the `Subtract` layer.

