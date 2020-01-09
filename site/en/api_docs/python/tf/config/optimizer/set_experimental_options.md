page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.optimizer.set_experimental_options


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/optimizer/set_experimental_options">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L117-L156">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Set experimental optimizer options.

### Aliases:

* <a href="/api_docs/python/tf/config/optimizer/set_experimental_options"><code>tf.compat.v1.config.optimizer.set_experimental_options</code></a>
* <a href="/api_docs/python/tf/config/optimizer/set_experimental_options"><code>tf.compat.v2.config.optimizer.set_experimental_options</code></a>


``` python
tf.config.optimizer.set_experimental_options(options)
```



<!-- Placeholder for "Used in" -->

Note that optimizations are only applied in graph mode, (within tf.function).
In addition, as these are experimental options, the list is subject to change.

#### Args:


* <b>`options`</b>: Dictionary of experimental optimizer options to configure.
  Valid keys:
  - layout_optimizer: Optimize tensor layouts
    e.g. This will try to use NCHW layout on GPU which is faster.
  - constant_folding: Fold constants
    Statically infer the value of tensors when possible, and materialize the
    result using constants.
  - shape_optimization: Simplify computations made on shapes.
  - remapping: Remap subgraphs onto more efficient implementations.
  - arithmetic_optimization: Simplify arithmetic ops with common
    sub-expression elimination and arithmetic simplification.
  - dependency_optimization: Control dependency optimizations. Remove
    redundant control dependencies, which may enable other optimization.
    This optimizer is also essential for pruning Identity and NoOp nodes.
  - loop_optimization: Loop optimizations.
  - function_optimization: Function optimizations and inlining.
  - debug_stripper: Strips debug-related nodes from the graph.
  - disable_model_pruning: Disable removal of unnecessary ops from the graph
  - scoped_allocator_optimization: Try to allocate some independent Op
    outputs contiguously in order to merge or eliminate downstream Ops.
  - pin_to_host_optimization: Force small ops onto the CPU.
  - implementation_selector: Enable the swap of kernel implementations based
    on the device placement.
  - auto_mixed_precision: Change certain float32 ops to float16 on Volta
    GPUs and above. Without the use of loss scaling, this can cause
    numerical underflow (see
    <a href="../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer"><code>keras.mixed_precision.experimental.LossScaleOptimizer</code></a>).
  - disable_meta_optimizer: Disable the entire meta optimizer.
  - min_graph_nodes: The minimum number of nodes in a graph to optimizer.
    For smaller graphs, optimization is skipped.
