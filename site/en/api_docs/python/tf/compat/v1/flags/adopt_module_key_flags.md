page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.adopt_module_key_flags


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Declares that all flags key to a module are key to the current module.

### Aliases:

* `tf.compat.v1.app.flags.adopt_module_key_flags`


``` python
tf.compat.v1.flags.adopt_module_key_flags(
    module,
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`module`</b>: module, the module object from which all key flags will be declared
    as key flags to the current module.
* <b>`flag_values`</b>: FlagValues, the FlagValues instance in which the flags will
    be declared as key flags. This should almost never need to be
    overridden.


#### Raises:


* <b>`Error`</b>: Raised when given an argument that is a module name (a string),
    instead of a module object.
