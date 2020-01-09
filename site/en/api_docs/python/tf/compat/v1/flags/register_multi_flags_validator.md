page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.register_multi_flags_validator


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Adds a constraint to multiple flags.

### Aliases:

* `tf.compat.v1.app.flags.register_multi_flags_validator`


``` python
tf.compat.v1.flags.register_multi_flags_validator(
    flag_names,
    multi_flags_checker,
    message='Flags validation failed',
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->

The constraint is validated when flags are initially parsed, and after each
change of the corresponding flag's value.

#### Args:


* <b>`flag_names`</b>: [str], a list of the flag names to be checked.
* <b>`multi_flags_checker`</b>: callable, a function to validate the flag.
    input - dict, with keys() being flag_names, and value for each key
        being the value of the corresponding flag (string, boolean, etc).
    output - bool, True if validator constraint is satisfied.
        If constraint is not satisfied, it should either return False or
        raise flags.ValidationError.
* <b>`message`</b>: str, error text to be shown to the user if checker returns False.
    If checker raises flags.ValidationError, message from the raised
    error will be shown.
* <b>`flag_values`</b>: flags.FlagValues, optional FlagValues instance to validate
    against.


#### Raises:


* <b>`AttributeError`</b>: Raised when a flag is not registered as a valid flag name.
