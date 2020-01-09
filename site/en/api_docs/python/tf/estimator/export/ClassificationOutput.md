page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.ClassificationOutput


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L102-L167">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ClassificationOutput`

Represents the output of a classification head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput)

### Aliases:

* Class `tf.compat.v1.estimator.export.ClassificationOutput`
* Class `tf.compat.v2.estimator.export.ClassificationOutput`


<!-- Placeholder for "Used in" -->

Either classes or scores or both must be set.

The classes `Tensor` must provide string labels, not integer class IDs.

If only classes is set, it is interpreted as providing top-k results in
descending order.

If only scores is set, it is interpreted as providing a score for every class
in order of class ID.

If both classes and scores are set, they are interpreted as zipped, so each
score corresponds to the class at the same index.  Clients should not depend
on the order of the entries.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L120-L148">View source</a>

``` python
__init__(
    scores=None,
    classes=None
)
```

Constructor for `ClassificationOutput`.


#### Args:


* <b>`scores`</b>: A float `Tensor` giving scores (sometimes but not always
    interpretable as probabilities) for each class.  May be `None`, but
    only if `classes` is set.  Interpretation varies-- see class doc.
* <b>`classes`</b>: A string `Tensor` giving predicted class labels.  May be `None`,
    but only if `scores` is set.  Interpretation varies-- see class doc.


#### Raises:


* <b>`ValueError`</b>: if neither classes nor scores is set, or one of them is not a
    `Tensor` with the correct dtype.



## Properties

<h3 id="classes"><code>classes</code></h3>




<h3 id="scores"><code>scores</code></h3>






## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/model_utils/export_output.py#L158-L167">View source</a>

``` python
as_signature_def(receiver_tensors)
```

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

#### Args:


* <b>`receiver_tensors`</b>: a `Tensor`, or a dict of string to `Tensor`, specifying
  input nodes that will be fed.
