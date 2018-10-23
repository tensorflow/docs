

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.all_candidate_sampler

``` python
tf.nn.all_candidate_sampler(
    true_classes,
    num_true,
    num_sampled,
    unique,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/candidate_sampling_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/candidate_sampling_ops.py).

Generate the set of all classes.

Deterministically generates and returns the set of all possible classes.
For testing purposes.  There is no need to use this, since you might as
well use full softmax or full logistic regression.

#### Args:

* <b>`true_classes`</b>: A `Tensor` of type `int64` and shape `[batch_size,
    num_true]`. The target classes.
* <b>`num_true`</b>: An `int`.  The number of target classes per training example.
* <b>`num_sampled`</b>: An `int`.  The number of possible classes.
* <b>`unique`</b>: A `bool`. Ignored.
    unique.
* <b>`seed`</b>: An `int`. An operation-specific seed. Default is 0.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

* <b>`sampled_candidates`</b>: A tensor of type `int64` and shape `[num_sampled]`.
    This operation deterministically returns the entire range
    `[0, num_sampled]`.
* <b>`true_expected_count`</b>: A tensor of type `float`.  Same shape as
    `true_classes`. The expected counts under the sampling distribution
    of each of `true_classes`. All returned values are 1.0.
* <b>`sampled_expected_count`</b>: A tensor of type `float`. Same shape as
    `sampled_candidates`. The expected counts under the sampling distribution
    of each of `sampled_candidates`. All returned values are 1.0.