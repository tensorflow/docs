page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.flags.mark_flags_as_required


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Ensures that flags are not None during program execution.

### Aliases:

* `tf.compat.v1.app.flags.mark_flags_as_required`


``` python
tf.compat.v1.flags.mark_flags_as_required(
    flag_names,
    flag_values=_flagvalues.FLAGS
)
```



<!-- Placeholder for "Used in" -->


#### Recommended usage:


if __name__ == '__main__':
  flags.mark_flags_as_required(['flag1', 'flag2', 'flag3'])
  app.run()



#### Args:


* <b>`flag_names`</b>: Sequence[str], names of the flags.
* <b>`flag_values`</b>: flags.FlagValues, optional FlagValues instance where the flags
    are defined.

#### Raises:


* <b>`AttributeError`</b>: If any of flag name has not already been defined as a flag.
