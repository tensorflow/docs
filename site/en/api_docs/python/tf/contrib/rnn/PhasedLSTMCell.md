page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.PhasedLSTMCell

## Class `PhasedLSTMCell`

Phased LSTM recurrent network cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

https://arxiv.org/pdf/1610.09513v1.pdf

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    use_peepholes=False,
    leak=0.001,
    ratio_on=0.1,
    trainable_ratio_on=True,
    period_init_min=1.0,
    period_init_max=1000.0,
    reuse=None
)
```

Initialize the Phased LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the Phased LSTM cell.
* <b>`use_peepholes`</b>: bool, set True to enable peephole connections.
* <b>`leak`</b>: float or scalar float Tensor with value in [0, 1]. Leak applied
    during training.
* <b>`ratio_on`</b>: float or scalar float Tensor with value in [0, 1]. Ratio of the
    period during which the gates are open.
* <b>`trainable_ratio_on`</b>: bool, weather ratio_on is trainable.
* <b>`period_init_min`</b>: float or scalar float Tensor. With value > 0.
    Minimum value of the initialized period.
    The period values are initialized by drawing from the distribution:
    e^U(log(period_init_min), log(period_init_max))
    Where U(.,.) is the uniform distribution.
* <b>`period_init_max`</b>: float or scalar float Tensor.
    With value > period_init_min. Maximum value of the initialized period.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope. If not `True`, and the existing scope already has
  the given variables, an error is raised.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```

Return zero-filled state tensor(s).


#### Args:


* <b>`batch_size`</b>: int, float, or unit Tensor representing the batch size.
* <b>`dtype`</b>: the data type to use for the state.


#### Returns:

If `state_size` is an int or TensorShape, then the return value is a
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.




