

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_str_any

### Aliases:

* `tf.compat.as_str_any`
* `tf.contrib.meta_graph_transform.meta_graph_transform.compat.as_str_any`

``` python
tf.compat.as_str_any(value)
```



Defined in [`tensorflow/python/util/compat.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/util/compat.py).

Converts to `str` as `str(value)`, but use `as_str` for `bytes`.

#### Args:

* <b>`value`</b>: A object that can be converted to `str`.


#### Returns:

A `str` object.