page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_variables_to_restore


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L428-L461">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the list of the variables to restore.

``` python
tf.contrib.framework.get_variables_to_restore(
    include=None,
    exclude=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`include`</b>: an optional list/tuple of scope strings for filtering which
  variables from the VARIABLES collection to include. None would include all
  the variables.
* <b>`exclude`</b>: an optional list/tuple of scope strings for filtering which
  variables from the VARIABLES collection to exclude. None it would not
  exclude any.


#### Returns:

a list of variables to restore.



#### Raises:


* <b>`TypeError`</b>: include or exclude is provided but is not a list or a tuple.
