

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.warm_start

``` python
tf.train.warm_start(
    ckpt_to_initialize_from,
    vars_to_warm_start='.*',
    var_name_to_vocab_info=None,
    var_name_to_prev_var_name=None
)
```



Defined in [`tensorflow/python/training/warm_starting_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/training/warm_starting_util.py).

Warm-starts a model using the given settings.

If you are using a tf.estimator.Estimator, this will automatically be called
during training.

#### Args:

* <b>`ckpt_to_initialize_from`</b>: [Required] A string specifying the directory with
    checkpoint file(s) or path to checkpoint from which to warm-start the
    model parameters.
* <b>`vars_to_warm_start`</b>: [Optional] A regular expression that captures which
    variables to warm-start (see tf.get_collection).  Defaults to `'.*'`,
    which warm-starts all variables.  If `None` is explicitly given, only
    variables specified in `var_name_to_vocab_info` will be warm-started.
* <b>`var_name_to_vocab_info`</b>: [Optional] Dict of variable names (strings) to
    VocabInfo. The variable names should be "full" variables, not the names
    of the partitions.  If not explicitly provided, the variable is assumed to
    have no vocabulary.
* <b>`var_name_to_prev_var_name`</b>: [Optional] Dict of variable names (strings) to
    name of the previously-trained variable in `ckpt_to_initialize_from`. If
    not explicitly provided, the name of the variable is assumed to be same
    between previous checkpoint and current model.

#### Raises:

* <b>`ValueError`</b>: If the WarmStartSettings contains prev_var_name or VocabInfo
    configuration for variable names that are not used.  This is to ensure
    a stronger check for variable configuration than relying on users to
    examine the logs.