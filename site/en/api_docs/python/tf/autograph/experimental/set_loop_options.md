page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.experimental.set_loop_options

Specifies additional arguments to be passed to the enclosing while_loop.

### Aliases:

* `tf.autograph.experimental.set_loop_options`
* `tf.compat.v1.autograph.experimental.set_loop_options`
* `tf.compat.v2.autograph.experimental.set_loop_options`
* `tf.contrib.autograph.set_loop_options`

``` python
tf.autograph.experimental.set_loop_options(
    parallel_iterations=UNSPECIFIED,
    back_prop=UNSPECIFIED,
    swap_memory=UNSPECIFIED,
    maximum_iterations=UNSPECIFIED
)
```



Defined in [`python/autograph/lang/directives.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/lang/directives.py).

<!-- Placeholder for "Used in" -->

The parameters apply to and only to the immediately enclosing loop. It only
has effect if the loop is staged as a TF while_loop; otherwise the parameters
have no effect.

#### Usage example:


@tf.function(autograph=True)
def dynamic_rnn(..., parallel_iterations=32):
  num_steps = ...
  for t in tf.range(num_steps):
    tf.autograph.experimental.set_loop_options(
        parallel_iterations=parallel_iterations)
    ...



#### Args:


* <b>`parallel_iterations`</b>: See tf.while_loop.
* <b>`back_prop`</b>: See tf.while_loop.
* <b>`swap_memory`</b>: See tf.while_loop.
* <b>`maximum_iterations`</b>: See tf.while_loop.