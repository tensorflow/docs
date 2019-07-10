page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.experimental.Feature

## Class `Feature`

Represents conversion options that can be toggled on or off.



### Aliases:

* Class `tf.autograph.experimental.Feature`
* Class `tf.compat.v1.autograph.experimental.Feature`
* Class `tf.compat.v2.autograph.experimental.Feature`
* Class `tf.contrib.autograph.Feature`



Defined in [`python/autograph/core/converter.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/core/converter.py).

<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`ALL`</b>: Enable all features.
* <b>`AUTO_CONTROL_DEPS`</b>: Insert of control dependencies in the generated code.
* <b>`ASSERT_STATEMENTS`</b>: Convert Tensor-dependent assert statements to tf.Assert.
* <b>`BUILTIN_FUNCTIONS`</b>: Convert builtin functions applied to Tensors to
  their TF counterparts.
* <b>`LISTS`</b>: Convert list idioms, like initializers, slices, append, etc.
* <b>`LOGICAL_EXPRESSIONS`</b>: Convert data-dependent logical expressions applied to
  Tensors to their TF counterparts.
* <b>`NAME_SCOPES`</b>: Insert name scopes that name ops according to context, like the
  function they were defined in.

## Class Members

* `ALL` <a id="ALL"></a>
* `ASSERT_STATEMENTS` <a id="ASSERT_STATEMENTS"></a>
* `AUTO_CONTROL_DEPS` <a id="AUTO_CONTROL_DEPS"></a>
* `BUILTIN_FUNCTIONS` <a id="BUILTIN_FUNCTIONS"></a>
* `LISTS` <a id="LISTS"></a>
* `LOGICAL_EXPRESSIONS` <a id="LOGICAL_EXPRESSIONS"></a>
* `NAME_SCOPES` <a id="NAME_SCOPES"></a>
