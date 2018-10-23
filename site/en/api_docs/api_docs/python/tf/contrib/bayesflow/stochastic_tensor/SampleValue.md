

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.stochastic_tensor.SampleValue

## Class `SampleValue`





Defined in [`tensorflow/contrib/bayesflow/python/ops/stochastic_tensor_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/bayesflow/python/ops/stochastic_tensor_impl.py).

See the guide: [BayesFlow Stochastic Tensors (contrib) > Stochastic Tensor Value Types](../../../../../../api_guides/python/contrib.bayesflow.stochastic_tensor#Stochastic_Tensor_Value_Types)

Draw samples, possibly adding new outer dimensions along the way.

This ValueType draws samples from StochasticTensors run within its
context, increasing the rank according to the requested shape.

Examples:

```python
mu = tf.zeros((2,3))
sigma = tf.ones((2, 3))
with sg.value_type(sg.SampleValue()):
  st = sg.StochasticTensor(
    tf.contrib.distributions.Normal, mu=mu, sigma=sigma)
# draws 1 sample and does not reshape
assertEqual(st.value().get_shape(), (2, 3))
```

```python
mu = tf.zeros((2,3))
sigma = tf.ones((2, 3))
with sg.value_type(sg.SampleValue(4)):
  st = sg.StochasticTensor(
    tf.contrib.distributions.Normal, mu=mu, sigma=sigma)
# draws 4 samples each with shape (2, 3) and concatenates
assertEqual(st.value().get_shape(), (4, 2, 3))
```

## Properties

<h3 id="shape"><code>shape</code></h3>



<h3 id="stop_gradient"><code>stop_gradient</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    shape=(),
    stop_gradient=False
)
```

Sample according to shape.

For the given StochasticTensor `st` using this value type,
the shape of `st.value()` will match that of
`st.distribution.sample(shape)`.

#### Args:

* <b>`shape`</b>: A shape tuple or int32 tensor.  The sample shape.
    Default is a scalar: take one sample and do not change the size.
* <b>`stop_gradient`</b>: If `True`, StochasticTensors' values are wrapped in
    `stop_gradient`, to avoid backpropagation through.

<h3 id="declare_inputs"><code>declare_inputs</code></h3>

``` python
declare_inputs(
    unused_stochastic_tensor,
    unused_inputs_dict
)
```



<h3 id="popped_above"><code>popped_above</code></h3>

``` python
popped_above(unused_value_type)
```



<h3 id="pushed_above"><code>pushed_above</code></h3>

``` python
pushed_above(unused_value_type)
```





