page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.set_element_type

Indicates that the entity is expected hold items of specified type/shape.

``` python
tf.contrib.autograph.set_element_type(
    entity,
    dtype,
    shape=UNSPECIFIED
)
```



Defined in [`python/autograph/lang/directives.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/lang/directives.py).

<!-- Placeholder for "Used in" -->

The staged TensorFlow ops will reflect and assert this data type. Ignored
otherwise.

#### Args:


* <b>`entity`</b>: The entity to annotate.
* <b>`dtype`</b>: TensorFlow dtype value to assert for entity.
* <b>`shape`</b>: Optional shape to assert for entity.