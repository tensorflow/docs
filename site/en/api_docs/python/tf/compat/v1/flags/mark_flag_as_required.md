page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.mark_flag_as_required


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Ensures that flag is not None during program execution.

### Aliases:

* `tf.compat.v1.app.flags.mark_flag_as_required`


``` python
tf.compat.v1.flags.mark_flag_as_required(
    flag_name,
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->

Registers a flag validator, which will follow usual validator rules.
Important note: validator will pass for any non-None value, such as False,
0 (zero), '' (empty string) and so on.

It is recommended to call this method like this:

  if __name__ == '__main__':
    flags.mark_flag_as_required('your_flag_name')
    app.run()

Because validation happens at app.run() we want to ensure required-ness
is enforced at that time. You generally do not want to force users who import
your code to have additional required flags for their own binaries or tests.

#### Args:


* <b>`flag_name`</b>: str, name of the flag
* <b>`flag_values`</b>: flags.FlagValues, optional FlagValues instance where the flag
    is defined.

#### Raises:


* <b>`AttributeError`</b>: Raised when flag_name is not registered as a valid flag
    name.
