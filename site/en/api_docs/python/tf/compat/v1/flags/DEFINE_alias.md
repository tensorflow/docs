page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.DEFINE_alias


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Defines an alias flag for an existing one.

### Aliases:

* `tf.compat.v1.app.flags.DEFINE_alias`


``` python
tf.compat.v1.flags.DEFINE_alias(
    name,
    original_name,
    flag_values=_flagvalues.FLAGS,
    module_name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`name`</b>: str, the flag name.
* <b>`original_name`</b>: str, the original flag name.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance with which the flag will
    be registered. This should almost never need to be overridden.
* <b>`module_name`</b>: A string, the name of the module that defines this flag.


#### Raises:


* <b>`flags.FlagError`</b>:   UnrecognizedFlagError: if the referenced flag doesn't exist.
  DuplicateFlagError: if the alias name has been used by some existing flag.
