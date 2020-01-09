page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.trace


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/autograph/utils/ag_logging.py#L91-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Traces argument information at compilation time.

### Aliases:

* `tf.compat.v1.autograph.trace`
* `tf.compat.v2.autograph.trace`


``` python
tf.autograph.trace(*args)
```



<!-- Placeholder for "Used in" -->

`trace` is useful when debugging, and it always executes during the tracing
phase, that is, when the TF graph is constructed.

_Example usage_

```python
import tensorflow as tf

for i in tf.range(10):
  tf.autograph.trace(i)
# Output: <Tensor ...>
```

#### Args:


* <b>`*args`</b>: Arguments to print to `sys.stdout`.
