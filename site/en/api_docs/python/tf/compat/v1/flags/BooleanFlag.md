page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.BooleanFlag


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `BooleanFlag`

Basic boolean flag.

Inherits From: [`Flag`](../../../../tf/compat/v1/flags/Flag)

### Aliases:

* Class `tf.compat.v1.app.flags.BooleanFlag`


<!-- Placeholder for "Used in" -->

Boolean flags do not take any arguments, and their value is either
True (1) or False (0).  The false value is specified on the command
line by prepending the word 'no' to either the long or the short flag
name.

For example, if a Boolean flag was created whose long name was
'update' and whose short name was 'x', then this flag could be
explicitly unset through either --noupdate or --nox.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name,
    default,
    help,
    short_name=None,
    **args
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

Returns a str that describes the type of the flag.

NOTE: we use strings, and not the types.*Type constants because
our flags can have more exotic types, e.g., 'comma separated list
of strings', 'whitespace separated list of strings', etc.

<h3 id="parse"><code>parse</code></h3>

``` python
parse(argument)
```

Parses string and sets flag value.


#### Args:


* <b>`argument`</b>: str or the correct flag value type, argument to be parsed.

<h3 id="serialize"><code>serialize</code></h3>

``` python
serialize()
```

Serializes the flag.


<h3 id="unparse"><code>unparse</code></h3>

``` python
unparse()
```
