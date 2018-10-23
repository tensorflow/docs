

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.export.ClassificationOutput

### `class tf.estimator.export.ClassificationOutput`



Defined in [`tensorflow/python/estimator/export/export_output.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/estimator/export/export_output.py).

Represents the output of a classification head.

Either classes or scores or both must be set.

The classes `Tensor` must provide string labels, not integer class IDs.

If only classes is set, it is interpreted as providing top-k results in
descending order.

If only scores is set, it is interpreted as providing a score for every class
in order of class ID.

If both classes and scores are set, they are interpreted as zipped, so each
score corresponds to the class at the same index.  Clients should not depend
on the order of the entries.

## Properties

<h3 id="classes"><code>classes</code></h3>



<h3 id="scores"><code>scores</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    scores=None,
    classes=None
)
```

Constructor for `ClassifyOutput`.

#### Args:

* <b>`scores`</b>: A float `Tensor` giving scores (sometimes but not always
      interpretable as probabilities) for each class.  May be `None`, but
      only if `classes` is set.  Interpretation varies-- see class doc.
* <b>`classes`</b>: A string `Tensor` giving predicted class labels.  May be `None`,
      but only if `scores` is set.  Interpretation varies-- see class doc.


#### Raises:

* <b>`ValueError`</b>: if neither classes nor scores is set, or one of them is not a
      `Tensor` with the correct dtype.

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

``` python
as_signature_def(receiver_tensors)
```





