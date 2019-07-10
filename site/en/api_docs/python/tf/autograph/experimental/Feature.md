page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.experimental.Feature

## Class `Feature`



### Aliases:

* Class `tf.autograph.experimental.Feature`
* Class `tf.contrib.autograph.Feature`



Defined in [`tensorflow/python/autograph/core/converter.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/core/converter.py).

Represents conversion options that can be toggled on or off.

#### Attributes:

* <b>`ALL`</b>: Enable all features.
* <b>`AUTO_CONTROL_DEPS`</b>: Insert of control dependencies in the generated code.
* <b>`DECORATORS`</b>: Allow decorators in local functions. Note that special
    decorators, like `tf.function`, are allowed regardless of this toggle.
* <b>`ERROR_REWRITING`</b>: Rewrite errors that occur in the generated code to
    indicate the source code to which the failing code corresponds.
* <b>`LISTS`</b>: Convert list idioms, like initializers, slices, append, etc.
* <b>`NAME_SCOPES`</b>: Insert name scopes that name ops according to context, like the
    function they were defined in.

## Class Members

<h3 id="ALL"><code>ALL</code></h3>

<h3 id="AUTO_CONTROL_DEPS"><code>AUTO_CONTROL_DEPS</code></h3>

<h3 id="DECORATORS"><code>DECORATORS</code></h3>

<h3 id="ERROR_REWRITING"><code>ERROR_REWRITING</code></h3>

<h3 id="LISTS"><code>LISTS</code></h3>

<h3 id="NAME_SCOPES"><code>NAME_SCOPES</code></h3>

<h3 id="__members__"><code>__members__</code></h3>

