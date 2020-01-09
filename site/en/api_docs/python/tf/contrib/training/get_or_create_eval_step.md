page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.get_or_create_eval_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/evaluation.py#L37-L61">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets or creates the eval step `Tensor`.

``` python
tf.contrib.training.get_or_create_eval_step()
```



<!-- Placeholder for "Used in" -->


#### Returns:

A `Tensor` representing a counter for the evaluation step.



#### Raises:


* <b>`ValueError`</b>: If multiple `Tensors` have been added to the
  <a href="../../../tf/GraphKeys#EVAL_STEP"><code>tf.GraphKeys.EVAL_STEP</code></a> collection.
