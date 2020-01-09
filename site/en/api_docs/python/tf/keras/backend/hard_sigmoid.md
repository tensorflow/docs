page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.hard_sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L4604-L4623">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Segment-wise linear approximation of sigmoid.

### Aliases:

* `tf.compat.v1.keras.backend.hard_sigmoid`
* `tf.compat.v2.keras.backend.hard_sigmoid`


``` python
tf.keras.backend.hard_sigmoid(x)
```



<!-- Placeholder for "Used in" -->

Faster than sigmoid.
Returns `0.` if `x < -2.5`, `1.` if `x > 2.5`.
In `-2.5 <= x <= 2.5`, returns `0.2 * x + 0.5`.

#### Arguments:


* <b>`x`</b>: A tensor or variable.


#### Returns:

A tensor.
