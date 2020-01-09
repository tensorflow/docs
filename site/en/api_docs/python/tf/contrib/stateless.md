page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.stateless


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/stateless/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stateless random ops which take seed as a tensor input.

<!-- Placeholder for "Used in" -->

DEPRECATED: Use <a href="../../tf/random/stateless_uniform"><code>tf.random.stateless_uniform</code></a> rather than
<a href="../../tf/random/stateless_uniform"><code>tf.contrib.stateless.stateless_random_uniform</code></a>, and similarly for the other
routines.

Instead of taking `seed` as an attr which initializes a mutable state within
the op, these random ops take `seed` as an input, and the random numbers are
a deterministic function of `shape` and `seed`.

WARNING: These ops are in contrib, and are not stable.  They should be
consistent across multiple runs on the same hardware, but only for the same
version of the code.


## Functions

[`stateless_multinomial(...)`](../../tf/random/stateless_multinomial): Draws deterministic pseudorandom samples from a multinomial distribution. (deprecated)

[`stateless_random_normal(...)`](../../tf/random/stateless_normal): Outputs deterministic pseudorandom values from a normal distribution.

[`stateless_random_uniform(...)`](../../tf/random/stateless_uniform): Outputs deterministic pseudorandom values from a uniform distribution.

[`stateless_truncated_normal(...)`](../../tf/random/stateless_truncated_normal): Outputs deterministic pseudorandom values, truncated normally distributed.
