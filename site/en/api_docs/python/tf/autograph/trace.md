page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.trace


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/autograph/trace">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/utils/ag_logging.py#L91-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Traces argument information at compilation time.

### Aliases:

* <a href="/api_docs/python/tf/autograph/trace"><code>tf.compat.v1.autograph.trace</code></a>
* <a href="/api_docs/python/tf/autograph/trace"><code>tf.compat.v2.autograph.trace</code></a>


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
