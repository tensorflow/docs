page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_list


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a flag whose value is a comma-separated list of strings.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_list`


``` python
tf.compat.v1.flags.DEFINE_list(
    name,
    default,
    help,
    flag_values=_flagvalues.FLAGS,
    **args
)
```



<!-- Placeholder for "Used in" -->

The flag value is parsed with a CSV parser.

#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: list|str|None, the default value of the flag.
* <b>`help`</b>: str, the help message.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`**args`</b>: Dictionary with extra keyword args that are passed to the
    Flag __init__.
