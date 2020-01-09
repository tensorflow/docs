page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.flag_dict_to_args


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Convert a dict of values into process call parameters.

### Aliases:

* `tf.compat.v1.app.flags.flag_dict_to_args`


``` python
tf.compat.v1.flags.flag_dict_to_args(flag_map)
```



<!-- Placeholder for "Used in" -->

This method is used to convert a dictionary into a sequence of parameters
for a binary that parses arguments using this module.

#### Args:


* <b>`flag_map`</b>: dict, a mapping where the keys are flag names (strings).
    values are treated according to their type:
    * If value is None, then only the name is emitted.
    * If value is True, then only the name is emitted.
    * If value is False, then only the name prepended with 'no' is emitted.
    * If value is a string then --name=value is emitted.
    * If value is a collection, this will emit --name=value1,value2,value3.
    * Everything else is converted to string an passed as such.

#### Yields:

sequence of string suitable for a subprocess execution.
