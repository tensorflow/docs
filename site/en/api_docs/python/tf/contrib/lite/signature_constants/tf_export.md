page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.signature_constants.tf_export

## Class `tf_export`



### Aliases:

* Class `tf.contrib.lite.signature_constants.tf_export`
* Class `tf.contrib.lite.tag_constants.tf_export`



Defined in [`tensorflow/python/util/tf_export.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/util/tf_export.py).

Provides ways to export symbols to the TensorFlow API.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    *args,
    **kwargs
)
```

Export under the names *args (first one is considered canonical).

#### Args:

* <b>`*args`</b>: API names in dot delimited format.
* <b>`**kwargs`</b>: Optional keyed arguments.
      overrides: List of symbols that this is overriding
      (those overrided api exports will be removed). Note: passing overrides
      has no effect on exporting a constant.
      allow_multiple_exports: Allows exporting the same symbol multiple
      times with multiple `tf_export` usages. Prefer however, to list all
      of the exported names in a single `tf_export` usage when possible.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(func)
```

Calls this decorator.

#### Args:

* <b>`func`</b>: decorated symbol (function or class).


#### Returns:

The input function with _tf_api_names attribute set.


#### Raises:

* <b>`SymbolAlreadyExposedError`</b>: Raised when a symbol already has API names
    and kwarg `allow_multiple_exports` not set.

<h3 id="export_constant"><code>export_constant</code></h3>

``` python
export_constant(
    module_name,
    name
)
```

Store export information for constants/string literals.

Export information is stored in the module where constants/string literals
are defined.

e.g.

```python
foo = 1
bar = 2
tf_export("consts.foo").export_constant(__name__, 'foo')
tf_export("consts.bar").export_constant(__name__, 'bar')
```

#### Args:

* <b>`module_name`</b>: (string) Name of the module to store constant at.
* <b>`name`</b>: (string) Current constant name.



