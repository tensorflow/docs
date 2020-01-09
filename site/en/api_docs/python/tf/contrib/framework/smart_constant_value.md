page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.smart_constant_value


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/smart_cond.py#L62-L90">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return the bool value for `pred`, or None if `pred` had a dynamic value.

``` python
tf.contrib.framework.smart_constant_value(pred)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`pred`</b>: A scalar, either a Python bool or tensor.


#### Returns:

True or False if `pred` has a constant boolean value, None otherwise.



#### Raises:


* <b>`TypeError`</b>: If `pred` is not a Tensor or bool.
