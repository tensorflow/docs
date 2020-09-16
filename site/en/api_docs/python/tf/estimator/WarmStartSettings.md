description: Settings for warm-starting in tf.estimator.Estimators.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.WarmStartSettings" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="ckpt_to_initialize_from"/>
<meta itemprop="property" content="var_name_to_prev_var_name"/>
<meta itemprop="property" content="var_name_to_vocab_info"/>
<meta itemprop="property" content="vars_to_warm_start"/>
</div>

# tf.estimator.WarmStartSettings

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Settings for warm-starting in `tf.estimator.Estimators`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.WarmStartSettings`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.WarmStartSettings(
    ckpt_to_initialize_from, vars_to_warm_start='.*', var_name_to_vocab_info=None,
    var_name_to_prev_var_name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Example Use with canned <a href="../../tf/estimator/DNNEstimator.md"><code>tf.estimator.DNNEstimator</code></a>:

```
emb_vocab_file = tf.feature_column.embedding_column(
    tf.feature_column.categorical_column_with_vocabulary_file(
        "sc_vocab_file", "new_vocab.txt", vocab_size=100),
    dimension=8)
emb_vocab_list = tf.feature_column.embedding_column(
    tf.feature_column.categorical_column_with_vocabulary_list(
        "sc_vocab_list", vocabulary_list=["a", "b"]),
    dimension=8)
estimator = tf.estimator.DNNClassifier(
  hidden_units=[128, 64], feature_columns=[emb_vocab_file, emb_vocab_list],
  warm_start_from=ws)
```

where `ws` could be defined as:

Warm-start all weights in the model (input layer and hidden weights).
Either the directory or a specific checkpoint can be provided (in the case
of the former, the latest checkpoint will be used):

```
ws = WarmStartSettings(ckpt_to_initialize_from="/tmp")
ws = WarmStartSettings(ckpt_to_initialize_from="/tmp/model-1000")
```

Warm-start only the embeddings (input layer):

```
ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                       vars_to_warm_start=".*input_layer.*")
```

Warm-start all weights but the embedding parameters corresponding to
`sc_vocab_file` have a different vocab from the one used in the current
model:

```
vocab_info = tf.estimator.VocabInfo(
    new_vocab=sc_vocab_file.vocabulary_file,
    new_vocab_size=sc_vocab_file.vocabulary_size,
    num_oov_buckets=sc_vocab_file.num_oov_buckets,
    old_vocab="old_vocab.txt"
)
ws = WarmStartSettings(
    ckpt_to_initialize_from="/tmp",
    var_name_to_vocab_info={
        "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
    })
```

Warm-start only `sc_vocab_file` embeddings (and no other variables), which
have a different vocab from the one used in the current model:

```
vocab_info = tf.estimator.VocabInfo(
    new_vocab=sc_vocab_file.vocabulary_file,
    new_vocab_size=sc_vocab_file.vocabulary_size,
    num_oov_buckets=sc_vocab_file.num_oov_buckets,
    old_vocab="old_vocab.txt"
)
ws = WarmStartSettings(
    ckpt_to_initialize_from="/tmp",
    vars_to_warm_start=None,
    var_name_to_vocab_info={
        "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
    })
```

Warm-start all weights but the parameters corresponding to `sc_vocab_file`
have a different vocab from the one used in current checkpoint, and only
100 of those entries were used:

```
vocab_info = tf.estimator.VocabInfo(
    new_vocab=sc_vocab_file.vocabulary_file,
    new_vocab_size=sc_vocab_file.vocabulary_size,
    num_oov_buckets=sc_vocab_file.num_oov_buckets,
    old_vocab="old_vocab.txt",
    old_vocab_size=100
)
ws = WarmStartSettings(
    ckpt_to_initialize_from="/tmp",
    var_name_to_vocab_info={
        "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
    })
```

Warm-start all weights but the parameters corresponding to `sc_vocab_file`
have a different vocab from the one used in current checkpoint and the
parameters corresponding to `sc_vocab_list` have a different name from the
current checkpoint:

```
vocab_info = tf.estimator.VocabInfo(
    new_vocab=sc_vocab_file.vocabulary_file,
    new_vocab_size=sc_vocab_file.vocabulary_size,
    num_oov_buckets=sc_vocab_file.num_oov_buckets,
    old_vocab="old_vocab.txt",
    old_vocab_size=100
)
ws = WarmStartSettings(
    ckpt_to_initialize_from="/tmp",
    var_name_to_vocab_info={
        "input_layer/sc_vocab_file_embedding/embedding_weights": vocab_info
    },
    var_name_to_prev_var_name={
        "input_layer/sc_vocab_list_embedding/embedding_weights":
            "old_tensor_name"
    })
```

Warm-start all TRAINABLE variables:

```
ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                       vars_to_warm_start=".*")
```

Warm-start all variables (including non-TRAINABLE):

```
ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                       vars_to_warm_start=[".*"])
```

Warm-start non-TRAINABLE variables "v1", "v1/Momentum", and "v2" but not
"v2/momentum":

```
ws = WarmStartSettings(ckpt_to_initialize_from="/tmp",
                       vars_to_warm_start=["v1", "v2[^/]"])
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

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
[Optional] One of the following:  - A regular expression
(string) that captures which variables to warm-start (see
tf.compat.v1.get_collection).  This expression will only consider
variables in the TRAINABLE_VARIABLES collection -- if you need to
warm-start non_TRAINABLE vars (such as optimizer accumulators or batch
norm statistics), please use the below option. - A list of strings, each a
regex scope provided to tf.compat.v1.get_collection with GLOBAL_VARIABLES
(please see tf.compat.v1.get_collection).  For backwards compatibility
reasons, this is separate from the single-string argument type. - A list
of Variables to warm-start.  If you do not have access to the `Variable`
objects at the call site, please use the above option. - `None`, in which
case only TRAINABLE variables specified in `var_name_to_vocab_info` will
be warm-started.  Defaults to `'.*'`, which warm-starts all variables in
the TRAINABLE_VARIABLES collection.  Note that this excludes variables
such as accumulators and moving statistics from batch norm.
</td>
</tr><tr>
<td>
`var_name_to_vocab_info`
</td>
<td>
[Optional] Dict of variable names (strings) to
<a href="../../tf/estimator/VocabInfo.md"><code>tf.estimator.VocabInfo</code></a>. The variable names should be "full" variables,
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



## Class Variables

* `ckpt_to_initialize_from` <a id="ckpt_to_initialize_from"></a>
* `var_name_to_prev_var_name` <a id="var_name_to_prev_var_name"></a>
* `var_name_to_vocab_info` <a id="var_name_to_vocab_info"></a>
* `vars_to_warm_start` <a id="vars_to_warm_start"></a>
