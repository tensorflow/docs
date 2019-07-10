page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.estimator.TPUGANEstimator

## Class `TPUGANEstimator`

An estimator for Generative Adversarial Networks (GANs) on TPU.

Inherits From: [`TPUEstimator`](../../../../tf/estimator/tpu/TPUEstimator)

### Aliases:

* Class `tf.contrib.gan.estimator.TPUGANEstimator`
* Class `tf.contrib.gan.estimator.tpu_gan_estimator.TPUGANEstimator`



Defined in [`contrib/gan/python/estimator/python/tpu_gan_estimator_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/estimator/python/tpu_gan_estimator_impl.py).

<!-- Placeholder for "Used in" -->

This Estimator is backed by TFGAN. It is similar to `tfgan.GANEstimator`,
but works on TPU.

#### Example:



```python
    import tensorflow as tf
    tfgan = tf.contrib.gan

    # See TFGAN's `train.py` for a description of the generator and
    # discriminator API.
    def generator_fn(generator_inputs):
      ...
      return generated_data

    def discriminator_fn(data, conditioning):
      ...
      return logits

    # Create GAN estimator.
    config = tpu_config.RunConfig(model_dir='/my/dir')
    gan_estimator = tfgan.estimator.TPUGANEstimator(
        generator_fn=generator_fn,
        discriminator_fn=discriminator_fn,
        generator_loss_fn=tfgan.losses.wasserstein_generator_loss,
        discriminator_loss_fn=tfgan.losses.wasserstein_discriminator_loss,
        generator_optimizer=tf.compat.v1.train.AdamOptimizer(0.1, 0.5),
        discriminator_optimizer=tf.compat.v1.train.AdamOptimizer(0.1, 0.5),
        train_batch_size=4,
        config=config)

    # Train estimator.
    gan_estimator.train(train_input_fn, train_steps)

    # Evaluate resulting estimator.
    gan_estimator.evaluate(eval_input_fn, eval_steps)

    # Generate samples from generator.
    predictions = np.array([
        x['generated_data'] for x in gan_estimator.predict(predict_input_fn)])
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    generator_fn=None,
    discriminator_fn=None,
    generator_loss_fn=None,
    discriminator_loss_fn=None,
    generator_optimizer=None,
    discriminator_optimizer=None,
    get_eval_metric_ops_fn=None,
    add_summaries=None,
    joint_train=False,
    gan_train_steps=tfgan_tuples.GANTrainSteps(1, 1),
    model_dir=None,
    config=None,
    params=None,
    use_tpu=True,
    train_batch_size=None,
    eval_batch_size=None,
    predict_batch_size=None,
    batch_axis=None,
    eval_on_tpu=True,
    export_to_tpu=True,
    warm_start_from=None
)
```

Initializes a TPUGANEstimator instance.


#### Args:


* <b>`generator_fn`</b>: A python function that takes a Tensor, Tensor list, or
  Tensor dictionary as inputs and returns the outputs of the GAN
  generator. See `TFGAN` for more details and examples. Additionally, if
  it has an argument called `mode`, the Estimator's `mode` will be passed
  in (ex TRAIN, EVAL, PREDICT). This is useful for things like batch
  normalization.
* <b>`discriminator_fn`</b>: A python function that takes the output of
  `generator_fn` or real data in the GAN setup, and `generator_inputs`.
  Outputs a Tensor in the range [-inf, inf]. See `TFGAN` for more details
  and examples.
* <b>`generator_loss_fn`</b>: The loss function on the generator. Takes a `GANModel`
  tuple.
* <b>`discriminator_loss_fn`</b>: The loss function on the discriminator. Takes a
  `GANModel` tuple.
* <b>`generator_optimizer`</b>: The optimizer for generator updates, or a function
  that takes no arguments and returns an optimizer. This function will
  be called when the default graph is the `GANEstimator`'s graph, so
  utilities like <a href="../../../../tf/contrib/framework/get_or_create_global_step"><code>tf.contrib.framework.get_or_create_global_step</code></a> will
  work.
* <b>`discriminator_optimizer`</b>: Same as `generator_optimizer`, but for the
  discriminator updates.
* <b>`get_eval_metric_ops_fn`</b>: A function that takes a list of arguments and
  returns a dict of metric results keyed by name. The output of this
  function is passed into <a href="../../../../tf/estimator/EstimatorSpec"><code>tf.estimator.EstimatorSpec</code></a> during evaluation.
  The arguments must be:
      * generator_inputs
      * generated_data
      * real_data
      * discriminator_real_outputs
      * discriminator_gen_outputs
* <b>`add_summaries`</b>: `None`, a single `SummaryType`, or a list of `SummaryType`.
  This is ignored for jobs that run on TPU, such as the train job if
  `use_tpu` is `True` or the eval job if `eval_on_tpu` is `True`.
* <b>`joint_train`</b>: A Python boolean. If `True`, jointly train the generator and
  the discriminator. If `False`, sequentially train them. See `train.py`
  in TFGAN for more details on the differences between the two GAN
  training methods.
* <b>`gan_train_steps`</b>: A `tfgan.GANTrainSteps` named tuple describing the ratio
  of generator to discriminator steps. For now, only supports 1:1
  training.
* <b>`model_dir`</b>: Same as `TPUEstimator`: Directory to save model parameters,
  graph and etc. This can also be used to load checkpoints from the
  directory into a estimator to continue training a previously saved
  model. If `None`, the model_dir in `config` will be used if set. If both
  are set, they must be same. If both are `None`, a temporary directory
  will be used.
* <b>`config`</b>: Same as `TPUEstimator`: An `tpu_config.RunConfig` configuration
  object. Cannot be `None`.
* <b>`params`</b>: Same as `TPUEstimator`: An optional `dict` of hyper parameters
  that will be passed into `input_fn` and `model_fn`.  Keys are names of
  parameters, values are basic python types. There are reserved keys for
  `TPUEstimator`, including 'batch_size'.
* <b>`use_tpu`</b>: Same as `TPUEstimator`: A bool indicating whether TPU support is
  enabled. Currently, TPU training and evaluation respect this bit, but
  eval_on_tpu can override execution of eval. See below. Predict still
  happens on CPU.
* <b>`train_batch_size`</b>: Same as `TPUEstimator`: An int representing the global
  training batch size. TPUEstimator transforms this global batch size to a
  per-shard batch size, as params['batch_size'], when calling `input_fn`
  and `model_fn`. Cannot be `None` if `use_tpu` is `True`. Must be
  divisible by total number of replicas.
* <b>`eval_batch_size`</b>: Same as `TPUEstimator`: An int representing evaluation
  batch size. Must be divisible by total number of replicas.
* <b>`predict_batch_size`</b>: Same as `TPUEstimator`: An int representing the
  prediction batch size. Must be divisible by total number of replicas.
* <b>`batch_axis`</b>: Same as `TPUEstimator`: A python tuple of int values
  describing how each tensor produced by the Estimator `input_fn` should
  be split across the TPU compute shards. For example, if your input_fn
  produced (images, labels) where the images tensor is in `HWCN` format,
  your shard dimensions would be [3, 0], where 3 corresponds to the `N`
  dimension of your images Tensor, and 0 corresponds to the dimension
  along which to split the labels to match up with the corresponding
  images. If None is supplied, and per_host_input_for_training is True,
  batches will be sharded based on the major dimension. If
  tpu_config.per_host_input_for_training is False or `PER_HOST_V2`,
  batch_axis is ignored.
* <b>`eval_on_tpu`</b>: Same as `TPUEstimator`: If False, evaluation runs on CPU or
  GPU. In this case, the model_fn must return `EstimatorSpec` when called
  with `mode` as `EVAL`.
* <b>`export_to_tpu`</b>: Same as `TPUEstimator`: If True, `export_savedmodel()`
  exports a metagraph for serving on TPU besides the one on CPU.
* <b>`warm_start_from`</b>: Same as `TPUEstimator`: Optional string filepath to a
  checkpoint or SavedModel to warm-start from, or a
  <a href="../../../../tf/estimator/WarmStartSettings"><code>tf.estimator.WarmStartSettings</code></a> object to fully configure
  warm-starting.  If the string filepath is provided instead of a
  `WarmStartSettings`, then all variables are warm-started, and it is
  assumed that vocabularies and Tensor names are unchanged.


#### Raises:


* <b>`ValueError`</b>: If loss functions aren't callable.
* <b>`ValueError`</b>: If `gan_train_steps` isn't a `tfgan_tuples.GANTrainSteps`
  tuple.
* <b>`ValueError`</b>: If `gan_train_steps` isn't 1:1 training.



## Properties

<h3 id="config"><code>config</code></h3>




<h3 id="model_dir"><code>model_dir</code></h3>




<h3 id="model_fn"><code>model_fn</code></h3>

Returns the `model_fn` which is bound to `self.params`.


#### Returns:

The `model_fn` with following signature:
  `def model_fn(features, labels, mode, config)`


<h3 id="params"><code>params</code></h3>






## Methods

<h3 id="eval_dir"><code>eval_dir</code></h3>

``` python
eval_dir(name=None)
```

Shows the directory name where evaluation metrics are dumped.


#### Args:


* <b>`name`</b>: Name of the evaluation if user needs to run multiple evaluations on
  different data sets, such as on training data vs test data. Metrics for
  different evaluations are saved in separate folders, and appear
  separately in tensorboard.


#### Returns:

A string which is the path of directory contains evaluation metrics.


<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(
    input_fn,
    steps=None,
    hooks=None,
    checkpoint_path=None,
    name=None
)
```




<h3 id="experimental_export_all_saved_models"><code>experimental_export_all_saved_models</code></h3>

``` python
experimental_export_all_saved_models(
    export_dir_base,
    input_receiver_fn_map,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None
)
```

Exports a `SavedModel` with `tf.MetaGraphDefs` for each requested mode.

For each mode passed in via the `input_receiver_fn_map`,
this method builds a new graph by calling the `input_receiver_fn` to obtain
feature and label `Tensor`s. Next, this method calls the `Estimator`'s
`model_fn` in the passed mode to generate the model graph based on
those features and labels, and restores the given checkpoint
(or, lacking that, the most recent checkpoint) into the graph.
Only one of the modes is used for saving variables to the `SavedModel`
(order of preference: <a href="../../../../tf/estimator/ModeKeys#TRAIN"><code>tf.estimator.ModeKeys.TRAIN</code></a>,
<a href="../../../../tf/estimator/ModeKeys#EVAL"><code>tf.estimator.ModeKeys.EVAL</code></a>, then
<a href="../../../../tf/estimator/ModeKeys#PREDICT"><code>tf.estimator.ModeKeys.PREDICT</code></a>), such that up to three
`tf.MetaGraphDefs` are saved with a single set of variables in a single
`SavedModel` directory.

For the variables and `tf.MetaGraphDefs`, a timestamped export directory
below
`export_dir_base`, and writes a `SavedModel` into it containing
the <a href="../../../../tf/MetaGraphDef"><code>tf.MetaGraphDef</code></a> for the given mode and its associated signatures.

For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
for each element of the `export_outputs` dict returned from the `model_fn`,
named using the same keys.  One of these keys is always
<a href="../../../../tf/saved_model/signature_constants#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

For training and evaluation, the `train_op` is stored in an extra
collection,
and loss, metrics, and predictions are included in a `SignatureDef` for the
mode in question.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`input_receiver_fn_map`</b>: dict of <a href="../../../../tf/estimator/ModeKeys"><code>tf.estimator.ModeKeys</code></a> to
  `input_receiver_fn` mappings, where the `input_receiver_fn` is a
  function that takes no arguments and returns the appropriate subclass of
  `InputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if any `input_receiver_fn` is `None`, no `export_outputs`
  are provided, or no checkpoint can be found.

<h3 id="export_saved_model"><code>export_saved_model</code></h3>

``` python
export_saved_model(
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    experimental_mode=ModeKeys.PREDICT
)
```

Exports inference graph as a `SavedModel` into the given dir.

For a detailed guide, see
[Using SavedModel with Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single <a href="../../../../tf/MetaGraphDef"><code>tf.MetaGraphDef</code></a> saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
<a href="../../../../tf/saved_model/signature_constants#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

The experimental_mode parameter can be used to export a single
train/eval/predict graph as a `SavedModel`.
See `experimental_export_all_saved_models` for full docs.

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and returns a
  <a href="../../../../tf/estimator/export/ServingInputReceiver"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../../tf/estimator/export/TensorServingInputReceiver"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.
* <b>`experimental_mode`</b>: <a href="../../../../tf/estimator/ModeKeys"><code>tf.estimator.ModeKeys</code></a> value indicating with mode
  will be exported. Note that this feature is experimental.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.

<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>

``` python
export_savedmodel(
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    strip_default_attrs=False
)
```

Exports inference graph as a `SavedModel` into the given dir. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function has been renamed, use `export_saved_model` instead.

For a detailed guide, see
[Using SavedModel with Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single <a href="../../../../tf/MetaGraphDef"><code>tf.MetaGraphDef</code></a> saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
<a href="../../../../tf/saved_model/signature_constants#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and returns a
  <a href="../../../../tf/estimator/export/ServingInputReceiver"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../../tf/estimator/export/TensorServingInputReceiver"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
  removed from the `NodeDef`s. For a detailed guide, see [Stripping
  Default-Valued Attributes](
  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.

<h3 id="get_variable_names"><code>get_variable_names</code></h3>

``` python
get_variable_names()
```

Returns list of all variable names in this model.


#### Returns:

List of names.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="get_variable_value"><code>get_variable_value</code></h3>

``` python
get_variable_value(name)
```

Returns value of the variable given by name.


#### Args:


* <b>`name`</b>: string or a list of string, name of the tensor.


#### Returns:

Numpy array - value of the tensor.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

``` python
latest_checkpoint()
```

Finds the filename of the latest saved checkpoint file in `model_dir`.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was
found.


<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    input_fn,
    predict_keys=None,
    hooks=None,
    checkpoint_path=None,
    yield_single_examples=True
)
```




<h3 id="train"><code>train</code></h3>

``` python
train(
    input_fn,
    hooks=None,
    steps=None,
    max_steps=None,
    saving_listeners=None
)
```






