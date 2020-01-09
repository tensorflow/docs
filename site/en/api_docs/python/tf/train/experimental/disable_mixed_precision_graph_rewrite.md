page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.experimental.disable_mixed_precision_graph_rewrite


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/mixed_precision.py#L196-L217">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Disables the mixed precision graph rewrite.

### Aliases:

* `tf.compat.v2.train.experimental.disable_mixed_precision_graph_rewrite`


``` python
tf.train.experimental.disable_mixed_precision_graph_rewrite()
```



<!-- Placeholder for "Used in" -->

After this is called, the mixed precision graph rewrite will no longer run for
tf.functions, and so float32 operations will no longer be converted to
float16.

This does not undo the effects of loss scaling. Any optimizers wrapped with a
LossScaleOptimizer will continue to do loss scaling, although this loss
scaling will no longer be useful, as the graph rewrite no longer converts
tf.functions to use float16.

This function is useful for unit testing. A unit test can test using the mixed
precision graph rewrite, then disable it so future unit tests continue using
float32.
