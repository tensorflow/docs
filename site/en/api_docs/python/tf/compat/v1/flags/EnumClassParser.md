page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.EnumClassParser


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



## Class `EnumClassParser`

Parser of an Enum class member.

Inherits From: [`ArgumentParser`](../../../../tf/compat/v1/flags/ArgumentParser)

### Aliases:

* Class `tf.compat.v1.app.flags.EnumClassParser`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(enum_class)
```

Initializes EnumParser.


#### Args:


* <b>`enum_class`</b>: class, the Enum class with all possible flag values.


#### Raises:


* <b>`TypeError`</b>: When enum_class is not a subclass of Enum.
* <b>`ValueError`</b>: When enum_class is empty.



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

Determines validity of argument and returns the correct element of enum.


#### Args:


* <b>`argument`</b>: str or Enum class member, the supplied flag value.


#### Returns:

The first matching Enum class member in Enum class.



#### Raises:


* <b>`ValueError`</b>: Raised when argument didn't match anything in enum.
