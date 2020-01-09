page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.bfloat16_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/bfloat16.py#L71-L80">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Scope class for bfloat16 variables so that the model uses custom getter.

### Aliases:

* <a href="/api_docs/python/tf/tpu/bfloat16_scope"><code>tf.compat.v1.tpu.bfloat16_scope</code></a>
* <a href="/api_docs/python/tf/tpu/bfloat16_scope"><code>tf.contrib.tpu.bfloat16_scope</code></a>


``` python
tf.tpu.bfloat16_scope()
```



<!-- Placeholder for "Used in" -->

This enables variables to be read as bfloat16 type when using get_variable.
