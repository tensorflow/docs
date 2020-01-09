page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.xla.experimental.jit_scope


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Enable or disable JIT compilation of operators within the scope.

### Aliases:

* `tf.compat.v1.xla.experimental.jit_scope`
* `tf.compat.v2.xla.experimental.jit_scope`


``` python
tf.xla.experimental.jit_scope(
    *args,
    **kwds
)
```



<!-- Placeholder for "Used in" -->

NOTE: This is an experimental feature.

The compilation is a hint and only supported on a best-effort basis.

#### Example usage:

with tf.xla.experimental.jit_scope():
  c = tf.matmul(a, b)  # compiled
with tf.xla.experimental.jit_scope(compile_ops=False):
  d = tf.matmul(a, c)  # not compiled
with tf.xla.experimental.jit_scope(
    compile_ops=lambda node_def: 'matmul' in node_def.op.lower()):
  e = tf.matmul(a, b) + d  # matmul is compiled, the addition is not.


Example of separate_compiled_gradients:
  # In the example below, the computations for f, g and h will all be compiled
  # in separate scopes.
  with tf.xla.experimental.jit_scope(
      separate_compiled_gradients=True):
    f = tf.matmul(a, b)
  g = tf.gradients([f], [a, b], name='mygrads1')
  h = tf.gradients([f], [a, b], name='mygrads2')

#### Args:


* <b>`compile_ops`</b>: Whether to enable or disable compilation in the scope.
  Either a Python bool, or a callable that accepts the parameter
  `node_def` and returns a python bool.
* <b>`separate_compiled_gradients`</b>: If true put each gradient subgraph into a
  separate compilation scope. This gives fine-grained control over which
  portions of the graph will be compiled as a single unit. Compiling
  gradients separately may yield better performance for some graphs.
  The scope is named based on the scope of the forward computation as well
  as the name of the gradients. As a result, the gradients will be compiled
  in a scope that is separate from both the forward computation, and from
  other gradients.

#### Raises:


* <b>`RuntimeError`</b>: if called when eager execution is enabled.

#### Yields:

The current scope, enabling or disabling compilation.
