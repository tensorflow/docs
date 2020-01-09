page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.RNNCellDeviceWrapper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py#L115-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RNNCellDeviceWrapper`

Operator that ensures an RNNCell runs on a particular device.



### Aliases:

* Class `tf.compat.v2.nn.RNNCellDeviceWrapper`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py#L119-L120">View source</a>

``` python
__init__(
    *args,
    **kwargs
)
```

Construct a `DeviceWrapper` for `cell` with device `device`.

Ensures the wrapped `cell` is called with <a href="../../tf/device"><code>tf.device(device)</code></a>.

#### Args:


* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`device`</b>: A device string or function, for passing to <a href="../../tf/device"><code>tf.device</code></a>.
* <b>`**kwargs`</b>: dict of keyword arguments for base layer.



## Properties

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="state_size"><code>state_size</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L976-L977">View source</a>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/rnn_cell_wrapper_impl.py#L428-L431">View source</a>

``` python
zero_state(
    batch_size,
    dtype
)
```
