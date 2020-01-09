page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.tanh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/activations.py#L201-L221">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Hyperbolic Tangent (tanh) activation function.

### Aliases:

* `tf.compat.v1.keras.activations.tanh`
* `tf.compat.v2.keras.activations.tanh`


``` python
tf.keras.activations.tanh(x)
```



<!-- Placeholder for "Used in" -->


#### For example:



```python
# Constant 1-D tensor populated with value list.
a = tf.constant([-3.0,-1.0, 0.0,1.0,3.0], dtype = tf.float32)
b = tf.keras.activations.tanh(a) #[-0.9950547,-0.7615942,
0.,0.7615942,0.9950547]
```
Arguments:
    x: Input tensor.

#### Returns:

A tensor of same shape and dtype of input `x`.
The tanh activation: `tanh(x) = sinh(x)/cosh(x) = ((exp(x) -
exp(-x))/(exp(x) + exp(-x)))`.
