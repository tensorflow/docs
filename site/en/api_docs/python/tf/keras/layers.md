

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.keras.layers



Defined in [`tensorflow/python/keras/layers/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/layers/__init__.py).

Keras layers API.

## Classes

[`class Activation`](../../tf/keras/layers/Activation): Applies an activation function to an output.

[`class ActivityRegularization`](../../tf/keras/layers/ActivityRegularization): Layer that applies an update to the cost function based input activity.

[`class Add`](../../tf/keras/layers/Add): Layer that adds a list of inputs.

[`class AlphaDropout`](../../tf/keras/layers/AlphaDropout): Applies Alpha Dropout to the input.

[`class Average`](../../tf/keras/layers/Average): Layer that averages a list of inputs.

[`class AveragePooling1D`](../../tf/keras/layers/AveragePooling1D): Average pooling for temporal data.

[`class AveragePooling2D`](../../tf/keras/layers/AveragePooling2D): Average pooling operation for spatial data.

[`class AveragePooling3D`](../../tf/keras/layers/AveragePooling3D): Average pooling operation for 3D data (spatial or spatio-temporal).

[`class AvgPool1D`](../../tf/keras/layers/AveragePooling1D): Average pooling for temporal data.

[`class AvgPool2D`](../../tf/keras/layers/AveragePooling2D): Average pooling operation for spatial data.

[`class AvgPool3D`](../../tf/keras/layers/AveragePooling3D): Average pooling operation for 3D data (spatial or spatio-temporal).

[`class BatchNormalization`](../../tf/keras/layers/BatchNormalization): Batch normalization layer (Ioffe and Szegedy, 2014).

[`class Bidirectional`](../../tf/keras/layers/Bidirectional): Bidirectional wrapper for RNNs.

[`class Concatenate`](../../tf/keras/layers/Concatenate): Layer that concatenates a list of inputs.

[`class Conv1D`](../../tf/keras/layers/Conv1D): 1D convolution layer (e.g. temporal convolution).

[`class Conv2D`](../../tf/keras/layers/Conv2D): 2D convolution layer (e.g. spatial convolution over images).

[`class Conv2DTranspose`](../../tf/keras/layers/Conv2DTranspose): Transposed convolution layer (sometimes called Deconvolution).

[`class Conv3D`](../../tf/keras/layers/Conv3D): 3D convolution layer (e.g. spatial convolution over volumes).

[`class Conv3DTranspose`](../../tf/keras/layers/Conv3DTranspose): Transposed convolution layer (sometimes called Deconvolution).

[`class ConvLSTM2D`](../../tf/keras/layers/ConvLSTM2D): Convolutional LSTM.

[`class Convolution1D`](../../tf/keras/layers/Conv1D): 1D convolution layer (e.g. temporal convolution).

[`class Convolution2D`](../../tf/keras/layers/Conv2D): 2D convolution layer (e.g. spatial convolution over images).

[`class Convolution2DTranspose`](../../tf/keras/layers/Conv2DTranspose): Transposed convolution layer (sometimes called Deconvolution).

[`class Convolution3D`](../../tf/keras/layers/Conv3D): 3D convolution layer (e.g. spatial convolution over volumes).

[`class Convolution3DTranspose`](../../tf/keras/layers/Conv3DTranspose): Transposed convolution layer (sometimes called Deconvolution).

[`class Cropping1D`](../../tf/keras/layers/Cropping1D): Cropping layer for 1D input (e.g. temporal sequence).

[`class Cropping2D`](../../tf/keras/layers/Cropping2D): Cropping layer for 2D input (e.g. picture).

[`class Cropping3D`](../../tf/keras/layers/Cropping3D): Cropping layer for 3D data (e.g.

[`class Dense`](../../tf/keras/layers/Dense): Just your regular densely-connected NN layer.

[`class Dot`](../../tf/keras/layers/Dot): Layer that computes a dot product between samples in two tensors.

[`class Dropout`](../../tf/keras/layers/Dropout): Applies Dropout to the input.

[`class ELU`](../../tf/keras/layers/ELU): Exponential Linear Unit.

[`class Embedding`](../../tf/keras/layers/Embedding): Turns positive integers (indexes) into dense vectors of fixed size.

[`class Flatten`](../../tf/keras/layers/Flatten): Flattens the input. Does not affect the batch size.

[`class GRU`](../../tf/keras/layers/GRU): Gated Recurrent Unit - Cho et al.

[`class GRUCell`](../../tf/keras/layers/GRUCell): Cell class for the GRU layer.

[`class GaussianDropout`](../../tf/keras/layers/GaussianDropout): Apply multiplicative 1-centered Gaussian noise.

[`class GaussianNoise`](../../tf/keras/layers/GaussianNoise): Apply additive zero-centered Gaussian noise.

[`class GlobalAveragePooling1D`](../../tf/keras/layers/GlobalAveragePooling1D): Global average pooling operation for temporal data.

[`class GlobalAveragePooling2D`](../../tf/keras/layers/GlobalAveragePooling2D): Global average pooling operation for spatial data.

[`class GlobalAveragePooling3D`](../../tf/keras/layers/GlobalAveragePooling3D): Global Average pooling operation for 3D data.

[`class GlobalAvgPool1D`](../../tf/keras/layers/GlobalAveragePooling1D): Global average pooling operation for temporal data.

[`class GlobalAvgPool2D`](../../tf/keras/layers/GlobalAveragePooling2D): Global average pooling operation for spatial data.

[`class GlobalAvgPool3D`](../../tf/keras/layers/GlobalAveragePooling3D): Global Average pooling operation for 3D data.

[`class GlobalMaxPool1D`](../../tf/keras/layers/GlobalMaxPool1D): Global max pooling operation for temporal data.

[`class GlobalMaxPool2D`](../../tf/keras/layers/GlobalMaxPool2D): Global max pooling operation for spatial data.

[`class GlobalMaxPool3D`](../../tf/keras/layers/GlobalMaxPool3D): Global Max pooling operation for 3D data.

[`class GlobalMaxPooling1D`](../../tf/keras/layers/GlobalMaxPool1D): Global max pooling operation for temporal data.

[`class GlobalMaxPooling2D`](../../tf/keras/layers/GlobalMaxPool2D): Global max pooling operation for spatial data.

[`class GlobalMaxPooling3D`](../../tf/keras/layers/GlobalMaxPool3D): Global Max pooling operation for 3D data.

[`class InputLayer`](../../tf/keras/layers/InputLayer): Layer to be used as an entry point into a Network (a graph of layers).

[`class InputSpec`](../../tf/layers/InputSpec): Specifies the ndim, dtype and shape of every input to a layer.

[`class LSTM`](../../tf/keras/layers/LSTM): Long-Short Term Memory layer - Hochreiter 1997.

[`class LSTMCell`](../../tf/keras/layers/LSTMCell): Cell class for the LSTM layer.

[`class Lambda`](../../tf/keras/layers/Lambda): Wraps arbitrary expression as a `Layer` object.

[`class Layer`](../../tf/keras/layers/Layer): Abstract base layer class.

[`class LeakyReLU`](../../tf/keras/layers/LeakyReLU): Leaky version of a Rectified Linear Unit.

[`class LocallyConnected1D`](../../tf/keras/layers/LocallyConnected1D): Locally-connected layer for 1D inputs.

[`class LocallyConnected2D`](../../tf/keras/layers/LocallyConnected2D): Locally-connected layer for 2D inputs.

[`class Masking`](../../tf/keras/layers/Masking): Masks a sequence by using a mask value to skip timesteps.

[`class MaxPool1D`](../../tf/keras/layers/MaxPool1D): Max pooling operation for temporal data.

[`class MaxPool2D`](../../tf/keras/layers/MaxPool2D): Max pooling operation for spatial data.

[`class MaxPool3D`](../../tf/keras/layers/MaxPool3D): Max pooling operation for 3D data (spatial or spatio-temporal).

[`class MaxPooling1D`](../../tf/keras/layers/MaxPool1D): Max pooling operation for temporal data.

[`class MaxPooling2D`](../../tf/keras/layers/MaxPool2D): Max pooling operation for spatial data.

[`class MaxPooling3D`](../../tf/keras/layers/MaxPool3D): Max pooling operation for 3D data (spatial or spatio-temporal).

[`class Maximum`](../../tf/keras/layers/Maximum): Layer that computes the maximum (element-wise) a list of inputs.

[`class Multiply`](../../tf/keras/layers/Multiply): Layer that multiplies (element-wise) a list of inputs.

[`class PReLU`](../../tf/keras/layers/PReLU): Parametric Rectified Linear Unit.

[`class Permute`](../../tf/keras/layers/Permute): Permutes the dimensions of the input according to a given pattern.

[`class RNN`](../../tf/keras/layers/RNN): Base class for recurrent layers.

[`class RepeatVector`](../../tf/keras/layers/RepeatVector): Repeats the input n times.

[`class Reshape`](../../tf/keras/layers/Reshape): Reshapes an output to a certain shape.

[`class SeparableConv1D`](../../tf/keras/layers/SeparableConv1D): Depthwise separable 1D convolution.

[`class SeparableConv2D`](../../tf/keras/layers/SeparableConv2D): Depthwise separable 2D convolution.

[`class SeparableConvolution1D`](../../tf/keras/layers/SeparableConv1D): Depthwise separable 1D convolution.

[`class SeparableConvolution2D`](../../tf/keras/layers/SeparableConv2D): Depthwise separable 2D convolution.

[`class SimpleRNN`](../../tf/keras/layers/SimpleRNN): Fully-connected RNN where the output is to be fed back to input.

[`class SimpleRNNCell`](../../tf/keras/layers/SimpleRNNCell): Cell class for SimpleRNN.

[`class Softmax`](../../tf/keras/layers/Softmax): Softmax activation function.

[`class SpatialDropout1D`](../../tf/keras/layers/SpatialDropout1D): Spatial 1D version of Dropout.

[`class SpatialDropout2D`](../../tf/keras/layers/SpatialDropout2D): Spatial 2D version of Dropout.

[`class SpatialDropout3D`](../../tf/keras/layers/SpatialDropout3D): Spatial 3D version of Dropout.

[`class StackedRNNCells`](../../tf/keras/layers/StackedRNNCells): Wrapper allowing a stack of RNN cells to behave as a single cell.

[`class ThresholdedReLU`](../../tf/keras/layers/ThresholdedReLU): Thresholded Rectified Linear Unit.

[`class TimeDistributed`](../../tf/keras/layers/TimeDistributed): This wrapper allows to apply a layer to every temporal slice of an input.

[`class UpSampling1D`](../../tf/keras/layers/UpSampling1D): Upsampling layer for 1D inputs.

[`class UpSampling2D`](../../tf/keras/layers/UpSampling2D): Upsampling layer for 2D inputs.

[`class UpSampling3D`](../../tf/keras/layers/UpSampling3D): Upsampling layer for 3D inputs.

[`class Wrapper`](../../tf/keras/layers/Wrapper): Abstract wrapper base class.

[`class ZeroPadding1D`](../../tf/keras/layers/ZeroPadding1D): Zero-padding layer for 1D input (e.g. temporal sequence).

[`class ZeroPadding2D`](../../tf/keras/layers/ZeroPadding2D): Zero-padding layer for 2D input (e.g. picture).

[`class ZeroPadding3D`](../../tf/keras/layers/ZeroPadding3D): Zero-padding layer for 3D data (spatial or spatio-temporal).

## Functions

[`Input(...)`](../../tf/keras/Input): `Input()` is used to instantiate a Keras tensor.

[`add(...)`](../../tf/keras/layers/add): Functional interface to the `Add` layer.

[`average(...)`](../../tf/keras/layers/average): Functional interface to the `Average` layer.

[`concatenate(...)`](../../tf/keras/layers/concatenate): Functional interface to the `Concatenate` layer.

[`dot(...)`](../../tf/keras/layers/dot): Functional interface to the `Dot` layer.

[`maximum(...)`](../../tf/keras/layers/maximum): Functional interface to the `Maximum` layer.

[`multiply(...)`](../../tf/keras/layers/multiply): Functional interface to the `Multiply` layer.

