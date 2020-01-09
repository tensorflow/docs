page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.experimental.Feature


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/autograph/core/converter.py#L90-L139">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Feature`

This enumeration represents optional conversion options.



### Aliases:

* Class `tf.compat.v1.autograph.experimental.Feature`
* Class `tf.compat.v2.autograph.experimental.Feature`


<!-- Placeholder for "Used in" -->

These conversion options are experimental. They are subject to change without
notice and offer no guarantees.

_Example Usage_

```python
optionals= tf.autograph.experimental.Feature.EQUALITY_OPERATORS
@tf.function(experimental_autograph_options=optionals)
def f(i):
  if i == 0:  # EQUALITY_OPERATORS allows the use of == here.
    tf.print('i is zero')
```

#### Attributes:


* <b>`ALL`</b>: Enable all features.
* <b>`AUTO_CONTROL_DEPS`</b>: Insert of control dependencies in the generated code.
* <b>`ASSERT_STATEMENTS`</b>: Convert Tensor-dependent assert statements to tf.Assert.
* <b>`BUILTIN_FUNCTIONS`</b>: Convert builtin functions applied to Tensors to
  their TF counterparts.
* <b>`EQUALITY_OPERATORS`</b>: Whether to convert the comparison operators, like
  equality. This is soon to be deprecated as support is being added to the
  Tensor class.
* <b>`LISTS`</b>: Convert list idioms, like initializers, slices, append, etc.
* <b>`NAME_SCOPES`</b>: Insert name scopes that name ops according to context, like the
  function they were defined in.

## Class Members

* `ALL` <a id="ALL"></a>
* `ASSERT_STATEMENTS` <a id="ASSERT_STATEMENTS"></a>
* `AUTO_CONTROL_DEPS` <a id="AUTO_CONTROL_DEPS"></a>
* `BUILTIN_FUNCTIONS` <a id="BUILTIN_FUNCTIONS"></a>
* `EQUALITY_OPERATORS` <a id="EQUALITY_OPERATORS"></a>
* `LISTS` <a id="LISTS"></a>
* `NAME_SCOPES` <a id="NAME_SCOPES"></a>
