page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.CustomObjectScope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L41-L73">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CustomObjectScope`

Provides a scope that changes to `_GLOBAL_CUSTOM_OBJECTS` cannot escape.



### Aliases:

* Class `tf.compat.v1.keras.utils.CustomObjectScope`
* Class `tf.compat.v2.keras.utils.CustomObjectScope`


<!-- Placeholder for "Used in" -->

Code within a `with` statement will be able to access custom objects
by name. Changes to global custom objects persist
within the enclosing `with` statement. At end of the `with` statement,
global custom objects are reverted to state
at beginning of the `with` statement.

#### Example:



Consider a custom object `MyObject` (e.g. a class):

```python
    with CustomObjectScope({'MyObject':MyObject}):
        layer = Dense(..., kernel_regularizer='MyObject')
        # save, load, etc. will recognize custom object by name
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L61-L63">View source</a>

``` python
__init__(*args)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L65-L69">View source</a>

``` python
__enter__()
```




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L71-L73">View source</a>

``` python
__exit__(
    *args,
    **kwargs
)
```
