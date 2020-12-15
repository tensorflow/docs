description: An n-way switch statement which calls a single branch function.

robots: noindex

# tf.raw_ops.StatelessCase

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An n-way switch statement which calls a single branch function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StatelessCase`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessCase(
    branch_index, input, Tout, branches, output_shapes=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

    An n-way switch statement, implementing the following:
    ```
    switch (branch_index) {
      case 0:
        output = branches[0](input);
        break;
      case 1:
        output = branches[1](input);
        break;
      ...
      case [[nbranches-1]]:
      default:
        output = branches[nbranches-1](input);
        break;
    }
    ```

    This should only be used when the none of branches has stateful ops.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`branch_index`
</td>
<td>
A `Tensor` of type `int32`.
The branch selector, an int32 Tensor.
</td>
</tr><tr>
<td>
`input`
</td>
<td>
A list of `Tensor` objects.
A list of input tensors passed to the branch function.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A list of `tf.DTypes`. A list of output types.
</td>
</tr><tr>
<td>
`branches`
</td>
<td>
A list of functions decorated with @Defun that has length `>= 1`.
A list of functions each of which takes 'inputs' and returns a list of
tensors, whose types are the same as what every other branch returns.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of `Tensor` objects of type `Tout`.
</td>
</tr>

</table>

