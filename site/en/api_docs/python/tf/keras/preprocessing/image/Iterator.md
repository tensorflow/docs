

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.Iterator

## Class `Iterator`

Inherits From: [`Sequence`](../../../../tf/keras/utils/Sequence)



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Base class for image data iterators.

Every `Iterator` must implement the `_get_batches_of_transformed_samples`
method.

#### Arguments:

* <b>`n`</b>: Integer, total number of samples in the dataset to loop over.
* <b>`batch_size`</b>: Integer, size of a batch.
* <b>`shuffle`</b>: Boolean, whether to shuffle the data between epochs.
* <b>`seed`</b>: Random seeding for data shuffling.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    n,
    batch_size,
    shuffle,
    seed
)
```



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



<h3 id="__next__"><code>__next__</code></h3>

``` python
__next__(
    *args,
    **kwargs
)
```



<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end()
```



<h3 id="reset"><code>reset</code></h3>

``` python
reset()
```





