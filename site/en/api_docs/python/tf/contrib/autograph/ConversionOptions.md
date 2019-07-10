page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.ConversionOptions

## Class `ConversionOptions`





Defined in [`tensorflow/python/autograph/core/converter.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/core/converter.py).

Immutable container for global conversion flags.

#### Attributes:

* <b>`recursive`</b>: bool, whether to recursively convert any user functions or
    classes that the converted function may use.
* <b>`verbose`</b>: Verbosity, the level of verbosity to use.
* <b>`strip_decorators`</b>: Tuple[Callable], contains decorators that should be in
    excluded from the compiled output. By default, when converting a function
    before the decorators are applied, the compiled output will include those
    decorators.
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
    verbose=Verbosity.VERBOSE,
    strip_decorators=None,
    force_conversion=False,
    internal_convert_user_code=True,
    optional_features=tf.autograph.experimental.Feature.ALL
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Properties

<h3 id="strip_decorators"><code>strip_decorators</code></h3>





## Methods

<h3 id="should_strip"><code>should_strip</code></h3>

``` python
should_strip(decorator)
```



<h3 id="to_ast"><code>to_ast</code></h3>

``` python
to_ast(
    ctx,
    internal_convert_user_code=None
)
```

Returns a representation of this object as an AST node.

The AST node encodes a constructor that would create an object with the
same contents.

#### Args:

* <b>`ctx`</b>: EntityContext, the entity with which this AST needs to be consistent.
* <b>`internal_convert_user_code`</b>: Optional[bool], allows ovrriding the
    corresponding value.


#### Returns:

ast.Node

<h3 id="uses"><code>uses</code></h3>

``` python
uses(feature)
```





