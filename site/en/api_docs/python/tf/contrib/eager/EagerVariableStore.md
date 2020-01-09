page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.EagerVariableStore


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1387-L1461">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `EagerVariableStore`

Wrapper allowing functional layers to be used with eager execution.



<!-- Placeholder for "Used in" -->

When eager execution is enabled Variables get deleted when they go out of
scope, and are not stored in global collections by default. A lot of code
(mostly the functional layers in tf.layers) assumes that variables are kept in
a global list.

EagerVariableStore can be used in conjunction with this code to make it
eager-friendly. For example, to create a dense layer, use:

```
  container = tfe.EagerVariableStore()
  for input in dataset_iterator:
    with container.as_default():
      x = tf.compat.v1.layers.dense(input, name="l1")
  print(container.variables)  # Should print the variables used in the layer.
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1407-L1416">View source</a>

``` python
__init__(store=None)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="as_default"><code>as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1418-L1419">View source</a>

``` python
as_default()
```




<h3 id="copy"><code>copy</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1436-L1461">View source</a>

``` python
copy()
```

Copy this variable store and all of its contents.

Variables contained in this store will be copied over to the new variable
store, meaning that they can be modified without affecting the variables in
this store.

#### Returns:

A new EagerVariableStore instance containing copied variables.


<h3 id="non_trainable_variables"><code>non_trainable_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1430-L1433">View source</a>

``` python
non_trainable_variables()
```




<h3 id="trainable_variables"><code>trainable_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1424-L1427">View source</a>

``` python
trainable_variables()
```




<h3 id="variables"><code>variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variable_scope.py#L1421-L1422">View source</a>

``` python
variables()
```
