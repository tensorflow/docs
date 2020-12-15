description: Category crossing layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.CategoryCrossing" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="partial_crossing"/>
</div>

# tf.keras.layers.experimental.preprocessing.CategoryCrossing

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/category_crossing.py#L38-L210">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Category crossing layer.

Inherits From: [`Layer`](../../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.CategoryCrossing`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.CategoryCrossing(
    depth=None, name=None, separator=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer concatenates multiple categorical inputs into a single categorical
output (similar to Cartesian product). The output dtype is string.

#### Usage:


>>> inp_1 = ['a', 'b', 'c']
>>> inp_2 = ['d', 'e', 'f']
>>> layer = tf.keras.layers.experimental.preprocessing.CategoryCrossing()
>>> layer([inp_1, inp_2])
<tf.Tensor: shape=(3, 1), dtype=string, numpy=
  array([[b'a_X_d'],
         [b'b_X_e'],
         [b'c_X_f']], dtype=object)>


```
>>> inp_1 = ['a', 'b', 'c']
>>> inp_2 = ['d', 'e', 'f']
>>> layer = tf.keras.layers.experimental.preprocessing.CategoryCrossing(
...    separator='-')
>>> layer([inp_1, inp_2])
<tf.Tensor: shape=(3, 1), dtype=string, numpy=
  array([[b'a-d'],
         [b'b-e'],
         [b'c-f']], dtype=object)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`depth`
</td>
<td>
depth of input crossing. By default None, all inputs are crossed into
one output. It can also be an int or tuple/list of ints. Passing an
integer will create combinations of crossed outputs with depth up to that
integer, i.e., [1, 2, ..., `depth`), and passing a tuple of integers will
create crossed outputs with depth for the specified values in the tuple,
i.e., `depth`=(N1, N2) will create all possible crossed outputs with depth
equal to N1 or N2. Passing `None` means a single crossed output with all
inputs. For example, with inputs `a`, `b` and `c`, `depth=2` means the
output will be [a;b;c;cross(a, b);cross(bc);cross(ca)].
</td>
</tr><tr>
<td>
`separator`
</td>
<td>
A string added between each input being joined. Defaults to
'_X_'.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name to give to the layer.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments to construct a layer.
</td>
</tr>
</table>


Input shape: a list of string or int tensors or sparse tensors of shape
  `[batch_size, d1, ..., dm]`

Output shape: a single string or int tensor or sparse tensor of shape
  `[batch_size, d1, ..., dm]`

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
If any input is `RaggedTensor`, the output is `RaggedTensor`.
Else, if any input is `SparseTensor`, the output is `SparseTensor`.
Otherwise, the output is `Tensor`.
</td>
</tr>

</table>


Example: (`depth`=None)
  If the layer receives three inputs:
  `a=[[1], [4]]`, `b=[[2], [5]]`, `c=[[3], [6]]`
  the output will be a string tensor:
  `[[b'1_X_2_X_3'], [b'4_X_5_X_6']]`

Example: (`depth` is an integer)
  With the same input above, and if `depth`=2,
  the output will be a list of 6 string tensors:
  `[[b'1'], [b'4']]`
  `[[b'2'], [b'5']]`
  `[[b'3'], [b'6']]`
  `[[b'1_X_2'], [b'4_X_5']]`,
  `[[b'2_X_3'], [b'5_X_6']]`,
  `[[b'3_X_1'], [b'6_X_4']]`

Example: (`depth` is a tuple/list of integers)
  With the same input above, and if `depth`=(2, 3)
  the output will be a list of 4 string tensors:
  `[[b'1_X_2'], [b'4_X_5']]`,
  `[[b'2_X_3'], [b'5_X_6']]`,
  `[[b'3_X_1'], [b'6_X_4']]`,
  `[[b'1_X_2_X_3'], [b'4_X_5_X_6']]`

## Methods

<h3 id="partial_crossing"><code>partial_crossing</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/category_crossing.py#L127-L140">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>partial_crossing(
    partial_inputs, ragged_out, sparse_out
)
</code></pre>

Gets the crossed output from a partial list/tuple of inputs.




