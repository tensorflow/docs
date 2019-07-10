page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.export.ServingInputReceiver

## Class `ServingInputReceiver`

A return type for a serving_input_receiver_fn.



### Aliases:

* Class `tf.compat.v1.estimator.export.ServingInputReceiver`
* Class `tf.compat.v2.estimator.export.ServingInputReceiver`
* Class `tf.estimator.export.ServingInputReceiver`



Defined in [`python/estimator/export/export.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/export/export.py).

<!-- Placeholder for "Used in" -->

The expected return values are:
  features: A `Tensor`, `SparseTensor`, or dict of string or int to `Tensor`
    or `SparseTensor`, specifying the features to be passed to the model.
    Note: if `features` passed is not a dict, it will be wrapped in a dict
    with a single entry, using 'feature' as the key.  Consequently, the model
    must accept a feature dict of the form {'feature': tensor}.  You may use
    `TensorServingInputReceiver` if you want the tensor to be passed as is.
  receiver_tensors: A `Tensor`, `SparseTensor`, or dict of string to `Tensor`
    or `SparseTensor`, specifying input nodes where this receiver expects to
    be fed by default.  Typically, this is a single placeholder expecting
    serialized `tf.Example` protos.
  receiver_tensors_alternatives: a dict of string to additional
    groups of receiver tensors, each of which may be a `Tensor`,
    `SparseTensor`, or dict of string to `Tensor` or`SparseTensor`.
    These named receiver tensor alternatives generate additional serving
    signatures, which may be used to feed inputs at different points within
    the input receiver subgraph.  A typical usage is to allow feeding raw
    feature `Tensor`s *downstream* of the tf.parse_example() op.
    Defaults to None.

## Properties

<h3 id="features"><code>features</code></h3>




<h3 id="receiver_tensors"><code>receiver_tensors</code></h3>




<h3 id="receiver_tensors_alternatives"><code>receiver_tensors_alternatives</code></h3>






