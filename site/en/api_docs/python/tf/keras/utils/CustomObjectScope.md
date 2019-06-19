page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.CustomObjectScope

## Class `CustomObjectScope`





Defined in [`tensorflow/python/keras/utils/generic_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/utils/generic_utils.py).

Provides a scope that changes to `_GLOBAL_CUSTOM_OBJECTS` cannot escape.

Code within a `with` statement will be able to access custom objects
by name. Changes to global custom objects persist
within the enclosing `with` statement. At end of the `with` statement,
global custom objects are reverted to state
at beginning of the `with` statement.

Example:

Consider a custom object `MyObject` (e.g. a class):

```python
    with CustomObjectScope({'MyObject':MyObject}):
        layer = Dense(..., kernel_regularizer='MyObject')
        # save, load, etc. will recognize custom object by name
```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(*args)
```



<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    *args,
    **kwargs
)
```





