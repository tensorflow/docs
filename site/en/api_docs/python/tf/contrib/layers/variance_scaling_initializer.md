page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.variance_scaling_initializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/initializers.py#L62-L153">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns an initializer that generates tensors without scaling variance.

``` python
tf.contrib.layers.variance_scaling_initializer(
    factor=2.0,
    mode='FAN_IN',
    uniform=False,
    seed=None,
    dtype=tf.dtypes.float32
)
```



<!-- Placeholder for "Used in" -->

When initializing a deep network, it is in principle advantageous to keep
the scale of the input variance constant, so it does not explode or diminish
by reaching the final layer. This initializer use the following formula:

```python
  if mode='FAN_IN': # Count only number of input connections.
    n = fan_in
  elif mode='FAN_OUT': # Count only number of output connections.
    n = fan_out
  elif mode='FAN_AVG': # Average number of inputs and output connections.
    n = (fan_in + fan_out)/2.0

    truncated_normal(shape, 0.0, stddev=sqrt(factor / n))
```

* To get [Delving Deep into Rectifiers](
   http://arxiv.org/pdf/1502.01852v1.pdf) (also know as the "MSRA 
   initialization"), use (Default):<br/>
  `factor=2.0 mode='FAN_IN' uniform=False`
* To get [Convolutional Architecture for Fast Feature Embedding](
   http://arxiv.org/abs/1408.5093), use:<br/>
  `factor=1.0 mode='FAN_IN' uniform=True`
* To get [Understanding the difficulty of training deep feedforward neural
  networks](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf),
  use:<br/>
  `factor=1.0 mode='FAN_AVG' uniform=True.`
* To get `xavier_initializer` use either:<br/>
  `factor=1.0 mode='FAN_AVG' uniform=True`, or<br/>
  `factor=1.0 mode='FAN_AVG' uniform=False`.

#### Args:


* <b>`factor`</b>: Float.  A multiplicative factor.
* <b>`mode`</b>: String.  'FAN_IN', 'FAN_OUT', 'FAN_AVG'.
* <b>`uniform`</b>: Whether to use uniform or normal distributed random initialization.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
      <a href="../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: The data type. Only floating point types are supported.


#### Returns:

An initializer that generates tensors with unit variance.



#### Raises:


* <b>`ValueError`</b>: if `dtype` is not a floating point type.
* <b>`TypeError`</b>: if `mode` is not in ['FAN_IN', 'FAN_OUT', 'FAN_AVG'].
