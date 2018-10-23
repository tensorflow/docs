

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.export.ServingInputReceiver

### `class tf.estimator.export.ServingInputReceiver`



Defined in [`tensorflow/python/estimator/export/export.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/estimator/export/export.py).

A return type for a serving_input_receiver_fn.

The expected return values are:
  features: A dict of string to `Tensor` or `SparseTensor`, specifying the
    features to be passed to the model.
  receiver_tensors: a `Tensor`, or a dict of string to `Tensor`, specifying
    input nodes where this receiver expects to be fed.  Typically, this is a
    single placeholder expecting serialized `tf.Example` protos.

## Properties

<h3 id="features"><code>features</code></h3>

Alias for field number 0

<h3 id="receiver_tensors"><code>receiver_tensors</code></h3>

Alias for field number 1



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    cls,
    features,
    receiver_tensors
)
```





