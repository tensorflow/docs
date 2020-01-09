page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.metrics.accuracy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/metrics/python/metrics/classification.py#L32-L67">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the percentage of times that predictions matches labels.

``` python
tf.contrib.metrics.accuracy(
    predictions,
    labels,
    weights=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`predictions`</b>: the predicted values, a `Tensor` whose dtype and shape
             matches 'labels'.
* <b>`labels`</b>: the ground truth values, a `Tensor` of any shape and
        bool, integer, or string dtype.
* <b>`weights`</b>: None or `Tensor` of float values to reweight the accuracy.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

Accuracy `Tensor`.



#### Raises:


* <b>`ValueError`</b>: if dtypes don't match or
            if dtype is not bool, integer, or string.
