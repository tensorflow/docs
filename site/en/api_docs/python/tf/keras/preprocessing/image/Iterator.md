page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.Iterator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/image/Iterator">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/preprocessing/image.py#L135-L136">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Iterator`

Base class for image data iterators.

Inherits From: [`Sequence`](../../../../tf/keras/utils/Sequence)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/preprocessing/image/Iterator"><code>tf.compat.v1.keras.preprocessing.image.Iterator</code></a>
* Class <a href="/api_docs/python/tf/keras/preprocessing/image/Iterator"><code>tf.compat.v2.keras.preprocessing.image.Iterator</code></a>


<!-- Placeholder for "Used in" -->

Every `Iterator` must implement the `_get_batches_of_transformed_samples`
method.

# Arguments
    n: Integer, total number of samples in the dataset to loop over.
    batch_size: Integer, size of a batch.
    shuffle: Boolean, whether to shuffle the data between epochs.
    seed: Random seeding for data shuffling.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    n,
    batch_size,
    shuffle,
    seed
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(idx)
```

Gets batch at position `index`.


#### Arguments:


* <b>`index`</b>: position of the batch in the Sequence.


#### Returns:

A batch


<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```

Create a generator that iterate over the Sequence.


<h3 id="__len__"><code>__len__</code></h3>

``` python
__len__()
```

Number of batch in the Sequence.


#### Returns:

The number of batches in the Sequence.


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

Method called at the end of every epoch.
    

<h3 id="reset"><code>reset</code></h3>

``` python
reset()
```






## Class Members

* `white_list_formats` <a id="white_list_formats"></a>
