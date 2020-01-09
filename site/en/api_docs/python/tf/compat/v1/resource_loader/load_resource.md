page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.resource_loader.load_resource


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/resource_loader.py#L27-L45">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Load the resource at given path, where path is relative to tensorflow/.

``` python
tf.compat.v1.resource_loader.load_resource(path)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: a string resource path relative to tensorflow/.


#### Returns:

The contents of that resource.



#### Raises:


* <b>`IOError`</b>: If the path is not found, or the resource can't be opened.
