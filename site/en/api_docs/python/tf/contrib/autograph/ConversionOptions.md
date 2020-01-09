page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.ConversionOptions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L145-L233">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ConversionOptions`

Immutable container for global conversion flags.



<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`recursive`</b>: bool, whether to recursively convert any user functions or
  classes that the converted function may use.
* <b>`user_requested`</b>: bool, whether the conversion was explicitly requested by
  the user, as opposed to being performed as a result of other logic. This
  value always auto-resets resets to False in child conversions.
* <b>`optional_features`</b>: Union[Feature, Set[Feature]], controls the use of
  optional features in the conversion process. See Feature for available
  options.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L159-L174">View source</a>

``` python
__init__(
    recursive=False,
    user_requested=False,
    internal_convert_user_code=True,
    optional_features=tf.autograph.experimental.Feature.ALL
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L183-L185">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="as_tuple"><code>as_tuple</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L176-L178">View source</a>

``` python
as_tuple()
```




<h3 id="call_options"><code>call_options</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L194-L200">View source</a>

``` python
call_options()
```

Returns the corresponding options to be used for recursive conversion.


<h3 id="to_ast"><code>to_ast</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L202-L233">View source</a>

``` python
to_ast()
```

Returns a representation of this object as an AST node.

The AST node encodes a constructor that would create an object with the
same contents.

#### Returns:

ast.Node


<h3 id="uses"><code>uses</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/core/converter.py#L190-L192">View source</a>

``` python
uses(feature)
```
