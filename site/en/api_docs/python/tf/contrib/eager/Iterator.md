

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.Iterator

## Class `Iterator`





Defined in [`tensorflow/contrib/eager/python/datasets.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/eager/python/datasets.py).

An iterator producing tf.Tensor objects from a tf.data.Dataset.

## Properties

<h3 id="output_classes"><code>output_classes</code></h3>

Returns the class of each component of an element of this iterator.

The expected values are `tf.Tensor` and `tf.SparseTensor`.

#### Returns:

A nested structure of Python `type` objects corresponding to each
component of an element of this dataset.

<h3 id="output_shapes"><code>output_shapes</code></h3>

Returns the shape of each component of an element of this iterator.

#### Returns:

A nested structure of `tf.TensorShape` objects corresponding to each
component of an element of this dataset.

<h3 id="output_types"><code>output_types</code></h3>

Returns the type of each component of an element of this iterator.

#### Returns:

A nested structure of `tf.DType` objects corresponding to each component
of an element of this dataset.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(dataset)
```

Creates a new iterator over the given dataset.

For example:

```python
dataset = tf.data.Dataset.range(4)
for x in Iterator(dataset):
  print(x)
```

Tensors produced will be placed on the device on which this iterator object
was created.

#### Args:

* <b>`dataset`</b>: A `tf.data.Dataset` object.


#### Raises:

* <b>`RuntimeError`</b>: When invoked without eager execution enabled.

<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```



<h3 id="__next__"><code>__next__</code></h3>

``` python
__next__()
```



<h3 id="get_next"><code>get_next</code></h3>

``` python
get_next(name=None)
```

Returns a nested structure of `tf.Tensor`s containing the next element.

#### Args:

* <b>`name`</b>: (Optional.) A name for the created operation. Currently unused.


#### Returns:

A nested structure of `tf.Tensor` objects.


#### Raises:

`tf.errors.OutOfRangeError`: If the end of the dataset has been reached.

<h3 id="next"><code>next</code></h3>

``` python
next()
```

Returns a nested structure of `tf.Tensor`s containing the next element.
    



