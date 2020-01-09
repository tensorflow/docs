page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.simple_save


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/simple_save.py#L30-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convenience function to build a SavedModel suitable for serving. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/saved_model/simple_save"><code>tf.compat.v1.saved_model.simple_save</code></a>


``` python
tf.saved_model.simple_save(
    session,
    export_dir,
    inputs,
    outputs,
    legacy_init_op=None
)
```



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
    <a href="../../tf/saved_model#SERVING"><code>saved_model.SERVING</code></a>)
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
    assets to the <a href="../../tf/GraphKeys#ASSET_FILEPATHS"><code>GraphKeys.ASSET_FILEPATHS</code></a> collection. Only assets in that
    collection are exported; if you need more custom behavior, you'll need to
    use the
    [SavedModelBuilder](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/builder.py).

More information about SavedModel and signatures can be found here:
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md.

#### Args:


* <b>`session`</b>: The TensorFlow session from which to save the meta graph and
    variables.
* <b>`export_dir`</b>: The path to which the SavedModel will be stored.
* <b>`inputs`</b>: dict mapping string input names to tensors. These are added
    to the SignatureDef as the inputs.
* <b>`outputs`</b>:  dict mapping string output names to tensors. These are added
    to the SignatureDef as the outputs.
* <b>`legacy_init_op`</b>: Legacy support for op or group of ops to execute after the
    restore op upon a load.
