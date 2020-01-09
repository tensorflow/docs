page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.optimizer.get_jit


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L79-L88">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get if JIT compilation is enabled.

### Aliases:

* `tf.compat.v1.config.optimizer.get_jit`
* `tf.compat.v2.config.optimizer.get_jit`


``` python
tf.config.optimizer.get_jit()
```



<!-- Placeholder for "Used in" -->

Note that optimizations are only applied in graph mode, (within tf.function).

#### Returns:

If JIT compilation is enabled.
