page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.RNNCellDeviceWrapper

## Class `RNNCellDeviceWrapper`

Operator that ensures an RNNCell runs on a particular device.





Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Construct a `DeviceWrapper` for `cell` with device `device`.

Ensures the wrapped `cell` is called with <a href="../../../../tf/device"><code>tf.device(device)</code></a>.

#### Args:


* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`device`</b>: A device string or function, for passing to <a href="../../../../tf/device"><code>tf.device</code></a>.



## Properties

<h3 id="output_size"><code>output_size</code></h3>




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






