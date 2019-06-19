page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.WarmStartSettings

## Class `WarmStartSettings`





Defined in [`tensorflow/python/estimator/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/estimator/estimator.py).

Settings for warm-starting in Estimators.

Example Use with canned `DNNEstimator`:

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

#### Attributes:

* <b>`ckpt_to_initialize_from`</b>: [Required] A string specifying the directory with
    checkpoint file(s) or path to checkpoint from which to warm-start the
    model parameters.
* <b>`vars_to_warm_start`</b>: [Optional] One of the following:

    - A regular expression (string) that captures which variables to
      warm-start (see tf.get_collection).  This expression will only consider
      variables in the TRAINABLE_VARIABLES collection.
    - A list of Variables to warm-start.
    - A list of strings, each representing a full variable name to warm-start.
    - `None`, in which case only variables specified in
      `var_name_to_vocab_info` will be warm-started.

    Defaults to `'.*'`, which warm-starts all variables in the
    TRAINABLE_VARIABLES collection.  Note that this excludes variables such as
    accumulators and moving statistics from batch norm.
* <b>`var_name_to_vocab_info`</b>: [Optional] Dict of variable names (strings) to
    VocabInfo. The variable names should be "full" variables, not the names
    of the partitions.  If not explicitly provided, the variable is assumed to
    have no vocabulary.
* <b>`var_name_to_prev_var_name`</b>: [Optional] Dict of variable names (strings) to
    name of the previously-trained variable in `ckpt_to_initialize_from`. If
    not explicitly provided, the name of the variable is assumed to be same
    between previous checkpoint and current model.

## Properties

<h3 id="ckpt_to_initialize_from"><code>ckpt_to_initialize_from</code></h3>

Alias for field number 0

<h3 id="var_name_to_prev_var_name"><code>var_name_to_prev_var_name</code></h3>

Alias for field number 3

<h3 id="var_name_to_vocab_info"><code>var_name_to_vocab_info</code></h3>

Alias for field number 2

<h3 id="vars_to_warm_start"><code>vars_to_warm_start</code></h3>

Alias for field number 1



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    ckpt_to_initialize_from,
    vars_to_warm_start='.*',
    var_name_to_vocab_info=None,
    var_name_to_prev_var_name=None
)
```





