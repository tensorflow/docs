page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.ConversionOptions

## Class `ConversionOptions`

Immutable container for global conversion flags.





Defined in [`python/autograph/core/converter.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/core/converter.py).

<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`recursive`</b>: bool, whether to recursively convert any user functions or
  classes that the converted function may use.
* <b>`force_conversion`</b>: bool, whether to force convertinng the target entity. When
  force_conversion is turned off, the converter may decide to return the
  function as-is.
* <b>`optional_features`</b>: Union[Feature, Set[Feature]], controls the use of
  optional features in the conversion process. See Feature for available
  options.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    recursive=False,
    force_conversion=False,
    internal_convert_user_code=True,
    optional_features=tf.autograph.experimental.Feature.ALL
)
```






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```




<h3 id="as_tuple"><code>as_tuple</code></h3>

``` python
as_tuple()
```




<h3 id="to_ast"><code>to_ast</code></h3>

``` python
to_ast(internal_convert_user_code=None)
```

Returns a representation of this object as an AST node.

The AST node encodes a constructor that would create an object with the
same contents.

#### Args:


* <b>`internal_convert_user_code`</b>: Optional[bool], allows ovrriding the
  corresponding value.


#### Returns:

ast.Node


<h3 id="uses"><code>uses</code></h3>

``` python
uses(feature)
```






