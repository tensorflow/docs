description: Convenience function to build a SavedModel suitable for serving. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model.simple_save" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.saved_model.simple_save

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/simple_save.py#L30-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convenience function to build a SavedModel suitable for serving. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.saved_model.simple_save(
    session, export_dir, inputs, outputs, legacy_init_op=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.simple_save.

In many common cases, saving models for serving will be as simple as:

    simple_save(session,
                export_dir,
                inputs={"x": x, "y": y},
                outputs={"z": z})

Although in many cases it's not necessary to understand all of the many ways
    to configure a SavedModel, this method has a few practical implications:
  - It will be treated as a graph for inference / serving (i.e. uses the tag
    `saved_model.SERVING`)
  - The SavedModel will load in TensorFlow Serving and supports the
    [Predict
    API](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/apis/predict.proto).
    To use the Classify, Regress, or MultiInference APIs, please
    use either
    [tf.Estimator](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator)
    or the lower level
    [SavedModel
    APIs](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md).
  - Some TensorFlow ops depend on information on disk or other information
    called "assets". These are generally handled automatically by adding the
    assets to the `GraphKeys.ASSET_FILEPATHS` collection. Only assets in that
    collection are exported; if you need more custom behavior, you'll need to
    use the
    [SavedModelBuilder](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/builder.py).

More information about SavedModel and signatures can be found here:
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`session`
</td>
<td>
The TensorFlow session from which to save the meta graph and
variables.
</td>
</tr><tr>
<td>
`export_dir`
</td>
<td>
The path to which the SavedModel will be stored.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
dict mapping string input names to tensors. These are added
to the SignatureDef as the inputs.
</td>
</tr><tr>
<td>
`outputs`
</td>
<td>
dict mapping string output names to tensors. These are added
to the SignatureDef as the outputs.
</td>
</tr><tr>
<td>
`legacy_init_op`
</td>
<td>
Legacy support for op or group of ops to execute after the
restore op upon a load.
</td>
</tr>
</table>

