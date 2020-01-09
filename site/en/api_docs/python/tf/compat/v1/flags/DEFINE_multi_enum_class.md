page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_multi_enum_class


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a flag whose value can be a list of enum members.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_multi_enum_class`


``` python
tf.compat.v1.flags.DEFINE_multi_enum_class(
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

Use the flag on the command line multiple times to place multiple
enum values into the list.

#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: Union[Iterable[Enum], Iterable[Text], Enum, Text, None], the
    default value of the flag; see
    `DEFINE_multi`; only differences are documented here. If the value is
    a single Enum, it is treated as a single-item list of that Enum value.
    If it is an iterable, text values within the iterable will be converted
    to the equivalent Enum objects.
* <b>`enum_class`</b>: class, the Enum class with all the possible values for the flag.
    help: str, the help message.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will be
  registered. This should almost never need to be overridden.
* <b>`module_name`</b>: A string, the name of the Python module declaring this flag. If
  not provided, it will be computed using the stack trace of this call.
* <b>`**args`</b>: Dictionary with extra keyword args that are passed to the Flag
  __init__.
