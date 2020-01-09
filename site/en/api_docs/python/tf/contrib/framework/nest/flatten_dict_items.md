page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.flatten_dict_items


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/nest.py#L329-L382">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a dictionary with flattened keys and values.

``` python
tf.contrib.framework.nest.flatten_dict_items(dictionary)
```



<!-- Placeholder for "Used in" -->

This function flattens the keys and values of a dictionary, which can be
arbitrarily nested structures, and returns the flattened version of such
structures:

```python
example_dictionary = {(4, 5, (6, 8)): ("a", "b", ("c", "d"))}
result = {4: "a", 5: "b", 6: "c", 8: "d"}
flatten_dict_items(example_dictionary) == result
```

The input dictionary must satisfy two properties:

1. Its keys and values should have the same exact nested structure.
2. The set of all flattened keys of the dictionary must not contain repeated
   keys.

#### Args:


* <b>`dictionary`</b>: the dictionary to zip


#### Returns:

The zipped dictionary.



#### Raises:


* <b>`TypeError`</b>: If the input is not a dictionary.
* <b>`ValueError`</b>: If any key and value do not have the same structure layout, or
if keys are not unique.
