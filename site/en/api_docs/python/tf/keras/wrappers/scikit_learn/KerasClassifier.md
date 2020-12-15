description: Implementation of the scikit-learn classifier API for Keras.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.wrappers.scikit_learn.KerasClassifier" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="check_params"/>
<meta itemprop="property" content="filter_sk_params"/>
<meta itemprop="property" content="fit"/>
<meta itemprop="property" content="get_params"/>
<meta itemprop="property" content="predict"/>
<meta itemprop="property" content="predict_proba"/>
<meta itemprop="property" content="score"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.wrappers.scikit_learn.KerasClassifier

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L191-L310">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Implementation of the scikit-learn classifier API for Keras.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.wrappers.scikit_learn.KerasClassifier`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.wrappers.scikit_learn.KerasClassifier(
    build_fn=None, **sk_params
)
</code></pre>



<!-- Placeholder for "Used in" -->
  

## Methods

<h3 id="check_params"><code>check_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L79-L106">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>check_params(
    params
)
</code></pre>

Checks for user typos in `params`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`params`
</td>
<td>
dictionary; the parameters to be checked
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
if any member of `params` is not a valid argument.
</td>
</tr>
</table>



<h3 id="filter_sk_params"><code>filter_sk_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L170-L187">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>filter_sk_params(
    fn, override=None
)
</code></pre>

Filters `sk_params` and returns those in `fn`'s arguments.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`fn`
</td>
<td>
arbitrary function
</td>
</tr><tr>
<td>
`override`
</td>
<td>
dictionary, values to override `sk_params`
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`res`
</td>
<td>
dictionary containing variables
in both `sk_params` and `fn`'s arguments.
</td>
</tr>
</table>



<h3 id="fit"><code>fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L195-L223">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>fit(
    x, y, **kwargs
)
</code></pre>

Constructs a new model with `build_fn` & fit the model to `(x, y)`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
array-like, shape `(n_samples, n_features)`
Training samples where `n_samples` is the number of samples
and `n_features` is the number of features.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
True labels for `x`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
dictionary arguments
Legal arguments are the arguments of <a href="../../../../tf/keras/Model.md#fit"><code>Sequential.fit</code></a>
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`history`
</td>
<td>
object
details about the training history at each epoch.
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
In case of invalid shape for `y` argument.
</td>
</tr>
</table>



<h3 id="get_params"><code>get_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L108-L119">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_params(
    **params
)
</code></pre>

Gets parameters for this estimator.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`**params`
</td>
<td>
ignored (exists for API compatibility).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Dictionary of parameter names mapped to their values.
</td>
</tr>

</table>



<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L225-L242">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict(
    x, **kwargs
)
</code></pre>

Returns the class predictions for the given test data.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
array-like, shape `(n_samples, n_features)`
Test samples where `n_samples` is the number of samples
and `n_features` is the number of features.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
dictionary arguments
Legal arguments are the arguments
of <a href="../../../../tf/keras/Sequential.md#predict_classes"><code>Sequential.predict_classes</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`preds`
</td>
<td>
array-like, shape `(n_samples,)`
Class predictions.
</td>
</tr>
</table>



<h3 id="predict_proba"><code>predict_proba</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L244-L270">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict_proba(
    x, **kwargs
)
</code></pre>

Returns class probability estimates for the given test data.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
array-like, shape `(n_samples, n_features)`
Test samples where `n_samples` is the number of samples
and `n_features` is the number of features.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
dictionary arguments
Legal arguments are the arguments
of <a href="../../../../tf/keras/Sequential.md#predict_classes"><code>Sequential.predict_classes</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`proba`
</td>
<td>
array-like, shape `(n_samples, n_outputs)`
Class probability estimates.
In the case of binary classification,
to match the scikit-learn API,
will return an array of shape `(n_samples, 2)`
(instead of `(n_sample, 1)` as in Keras).
</td>
</tr>
</table>



<h3 id="score"><code>score</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L272-L310">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>score(
    x, y, **kwargs
)
</code></pre>

Returns the mean accuracy on the given test data and labels.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`x`
</td>
<td>
array-like, shape `(n_samples, n_features)`
Test samples where `n_samples` is the number of samples
and `n_features` is the number of features.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
True labels for `x`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
dictionary arguments
Legal arguments are the arguments of <a href="../../../../tf/keras/Model.md#evaluate"><code>Sequential.evaluate</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`score`
</td>
<td>
float
Mean accuracy of predictions on `x` wrt. `y`.
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
If the underlying model isn't configured to
compute accuracy. You should pass `metrics=["accuracy"]` to
the `.compile()` method of the model.
</td>
</tr>
</table>



<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/wrappers/scikit_learn.py#L121-L132">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    **params
)
</code></pre>

Sets the parameters of this estimator.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`**params`
</td>
<td>
Dictionary of parameter names mapped to their values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
self
</td>
</tr>

</table>





