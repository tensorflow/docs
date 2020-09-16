description: Computes the confusion matrix from predictions and labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.confusion_matrix" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.confusion_matrix

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/confusion_matrix.py#L95-L201">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the confusion matrix from predictions and labels.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.confusion_matrix(
    labels, predictions, num_classes=None, weights=None, dtype=tf.dtypes.int32,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The matrix columns represent the prediction labels and the rows represent the
real labels. The confusion matrix is always a 2-D array of shape `[n, n]`,
where `n` is the number of valid labels for a given classification task. Both
prediction and labels must be 1-D arrays of the same shape in order for this
function to work.

If `num_classes` is `None`, then `num_classes` will be set to one plus the
maximum value in either predictions or labels. Class labels are expected to
start at 0. For example, if `num_classes` is 3, then the possible labels
would be `[0, 1, 2]`.

If `weights` is not `None`, then each prediction contributes its
corresponding weight to the total value of the confusion matrix cell.

#### For example:



```python
  tf.math.confusion_matrix([1, 2, 4], [2, 2, 4]) ==>
      [[0 0 0 0 0]
       [0 0 1 0 0]
       [0 0 1 0 0]
       [0 0 0 0 0]
       [0 0 0 0 1]]
```

Note that the possible labels are assumed to be `[0, 1, 2, 3, 4]`,
resulting in a 5x5 confusion matrix.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
1-D `Tensor` of real labels for the classification task.
</td>
</tr><tr>
<td>
`predictions`
</td>
<td>
1-D `Tensor` of predictions for a given classification.
</td>
</tr><tr>
<td>
`num_classes`
</td>
<td>
The possible number of labels the classification task can
have. If this value is not provided, it will be calculated
using both predictions and labels array.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
An optional `Tensor` whose shape matches `predictions`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Data type of the confusion matrix.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Scope name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `dtype` with shape `[n, n]` representing the confusion
matrix, where `n` is the number of possible labels in the classification
task.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both predictions and labels are not 1-D vectors and have
mismatched shapes, or if `weights` is not `None` and its shape doesn't
match `predictions`.
</td>
</tr>
</table>

