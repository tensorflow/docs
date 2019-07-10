page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_name_scope

Returns the current name scope of the default graph.

``` python
tf.contrib.framework.get_name_scope()
```



Defined in [`contrib/framework/python/ops/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/ops.py).

<!-- Placeholder for "Used in" -->


#### For example:


```python
with tf.name_scope('scope1'):
  with tf.name_scope('scope2'):
    print(tf.contrib.framework.get_name_scope())
```
would print the string `scope1/scope2`.



#### Returns:

A string representing the current name scope.
