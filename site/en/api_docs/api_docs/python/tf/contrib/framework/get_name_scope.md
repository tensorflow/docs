

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.get_name_scope

``` python
tf.contrib.framework.get_name_scope()
```



Defined in [`tensorflow/contrib/framework/python/ops/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/framework/python/ops/ops.py).

Returns the current name scope of the default graph.

For example:

>     with tf.name_scope('scope1'):
>       with tf.name_scope('scope2'):
>         print(tf.contrib.framework.get_name_scope())
  would print the string `scope1/scope2`.

#### Returns:

A string representing the current name scope.