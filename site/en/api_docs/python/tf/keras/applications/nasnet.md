description: NASNet-A models for Keras.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.applications.nasnet" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.keras.applications.nasnet

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



NASNet-A models for Keras.


NASNet refers to Neural Architecture Search Network, a family of models
that were designed automatically by learning the model architectures
directly on the dataset of interest.

Here we consider NASNet-A, the highest performance model that was found
for the CIFAR-10 dataset, and then extended to ImageNet 2012 dataset,
obtaining state of the art performance on CIFAR-10 and ImageNet 2012.
Only the NASNet-A models, and their respective weights, which are suited
for ImageNet 2012 are provided.

The below table describes the performance on ImageNet 2012:
--------------------------------------------------------------------------------
      Architecture       | Top-1 Acc | Top-5 Acc |  Multiply-Adds |  Params (M)
--------------------------------------------------------------------------------
|   NASNet-A (4 @ 1056)  |   74.0 %  |   91.6 %  |       564 M    |     5.3    |
|   NASNet-A (6 @ 4032)  |   82.7 %  |   96.2 %  |      23.8 B    |    88.9    |
--------------------------------------------------------------------------------

#### Reference paper:

- [Learning Transferable Architectures for Scalable Image Recognition]
  (https://arxiv.org/abs/1707.07012) (CVPR 2018)


## Functions

[`NASNetLarge(...)`](../../../tf/keras/applications/NASNetLarge.md): Instantiates a NASNet model in ImageNet mode.

[`NASNetMobile(...)`](../../../tf/keras/applications/NASNetMobile.md): Instantiates a Mobile NASNet model in ImageNet mode.

[`decode_predictions(...)`](../../../tf/keras/applications/nasnet/decode_predictions.md): Decodes the prediction of an ImageNet model.

[`preprocess_input(...)`](../../../tf/keras/applications/nasnet/preprocess_input.md): Preprocesses a tensor or Numpy array encoding a batch of images.

