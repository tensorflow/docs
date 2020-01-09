page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_integer


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a flag whose value must be an integer.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_integer`


``` python
tf.compat.v1.flags.DEFINE_integer(
    name,
    default,
    help,
    lower_bound=None,
    upper_bound=None,
    flag_values=_flagvalues.FLAGS,
    **args
)
```



<!-- Placeholder for "Used in" -->

If lower_bound, or upper_bound are set, then this flag must be
within the given range.

#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: int|str|None, the default value of the flag.
* <b>`help`</b>: str, the help message.
* <b>`lower_bound`</b>: int, min value of the flag.
* <b>`upper_bound`</b>: int, max value of the flag.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`**args`</b>: dict, the extra keyword args that are passed to DEFINE.
