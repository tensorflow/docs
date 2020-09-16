description: Warm-starts a model using the given settings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.warm_start" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.warm_start

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/warm_starting_util.py#L414-L553">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Warm-starts a model using the given settings.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.warm_start(
    ckpt_to_initialize_from, vars_to_warm_start='.*', var_name_to_vocab_info=None,
    var_name_to_prev_var_name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If you are using a tf.estimator.Estimator, this will automatically be called
during training.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ckpt_to_initialize_from`
</td>
<td>
[Required] A string specifying the directory with
checkpoint file(s) or path to checkpoint from which to warm-start the
model parameters.
</td>
</tr><tr>
<td>
`vars_to_warm_start`
</td>
<td>
[Optional] One of the following:

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
</td>
</tr><tr>
<td>
`var_name_to_vocab_info`
</td>
<td>
[Optional] Dict of variable names (strings) to
<a href="../../../../tf/estimator/VocabInfo.md"><code>tf.estimator.VocabInfo</code></a>. The variable names should be "full" variables,
not the names of the partitions.  If not explicitly provided, the variable
is assumed to have no (changes to) vocabulary.
</td>
</tr><tr>
<td>
`var_name_to_prev_var_name`
</td>
<td>
[Optional] Dict of variable names (strings) to
name of the previously-trained variable in `ckpt_to_initialize_from`. If
not explicitly provided, the name of the variable is assumed to be same
between previous checkpoint and current model.  Note that this has no
effect on the set of variables that is warm-started, and only controls
name mapping (use `vars_to_warm_start` for controlling what variables to
warm-start).
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
If the WarmStartSettings contains prev_var_name or VocabInfo
configuration for variable names that are not used.  This is to ensure
a stronger check for variable configuration than relying on users to
examine the logs.
</td>
</tr>
</table>

