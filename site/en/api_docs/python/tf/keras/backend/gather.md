page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.gather


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L1943-L1954">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retrieves the elements of indices `indices` in the tensor `reference`.

### Aliases:

* `tf.compat.v1.keras.backend.gather`
* `tf.compat.v2.keras.backend.gather`


``` python
tf.keras.backend.gather(
    reference,
    indices
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`reference`</b>: A tensor.
* <b>`indices`</b>: An integer tensor of indices.


#### Returns:

A tensor of same type as `reference`.
