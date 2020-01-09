page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.SaveOptions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/save_options.py#L28-L48">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SaveOptions`

Options for saving to SavedModel.



### Aliases:

* Class `tf.compat.v1.saved_model.SaveOptions`
* Class `tf.compat.v2.saved_model.SaveOptions`


<!-- Placeholder for "Used in" -->

This function may be used in the `options` argument in functions that
save a SavedModel (<a href="../../tf/saved_model/save"><code>tf.saved_model.save</code></a>, <a href="../../tf/keras/models/save_model"><code>tf.keras.models.save_model</code></a>).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/save_options.py#L38-L48">View source</a>

``` python
__init__(namespace_whitelist=None)
```

Creates an object that stores options for SavedModel saving.


#### Args:


* <b>`namespace_whitelist`</b>: List of strings containing op namespaces to whitelist
  when saving a model. Saving an object that uses namespaced ops must
  explicitly add all namespaces to the whitelist. The namespaced ops must
  be registered into the framework when loading the SavedModel.



## Class Members

* `namespace_whitelist` <a id="namespace_whitelist"></a>
