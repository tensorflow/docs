description: Abstract base class used to build new callbacks.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.callbacks.Callback" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="on_batch_begin"/>
<meta itemprop="property" content="on_batch_end"/>
<meta itemprop="property" content="on_epoch_begin"/>
<meta itemprop="property" content="on_epoch_end"/>
<meta itemprop="property" content="on_predict_batch_begin"/>
<meta itemprop="property" content="on_predict_batch_end"/>
<meta itemprop="property" content="on_predict_begin"/>
<meta itemprop="property" content="on_predict_end"/>
<meta itemprop="property" content="on_test_batch_begin"/>
<meta itemprop="property" content="on_test_batch_end"/>
<meta itemprop="property" content="on_test_begin"/>
<meta itemprop="property" content="on_test_end"/>
<meta itemprop="property" content="on_train_batch_begin"/>
<meta itemprop="property" content="on_train_batch_end"/>
<meta itemprop="property" content="on_train_begin"/>
<meta itemprop="property" content="on_train_end"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.callbacks.Callback

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L607-L869">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Abstract base class used to build new callbacks.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.callbacks.Callback`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.callbacks.Callback()
</code></pre>



<!-- Placeholder for "Used in" -->

The `logs` dictionary that callback methods
take as argument will contain keys for quantities relevant to
the current batch or epoch (see method-specific docstrings).



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`params`
</td>
<td>
Dict. Training parameters
(eg. verbosity, batch size, number of epochs...).
</td>
</tr><tr>
<td>
`model`
</td>
<td>
Instance of <a href="../../../tf/keras/Model.md"><code>keras.models.Model</code></a>.
Reference of the model being trained.
</td>
</tr>
</table>



## Methods

<h3 id="on_batch_begin"><code>on_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L636-L639">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_batch_begin(
    batch, logs=None
)
</code></pre>

A backwards compatibility alias for `on_train_batch_begin`.


<h3 id="on_batch_end"><code>on_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L641-L644">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_batch_end(
    batch, logs=None
)
</code></pre>

A backwards compatibility alias for `on_train_batch_end`.


<h3 id="on_epoch_begin"><code>on_epoch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L646-L657">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_epoch_begin(
    epoch, logs=None
)
</code></pre>

Called at the start of an epoch.

Subclasses should override for any actions to run. This function should only
be called during TRAIN mode.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`epoch`
</td>
<td>
Integer, index of epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict. Currently no data is passed to this argument for this method
but that may change in the future.
</td>
</tr>
</table>



<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L659-L672">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_epoch_end(
    epoch, logs=None
)
</code></pre>

Called at the end of an epoch.

Subclasses should override for any actions to run. This function should only
be called during TRAIN mode.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`epoch`
</td>
<td>
Integer, index of epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict, metric results for this training epoch, and for the
validation epoch if validation is performed. Validation result keys
are prefixed with `val_`. For training epoch, the values of the  
`Model`'s metrics are returned. Example : `{'loss': 0.2, 'acc': 0.7}`.
</td>
</tr>
</table>



<h3 id="on_predict_batch_begin"><code>on_predict_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L752-L768">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_predict_batch_begin(
    batch, logs=None
)
</code></pre>

Called at the beginning of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
<a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is set to `N`, this method will only be called every `N`
batches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`batch`
</td>
<td>
Integer, index of batch within the current epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict, contains the return value of `model.predict_step`,
it typically returns a dict with a key 'outputs' containing
the model's outputs.
</td>
</tr>
</table>



<h3 id="on_predict_batch_end"><code>on_predict_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L770-L784">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_predict_batch_end(
    batch, logs=None
)
</code></pre>

Called at the end of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
<a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is set to `N`, this method will only be called every `N`
batches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`batch`
</td>
<td>
Integer, index of batch within the current epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict. Aggregated metric results up until this batch.
</td>
</tr>
</table>



<h3 id="on_predict_begin"><code>on_predict_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L832-L841">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_predict_begin(
    logs=None
)
</code></pre>

Called at the beginning of prediction.

Subclasses should override for any actions to run.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`logs`
</td>
<td>
Dict. Currently no data is passed to this argument for this method
but that may change in the future.
</td>
</tr>
</table>



<h3 id="on_predict_end"><code>on_predict_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L843-L852">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_predict_end(
    logs=None
)
</code></pre>

Called at the end of prediction.

Subclasses should override for any actions to run.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`logs`
</td>
<td>
Dict. Currently no data is passed to this argument for this method
but that may change in the future.
</td>
</tr>
</table>



<h3 id="on_test_batch_begin"><code>on_test_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L712-L731">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_test_batch_begin(
    batch, logs=None
)
</code></pre>

Called at the beginning of a batch in `evaluate` methods.

Also called at the beginning of a validation batch in the `fit`
methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
<a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is set to `N`, this method will only be called every `N`
batches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`batch`
</td>
<td>
Integer, index of batch within the current epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict, contains the return value of `model.test_step`. Typically,
the values of the `Model`'s metrics are returned.  Example:
`{'loss': 0.2, 'accuracy': 0.7}`.
</td>
</tr>
</table>



<h3 id="on_test_batch_end"><code>on_test_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L733-L750">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_test_batch_end(
    batch, logs=None
)
</code></pre>

Called at the end of a batch in `evaluate` methods.

Also called at the end of a validation batch in the `fit`
methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
<a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is set to `N`, this method will only be called every `N`
batches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`batch`
</td>
<td>
Integer, index of batch within the current epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict. Aggregated metric results up until this batch.
</td>
</tr>
</table>



<h3 id="on_test_begin"><code>on_test_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L809-L818">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_test_begin(
    logs=None
)
</code></pre>

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`logs`
</td>
<td>
Dict. Currently no data is passed to this argument for this method
but that may change in the future.
</td>
</tr>
</table>



<h3 id="on_test_end"><code>on_test_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L820-L830">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_test_end(
    logs=None
)
</code></pre>

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`logs`
</td>
<td>
Dict. Currently the output of the last call to
`on_test_batch_end()` is passed to this argument for this method
but that may change in the future.
</td>
</tr>
</table>



<h3 id="on_train_batch_begin"><code>on_train_batch_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L674-L692">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_train_batch_begin(
    batch, logs=None
)
</code></pre>

Called at the beginning of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
<a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is set to `N`, this method will only be called every `N`
batches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`batch`
</td>
<td>
Integer, index of batch within the current epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict, contains the return value of `model.train_step`. Typically,
the values of the `Model`'s metrics are returned.  Example:
`{'loss': 0.2, 'accuracy': 0.7}`.
</td>
</tr>
</table>



<h3 id="on_train_batch_end"><code>on_train_batch_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L694-L710">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_train_batch_end(
    batch, logs=None
)
</code></pre>

Called at the end of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in
<a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is set to `N`, this method will only be called every `N`
batches.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`batch`
</td>
<td>
Integer, index of batch within the current epoch.
</td>
</tr><tr>
<td>
`logs`
</td>
<td>
Dict. Aggregated metric results up until this batch.
</td>
</tr>
</table>



<h3 id="on_train_begin"><code>on_train_begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L786-L795">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_train_begin(
    logs=None
)
</code></pre>

Called at the beginning of training.

Subclasses should override for any actions to run.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`logs`
</td>
<td>
Dict. Currently no data is passed to this argument for this method
but that may change in the future.
</td>
</tr>
</table>



<h3 id="on_train_end"><code>on_train_end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L797-L807">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_train_end(
    logs=None
)
</code></pre>

Called at the end of training.

Subclasses should override for any actions to run.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`logs`
</td>
<td>
Dict. Currently the output of the last call to `on_epoch_end()`
is passed to this argument for this method but that may change in
the future.
</td>
</tr>
</table>



<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L633-L634">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>




<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L630-L631">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






