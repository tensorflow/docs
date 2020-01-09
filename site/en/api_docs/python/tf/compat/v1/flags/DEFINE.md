page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a generic Flag object.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE`


``` python
tf.compat.v1.flags.DEFINE(
    parser,
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    serializer=None,
    module_name=None,
    **args
)
```



<!-- Placeholder for "Used in" -->

NOTE: in the docstrings of all DEFINE* functions, "registers" is short
for "creates a new flag and registers it".

Auxiliary function: clients should use the specialized DEFINE_<type>
function instead.

#### Args:


* <b>`parser`</b>: ArgumentParser, used to parse the flag arguments.
* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: The default value of the flag.
* <b>`help`</b>: str, the help message.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`serializer`</b>: ArgumentSerializer, the flag serializer instance.
* <b>`module_name`</b>: str, the name of the Python module declaring this flag.
    If not provided, it will be computed using the stack trace of this call.
* <b>`**args`</b>: dict, the extra keyword args that are passed to Flag __init__.
