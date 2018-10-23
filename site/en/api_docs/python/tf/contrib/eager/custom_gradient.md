

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.custom_gradient

``` python
tf.contrib.eager.custom_gradient(f)
```



Defined in [`tensorflow/python/eager/custom_gradient.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/eager/custom_gradient.py).

Decorator to define a function with a custom gradient.

The input function is expected to return the tuple
  (results, gradient_function).

The output function will return results while possibly recording the
gradient_function and inputs in the tape.

#### Args:

* <b>`f`</b>: function to be decorated.


#### Returns:

decorated function.