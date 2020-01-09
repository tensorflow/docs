page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.set_soft_device_placement


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L174-L186">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Set if soft device placement is enabled.

### Aliases:

* `tf.compat.v1.config.set_soft_device_placement`
* `tf.compat.v2.config.set_soft_device_placement`


``` python
tf.config.set_soft_device_placement(enabled)
```



### Used in the guide:

* [Use a GPU](https://www.tensorflow.org/guide/gpu)



If enabled, an op will be placed on CPU if any of the following are true
  1. there's no GPU implementation for the OP
  2. no GPU devices are known or registered
  3. need to co-locate with reftype input(s) which are from CPU

#### Args:


* <b>`enabled`</b>: Whether to enable soft placement.
