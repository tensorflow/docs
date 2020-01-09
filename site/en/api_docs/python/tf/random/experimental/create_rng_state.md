page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.experimental.create_rng_state


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/stateful_random_ops.py#L140-L151">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a RNG state.

### Aliases:

* `tf.compat.v1.random.experimental.create_rng_state`
* `tf.compat.v2.random.experimental.create_rng_state`


``` python
tf.random.experimental.create_rng_state(
    seed,
    algorithm
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`seed`</b>: an integer or 1-D tensor.
* <b>`algorithm`</b>: an integer representing the RNG algorithm.


#### Returns:

a 1-D tensor whose size depends on the algorithm.
