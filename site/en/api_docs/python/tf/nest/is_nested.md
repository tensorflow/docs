page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nest.is_nested


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/nest.py#L217-L228">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns true if its input is a collections.abc.Sequence (except strings).

### Aliases:

* `tf.compat.v1.nest.is_nested`
* `tf.compat.v2.nest.is_nested`


``` python
tf.nest.is_nested(seq)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`seq`</b>: an input sequence.


#### Returns:

True if the sequence is a not a string and is a collections.abc.Sequence
or a dict.
