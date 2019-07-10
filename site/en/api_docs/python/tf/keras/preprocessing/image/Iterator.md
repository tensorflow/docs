page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.Iterator

## Class `Iterator`



Inherits From: [`Sequence`](../../../../tf/keras/utils/Sequence)

### Aliases:

* Class `tf.compat.v1.keras.preprocessing.image.Iterator`
* Class `tf.compat.v2.keras.preprocessing.image.Iterator`
* Class `tf.keras.preprocessing.image.Iterator`



Defined in [`python/keras/preprocessing/image.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/preprocessing/image.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    n,
    batch_size,
    shuffle,
    seed
)
```






## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(idx)
```




<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```




<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```




<h3 id="next"><code>next</code></h3>

``` python
next()
```

For python 2.x.

# Returns
    The next batch.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end()
```




<h3 id="reset"><code>reset</code></h3>

``` python
reset()
```






## Class Members

* `white_list_formats` <a id="white_list_formats"></a>
