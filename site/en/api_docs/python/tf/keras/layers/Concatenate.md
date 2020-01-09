page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Concatenate


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/merge.py#L356-L443">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Concatenate`

Layer that concatenates a list of inputs.



### Aliases:

* Class `tf.compat.v1.keras.layers.Concatenate`
* Class `tf.compat.v2.keras.layers.Concatenate`


### Used in the tutorials:

* [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)



It takes as input a list of tensors,
all of the same shape except for the concatenation axis,
and returns a single tensor, the concatenation of all inputs.

#### Arguments:


* <b>`axis`</b>: Axis along which to concatenate.
* <b>`**kwargs`</b>: standard layer keyword arguments.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/merge.py#L368-L372">View source</a>

``` python
__init__(
    axis=-1,
    **kwargs
)
```
