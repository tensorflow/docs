page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.sparsemax.sparsemax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/sparsemax/python/ops/sparsemax.py#L30-L94">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes sparsemax activations [1].

``` python
tf.contrib.sparsemax.sparsemax(
    logits,
    name=None
)
```



<!-- Placeholder for "Used in" -->

For each batch `i` and class `j` we have
  <div> $$sparsemax[i, j] = max(logits[i, j] - tau(logits[i, :]), 0)$$ </div>

[1]: https://arxiv.org/abs/1602.02068

#### Args:


* <b>`logits`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`,
  `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `logits`.
