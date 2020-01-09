page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.WhitespaceSeparatedListParser


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `WhitespaceSeparatedListParser`

Parser for a whitespace-separated list of strings.

Inherits From: [`BaseListParser`](../../../../tf/compat/v1/flags/BaseListParser)

### Aliases:

* Class `tf.compat.v1.app.flags.WhitespaceSeparatedListParser`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(comma_compat=False)
```

Initializer.


#### Args:


* <b>`comma_compat`</b>: bool, whether to support comma as an additional separator.
    If False then only whitespace is supported.  This is intended only for
    backwards compatibility with flags that used to be comma-separated.



## Methods

<h3 id="flag_type"><code>flag_type</code></h3>

``` python
flag_type()
```

See base class.


<h3 id="parse"><code>parse</code></h3>

``` python
parse(argument)
```

Parses argument as whitespace-separated list of strings.

It also parses argument as comma-separated list of strings if requested.

#### Args:


* <b>`argument`</b>: string argument passed in the commandline.


#### Returns:

[str], the parsed flag value.
