page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.MultiFlag


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `MultiFlag`

A flag that can appear multiple time on the command-line.

Inherits From: [`Flag`](../../../../tf/compat/v1/flags/Flag)

### Aliases:

* Class `tf.compat.v1.app.flags.MultiFlag`


<!-- Placeholder for "Used in" -->

The value of such a flag is a list that contains the individual values
from all the appearances of that flag on the command-line.

See the __doc__ for Flag for most behavior of this class.  Only
differences in behavior are described here:

  * The default value may be either a single value or an iterable of values.
    A single value is transformed into a single-item list of that value.

  * The value of the flag is always a list, even if the option was
    only supplied once, and even if the default value is a single
    value

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="value"><code>value</code></h3>






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ge__"><code>__ge__</code></h3>

``` python
__ge__(
    other,
    NotImplemented=NotImplemented
)
```

Return a >= b.  Computed by @total_ordering from (not a < b).


<h3 id="__gt__"><code>__gt__</code></h3>

``` python
__gt__(
    other,
    NotImplemented=NotImplemented
)
```

Return a > b.  Computed by @total_ordering from (not a < b) and (a != b).


<h3 id="__le__"><code>__le__</code></h3>

``` python
__le__(
    other,
    NotImplemented=NotImplemented
)
```

Return a <= b.  Computed by @total_ordering from (a < b) or (a == b).


<h3 id="__lt__"><code>__lt__</code></h3>

``` python
__lt__(other)
```

Return self<value.


<h3 id="flag_type"><code>flag_type</code></h3>

``` python
flag_type()
```

See base class.


<h3 id="parse"><code>parse</code></h3>

``` python
parse(arguments)
```

Parses one or more arguments with the installed parser.


#### Args:


* <b>`arguments`</b>: a single argument or a list of arguments (typically a
  list of default values); a single argument is converted
  internally into a list containing one item.

<h3 id="serialize"><code>serialize</code></h3>

``` python
serialize()
```

Serializes the flag.


<h3 id="unparse"><code>unparse</code></h3>

``` python
unparse()
```
