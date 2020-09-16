description: Configuration for the "train" part for the train_and_evaluate call.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.TrainSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="hooks"/>
<meta itemprop="property" content="input_fn"/>
<meta itemprop="property" content="max_steps"/>
</div>

# tf.estimator.TrainSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/training.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for the "train" part for the `train_and_evaluate` call.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.TrainSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.TrainSpec(
    input_fn, max_steps=None, hooks=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`TrainSpec` determines the input data for the training, as well as the
duration. Optional hooks run at various stages of training.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

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
* A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
tuple (features, labels) with same constraints as below.
* A tuple (features, labels): Where features is a `Tensor` or a
dictionary of string feature name to `Tensor` and labels is a
`Tensor` or a dictionary of string label name to `Tensor`.
</td>
</tr><tr>
<td>
`max_steps`
</td>
<td>
Int. Positive number of total steps for which to train model.
If `None`, train forever. The training `input_fn` is not expected to
generate `OutOfRangeError` or `StopIteration` exceptions. See the
`train_and_evaluate` stop condition section for details.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
Iterable of `tf.train.SessionRunHook` objects to run on all workers
(including chief) during training.
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
If any of the input arguments is invalid.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If any of the arguments is not of the expected type.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`input_fn`
</td>
<td>

</td>
</tr><tr>
<td>
`max_steps`
</td>
<td>

</td>
</tr><tr>
<td>
`hooks`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `hooks` <a id="hooks"></a>
* `input_fn` <a id="input_fn"></a>
* `max_steps` <a id="max_steps"></a>
