page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.register_validator


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Adds a constraint, which will be enforced during program execution.

### Aliases:

* `tf.compat.v1.app.flags.register_validator`


``` python
tf.compat.v1.flags.register_validator(
    flag_name,
    checker,
    message='Flag validation failed',
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->

The constraint is validated when flags are initially parsed, and after each
change of the corresponding flag's value.
Args:
  flag_name: str, name of the flag to be checked.
  checker: callable, a function to validate the flag.
      input - A single positional argument: The value of the corresponding
          flag (string, boolean, etc.  This value will be passed to checker
          by the library).
      output - bool, True if validator constraint is satisfied.
          If constraint is not satisfied, it should either return False or
          raise flags.ValidationError(desired_error_message).
  message: str, error text to be shown to the user if checker returns False.
      If checker raises flags.ValidationError, message from the raised
      error will be shown.
  flag_values: flags.FlagValues, optional FlagValues instance to validate
      against.
Raises:
  AttributeError: Raised when flag_name is not registered as a valid flag
      name.
