description: Clone any Model instance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.models.clone_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.models.clone_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/models.py#L384-L427">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Clone any `Model` instance.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.models.clone_model`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.models.clone_model(
    model, input_tensors=None, clone_function=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Model cloning is similar to calling a model on new inputs,
except that it creates new layers (and thus new weights) instead
of sharing the weights of the existing layers.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`model`
</td>
<td>
Instance of `Model`
(could be a functional model or a Sequential model).
</td>
</tr><tr>
<td>
`input_tensors`
</td>
<td>
optional list of input tensors or InputLayer objects
to build the model upon. If not provided,
placeholders will be created.
</td>
</tr><tr>
<td>
`clone_function`
</td>
<td>
Callable to be used to clone each layer in the target
model (except `InputLayer` instances). It takes as argument the layer
instance to be cloned, and returns the corresponding layer instance to
be used in the model copy. If unspecified, this callable defaults to
the following serialization/deserialization function:
`lambda layer: layer.__class__.from_config(layer.get_config())`.
By passing a custom callable, you can customize your copy of the
model, e.g. by wrapping certain layers of interest (you might want to
replace all `LSTM` instances with equivalent
`Bidirectional(LSTM(...))` instances, for example).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An instance of `Model` reproducing the behavior
of the original model, on top of new inputs tensors,
using newly instantiated weights. The cloned model might behave
differently from the original model if a custom clone_function
modifies the layer.
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
in case of invalid `model` argument value.
</td>
</tr>
</table>

