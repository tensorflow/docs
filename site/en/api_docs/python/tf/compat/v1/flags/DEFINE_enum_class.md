page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_enum_class


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a flag whose value can be the name of enum members.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_enum_class`


``` python
tf.compat.v1.flags.DEFINE_enum_class(
    name,
    default,
    enum_class,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    **args
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: Enum|str|None, the default value of the flag.
* <b>`enum_class`</b>: class, the Enum class with all the possible values for the flag.
* <b>`help`</b>: str, the help message.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`module_name`</b>: str, the name of the Python module declaring this flag.
    If not provided, it will be computed using the stack trace of this call.
* <b>`**args`</b>: dict, the extra keyword args that are passed to Flag __init__.
