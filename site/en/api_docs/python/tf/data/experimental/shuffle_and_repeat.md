page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.shuffle_and_repeat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/shuffle_ops.py#L54-L92">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Shuffles and repeats a Dataset returning a new permutation for each epoch. (deprecated)

### Aliases:

* `tf.compat.v1.data.experimental.shuffle_and_repeat`
* `tf.compat.v2.data.experimental.shuffle_and_repeat`


``` python
tf.data.experimental.shuffle_and_repeat(
    buffer_size,
    count=None,
    seed=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/Dataset#shuffle"><code>tf.data.Dataset.shuffle(buffer_size, seed)</code></a> followed by <a href="../../../tf/data/Dataset#repeat"><code>tf.data.Dataset.repeat(count)</code></a>. Static tf.data optimizations will take care of using the fused implementation.

`dataset.apply(tf.data.experimental.shuffle_and_repeat(buffer_size, count))`

is equivalent to

`dataset.shuffle(buffer_size, reshuffle_each_iteration=True).repeat(count)`

The difference is that the latter dataset is not serializable. So,
if you need to checkpoint an input pipeline with reshuffling you must use
this implementation.

#### Args:


* <b>`buffer_size`</b>: A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
  maximum number elements that will be buffered when prefetching.
* <b>`count`</b>: (Optional.) A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
  number of times the dataset should be repeated. The default behavior
  (if `count` is `None` or `-1`) is for the dataset be repeated
  indefinitely.
* <b>`seed`</b>: (Optional.) A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
  random seed that will be used to create the distribution. See
  <a href="../../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
