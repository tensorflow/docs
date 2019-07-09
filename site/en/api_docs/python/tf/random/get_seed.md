page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.get_seed

### Aliases:

* `tf.get_seed`
* `tf.random.get_seed`

``` python
tf.random.get_seed(op_seed)
```



Defined in [`tensorflow/python/framework/random_seed.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/random_seed.py).

Returns the local seeds an operation should use given an op-specific seed.

Given operation-specific seed, `op_seed`, this helper function returns two
seeds derived from graph-level and op-level seeds. Many random operations
internally use the two seeds to allow user to change the seed globally for a
graph, or for only specific operations.

For details on how the graph-level seed interacts with op seeds, see
<a href="../../tf/random/set_random_seed"><code>tf.random.set_random_seed</code></a>.

#### Args:

* <b>`op_seed`</b>: integer.


#### Returns:

A tuple of two integers that should be used for the local seed of this
operation.