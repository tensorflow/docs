page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.resource_loader.get_root_dir_with_all_resources


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/platform/resource_loader.py#L60-L97">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get a root directory containing all the data attributes in the build rule.

### Aliases:

* <a href="/api_docs/python/tf/resource_loader/get_root_dir_with_all_resources"><code>tf.compat.v1.resource_loader.get_root_dir_with_all_resources</code></a>


``` python
tf.resource_loader.get_root_dir_with_all_resources()
```



<!-- Placeholder for "Used in" -->


#### Returns:

The path to the specified file present in the data attribute of py_test
or py_binary. Falls back to returning the same as get_data_files_path if it
fails to detect a bazel runfiles directory.
