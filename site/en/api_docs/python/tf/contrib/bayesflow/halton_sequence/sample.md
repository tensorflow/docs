

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.halton_sequence.sample

``` python
sample(
    dim,
    num_samples=None,
    sample_indices=None,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/contrib/bayesflow/python/ops/halton_sequence_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/bayesflow/python/ops/halton_sequence_impl.py).

Returns a sample from the `m` dimensional Halton sequence.

Warning: The sequence elements take values only between 0 and 1. Care must be
taken to appropriately transform the domain of a function if it differs from
the unit cube before evaluating integrals using Halton samples. It is also
important to remember that quasi-random numbers are not a replacement for
pseudo-random numbers in every context. Quasi random numbers are completely
deterministic and typically have significant negative autocorrelation (unless
randomized).

Computes the members of the low discrepancy Halton sequence in dimension
`dim`. The d-dimensional sequence takes values in the unit hypercube in d
dimensions. Currently, only dimensions up to 1000 are supported. The prime
base for the `k`-th axes is the k-th prime starting from 2. For example,
if dim = 3, then the bases will be [2, 3, 5] respectively and the first
element of the sequence will be: [0.5, 0.333, 0.2]. For a more complete
description of the Halton sequences see:
https://en.wikipedia.org/wiki/Halton_sequence. For low discrepancy sequences
and their applications see:
https://en.wikipedia.org/wiki/Low-discrepancy_sequence.

The user must supply either `num_samples` or `sample_indices` but not both.
The former is the number of samples to produce starting from the first
element. If `sample_indices` is given instead, the specified elements of
the sequence are generated. For example, sample_indices=tf.range(10) is
equivalent to specifying n=10.

Example Use:

```python
bf = tf.contrib.bayesflow

# Produce the first 1000 members of the Halton sequence in 3 dimensions.
num_samples = 1000
dim = 3
sample = bf.halton_sequence.sample(dim, num_samples=num_samples)

# Evaluate the integral of x_1 * x_2^2 * x_3^3  over the three dimensional
# hypercube.
powers = tf.range(1.0, limit=dim + 1)
integral = tf.reduce_mean(tf.reduce_prod(sample ** powers, axis=-1))
true_value = 1.0 / tf.reduce_prod(powers + 1.0)
with tf.Session() as session:
  values = session.run((integral, true_value))

# Produces a relative absolute error of 1.7%.
print ("Estimated: %f, True Value: %f" % values)

# Now skip the first 1000 samples and recompute the integral with the next
# thousand samples. The sample_indices argument can be used to do this.


sample_indices = tf.range(start=1000, limit=1000 + num_samples,
                          dtype=tf.int32)
sample_leaped = halton.sample(dim, sample_indices=sample_indices)

integral_leaped = tf.reduce_mean(tf.reduce_prod(sample_leaped ** powers,
                                                axis=-1))
with tf.Session() as session:
  values = session.run((integral_leaped, true_value))
# Now produces a relative absolute error of 0.05%.
print ("Leaped Estimated: %f, True Value: %f" % values)
```

#### Args:

* <b>`dim`</b>: Positive Python `int` representing each sample's `event_size.` Must
    not be greater than 1000.
* <b>`num_samples`</b>: (Optional) positive Python `int`. The number of samples to
    generate. Either this parameter or sample_indices must be specified but
    not both. If this parameter is None, then the behaviour is determined by
    the `sample_indices`.
* <b>`sample_indices`</b>: (Optional) `Tensor` of dtype int32 and rank 1. The elements
    of the sequence to compute specified by their position in the sequence.
    The entries index into the Halton sequence starting with 0 and hence,
    must be whole numbers. For example, sample_indices=[0, 5, 6] will produce
    the first, sixth and seventh elements of the sequence. If this parameter
    is None, then the `num_samples` parameter must be specified which gives
    the number of desired samples starting from the first sample.
* <b>`dtype`</b>: (Optional) The dtype of the sample. One of `float32` or `float64`.
    Default is `float32`.
* <b>`name`</b>:  (Optional) Python `str` describing ops managed by this function. If
  not supplied the name of this function is used.


#### Returns:

* <b>`halton_elements`</b>: Elements of the Halton sequence. `Tensor` of supplied dtype
  and `shape` `[num_samples, dim]` if `num_samples` was specified or shape
  `[s, dim]` where s is the size of `sample_indices` if `sample_indices`
  were specified.


#### Raises:

* <b>`ValueError`</b>: if both `sample_indices` and `num_samples` were specified or
  if dimension `dim` is less than 1 or greater than 1000.