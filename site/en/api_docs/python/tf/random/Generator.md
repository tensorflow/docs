description: Random-number generator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.Generator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="binomial"/>
<meta itemprop="property" content="from_key_counter"/>
<meta itemprop="property" content="from_non_deterministic_state"/>
<meta itemprop="property" content="from_seed"/>
<meta itemprop="property" content="from_state"/>
<meta itemprop="property" content="make_seeds"/>
<meta itemprop="property" content="normal"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_from_key_counter"/>
<meta itemprop="property" content="reset_from_seed"/>
<meta itemprop="property" content="skip"/>
<meta itemprop="property" content="split"/>
<meta itemprop="property" content="truncated_normal"/>
<meta itemprop="property" content="uniform"/>
<meta itemprop="property" content="uniform_full_int"/>
</div>

# tf.random.Generator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L259-L904">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Random-number generator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.random.experimental.Generator`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.Generator`, `tf.compat.v1.random.experimental.Generator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.Generator(
    copy_from=None, state=None, alg=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



Creating a generator from a seed:

```
>>> g = tf.random.Generator.from_seed(1234)
>>> g.normal(shape=(2, 3))
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[ 0.9356609 ,  1.0854305 , -0.93788373],
       [-0.5061547 ,  1.3169702 ,  0.7137579 ]], dtype=float32)>
```

Creating a generator from a non-deterministic state:

```
>>> g = tf.random.Generator.from_non_deterministic_state()
>>> g.normal(shape=(2, 3))
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=...>
```

All the constructors allow explicitly choosing an Random-Number-Generation
(RNG) algorithm. Supported algorithms are `"philox"` and `"threefry"`. For
example:

```
>>> g = tf.random.Generator.from_seed(123, alg="philox")
>>> g.normal(shape=(2, 3))
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[ 0.8673864 , -0.29899067, -0.9310337 ],
       [-1.5828488 ,  1.2481191 , -0.6770643 ]], dtype=float32)>
```

CPU, GPU and TPU with the same algorithm and seed will generate the same
integer random numbers. Float-point results (such as the output of `normal`)
may have small numerical discrepancies between different devices.

This class uses a <a href="../../tf/Variable.md"><code>tf.Variable</code></a> to manage its internal state. Every time
random numbers are generated, the state of the generator will change. For
example:

```
>>> g = tf.random.Generator.from_seed(1234)
>>> g.state
<tf.Variable ... numpy=array([1234,    0,    0])>
>>> g.normal(shape=(2, 3))
<...>
>>> g.state
<tf.Variable ... numpy=array([2770,    0,    0])>
```

The shape of the state is algorithm-specific.

There is also a global generator:

```
>>> g = tf.random.get_global_generator()
>>> g.normal(shape=(2, 3))
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=...>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`copy_from`
</td>
<td>
a generator to be copied from.
</td>
</tr><tr>
<td>
`state`
</td>
<td>
a vector of dtype STATE_TYPE representing the initial state of the
RNG, whose length and semantics are algorithm-specific. If it's a
variable, the generator will reuse it instead of creating a new
variable.
</td>
</tr><tr>
<td>
`alg`
</td>
<td>
the RNG algorithm. Possible values are
<a href="../../tf/random/Algorithm.md#PHILOX"><code>tf.random.Algorithm.PHILOX</code></a> for the Philox algorithm and
<a href="../../tf/random/Algorithm.md#THREEFRY"><code>tf.random.Algorithm.THREEFRY</code></a> for the ThreeFry algorithm
(see paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
[https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]).
The string names `"philox"` and `"threefry"` can also be used.
Note `PHILOX` guarantees the same numbers are produced (given
the same random state) across all architectures (CPU, GPU, XLA etc).
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`algorithm`
</td>
<td>
The RNG algorithm id (a Python integer or scalar integer Tensor).
</td>
</tr><tr>
<td>
`key`
</td>
<td>
The 'key' part of the state of a counter-based RNG.

For a counter-base RNG algorithm such as Philox and ThreeFry (as
described in paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
[https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]),
the RNG state consists of two parts: counter and key. The output is
generated via the formula: output=hash(key, counter), i.e. a hashing of
the counter parametrized by the key. Two RNGs with two different keys can
be thought as generating two independent random-number streams (a stream
is formed by increasing the counter).
</td>
</tr><tr>
<td>
`state`
</td>
<td>
The internal state of the RNG.
</td>
</tr>
</table>



## Methods

<h3 id="binomial"><code>binomial</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L759-L815">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>binomial(
    shape, counts, probs, dtype=tf.dtypes.int32, name=None
)
</code></pre>

Outputs random values from a binomial distribution.

The generated values follow a binomial distribution with specified count and
probability of success parameters.

#### Example:



```python
counts = [10., 20.]
# Probability of success.
probs = [0.8]

rng = tf.random.Generator.from_seed(seed=234)
binomial_samples = rng.binomial(shape=[2], counts=counts, probs=probs)


counts = ... # Shape [3, 1, 2]
probs = ...  # Shape [1, 4, 2]
shape = [3, 4, 3, 4, 2]
rng = tf.random.Generator.from_seed(seed=1717)
# Sample shape will be [3, 4, 3, 4, 2]
binomial_samples = rng.binomial(shape=shape, counts=counts, probs=probs)
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output
tensor.
</td>
</tr><tr>
<td>
`counts`
</td>
<td>
Tensor. The counts of the binomial distribution. Must be
broadcastable with `probs`, and broadcastable with the rightmost
dimensions of `shape`.
</td>
</tr><tr>
<td>
`probs`
</td>
<td>
Tensor. The probability of success for the
binomial distribution. Must be broadcastable with `counts` and
broadcastable with the rightmost dimensions of `shape`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output. Default: tf.int32
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`samples`
</td>
<td>
A Tensor of the specified shape filled with random binomial
values.  For each i, each samples[i, ...] is an independent draw from
the binomial distribution on counts[i] trials with probability of
success probs[i].
</td>
</tr>
</table>



<h3 id="from_key_counter"><code>from_key_counter</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L472-L504">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_key_counter(
    key, counter, alg
)
</code></pre>

Creates a generator from a key and a counter.

This constructor only applies if the algorithm is a counter-based algorithm.
See method `key` for the meaning of "key" and "counter".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`key`
</td>
<td>
the key for the RNG, a scalar of type STATE_TYPE.
</td>
</tr><tr>
<td>
`counter`
</td>
<td>
a vector of dtype STATE_TYPE representing the initial counter for
the RNG, whose length is algorithm-specific.,
</td>
</tr><tr>
<td>
`alg`
</td>
<td>
the RNG algorithm. If None, it will be auto-selected. See
`__init__` for its possible values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The new generator.
</td>
</tr>

</table>



#### Throws:


* <b>`ValueError`</b>: if the generator is created inside a synchronous
  <a href="../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as `MirroredStrategy` or `TPUStrategy`,
  because there is ambiguity on how to replicate a generator (e.g. should
  it be copied so such each replica will get the same random numbers, or
  should it be "split" into different generators that generate
  different random numbers).


<h3 id="from_non_deterministic_state"><code>from_non_deterministic_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L443-L470">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_non_deterministic_state(
    alg=None
)
</code></pre>

Creates a generator by non-deterministically initializing its state.

The source of the non-determinism will be platform- and time-dependent.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`alg`
</td>
<td>
(optional) the RNG algorithm. If None, it will be auto-selected. See
`__init__` for its possible values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The new generator.
</td>
</tr>

</table>



#### Throws:


* <b>`ValueError`</b>: if the generator is created inside a synchronous
  <a href="../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as `MirroredStrategy` or `TPUStrategy`,
  because there is ambiguity on how to replicate a generator (e.g. should
  it be copied so such each replica will get the same random numbers, or
  should it be "split" into different generators that generate
  different random numbers).


<h3 id="from_seed"><code>from_seed</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L409-L441">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_seed(
    seed, alg=None
)
</code></pre>

Creates a generator from a seed.

A seed is a 1024-bit unsigned integer represented either as a Python
integer or a vector of integers. Seeds shorter than 1024-bit will be
padded. The padding, the internal structure of a seed and the way a seed
is converted to a state are all opaque (unspecified). The only semantics
specification of seeds is that two different seeds are likely to produce
two independent generators (but no guarantee).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`seed`
</td>
<td>
the seed for the RNG.
</td>
</tr><tr>
<td>
`alg`
</td>
<td>
(optional) the RNG algorithm. If None, it will be auto-selected. See
`__init__` for its possible values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The new generator.
</td>
</tr>

</table>



#### Throws:


* <b>`ValueError`</b>: if the generator is created inside a synchronous
  <a href="../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as `MirroredStrategy` or `TPUStrategy`,
  because there is ambiguity on how to replicate a generator (e.g. should
  it be copied so such each replica will get the same random numbers, or
  should it be "split" into different generators that generate
  different random numbers).


<h3 id="from_state"><code>from_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L386-L407">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_state(
    state, alg
)
</code></pre>

Creates a generator from a state.

See `__init__` for description of `state` and `alg`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`state`
</td>
<td>
the new state.
</td>
</tr><tr>
<td>
`alg`
</td>
<td>
the RNG algorithm.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The new generator.
</td>
</tr>

</table>



#### Throws:


* <b>`ValueError`</b>: if the generator is created inside a synchronous
  <a href="../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as `MirroredStrategy` or `TPUStrategy`,
  because there is ambiguity on how to replicate a generator (e.g. should
  it be copied so such each replica will get the same random numbers, or
  should it be "split" into different generators that generate
  different random numbers).


<h3 id="make_seeds"><code>make_seeds</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L826-L854">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_seeds(
    count=1
)
</code></pre>

Generates seeds for stateless random ops.


#### For example:



```python
seeds = get_global_generator().make_seeds(count=10)
for i in range(10):
  seed = seeds[:, i]
  numbers = stateless_random_normal(shape=[2, 3], seed=seed)
  ...
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`count`
</td>
<td>
the number of seed pairs (note that stateless random ops need a
pair of seeds to invoke).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor of shape [2, count] and dtype int64.
</td>
</tr>

</table>



<h3 id="normal"><code>normal</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L602-L624">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>normal(
    shape, mean=0.0, stddev=1.0, dtype=tf.dtypes.float32, name=None
)
</code></pre>

Outputs random values from a normal distribution.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output
tensor.
</td>
</tr><tr>
<td>
`mean`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The mean of the normal
distribution.
</td>
</tr><tr>
<td>
`stddev`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The standard
deviation of the normal distribution.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor of the specified shape filled with random normal values.
</td>
</tr>

</table>



<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L506-L516">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset(
    state
)
</code></pre>

Resets the generator by a new state.

See `__init__` for the meaning of "state".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`state`
</td>
<td>
the new state.
</td>
</tr>
</table>



<h3 id="reset_from_key_counter"><code>reset_from_key_counter</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L529-L545">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_from_key_counter(
    key, counter
)
</code></pre>

Resets the generator by a new key-counter pair.

See `from_key_counter` for the meaning of "key" and "counter".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`key`
</td>
<td>
the new key.
</td>
</tr><tr>
<td>
`counter`
</td>
<td>
the new counter.
</td>
</tr>
</table>



<h3 id="reset_from_seed"><code>reset_from_seed</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L518-L527">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_from_seed(
    seed
)
</code></pre>

Resets the generator by a new seed.

See `from_seed` for the meaning of "seed".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`seed`
</td>
<td>
the new seed.
</td>
</tr>
</table>



<h3 id="skip"><code>skip</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L589-L598">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>skip(
    delta
)
</code></pre>

Advance the counter of a counter-based RNG.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`delta`
</td>
<td>
the amount of advancement. The state of the RNG after
`skip(n)` will be the same as that after `normal([n])`
(or any other distribution). The actual increment added to the
counter is an unspecified implementation detail.
</td>
</tr>
</table>



<h3 id="split"><code>split</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L856-L904">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>split(
    count=1
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`count`
</td>
<td>
the number of generators to return.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list (length `count`) of `Generator` objects independent of each other.
The new generators have the same RNG algorithm as the old one.
</td>
</tr>

</table>



<h3 id="truncated_normal"><code>truncated_normal</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L630-L662">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>truncated_normal(
    shape, mean=0.0, stddev=1.0, dtype=tf.dtypes.float32, name=None
)
</code></pre>

Outputs random values from a truncated normal distribution.

The generated values follow a normal distribution with specified mean and
standard deviation, except that values whose magnitude is more than
2 standard deviations from the mean are dropped and re-picked.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output
tensor.
</td>
</tr><tr>
<td>
`mean`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The mean of the
truncated normal distribution.
</td>
</tr><tr>
<td>
`stddev`
</td>
<td>
A 0-D Tensor or Python value of type `dtype`. The standard
deviation of the normal distribution, before truncation.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor of the specified shape filled with random truncated normal
values.
</td>
</tr>

</table>



<h3 id="uniform"><code>uniform</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L673-L737">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>uniform(
    shape, minval=0, maxval=None, dtype=tf.dtypes.float32, name=None
)
</code></pre>

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

For full-range random integers, pass `minval=None` and `maxval=None` with an
integer `dtype` (for integer dtypes, `minval` and `maxval` must be both
`None` or both not `None`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output
tensor.
</td>
</tr><tr>
<td>
`minval`
</td>
<td>
A Tensor or Python value of type `dtype`, broadcastable with
`shape` (for integer types, broadcasting is not supported, so it needs
to be a scalar). The lower bound (included) on the range of random
values to generate. Pass `None` for full-range integers. Defaults to 0.
</td>
</tr><tr>
<td>
`maxval`
</td>
<td>
A Tensor or Python value of type `dtype`, broadcastable with
`shape` (for integer types, broadcasting is not supported, so it needs
to be a scalar). The upper bound (excluded) on the range of random
values to generate. Pass `None` for full-range integers. Defaults to 1
if `dtype` is floating point.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor of the specified shape filled with random uniform values.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `dtype` is integral and `maxval` is not specified.
</td>
</tr>
</table>



<h3 id="uniform_full_int"><code>uniform_full_int</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateful_random_ops.py#L739-L757">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>uniform_full_int(
    shape, dtype=tf.dtypes.uint64, name=None
)
</code></pre>

Uniform distribution on an integer type's entire range.

This method is the same as setting `minval` and `maxval` to `None` in the
`uniform` method.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
the shape of the output.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(optional) the integer type, default to uint64.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(optional) the name of the node.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor of random numbers of the required shape.
</td>
</tr>

</table>





