page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.resource_loader.get_path_to_datafile


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/platform/resource_loader.py#L100-L117">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get the path to the specified file in the data dependencies.

### Aliases:

* <a href="/api_docs/python/tf/resource_loader/get_path_to_datafile"><code>tf.compat.v1.resource_loader.get_path_to_datafile</code></a>


``` python
tf.resource_loader.get_path_to_datafile(path)
```



<!-- Placeholder for "Used in" -->

The path is relative to tensorflow/

#### Args:


* <b>`path`</b>: a string resource path relative to tensorflow/


#### Returns:

The path to the specified file present in the data attribute of py_test
or py_binary.



#### Raises:


* <b>`IOError`</b>: If the path is not found, or the resource can't be opened.
