page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_bool


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a boolean flag.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_bool`
* `tf.compat.v1.app.flags.DEFINE_boolean`
* `tf.compat.v1.flags.DEFINE_boolean`


``` python
tf.compat.v1.flags.DEFINE_bool(
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    **args
)
```



<!-- Placeholder for "Used in" -->

Such a boolean flag does not take an argument.  If a user wants to
specify a false value explicitly, the long option beginning with 'no'
must be used: i.e. --noflag

This flag will have a value of None, True or False.  None is possible
if default=None and the user does not specify the flag on the command
line.

#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: bool|str|None, the default value of the flag.
* <b>`help`</b>: str, the help message.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`module_name`</b>: str, the name of the Python module declaring this flag.
    If not provided, it will be computed using the stack trace of this call.
* <b>`**args`</b>: dict, the extra keyword args that are passed to Flag __init__.
