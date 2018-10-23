

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.export.ServingInputReceiver

## Class `ServingInputReceiver`





Defined in [`tensorflow/python/estimator/export/export.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/estimator/export/export.py).

A return type for a serving_input_receiver_fn.

The expected return values are:
  features: A dict of string to `Tensor` or `SparseTensor`, specifying the
    features to be passed to the model.
  receiver_tensors: a `Tensor`, or a dict of string to `Tensor`, specifying
    input nodes where this receiver expects to be fed by default.  Typically,
    this is a single placeholder expecting serialized `tf.Example` protos.
  receiver_tensors_alternatives: a dict of string to additional
    groups of receiver tensors, each of which may be a `Tensor` or a dict of
    string to `Tensor`.  These named receiver tensor alternatives generate
    additional serving signatures, which may be used to feed inputs at
    different points within the input reciever subgraph.  A typical usage is
    to allow feeding raw feature `Tensor`s *downstream* of the
    tf.parse_example() op.  Defaults to None.

## Properties

<h3 id="features"><code>features</code></h3>

Alias for field number 0

<h3 id="receiver_tensors"><code>receiver_tensors</code></h3>

Alias for field number 1

<h3 id="receiver_tensors_alternatives"><code>receiver_tensors_alternatives</code></h3>

Alias for field number 2



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    features,
    receiver_tensors,
    receiver_tensors_alternatives=None
)
```





