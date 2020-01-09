page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.CsvListSerializer


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `CsvListSerializer`

Base class for generating string representations of a flag value.

Inherits From: [`ArgumentSerializer`](../../../../tf/compat/v1/flags/ArgumentSerializer)

### Aliases:

* Class `tf.compat.v1.app.flags.CsvListSerializer`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(list_sep)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="serialize"><code>serialize</code></h3>

``` python
serialize(value)
```

Serializes a list as a CSV string or unicode.
