page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_multi


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a generic MultiFlag that parses its args with a given parser.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_multi`


``` python
tf.compat.v1.flags.DEFINE_multi(
    parser,
    serializer,
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    module_name=None,
    **args
)
```



<!-- Placeholder for "Used in" -->

Auxiliary function.  Normal users should NOT use it directly.

Developers who need to create their own 'Parser' classes for options
which can appear multiple times can call this module function to
register their flags.

#### Args:


* <b>`parser`</b>: ArgumentParser, used to parse the flag arguments.
* <b>`serializer`</b>: ArgumentSerializer, the flag serializer instance.
* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: Union[Iterable[T], Text, None], the default value of the flag.
    If the value is text, it will be parsed as if it was provided from
    the command line. If the value is a non-string iterable, it will be
    iterated over to create a shallow copy of the values. If it is None,
    it is left as-is.
* <b>`help`</b>: str, the help message.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`module_name`</b>: A string, the name of the Python module declaring this flag.
    If not provided, it will be computed using the stack trace of this call.
* <b>`**args`</b>: Dictionary with extra keyword args that are passed to the
    Flag __init__.
