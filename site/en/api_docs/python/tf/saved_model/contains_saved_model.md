page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.contains_saved_model

Checks whether the provided export directory could contain a SavedModel.

### Aliases:

* `tf.compat.v1.saved_model.contains_saved_model`
* `tf.compat.v1.saved_model.loader.maybe_saved_model_directory`
* `tf.compat.v1.saved_model.maybe_saved_model_directory`
* `tf.saved_model.contains_saved_model`
* `tf.saved_model.loader.maybe_saved_model_directory`
* `tf.saved_model.maybe_saved_model_directory`

``` python
tf.saved_model.contains_saved_model(export_dir)
```



Defined in [`python/saved_model/loader_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/saved_model/loader_impl.py).

<!-- Placeholder for "Used in" -->

Note that the method does not load any data by itself. If the method returns
`false`, the export directory definitely does not contain a SavedModel. If the
method returns `true`, the export directory may contain a SavedModel but
provides no guarantee that it can be loaded.

#### Args:


* <b>`export_dir`</b>: Absolute string path to possible export location. For example,
            '/my/foo/model'.


#### Returns:

True if the export directory contains SavedModel files, False otherwise.
