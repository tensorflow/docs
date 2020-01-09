page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.optimizer.get_experimental_options


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L101-L114">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get experimental optimizer options.

### Aliases:

* `tf.compat.v1.config.optimizer.get_experimental_options`
* `tf.compat.v2.config.optimizer.get_experimental_options`


``` python
tf.config.optimizer.get_experimental_options()
```



<!-- Placeholder for "Used in" -->

Refer to tf.config.optimizer.set_experimental_options for a list of current
options.

Note that optimizations are only applied in graph mode, (within tf.function).
In addition, as these are experimental options, the list is subject to change.

#### Returns:

Dictionary of configured experimental optimizer options
