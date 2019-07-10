page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.experimental.Generator

## Class `Generator`

Random-number generator.

Inherits From: [`Checkpointable`](../../../tf/contrib/checkpoint/Checkpointable)

### Aliases:

* Class `tf.compat.v1.random.experimental.Generator`
* Class `tf.compat.v2.random.experimental.Generator`
* Class `tf.random.experimental.Generator`



Defined in [`python/ops/stateful_random_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/stateful_random_ops.py).

<!-- Placeholder for "Used in" -->

It uses Variable to manage its internal state, and allows choosing an
Random-Number-Generation (RNG) algorithm.

CPU, GPU and TPU with the same algorithm and seed will generate the same
integer random numbers. Float-point results (such as the output of `normal`)
may have small numerical discrepancies between CPU and GPU.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    copy_from=None,
    state=None,
    alg=None
)
```

Creates a generator.

The new generator will be initialized by one of the following ways, with
decreasing precedence:
(1) If `copy_from` is not None, the new generator is initialized by copying
    information from another generator.
(3) If `state` and `alg` are not None (they must be set together), the new
    generator is initialized by a state.

#### Args:


* <b>`copy_from`</b>: a generator to be copied from.
* <b>`state`</b>: a vector of dtype STATE_TYPE representing the initial state of the
  RNG, whose length and semantics are algorithm-specific.
* <b>`alg`</b>: the RNG algorithm. Possible values are RNG_ALG_PHILOX for the
  Philox algorithm and RNG_ALG_THREEFRY for the ThreeFry
  algorithm (see paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
  [https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]).



## Properties

<h3 id="algorithm"><code>algorithm</code></h3>

The RNG algorithm.


<h3 id="key"><code>key</code></h3>

The 'key' part of the state of a counter-based RNG.

For a counter-base RNG algorithm such as Philox and ThreeFry (as
described in paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
[https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]),
the RNG state consists of two parts: counter and key. The output is
generated via the formula: output=hash(key, counter), i.e. a hashing of
the counter parametrized by the key. Two RNGs with two different keys can
be thought as generating two independent random-number streams (a stream
is formed by increasing the counter).

#### Returns:

A scalar which is the 'key' part of the state, if the RNG algorithm is
  counter-based; otherwise it raises a ValueError.


<h3 id="state"><code>state</code></h3>

The internal state of the RNG.




## Methods

<h3 id="binomial"><code>binomial</code></h3>

``` python
binomial(
    shape,
    counts,
    probs,
    dtype=tf.dtypes.int32,
    name=None
)
```

Outputs random values from a binomial distribution.

The generated values follow a binomial distribution with specified count and
probability of success parameters.

#### Example:



```python
counts = [10., 20.]
# Probability of success.
probs = [0.8, 0.9]

rng = tf.random.experimental.Generator(seed=234)
binomial_samples = rng.binomial(shape=[2], counts=counts, probs=probs)
```


#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output
  tensor.
* <b>`counts`</b>: A 0/1-D Tensor or Python value`. The counts of the binomial
  distribution.
* <b>`probs`</b>: A 0/1-D Tensor or Python value`. The probability of success for the
  binomial distribution.
* <b>`dtype`</b>: The type of the output. Default: tf.int32
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random binomial values.


<h3 id="from_key_counter"><code>from_key_counter</code></h3>

``` python
@classmethod
from_key_counter(
    cls,
    key,
    counter,
    alg
)
```

Creates a generator from a key and a counter.

This constructor only applies if the algorithm is a counter-based algorithm.
See method `key` for the meaning of "key" and "counter".

#### Args:


* <b>`key`</b>: the key for the RNG, a scalar of type STATE_TYPE.
* <b>`counter`</b>: a vector of dtype STATE_TYPE representing the initial counter for
  the RNG, whose length is algorithm-specific.,
* <b>`alg`</b>: the RNG algorithm. If None, it will be auto-selected. See
  `__init__` for its possible values.


#### Returns:

The new generator.


<h3 id="from_non_deterministic_state"><code>from_non_deterministic_state</code></h3>

``` python
@classmethod
from_non_deterministic_state(
    cls,
    alg=None
)
```

Creates a generator by non-deterministically initializing its state.

The source of the non-determinism will be platform- and time-dependent.

#### Args:


* <b>`alg`</b>: (optional) the RNG algorithm. If None, it will be auto-selected. See
  `__init__` for its possible values.


#### Returns:

The new generator.


<h3 id="from_seed"><code>from_seed</code></h3>

``` python
@classmethod
from_seed(
    cls,
    seed,
    alg=None
)
```

Creates a generator from a seed.

A seed is a 1024-bit unsigned integer represented either as a Python
integer or a vector of integers. Seeds shorter than 1024-bit will be
padded. The padding, the internal structure of a seed and the way a seed
is converted to a state are all opaque (unspecified). The only semantics
specification of seeds is that two different seeds are likely to produce
two independent generators (but no guarantee).

#### Args:


* <b>`seed`</b>: the seed for the RNG.
* <b>`alg`</b>: (optional) the RNG algorithm. If None, it will be auto-selected. See
  `__init__` for its possible values.


#### Returns:

The new generator.


<h3 id="from_state"><code>from_state</code></h3>

``` python
@classmethod
from_state(
    cls,
    state,
    alg
)
```

Creates a generator from a state.

See `__init__` for description of `state` and `alg`.

#### Args:


* <b>`state`</b>: the new state.
* <b>`alg`</b>: the RNG algorithm.


#### Returns:

The new generator.


<h3 id="make_seeds"><code>make_seeds</code></h3>

``` python
make_seeds(count=1)
```

Generates seeds for stateless random ops.


#### For example:



```python
seeds = get_global_generator().make_seeds(count=10)
for i in range(10):
  seed = seeds[:, i]
  numbers = stateless_random_normal(shape=[2, 3], seed=seed)
  ...
```

#### Args:


* <b>`count`</b>: the number of seed pairs (note that stateless random ops need a
  pair of seeds to invoke).


#### Returns:

A tensor of shape [2, count] and dtype int64.


<h3 id="normal"><code>normal</code></h3>

``` python
normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    name=None
)
```

Outputs random values from a normal distribution.


#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output
  tensor.
* <b>`mean`</b>: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
  distribution.
* <b>`stddev`</b>: A 0-D Tensor or Python value of type `dtype`. The standard
  deviation of the normal distribution.
* <b>`dtype`</b>: The type of the output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random normal values.


<h3 id="reset"><code>reset</code></h3>

``` python
reset(state)
```

Resets the generator by a new state.

See `__init__` for the meaning of "state".

#### Args:


* <b>`state`</b>: the new state.

<h3 id="reset_from_key_counter"><code>reset_from_key_counter</code></h3>

``` python
reset_from_key_counter(
    key,
    counter
)
```

Resets the generator by a new key-counter pair.

See `from_key_counter` for the meaning of "key" and "counter".

#### Args:


* <b>`key`</b>: the new key.
* <b>`counter`</b>: the new counter.

<h3 id="reset_from_seed"><code>reset_from_seed</code></h3>

``` python
reset_from_seed(seed)
```

Resets the generator by a new seed.

See `from_seed` for the meaning of "seed".

#### Args:


* <b>`seed`</b>: the new seed.

<h3 id="skip"><code>skip</code></h3>

``` python
skip(delta)
```

Advance the counter of a counter-based RNG.


#### Args:


* <b>`delta`</b>: the amount of advancement. The state of the RNG after
  `skip(n)` will be the same as that after `normal([n])`
  (or any other distribution). The actual increment added to the
  counter is an unspecified implementation detail.

<h3 id="split"><code>split</code></h3>

``` python
split(count=1)
```

Returns a list of independent `Generator` objects.

Two generators are independent of each other in the sense that the
random-number streams they generate don't have statistically detectable
correlations. The new generators are also independent of the old one.
The old generator's state will be changed (like other random-number
generating methods), so two calls of `split` will return different
new generators.

#### For example:



```python
gens = get_global_generator().split(count=10)
for gen in gens:
  numbers = gen.normal(shape=[2, 3])
  # ...
gens2 = get_global_generator().split(count=10)
# gens2 will be different from gens
```

The new generators will be put on the current device (possible different
from the old generator's), for example:

```python
with tf.device("/device:CPU:0"):
  gen = Generator(seed=1234)  # gen is on CPU
with tf.device("/device:GPU:0"):
  gens = gen.split(count=10)  # gens are on GPU
```

#### Args:


* <b>`count`</b>: the number of generators to return.


#### Returns:

A list (length `count`) of `Generator` objects independent of each other.
The new generators have the same RNG algorithm as the old one.


<h3 id="truncated_normal"><code>truncated_normal</code></h3>

``` python
truncated_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    name=None
)
```

Outputs random values from a truncated normal distribution.

The generated values follow a normal distribution with specified mean and
standard deviation, except that values whose magnitude is more than
2 standard deviations from the mean are dropped and re-picked.

#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output
  tensor.
* <b>`mean`</b>: A 0-D Tensor or Python value of type `dtype`. The mean of the
  truncated normal distribution.
* <b>`stddev`</b>: A 0-D Tensor or Python value of type `dtype`. The standard
  deviation of the normal distribution, before truncation.
* <b>`dtype`</b>: The type of the output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random truncated normal
  values.


<h3 id="uniform"><code>uniform</code></h3>

``` python
uniform(
    shape,
    minval=0,
    maxval=None,
    dtype=tf.dtypes.float32,
    name=None
)
```

Outputs random values from a uniform distribution.

The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while
the upper bound `maxval` is excluded. (For float numbers especially
low-precision types like bfloat16, because of
rounding, the result may sometimes include `maxval`.)

For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
be specified explicitly.

In the integer case, the random integers are slightly biased unless
`maxval - minval` is an exact power of two.  The bias is small for values of
`maxval - minval` significantly smaller than the range of the output (either
`2**32` or `2**64`).

#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output
  tensor.
* <b>`minval`</b>: A 0-D Tensor or Python value of type `dtype`. The lower bound on
  the range of random values to generate.  Defaults to 0.
* <b>`maxval`</b>: A 0-D Tensor or Python value of type `dtype`. The upper bound on
  the range of random values to generate.  Defaults to 1 if `dtype` is
  floating point.
* <b>`dtype`</b>: The type of the output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random uniform values.



#### Raises:


* <b>`ValueError`</b>: If `dtype` is integral and `maxval` is not specified.

<h3 id="uniform_full_int"><code>uniform_full_int</code></h3>

``` python
uniform_full_int(
    shape,
    dtype=tf.dtypes.uint64,
    name=None
)
```

Uniform distribution on an integer type's entire range.

The other method `uniform` only covers the range [minval, maxval), which
cannot be `dtype`'s full range because `maxval` is of type `dtype`.

#### Args:


* <b>`shape`</b>: the shape of the output.
* <b>`dtype`</b>: (optional) the integer type, default to uint64.
* <b>`name`</b>: (optional) the name of the node.


#### Returns:

A tensor of random numbers of the required shape.




