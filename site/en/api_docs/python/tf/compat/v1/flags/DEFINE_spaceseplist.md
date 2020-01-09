page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_spaceseplist


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a flag whose value is a whitespace-separated list of strings.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_spaceseplist`


``` python
tf.compat.v1.flags.DEFINE_spaceseplist(
    name,
    default,
    help,
    comma_compat=False,
    flag_values=_flagvalues.FLAGS,
    **args
)
```



<!-- Placeholder for "Used in" -->

Any whitespace can be used as a separator.

#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: list|str|None, the default value of the flag.
* <b>`help`</b>: str, the help message.
* <b>`comma_compat`</b>: bool - Whether to support comma as an additional separator.
    If false then only whitespace is supported.  This is intended only for
    backwards compatibility with flags that used to be comma-separated.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`**args`</b>: Dictionary with extra keyword args that are passed to the
    Flag __init__.
