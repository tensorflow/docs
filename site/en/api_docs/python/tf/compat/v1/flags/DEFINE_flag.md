page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_flag


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a 'Flag' object with a 'FlagValues' object.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_flag`


``` python
tf.compat.v1.flags.DEFINE_flag(
    flag,
    flag_values=_flagvalues.FLAGS,
    module_name=None
)
```



<!-- Placeholder for "Used in" -->

By default, the global FLAGS 'FlagValue' object is used.

Typical users will use one of the more specialized DEFINE_xxx
functions, such as DEFINE_string or DEFINE_integer.  But developers
who need to create Flag objects themselves should use this function
to register their flags.

#### Args:


* <b>`flag`</b>: Flag, a flag that is key to the module.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`module_name`</b>: str, the name of the Python module declaring this flag.
    If not provided, it will be computed using the stack trace of this call.
