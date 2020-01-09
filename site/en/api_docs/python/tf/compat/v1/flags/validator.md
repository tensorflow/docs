page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.validator


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



A function decorator for defining a flag validator.

### Aliases:

* `tf.compat.v1.app.flags.validator`


``` python
tf.compat.v1.flags.validator(
    flag_name,
    message='Flag validation failed',
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->

Registers the decorated function as a validator for flag_name, e.g.

@flags.validator('foo')
def _CheckFoo(foo):
  ...

See register_validator() for the specification of checker function.

#### Args:


* <b>`flag_name`</b>: str, name of the flag to be checked.
* <b>`message`</b>: str, error text to be shown to the user if checker returns False.
    If checker raises flags.ValidationError, message from the raised
    error will be shown.
* <b>`flag_values`</b>: flags.FlagValues, optional FlagValues instance to validate
    against.

#### Returns:

A function decorator that registers its function argument as a validator.


#### Raises:


* <b>`AttributeError`</b>: Raised when flag_name is not registered as a valid flag
    name.
