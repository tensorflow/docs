description: Public API for tf.random namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.random" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.random

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.random namespace.



## Modules

[`experimental`](../../../tf/compat/v1/random/experimental.md) module: Public API for tf.random.experimental namespace.

## Classes

[`class Algorithm`](../../../tf/random/Algorithm.md): An enumeration.

[`class Generator`](../../../tf/random/Generator.md): Random-number generator.

## Functions

[`all_candidate_sampler(...)`](../../../tf/random/all_candidate_sampler.md): Generate the set of all classes.

[`categorical(...)`](../../../tf/random/categorical.md): Draws samples from a categorical distribution.

[`create_rng_state(...)`](../../../tf/random/create_rng_state.md): Creates a RNG state from an integer or a vector.

[`fixed_unigram_candidate_sampler(...)`](../../../tf/random/fixed_unigram_candidate_sampler.md): Samples a set of classes using the provided (fixed) base distribution.

[`gamma(...)`](../../../tf/random/gamma.md): Draws `shape` samples from each of the given Gamma distribution(s).

[`get_global_generator(...)`](../../../tf/random/get_global_generator.md): Retrieves the global generator.

[`get_seed(...)`](../../../tf/compat/v1/get_seed.md): Returns the local seeds an operation should use given an op-specific seed.

[`learned_unigram_candidate_sampler(...)`](../../../tf/random/learned_unigram_candidate_sampler.md): Samples a set of classes from a distribution learned during training.

[`log_uniform_candidate_sampler(...)`](../../../tf/random/log_uniform_candidate_sampler.md): Samples a set of classes using a log-uniform (Zipfian) base distribution.

[`multinomial(...)`](../../../tf/compat/v1/multinomial.md): Draws samples from a multinomial distribution. (deprecated)

[`normal(...)`](../../../tf/random/normal.md): Outputs random values from a normal distribution.

[`poisson(...)`](../../../tf/compat/v1/random_poisson.md): Draws `shape` samples from each of the given Poisson distribution(s).

[`set_global_generator(...)`](../../../tf/random/set_global_generator.md): Replaces the global generator with another `Generator` object.

[`set_random_seed(...)`](../../../tf/compat/v1/set_random_seed.md): Sets the graph-level random seed for the default graph.

[`shuffle(...)`](../../../tf/random/shuffle.md): Randomly shuffles a tensor along its first dimension.

[`stateless_binomial(...)`](../../../tf/random/stateless_binomial.md): Outputs deterministic pseudorandom values from a binomial distribution.

[`stateless_categorical(...)`](../../../tf/random/stateless_categorical.md): Draws deterministic pseudorandom samples from a categorical distribution.

[`stateless_gamma(...)`](../../../tf/random/stateless_gamma.md): Outputs deterministic pseudorandom values from a gamma distribution.

[`stateless_multinomial(...)`](../../../tf/compat/v1/random/stateless_multinomial.md): Draws deterministic pseudorandom samples from a multinomial distribution. (deprecated)

[`stateless_normal(...)`](../../../tf/random/stateless_normal.md): Outputs deterministic pseudorandom values from a normal distribution.

[`stateless_parameterized_truncated_normal(...)`](../../../tf/random/stateless_parameterized_truncated_normal.md): Outputs random values from a truncated normal distribution.

[`stateless_poisson(...)`](../../../tf/random/stateless_poisson.md): Outputs deterministic pseudorandom values from a Poisson distribution.

[`stateless_truncated_normal(...)`](../../../tf/random/stateless_truncated_normal.md): Outputs deterministic pseudorandom values, truncated normally distributed.

[`stateless_uniform(...)`](../../../tf/random/stateless_uniform.md): Outputs deterministic pseudorandom values from a uniform distribution.

[`truncated_normal(...)`](../../../tf/random/truncated_normal.md): Outputs random values from a truncated normal distribution.

[`uniform(...)`](../../../tf/random/uniform.md): Outputs random values from a uniform distribution.

[`uniform_candidate_sampler(...)`](../../../tf/random/uniform_candidate_sampler.md): Samples a set of classes using a uniform base distribution.

