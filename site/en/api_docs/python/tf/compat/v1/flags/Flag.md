page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.Flag


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `Flag`

Information about a command-line flag.



### Aliases:

* Class `tf.compat.v1.app.flags.Flag`


<!-- Placeholder for "Used in" -->

'Flag' objects define the following fields:
  .name - the name for this flag;
  .default - the default value for this flag;
  .default_unparsed - the unparsed default value for this flag.
  .default_as_str - default value as repr'd string, e.g., "'true'" (or None);
  .value - the most recent parsed value of this flag; set by parse();
  .help - a help string or None if no help is available;
  .short_name - the single letter alias for this flag (or None);
  .boolean - if 'true', this flag does not accept arguments;
  .present - true if this flag was parsed from command line flags;
  .parser - an ArgumentParser object;
  .serializer - an ArgumentSerializer object;
  .allow_override - the flag may be redefined without raising an error, and
                    newly defined flag overrides the old one.
  .allow_override_cpp - use the flag from C++ if available; the flag
                        definition is replaced by the C++ flag after init;
  .allow_hide_cpp - use the Python flag despite having a C++ flag with
                    the same name (ignore the C++ flag);
  .using_default_value - the flag value has not been set by user;
  .allow_overwrite - the flag may be parsed more than once without raising
                     an error, the last set value will be used;
  .allow_using_method_names - whether this flag can be defined even if it has
                              a name that conflicts with a FlagValues method.

The only public method of a 'Flag' object is parse(), but it is
typically only called by a 'FlagValues' object.  The parse() method is
a thin wrapper around the 'ArgumentParser' parse() method.  The parsed
value is saved in .value, and the .present attribute is updated.  If
this flag was already present, an Error is raised.

parse() is also called during __init__ to parse the default value and
initialize the .value attribute.  This enables other python modules to
safely use flags even if the __main__ module neglects to parse the
command line arguments.  The .present attribute is cleared after
__init__ parsing.  If the default value is set to None, then the
__init__ parsing step is skipped and the .value attribute is
initialized to None.

Note: The default value is also presented to the user in the help
string, so it is important that it be a legal value for this flag.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    parser,
    serializer,
    name,
    default,
    help_string,
    short_name=None,
    boolean=False,
    allow_override=False,
    allow_override_cpp=False,
    allow_hide_cpp=False,
    allow_overwrite=True,
    allow_using_method_names=False
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
