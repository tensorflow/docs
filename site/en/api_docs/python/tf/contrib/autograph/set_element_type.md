page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.set_element_type


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/lang/directives.py#L34-L47">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Indicates that the entity is expected hold items of specified type/shape.

``` python
tf.contrib.autograph.set_element_type(
    entity,
    dtype,
    shape=UNSPECIFIED
)
```



<!-- Placeholder for "Used in" -->

The staged TensorFlow ops will reflect and assert this data type. Ignored
otherwise.

#### Args:


* <b>`entity`</b>: The entity to annotate.
* <b>`dtype`</b>: TensorFlow dtype value to assert for entity.
* <b>`shape`</b>: Optional shape to assert for entity.
