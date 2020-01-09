page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.declare_key_flag


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Declares one flag as key to the current module.

### Aliases:

* `tf.compat.v1.app.flags.declare_key_flag`


``` python
tf.compat.v1.flags.declare_key_flag(
    flag_name,
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->

Key flags are flags that are deemed really important for a module.
They are important when listing help messages; e.g., if the
--helpshort command-line flag is used, then only the key flags of the
main module are listed (instead of all flags, as in the case of
--helpfull).

#### Sample usage:


flags.declare_key_flag('flag_1')



#### Args:


* <b>`flag_name`</b>: str, the name of an already declared flag.
    (Redeclaring flags as key, including flags implicitly key
    because they were declared in this module, is a no-op.)
* <b>`flag_values`</b>: FlagValues, the FlagValues instance in which the flag will
    be declared as a key flag. This should almost never need to be
    overridden.


#### Raises:


* <b>`ValueError`</b>: Raised if flag_name not defined as a Python flag.
