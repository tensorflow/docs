page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.boosted_trees_classifier_train_in_memory


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/contrib/estimator/python/estimator/boosted_trees.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Trains a boosted tree classifier with in memory dataset.

``` python
tf.contrib.estimator.boosted_trees_classifier_train_in_memory(
    train_input_fn,
    feature_columns,
    model_dir=None,
    n_classes=canned_boosted_trees._HOLD_FOR_MULTI_CLASS_SUPPORT,
    weight_column=None,
    label_vocabulary=None,
    n_trees=100,
    max_depth=6,
    learning_rate=0.1,
    l1_regularization=0.0,
    l2_regularization=0.0,
    tree_complexity=0.0,
    min_node_weight=0.0,
    config=None,
    train_hooks=None,
    center_bias=False,
    pruning_mode='none',
    quantile_sketch_epsilon=0.01
)
```



<!-- Placeholder for "Used in" -->


#### Example:



```python
bucketized_feature_1 = bucketized_column(
  numeric_column('feature_1'), BUCKET_BOUNDARIES_1)
bucketized_feature_2 = bucketized_column(
  numeric_column('feature_2'), BUCKET_BOUNDARIES_2)

def train_input_fn():
  dataset = create-dataset-from-training-data
  # This is tf.data.Dataset of a tuple of feature dict and label.
  #   e.g. Dataset.zip((Dataset.from_tensors({'f1': f1_array, ...}),
  #                     Dataset.from_tensors(label_array)))
  # The returned Dataset shouldn't be batched.
  # If Dataset repeats, only the first repetition would be used for training.
  return dataset

classifier = boosted_trees_classifier_train_in_memory(
    train_input_fn,
    feature_columns=[bucketized_feature_1, bucketized_feature_2],
    n_trees=100,
    ... <some other params>
)

def input_fn_eval():
  ...
  return dataset

metrics = classifier.evaluate(input_fn=input_fn_eval, steps=10)
```

#### Args:


* <b>`train_input_fn`</b>: the input function returns a dataset containing a single
  epoch of *unbatched* features and labels.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
  the model. All items in the set should be instances of classes derived
  from `FeatureColumn`.
* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
  also be used to load checkpoints from the directory into an estimator
  to continue training a previously saved model.
* <b>`n_classes`</b>: number of label classes. Default is binary classification.
  Multiclass support is not yet implemented.
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
  <a href="../../../tf/feature_column/numeric_column"><code>tf.feature_column.numeric_column</code></a> defining feature column representing
  weights. It is used to downweight or boost examples during training. It
  will be multiplied by the loss of the example. If it is a string, it is
  used as a key to fetch weight tensor from the `features`. If it is a
  `_NumericColumn`, raw tensor is fetched by key `weight_column.key`,
  then weight_column.normalizer_fn is applied on it to get weight tensor.
* <b>`label_vocabulary`</b>: A list of strings represents possible label values. If
  given, labels must be string type and have any value in
  `label_vocabulary`. If it is not given, that means labels are
  already encoded as integer or float within [0, 1] for `n_classes=2` and
  encoded as integer values in {0, 1,..., n_classes-1} for `n_classes`>2 .
  Also there will be errors if vocabulary is not provided and labels are
  string.
* <b>`n_trees`</b>: number trees to be created.
* <b>`max_depth`</b>: maximum depth of the tree to grow.
* <b>`learning_rate`</b>: shrinkage parameter to be used when a tree added to the
  model.
* <b>`l1_regularization`</b>: regularization multiplier applied to the absolute
  weights of the tree leafs.
* <b>`l2_regularization`</b>: regularization multiplier applied to the square weights
  of the tree leafs.
* <b>`tree_complexity`</b>: regularization factor to penalize trees with more leaves.
* <b>`min_node_weight`</b>: minimum hessian a node must have for a split to be
    considered. The value will be compared with sum(leaf_hessian)/
    (batch_size * n_batches_per_layer).
* <b>`config`</b>: `RunConfig` object to configure the runtime settings.
* <b>`train_hooks`</b>: a list of Hook instances to be passed to estimator.train()
* <b>`center_bias`</b>: Whether bias centering needs to occur. Bias centering refers
    to the first node in the very first tree returning the prediction that
    is aligned with the original labels distribution. For example, for
    regression problems, the first node will return the mean of the labels.
    For binary classification problems, it will return a logit for a prior
    probability of label 1.
* <b>`pruning_mode`</b>: one of 'none', 'pre', 'post' to indicate no pruning, pre-
    pruning (do not split a node if not enough gain is observed) and post
    pruning (build the tree up to a max depth and then prune branches with
    negative gain). For pre and post pruning, you MUST provide
    tree_complexity >0.
* <b>`quantile_sketch_epsilon`</b>: float between 0 and 1. Error bound for quantile
    computation. This is only used for float feature columns, and the number
    of buckets generated per float feature is 1/quantile_sketch_epsilon.


#### Returns:

a `BoostedTreesClassifier` instance created with the given arguments and
  trained with the data loaded up on memory from the input_fn.



#### Raises:


* <b>`ValueError`</b>: when wrong arguments are given or unsupported functionalities
   are requested.
