page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.IndexedSlices


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/IndexedSlices">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L62-L175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `IndexedSlices`

A sparse representation of a set of tensor slices at given indices.



### Aliases:

* Class <a href="/api_docs/python/tf/IndexedSlices"><code>tf.compat.v1.IndexedSlices</code></a>
* Class <a href="/api_docs/python/tf/IndexedSlices"><code>tf.compat.v2.IndexedSlices</code></a>


<!-- Placeholder for "Used in" -->

This class is a simple wrapper for a pair of `Tensor` objects:

* `values`: A `Tensor` of any dtype with shape `[D0, D1, ..., Dn]`.
* `indices`: A 1-D integer `Tensor` with shape `[D0]`.

An `IndexedSlices` is typically used to represent a subset of a larger
tensor `dense` of shape `[LARGE0, D1, .. , DN]` where `LARGE0 >> D0`.
The values in `indices` are the indices in the first dimension of
the slices that have been extracted from the larger tensor.

The dense tensor `dense` represented by an `IndexedSlices` `slices` has

```python
dense[slices.indices[i], :, :, :, ...] = slices.values[i, :, :, :, ...]
```

The `IndexedSlices` class is used principally in the definition of
gradients for operations that have sparse gradients
(e.g. <a href="../tf/gather"><code>tf.gather</code></a>).

Contrast this representation with
<a href="../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>,
which uses multi-dimensional indices and scalar values.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L90-L95">View source</a>

``` python
__init__(
    values,
    indices,
    dense_shape=None
)
```

Creates an `IndexedSlices`.




## Properties

<h3 id="dense_shape"><code>dense_shape</code></h3>

A 1-D `Tensor` containing the shape of the corresponding dense tensor.


<h3 id="device"><code>device</code></h3>

The name of the device on which `values` will be produced, or `None`.


<h3 id="dtype"><code>dtype</code></h3>

The `DType` of elements in this tensor.


<h3 id="graph"><code>graph</code></h3>

The `Graph` that contains the values, indices, and shape tensors.


<h3 id="indices"><code>indices</code></h3>

A 1-D `Tensor` containing the indices of the slices.


<h3 id="name"><code>name</code></h3>

The name of this `IndexedSlices`.


<h3 id="op"><code>op</code></h3>

The `Operation` that produces `values` as an output.


<h3 id="values"><code>values</code></h3>

A `Tensor` containing the values of the slices.




## Methods

<h3 id="__neg__"><code>__neg__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L143-L144">View source</a>

``` python
__neg__()
```




<h3 id="consumers"><code>consumers</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L174-L175">View source</a>

``` python
consumers()
```
