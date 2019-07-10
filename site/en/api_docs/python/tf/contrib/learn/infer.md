page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.infer

``` python
tf.contrib.learn.infer(
    restore_checkpoint_path,
    output_dict,
    feed_dict=None
)
```



Defined in [`tensorflow/contrib/learn/python/learn/graph_actions.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/learn/python/learn/graph_actions.py).

Restore graph from `restore_checkpoint_path` and run `output_dict` tensors. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2017-02-15.
Instructions for updating:
graph_actions.py will be deleted. Use tf.train.* utilities instead. You can use learn/estimators/estimator.py as an example.

If `restore_checkpoint_path` is supplied, restore from checkpoint. Otherwise,
init all variables.

#### Args:

* <b>`restore_checkpoint_path`</b>: A string containing the path to a checkpoint to
    restore.
* <b>`output_dict`</b>: A `dict` mapping string names to `Tensor` objects to run.
    Tensors must all be from the same graph.
* <b>`feed_dict`</b>: `dict` object mapping `Tensor` objects to input values to feed.


#### Returns:

Dict of values read from `output_dict` tensors. Keys are the same as
`output_dict`, values are the results read from the corresponding `Tensor`
in `output_dict`.


#### Raises:

* <b>`ValueError`</b>: if `output_dict` or `feed_dicts` is None or empty.