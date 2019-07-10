page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.experimental.disable_mixed_precision_graph_rewrite

Disables the mixed precision graph rewrite.

### Aliases:

* `tf.compat.v1.train.experimental.disable_mixed_precision_graph_rewrite`
* `tf.train.experimental.disable_mixed_precision_graph_rewrite`

``` python
tf.train.experimental.disable_mixed_precision_graph_rewrite()
```



Defined in [`python/training/experimental/mixed_precision.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/experimental/mixed_precision.py).

<!-- Placeholder for "Used in" -->

After this is called, the mixed precision graph rewrite will no longer run for
new Sessions, and so float32 operations will no longer be converted to float16
in such Sessions. However, any existing Sessions will continue to have the
graph rewrite enabled if they were created after
`enable_mixed_precision_graph_rewrite` was called but before
`disable_mixed_precision_graph_rewrite` was called.

This does not undo the effects of loss scaling. Any optimizers wrapped with a
LossScaleOptimizer will continue to do loss scaling, although this loss
scaling will no longer be useful if the optimizer is used in new Sessions, as
the graph rewrite no longer converts the graph to use float16.

This function is useful for unit testing. A unit tests can test using the
mixed precision graph rewrite, then disable it so future unit tests continue
using float32. If this is done, unit tests should not share a single session,
as `enable_mixed_precision_graph_rewrite` and
`disable_mixed_precision_graph_rewrite` have no effect on existing sessions.