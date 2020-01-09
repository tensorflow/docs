page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.UnrecognizedFlagError


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `UnrecognizedFlagError`

Raised when a flag is unrecognized.

Inherits From: [`Error`](../../../../tf/compat/v1/flags/Error)

### Aliases:

* Class `tf.compat.v1.app.flags.UnrecognizedFlagError`


<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`flagname`</b>: str, the name of the unrecognized flag.
* <b>`flagvalue`</b>: The value of the flag, empty if the flag is not defined.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    flagname,
    flagvalue='',
    suggestions=None
)
```

Initialize self.  See help(type(self)) for accurate signature.
