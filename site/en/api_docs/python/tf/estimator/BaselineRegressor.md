description: A regressor that can establish a simple baseline.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.BaselineRegressor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="eval_dir"/>
<meta itemprop="property" content="evaluate"/>
<meta itemprop="property" content="experimental_export_all_saved_models"/>
<meta itemprop="property" content="export_saved_model"/>
<meta itemprop="property" content="get_variable_names"/>
<meta itemprop="property" content="get_variable_value"/>
<meta itemprop="property" content="latest_checkpoint"/>
<meta itemprop="property" content="predict"/>
<meta itemprop="property" content="train"/>
</div>

# tf.estimator.BaselineRegressor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/baseline.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A regressor that can establish a simple baseline.

Inherits From: [`Estimator`](../../tf/estimator/Estimator.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.BaselineRegressor(
    model_dir=None, label_dimension=1, weight_column=None, optimizer='Ftrl',
    config=None, loss_reduction=losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE
)
</code></pre>



<!-- Placeholder for "Used in" -->

This regressor ignores feature values and will learn to predict the average
value of each label.

#### Example:



```python

# Build BaselineRegressor
regressor = tf.estimator.BaselineRegressor()

# Input builders
def input_fn_train:
  # Returns tf.data.Dataset of (x, y) tuple where y represents label's class
  # index.
  pass

def input_fn_eval:
  # Returns tf.data.Dataset of (x, y) tuple where y represents label's class
  # index.
  pass

# Fit model.
regressor.train(input_fn=input_fn_train)

# Evaluate squared-loss between the test and train targets.
loss = regressor.evaluate(input_fn=input_fn_eval)["loss"]

# predict outputs the mean value seen during training.
predictions = regressor.predict(new_samples)
```

Input of `train` and `evaluate` should have following features,
  otherwise there will be a `KeyError`:

* if `weight_column` is not `None`, a feature with
   `key=weight_column` whose value is a `Tensor`.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`model_dir`
</td>
<td>
Directory to save model parameters, graph and etc. This can
also be used to load checkpoints from the directory into a estimator to
continue training a previously saved model.
</td>
</tr><tr>
<td>
`label_dimension`
</td>
<td>
Number of regression targets per example. This is the
size of the last dimension of the labels and logits `Tensor` objects
(typically, these have shape `[batch_size, label_dimension]`).
</td>
</tr><tr>
<td>
`weight_column`
</td>
<td>
A string or a `_NumericColumn` created by
<a href="../../tf/feature_column/numeric_column.md"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
weights. It will be multiplied by the loss of the example.
</td>
</tr><tr>
<td>
`optimizer`
</td>
<td>
String, `tf.keras.optimizers.*` object, or callable that
creates the optimizer to use for training. If not specified, will use
`Ftrl` as the default optimizer.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
`RunConfig` object to configure the runtime settings.
</td>
</tr><tr>
<td>
`loss_reduction`
</td>
<td>
One of <a href="../../tf/keras/losses/Reduction.md"><code>tf.losses.Reduction</code></a> except `NONE`. Describes how
to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.
</td>
</tr>
</table>



#### Eager Compatibility
Estimators can be used while eager execution is enabled. Note that `input_fn`
and all hooks are executed inside a graph context, so they have to be written
to be compatible with graph mode. Note that `input_fn` code using <a href="../../tf/data.md"><code>tf.data</code></a>
generally works in both graph and eager modes.





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`config`
</td>
<td>

</td>
</tr><tr>
<td>
`export_savedmodel`
</td>
<td>

</td>
</tr><tr>
<td>
`model_dir`
</td>
<td>

</td>
</tr><tr>
<td>
`model_fn`
</td>
<td>
Returns the `model_fn` which is bound to `self.params`.
</td>
</tr><tr>
<td>
`params`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="eval_dir"><code>eval_dir</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>eval_dir(
    name=None
)
</code></pre>

Shows the directory name where evaluation metrics are dumped.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Name of the evaluation if user needs to run multiple evaluations on
different data sets, such as on training data vs test data. Metrics for
different evaluations are saved in separate folders, and appear
separately in tensorboard.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A string which is the path of directory contains evaluation metrics.
</td>
</tr>

</table>



<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>evaluate(
    input_fn, steps=None, hooks=None, checkpoint_path=None, name=None
)
</code></pre>

Evaluates the model given evaluation data `input_fn`.

For each step, calls `input_fn`, which returns one batch of data.
Evaluates until:
- `steps` batches are processed, or
- `input_fn` raises an end-of-input exception (<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>
or
`StopIteration`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that constructs the input data for evaluation. See
[Premade Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The
function should construct and return one of the following:  * A
<a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a tuple
`(features, labels)` with same constraints as below. * A tuple
`(features, labels)`: Where `features` is a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or a dictionary
of string feature name to `Tensor` and `labels` is a `Tensor` or a
dictionary of string label name to `Tensor`. Both `features` and
`labels` are consumed by `model_fn`. They should satisfy the
expectation of `model_fn` from inputs.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Number of steps for which to evaluate model. If `None`, evaluates
until `input_fn` raises an end-of-input exception.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
List of `tf.train.SessionRunHook` subclass instances. Used for
callbacks inside the evaluation call.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
Path of a specific checkpoint to evaluate. If `None`, the
latest checkpoint in `model_dir` is used.  If there are no checkpoints
in `model_dir`, evaluation is run with newly initialized `Variables`
instead of ones restored from checkpoint.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name of the evaluation if user needs to run multiple evaluations on
different data sets, such as on training data vs test data. Metrics for
different evaluations are saved in separate folders, and appear
separately in tensorboard.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict containing the evaluation metrics specified in `model_fn` keyed by
name, as well as an entry `global_step` which contains the value of the
global step for which this evaluation was performed. For canned
estimators, the dict contains the `loss` (mean loss per mini-batch) and
the `average_loss` (mean loss per sample). Canned classifiers also return
the `accuracy`. Canned regressors also return the `label/mean` and the
`prediction/mean`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `steps <= 0`.
</td>
</tr>
</table>



<h3 id="experimental_export_all_saved_models"><code>experimental_export_all_saved_models</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_export_all_saved_models(
    export_dir_base, input_receiver_fn_map, assets_extra=None, as_text=(False),
    checkpoint_path=None
)
</code></pre>

Exports a `SavedModel` with `tf.MetaGraphDefs` for each requested mode.

For each mode passed in via the `input_receiver_fn_map`,
this method builds a new graph by calling the `input_receiver_fn` to obtain
feature and label `Tensor`s. Next, this method calls the `Estimator`'s
`model_fn` in the passed mode to generate the model graph based on
those features and labels, and restores the given checkpoint
(or, lacking that, the most recent checkpoint) into the graph.
Only one of the modes is used for saving variables to the `SavedModel`
(order of preference: <a href="../../tf/estimator/ModeKeys.md#TRAIN"><code>tf.estimator.ModeKeys.TRAIN</code></a>,
<a href="../../tf/estimator/ModeKeys.md#EVAL"><code>tf.estimator.ModeKeys.EVAL</code></a>, then
<a href="../../tf/estimator/ModeKeys.md#PREDICT"><code>tf.estimator.ModeKeys.PREDICT</code></a>), such that up to three
`tf.MetaGraphDefs` are saved with a single set of variables in a single
`SavedModel` directory.

For the variables and `tf.MetaGraphDefs`, a timestamped export directory
below
`export_dir_base`, and writes a `SavedModel` into it containing
the `tf.MetaGraphDef` for the given mode and its associated signatures.

For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
for each element of the `export_outputs` dict returned from the `model_fn`,
named using the same keys.  One of these keys is always
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_dir_base`
</td>
<td>
A string containing a directory in which to create
timestamped subdirectories containing exported `SavedModel`s.
</td>
</tr><tr>
<td>
`input_receiver_fn_map`
</td>
<td>
dict of <a href="../../tf/estimator/ModeKeys.md"><code>tf.estimator.ModeKeys</code></a> to
`input_receiver_fn` mappings, where the `input_receiver_fn` is a
function that takes no arguments and returns the appropriate subclass of
`InputReceiver`.
</td>
</tr><tr>
<td>
`assets_extra`
</td>
<td>
A dict specifying how to populate the assets.extra directory
within the exported `SavedModel`, or `None` if no extra assets are
needed.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
whether to write the `SavedModel` proto in text format.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.  If `None` (the default),
the most recent checkpoint found within the model directory is chosen.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to the exported directory as a bytes object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if any `input_receiver_fn` is `None`, no `export_outputs`
are provided, or no checkpoint can be found.
</td>
</tr>
</table>



<h3 id="export_saved_model"><code>export_saved_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>export_saved_model(
    export_dir_base, serving_input_receiver_fn, assets_extra=None, as_text=(False),
    checkpoint_path=None, experimental_mode=ModeKeys.PREDICT
)
</code></pre>

Exports inference graph as a `SavedModel` into the given dir.

For a detailed guide, see
[Using SavedModel with
Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single `tf.MetaGraphDef` saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_dir_base`
</td>
<td>
A string containing a directory in which to create
timestamped subdirectories containing exported `SavedModel`s.
</td>
</tr><tr>
<td>
`serving_input_receiver_fn`
</td>
<td>
A function that takes no argument and returns a
<a href="../../tf/estimator/export/ServingInputReceiver.md"><code>tf.estimator.export.ServingInputReceiver</code></a> or
<a href="../../tf/estimator/export/TensorServingInputReceiver.md"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
</td>
</tr><tr>
<td>
`assets_extra`
</td>
<td>
A dict specifying how to populate the assets.extra directory
within the exported `SavedModel`, or `None` if no extra assets are
needed.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
whether to write the `SavedModel` proto in text format.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.  If `None` (the default),
the most recent checkpoint found within the model directory is chosen.
</td>
</tr><tr>
<td>
`experimental_mode`
</td>
<td>
<a href="../../tf/estimator/ModeKeys.md"><code>tf.estimator.ModeKeys</code></a> value indicating with mode will
be exported. Note that this feature is experimental.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to the exported directory as a bytes object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.
</td>
</tr>
</table>



<h3 id="get_variable_names"><code>get_variable_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_variable_names()
</code></pre>

Returns list of all variable names in this model.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
List of names.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the `Estimator` has not produced a checkpoint yet.
</td>
</tr>
</table>



<h3 id="get_variable_value"><code>get_variable_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_variable_value(
    name
)
</code></pre>

Returns value of the variable given by name.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
string or a list of string, name of the tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Numpy array - value of the tensor.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the `Estimator` has not produced a checkpoint yet.
</td>
</tr>
</table>



<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>latest_checkpoint()
</code></pre>

Finds the filename of the latest saved checkpoint file in `model_dir`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The full path to the latest checkpoint or `None` if no checkpoint was
found.
</td>
</tr>

</table>



<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict(
    input_fn, predict_keys=None, hooks=None, checkpoint_path=None,
    yield_single_examples=(True)
)
</code></pre>

Yields predictions for given features.

Please note that interleaving two predict outputs does not work. See:
[issue/20506](
https://github.com/tensorflow/tensorflow/issues/20506#issuecomment-422208517)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that constructs the features. Prediction continues
until `input_fn` raises an end-of-input exception
(<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> or `StopIteration`). See [Premade
Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The function should construct and return one of
the following:
* <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object -- Outputs of `Dataset` object must have
same constraints as below.
* features -- A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or a dictionary of string feature name to
`Tensor`. features are consumed by `model_fn`. They should satisfy
the expectation of `model_fn` from inputs. * A tuple, in which case
the first item is extracted as features.
</td>
</tr><tr>
<td>
`predict_keys`
</td>
<td>
list of `str`, name of the keys to predict. It is used if
the <a href="../../tf/estimator/EstimatorSpec.md#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is a `dict`. If
`predict_keys` is used then rest of the predictions will be filtered
from the dictionary. If `None`, returns all.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
List of `tf.train.SessionRunHook` subclass instances. Used for
callbacks inside the prediction call.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
Path of a specific checkpoint to predict. If `None`, the
latest checkpoint in `model_dir` is used.  If there are no checkpoints
in `model_dir`, prediction is run with newly initialized `Variables`
instead of ones restored from checkpoint.
</td>
</tr><tr>
<td>
`yield_single_examples`
</td>
<td>
If `False`, yields the whole batch as returned by
the `model_fn` instead of decomposing the batch into individual
elements. This is useful if `model_fn` returns some tensors whose first
dimension is not equal to the batch size.
</td>
</tr>
</table>



#### Yields:

Evaluated values of `predictions` tensors.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If batch length of predictions is not the same and
`yield_single_examples` is `True`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If there is a conflict between `predict_keys` and
`predictions`. For example if `predict_keys` is not `None` but
<a href="../../tf/estimator/EstimatorSpec.md#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is not a `dict`.
</td>
</tr>
</table>



<h3 id="train"><code>train</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>train(
    input_fn, hooks=None, steps=None, max_steps=None, saving_listeners=None
)
</code></pre>

Trains a model given training data `input_fn`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that provides input data for training as minibatches.
See [Premade Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The function should construct and return one of
the following:
* A <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a
tuple `(features, labels)` with same constraints as below.
* A tuple `(features, labels)`: Where `features` is a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or a
dictionary of string feature name to `Tensor` and `labels` is a
`Tensor` or a dictionary of string label name to `Tensor`. Both
`features` and `labels` are consumed by `model_fn`. They should
satisfy the expectation of `model_fn` from inputs.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
List of `tf.train.SessionRunHook` subclass instances. Used for
callbacks inside the training loop.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Number of steps for which to train the model. If `None`, train
forever or train until `input_fn` generates the `tf.errors.OutOfRange`
error or `StopIteration` exception. `steps` works incrementally. If you
call two times `train(steps=10)` then training occurs in total 20 steps.
If `OutOfRange` or `StopIteration` occurs in the middle, training stops
before 20 steps. If you don't want to have incremental behavior please
set `max_steps` instead. If set, `max_steps` must be `None`.
</td>
</tr><tr>
<td>
`max_steps`
</td>
<td>
Number of total steps for which to train model. If `None`,
train forever or train until `input_fn` generates the
`tf.errors.OutOfRange` error or `StopIteration` exception. If set,
`steps` must be `None`. If `OutOfRange` or `StopIteration` occurs in the
middle, training stops before `max_steps` steps. Two calls to
`train(steps=100)` means 200 training iterations. On the other hand, two
calls to `train(max_steps=100)` means that the second call will not do
any iteration since first call did all 100 steps.
</td>
</tr><tr>
<td>
`saving_listeners`
</td>
<td>
list of `CheckpointSaverListener` objects. Used for
callbacks that run immediately before or after checkpoint savings.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`self`, for chaining.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both `steps` and `max_steps` are not `None`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If either `steps` or `max_steps <= 0`.
</td>
</tr>
</table>





