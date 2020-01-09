page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_multi_float


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Registers a flag whose value can be a list of arbitrary floats.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_multi_float`


``` python
tf.compat.v1.flags.DEFINE_multi_float(
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

Use the flag on the command line multiple times to place multiple
float values into the list.  The 'default' may be a single float
(which will be converted into a single-element list) or a list of
floats.

#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`default`</b>: Union[Iterable[float], Text, None], the default value of the flag;
    see `DEFINE_multi`.
* <b>`help`</b>: str, the help message.
* <b>`lower_bound`</b>: float, min values of the flag.
* <b>`upper_bound`</b>: float, max values of the flag.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`**args`</b>: Dictionary with extra keyword args that are passed to the
    Flag __init__.
