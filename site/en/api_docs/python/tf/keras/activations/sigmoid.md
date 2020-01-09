page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/activations.py#L224-L246">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sigmoid.

### Aliases:

* `tf.compat.v1.keras.activations.sigmoid`
* `tf.compat.v2.keras.activations.sigmoid`


``` python
tf.keras.activations.sigmoid(x)
```



<!-- Placeholder for "Used in" -->

Applies the sigmoid activation function. The sigmoid function is defined as
1 divided by (1 + exp(-x)). It's curve is like an "S" and is like a smoothed
version of the Heaviside (Unit Step Function) function. For small values
(<-5) the sigmoid returns a value close to zero and for larger values (>5)
the result of the function gets close to 1.
Arguments:
    x: A tensor or variable.

#### Returns:

A tensor.

Sigmoid activation function.

#### Arguments:


* <b>`x`</b>: Input tensor.


#### Returns:

The sigmoid activation: `(1.0 / (1.0 + exp(-x)))`.
