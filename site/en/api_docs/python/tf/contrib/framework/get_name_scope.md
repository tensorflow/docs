

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.get_name_scope

### `tf.contrib.framework.get_name_scope`

``` python
get_name_scope()
```



Defined in [`tensorflow/contrib/framework/python/ops/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/framework/python/ops/ops.py).

Returns the current name scope of the default graph.

For example:

>     with tf.name_scope('scope1'):
>       with tf.name_scope('scope2'):
>         print(tf.contrib.framework.get_name_scope())
  would print the string `scope1/scope2`.

#### Returns:

  A string represnting the current name scope.