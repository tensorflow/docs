page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.set_element_type

``` python
tf.contrib.autograph.set_element_type(
    entity,
    dtype,
    shape=UNSPECIFIED
)
```



Defined in [`tensorflow/python/autograph/lang/directives.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/autograph/lang/directives.py).

Indicates that the entity is expected hold items of specified type/shape.

The staged TensorFlow ops will reflect and assert this data type. Ignored
otherwise.

#### Args:

* <b>`entity`</b>: The entity to annotate.
* <b>`dtype`</b>: TensorFlow dtype value to assert for entity.
* <b>`shape`</b>: Optional shape to assert for entity.