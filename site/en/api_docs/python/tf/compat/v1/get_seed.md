page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.get_seed


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/random_seed.py#L37-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the local seeds an operation should use given an op-specific seed.

### Aliases:

* `tf.compat.v1.random.get_seed`


``` python
tf.compat.v1.get_seed(op_seed)
```



<!-- Placeholder for "Used in" -->

Given operation-specific seed, `op_seed`, this helper function returns two
seeds derived from graph-level and op-level seeds. Many random operations
internally use the two seeds to allow user to change the seed globally for a
graph, or for only specific operations.

For details on how the graph-level seed interacts with op seeds, see
<a href="../../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.random.set_random_seed</code></a>.

#### Args:


* <b>`op_seed`</b>: integer.


#### Returns:

A tuple of two integers that should be used for the local seed of this
operation.
