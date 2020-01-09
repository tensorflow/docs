page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/layers.py#L3010-L3062">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Builds a stack of layers by applying layer repeatedly using stack_args.

``` python
tf.contrib.layers.stack(
    inputs,
    layer,
    stack_args,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

`stack` allows you to repeatedly apply the same operation with different
arguments `stack_args[i]`. For each application of the layer, `stack` creates
a new scope appended with an increasing number. For example:

```python
  y = stack(x, fully_connected, [32, 64, 128], scope='fc')
  # It is equivalent to:

  x = fully_connected(x, 32, scope='fc/fc_1')
  x = fully_connected(x, 64, scope='fc/fc_2')
  y = fully_connected(x, 128, scope='fc/fc_3')
```

If the `scope` argument is not given in `kwargs`, it is set to
`layer.__name__`, or `layer.func.__name__` (for `functools.partial`
objects). If neither `__name__` nor `func.__name__` is available, the
layers are called with `scope='stack'`.

#### Args:


* <b>`inputs`</b>: A `Tensor` suitable for layer.
* <b>`layer`</b>: A layer with arguments `(inputs, *args, **kwargs)`
* <b>`stack_args`</b>: A list/tuple of parameters for each call of layer.
* <b>`**kwargs`</b>: Extra kwargs for the layer.


#### Returns:

A `Tensor` result of applying the stacked layers.



#### Raises:


* <b>`ValueError`</b>: If the op is unknown or wrong.
