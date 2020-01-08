page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.DNNRegressorWithLayerAnnotations

``` python
tf.contrib.estimator.DNNRegressorWithLayerAnnotations(
    hidden_units,
    feature_columns,
    model_dir=None,
    label_dimension=1,
    weight_column=None,
    optimizer='Adagrad',
    activation_fn=tf.nn.relu,
    dropout=None,
    input_layer_partitioner=None,
    config=None,
    warm_start_from=None,
    loss_reduction=losses.Reduction.SUM
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/dnn_with_layer_annotations.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/estimator/python/estimator/dnn_with_layer_annotations.py).

A regressor for TensorFlow DNN models with layer annotations.

This regressor is fuctionally identical to estimator.DNNRegressor as far as
training and evaluating models is concerned. The key difference is that this
classifier adds additional layer annotations, which can be used for computing
Integrated Gradients.

Integrated Gradients is a method for attributing a classifier's predictions
to its input features (https://arxiv.org/pdf/1703.01365.pdf). Given an input
instance, the method assigns attribution scores to individual features in
proportion to the feature's importance to the classifier's prediction.

See estimator.DNNRegressor for example code for training and evaluating models
using this regressor.

This regressor is checkpoint-compatible with estimator.DNNRegressor and
therefore the following should work seamlessly:

# Instantiate ordinary estimator as usual.
estimator = tf.estimator.DNNRegressor(
  config, feature_columns, hidden_units, ...)

# Train estimator, export checkpoint.
tf.estimator.train_and_evaluate(estimator, ...)

# Instantiate estimator with annotations with the same configuration as the
# ordinary estimator.
estimator_with_annotations = (
  tf.contrib.estimator.DNNRegressorWithLayerAnnotations(
    config, feature_columns, hidden_units, ...))

# Call export_savedmodel with the same arguments as the ordinary estimator,
# using the checkpoint produced for the ordinary estimator.
estimator_with_annotations.export_saved_model(
  export_dir_base, serving_input_receiver, ...
  checkpoint_path='/path/to/ordinary/estimator/checkpoint/model.ckpt-1234')

#### Args:

* <b>`hidden_units`</b>: Iterable of number hidden units per layer. All layers are
    fully connected. Ex. `[64, 32]` means first layer has 64 nodes and second
    one has 32.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by the
    model. All items in the set should be instances of classes derived from
    `_FeatureColumn`.
* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can also
    be used to load checkpoints from the directory into a estimator to
    continue training a previously saved model.
* <b>`label_dimension`</b>: Number of regression targets per example. This is the size
    of the last dimension of the labels and logits `Tensor` objects
    (typically, these have shape `[batch_size, label_dimension]`).
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    <a href="../../../tf/feature_column/numeric_column"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example. If it is a string, it is
    used as a key to fetch weight tensor from the `features`. If it is a
    `_NumericColumn`, raw tensor is fetched by key `weight_column.key`, then
    weight_column.normalizer_fn is applied on it to get weight tensor.
* <b>`optimizer`</b>: An instance of `tf.Optimizer` used to train the model. Defaults
    to Adagrad optimizer.
* <b>`activation_fn`</b>: Activation function applied to each layer. If `None`, will
    use <a href="../../../tf/nn/relu"><code>tf.nn.relu</code></a>.
* <b>`dropout`</b>: When not `None`, the probability we will drop out a given
    coordinate.
* <b>`input_layer_partitioner`</b>: Optional. Partitioner for input layer. Defaults to
    `min_max_variable_partitioner` with `min_slice_size` 64 << 20.
* <b>`config`</b>: `RunConfig` object to configure the runtime settings.
* <b>`warm_start_from`</b>: A string filepath to a checkpoint to warm-start from, or a
    `WarmStartSettings` object to fully configure warm-starting.  If the
    string filepath is provided instead of a `WarmStartSettings`, then all
    weights are warm-started, and it is assumed that vocabularies and Tensor
    names are unchanged.
* <b>`loss_reduction`</b>: One of <a href="../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> except `NONE`. Describes how to
    reduce training loss over batch. Defaults to `SUM`.


#### Returns:

DNNRegressor with layer annotations.