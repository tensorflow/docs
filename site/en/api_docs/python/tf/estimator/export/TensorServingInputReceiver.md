description: A return type for a serving_input_receiver_fn.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.export.TensorServingInputReceiver" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="features"/>
<meta itemprop="property" content="receiver_tensors"/>
<meta itemprop="property" content="receiver_tensors_alternatives"/>
</div>

# tf.estimator.export.TensorServingInputReceiver

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/export/export.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A return type for a serving_input_receiver_fn.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.export.TensorServingInputReceiver`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.export.TensorServingInputReceiver(
    features, receiver_tensors, receiver_tensors_alternatives=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is for use with models that expect a single `Tensor` or `SparseTensor`
as an input feature, as opposed to a dict of features.

The normal `ServingInputReceiver` always returns a feature dict, even if it
contains only one entry, and so can be used only with models that accept such
a dict.  For models that accept only a single raw feature, the
`serving_input_receiver_fn` provided to <a href="../../../tf/compat/v1/estimator/Estimator.md#export_saved_model"><code>Estimator.export_saved_model()</code></a>
should return this `TensorServingInputReceiver` instead.  See:
https://github.com/tensorflow/tensorflow/issues/11674

Note that the receiver_tensors and receiver_tensor_alternatives arguments
will be automatically converted to the dict representation in either case,
because the SavedModel format requires each input `Tensor` to have a name
(provided by the dict key).



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A single `Tensor` or `SparseTensor`, representing the feature to
be passed to the model.
</td>
</tr><tr>
<td>
`receiver_tensors`
</td>
<td>
A `Tensor`, `SparseTensor`, or dict of string to `Tensor`
or `SparseTensor`, specifying input nodes where this receiver expects to
be fed by default.  Typically, this is a single placeholder expecting
serialized `tf.Example` protos.
</td>
</tr><tr>
<td>
`receiver_tensors_alternatives`
</td>
<td>
a dict of string to additional groups of
receiver tensors, each of which may be a `Tensor`, `SparseTensor`, or dict
of string to `Tensor` or`SparseTensor`. These named receiver tensor
alternatives generate additional serving signatures, which may be used to
feed inputs at different points within the input receiver subgraph.  A
typical usage is to allow feeding raw feature `Tensor`s *downstream* of
the tf.parse_example() op. Defaults to None.
</td>
</tr>
</table>



## Class Variables

* `features` <a id="features"></a>
* `receiver_tensors` <a id="receiver_tensors"></a>
* `receiver_tensors_alternatives` <a id="receiver_tensors_alternatives"></a>
