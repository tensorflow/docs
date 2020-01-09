page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.elu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/activations.py#L75-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Exponential linear unit.

### Aliases:

* `tf.compat.v1.keras.activations.elu`
* `tf.compat.v2.keras.activations.elu`


``` python
tf.keras.activations.elu(
    x,
    alpha=1.0
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Input tensor.
* <b>`alpha`</b>: A scalar, slope of negative section.


#### Returns:

The exponential linear activation: `x` if `x > 0` and
  `alpha * (exp(x)-1)` if `x < 0`.



#### Reference:

- [Fast and Accurate Deep Network Learning by Exponential
  Linear Units (ELUs)](https://arxiv.org/abs/1511.07289)
