page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.multi_flags_validator


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



A function decorator for defining a multi-flag validator.

### Aliases:

* `tf.compat.v1.app.flags.multi_flags_validator`


``` python
tf.compat.v1.flags.multi_flags_validator(
    flag_names,
    message='Flag validation failed',
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->

Registers the decorated function as a validator for flag_names, e.g.

@flags.multi_flags_validator(['foo', 'bar'])
def _CheckFooBar(flags_dict):
  ...

See register_multi_flags_validator() for the specification of checker
function.

#### Args:


* <b>`flag_names`</b>: [str], a list of the flag names to be checked.
* <b>`message`</b>: str, error text to be shown to the user if checker returns False.
    If checker raises flags.ValidationError, message from the raised
    error will be shown.
* <b>`flag_values`</b>: flags.FlagValues, optional FlagValues instance to validate
    against.


#### Returns:

A function decorator that registers its function argument as a validator.



#### Raises:


* <b>`AttributeError`</b>: Raised when a flag is not registered as a valid flag name.
