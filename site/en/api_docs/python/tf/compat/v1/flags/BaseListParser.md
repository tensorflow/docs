page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.BaseListParser


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `BaseListParser`

Base class for a parser of lists of strings.

Inherits From: [`ArgumentParser`](../../../../tf/compat/v1/flags/ArgumentParser)

### Aliases:

* Class `tf.compat.v1.app.flags.BaseListParser`


<!-- Placeholder for "Used in" -->

To extend, inherit from this class; from the subclass __init__, call

    BaseListParser.__init__(self, token, name)

where token is a character used to tokenize, and name is a description
of the separator.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    token=None,
    name=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




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

See base class.
