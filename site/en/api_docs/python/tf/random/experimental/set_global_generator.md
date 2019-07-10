page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.experimental.set_global_generator

Replaces the global generator with another `Generator` object.

### Aliases:

* `tf.compat.v1.random.experimental.set_global_generator`
* `tf.compat.v2.random.experimental.set_global_generator`
* `tf.random.experimental.set_global_generator`

``` python
tf.random.experimental.set_global_generator(generator)
```



Defined in [`python/ops/stateful_random_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/stateful_random_ops.py).

<!-- Placeholder for "Used in" -->

This function creates a new Generator object (and the Variable object within),
which does not work well with tf.function because (1) tf.function puts
restrictions on Variable creation thus reset_global_generator can't be freely
used inside tf.function; (2) redirecting a global variable to
a new object is problematic with tf.function because the old object may be
captured by a 'tf.function'ed function and still be used by it.
A 'tf.function'ed function only keeps weak references to variables,
so deleting a variable and then calling that function again may raise an
error, as demonstrated by
random_test.py/RandomTest.testResetGlobalGeneratorBadWithDefun .

#### Args:


* <b>`generator`</b>: the new `Generator` object.