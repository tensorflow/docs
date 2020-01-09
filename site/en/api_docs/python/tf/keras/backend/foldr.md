page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.foldr


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5824-L5838">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reduce elems using fn to combine them from right to left.

### Aliases:

* `tf.compat.v1.keras.backend.foldr`
* `tf.compat.v2.keras.backend.foldr`


``` python
tf.keras.backend.foldr(
    fn,
    elems,
    initializer=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`fn`</b>: Callable that will be called upon each element in elems and an
    accumulator, for instance `lambda acc, x: acc + x`
* <b>`elems`</b>: tensor
* <b>`initializer`</b>: The first value used (`elems[-1]` in case of None)
* <b>`name`</b>: A string name for the foldr node in the graph


#### Returns:

Same type and shape as initializer
