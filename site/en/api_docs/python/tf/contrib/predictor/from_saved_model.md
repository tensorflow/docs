

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.predictor.from_saved_model

``` python
tf.contrib.predictor.from_saved_model(
    export_dir,
    signature_def_key=None,
    signature_def=None,
    tags=None,
    graph=None
)
```



Defined in [`tensorflow/contrib/predictor/predictor_factories.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/predictor/predictor_factories.py).

Constructs a `Predictor` from a `SavedModel` on disk.

#### Args:

* <b>`export_dir`</b>: a path to a directory containing a `SavedModel`.
* <b>`signature_def_key`</b>: Optional string specifying the signature to use. If
    `None`, then `DEFAULT_SERVING_SIGNATURE_DEF_KEY` is used. Only one of
  `signature_def_key` and `signature_def`
* <b>`signature_def`</b>: A `SignatureDef` proto specifying the inputs and outputs
    for prediction. Only one of `signature_def_key` and `signature_def`
    should be specified.
* <b>`tags`</b>: Optional. Tags that will be used to retrieve the correct
    `SignatureDef`. Defaults to `DEFAULT_TAGS`.
* <b>`graph`</b>: Optional. The Tensorflow `graph` in which prediction should be
    done.


#### Returns:

An initialized `Predictor`.


#### Raises:

* <b>`ValueError`</b>: More than one of `signature_def_key` and `signature_def` is
    specified.