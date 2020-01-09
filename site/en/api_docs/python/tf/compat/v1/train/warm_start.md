page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.warm_start


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/warm_starting_util.py#L411-L550">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Warm-starts a model using the given settings.

``` python
tf.compat.v1.train.warm_start(
    ckpt_to_initialize_from,
    vars_to_warm_start='.*',
    var_name_to_vocab_info=None,
    var_name_to_prev_var_name=None
)
```



<!-- Placeholder for "Used in" -->

If you are using a tf.estimator.Estimator, this will automatically be called
during training.

#### Args:


* <b>`ckpt_to_initialize_from`</b>: [Required] A string specifying the directory with
  checkpoint file(s) or path to checkpoint from which to warm-start the
  model parameters.
* <b>`vars_to_warm_start`</b>: [Optional] One of the following:

  - A regular expression (string) that captures which variables to
    warm-start (see tf.compat.v1.get_collection).  This expression will only
    consider variables in the TRAINABLE_VARIABLES collection -- if you need
    to warm-start non_TRAINABLE vars (such as optimizer accumulators or
    batch norm statistics), please use the below option.
  - A list of strings, each a regex scope provided to
    tf.compat.v1.get_collection with GLOBAL_VARIABLES (please see
    tf.compat.v1.get_collection).  For backwards compatibility reasons,
    this is separate from the single-string argument type.
  - A list of Variables to warm-start.  If you do not have access to the
    `Variable` objects at the call site, please use the above option.
  - `None`, in which case only TRAINABLE variables specified in
    `var_name_to_vocab_info` will be warm-started.

  Defaults to `'.*'`, which warm-starts all variables in the
  TRAINABLE_VARIABLES collection.  Note that this excludes variables such
  as accumulators and moving statistics from batch norm.
* <b>`var_name_to_vocab_info`</b>: [Optional] Dict of variable names (strings) to
  <a href="../../../../tf/estimator/VocabInfo"><code>tf.estimator.VocabInfo</code></a>. The variable names should be "full" variables,
  not the names of the partitions.  If not explicitly provided, the variable
  is assumed to have no (changes to) vocabulary.
* <b>`var_name_to_prev_var_name`</b>: [Optional] Dict of variable names (strings) to
  name of the previously-trained variable in `ckpt_to_initialize_from`. If
  not explicitly provided, the name of the variable is assumed to be same
  between previous checkpoint and current model.  Note that this has no
  effect on the set of variables that is warm-started, and only controls
  name mapping (use `vars_to_warm_start` for controlling what variables to
  warm-start).


#### Raises:


* <b>`ValueError`</b>: If the WarmStartSettings contains prev_var_name or VocabInfo
  configuration for variable names that are not used.  This is to ensure
  a stronger check for variable configuration than relying on users to
  examine the logs.
