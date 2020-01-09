page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.build_parsing_serving_input_receiver_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/export/export.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Build a serving_input_receiver_fn expecting fed tf.Examples.

### Aliases:

* `tf.compat.v1.estimator.export.build_parsing_serving_input_receiver_fn`
* `tf.compat.v2.estimator.export.build_parsing_serving_input_receiver_fn`


``` python
tf.estimator.export.build_parsing_serving_input_receiver_fn(
    feature_spec,
    default_batch_size=None
)
```



### Used in the guide:

* [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)



Creates a serving_input_receiver_fn that expects a serialized tf.Example fed
into a string placeholder.  The function parses the tf.Example according to
the provided feature_spec, and returns all parsed Tensors as features.

#### Args:


* <b>`feature_spec`</b>: a dict of string to `VarLenFeature`/`FixedLenFeature`.
* <b>`default_batch_size`</b>: the number of query examples expected per batch.
    Leave unset for variable batch size (recommended).


#### Returns:

A serving_input_receiver_fn suitable for use in serving.
