

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.Iterator

## Class `Iterator`





Defined in [`tensorflow/contrib/eager/python/datasets.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/eager/python/datasets.py).

An iterator producing tf.Tensor objects from a tf.data.Dataset.

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



<h3 id="next"><code>next</code></h3>

``` python
next()
```

Return the next tf.Tensor from the dataset.



