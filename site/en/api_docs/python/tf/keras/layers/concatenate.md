page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.concatenate


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/merge.py#L693-L705">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Functional interface to the `Concatenate` layer.

### Aliases:

* `tf.compat.v1.keras.layers.concatenate`
* `tf.compat.v2.keras.layers.concatenate`


``` python
tf.keras.layers.concatenate(
    inputs,
    axis=-1,
    **kwargs
)
```



### Used in the guide:

* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)

### Used in the tutorials:

* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)




#### Arguments:


* <b>`inputs`</b>: A list of input tensors (at least 2).
* <b>`axis`</b>: Concatenation axis.
* <b>`**kwargs`</b>: Standard layer keyword arguments.


#### Returns:

A tensor, the concatenation of the inputs alongside axis `axis`.
