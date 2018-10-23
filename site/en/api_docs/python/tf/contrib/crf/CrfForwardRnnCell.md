

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.crf.CrfForwardRnnCell

### `class tf.contrib.crf.CrfForwardRnnCell`



Defined in [`tensorflow/contrib/crf/python/ops/crf.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/crf/python/ops/crf.py).

See the guide: [CRF (contrib)](../../../../../api_guides/python/contrib.crf)

Computes the alpha values in a linear-chain CRF.

See http://www.cs.columbia.edu/~mcollins/fb.pdf for reference.

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(transition_params)
```

Initialize the CrfForwardRnnCell.

#### Args:

* <b>`transition_params`</b>: A [num_tags, num_tags] matrix of binary potentials.
      This matrix is expanded into a [1, num_tags, num_tags] in preparation
      for the broadcast summation occurring within the cell.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Build the CrfForwardRnnCell.

#### Args:

* <b>`inputs`</b>: A [batch_size, num_tags] matrix of unary potentials.
* <b>`state`</b>: A [batch_size, num_tags] matrix containing the previous alpha
      values.
* <b>`scope`</b>: Unused variable scope of this cell.


#### Returns:

  new_alphas, new_alphas: A pair of [batch_size, num_tags] matrices
      values containing the new alpha values.

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
  `N-D` tensor of shape `[batch_size x state_size]` filled with zeros.

  If `state_size` is a nested list or tuple, then the return value is
  a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size x s]` for each s in `state_size`.



