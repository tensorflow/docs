description: Import a ConcreteFunction and convert it to a textual MLIR module.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.mlir.experimental.convert_function" />
<meta itemprop="path" content="Stable" />
</div>

# tf.mlir.experimental.convert_function

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/compiler/mlir/mlir.py#L50-L88">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Import a ConcreteFunction and convert it to a textual MLIR module.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.mlir.experimental.convert_function`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.mlir.experimental.convert_function(
    concrete_function, pass_pipeline='tf-standard-pipeline'
)
</code></pre>



<!-- Placeholder for "Used in" -->

This API is only intended for inspecting the internals of TensorFlow and the
string returned is at the moment intended for debugging purposes.

A [tf.function](https://www.tensorflow.org/api_docs/python/tf/function) can be
imported and converted from TensorFlow to TensorFlow MLIR with this API by
extracting its ConcreteFunction (eagerly-executing wrapper around a
[tf.Graph](https://www.tensorflow.org/api_docs/python/tf/Graph)).

#### For example:


>>> @tf.function
... def add(a, b):
...   return a + b

```
>>> concrete_function = add.get_concrete_function(
...     tf.TensorSpec(None, tf.dtypes.float32),
...     tf.TensorSpec(None, tf.dtypes.float32))
>>> tf.mlir.experimental.convert_function(concrete_function)
'...module attributes {...} {...}'
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`concrete_function`
</td>
<td>
An object of type ConcreteFunction.
</td>
</tr><tr>
<td>
`pass_pipeline`
</td>
<td>
A textual description of an MLIR Pass Pipeline to run on the
module, see MLIR documentation for the
[textual pass pipeline syntax](https://mlir.llvm.org/docs/PassManagement/#textual-pass-pipeline-specification).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A textual representation of the MLIR module corresponding to the
ConcreteFunction.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
if concrete_function is invalid or cannot be converted
to MLIR.
</td>
</tr>
</table>

