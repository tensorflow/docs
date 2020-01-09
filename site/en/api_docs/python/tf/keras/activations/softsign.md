page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.softsign


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/activations.py#L165-L175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Softsign activation function.

### Aliases:

* `tf.compat.v1.keras.activations.softsign`
* `tf.compat.v2.keras.activations.softsign`


``` python
tf.keras.activations.softsign(x)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Input tensor.


#### Returns:

The softplus activation: `x / (abs(x) + 1)`.
