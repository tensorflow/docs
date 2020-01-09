page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.maximum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/merge.py#L647-L676">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Functional interface to the `Maximum` layer that computes

### Aliases:

* `tf.compat.v1.keras.layers.maximum`
* `tf.compat.v2.keras.layers.maximum`


``` python
tf.keras.layers.maximum(
    inputs,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

   the maximum (element-wise) list of `inputs`.

#### For example:



```python
input1 = tf.keras.layers.Input(shape=(16,))
x1 = tf.keras.layers.Dense(8, activation='relu')(input1) #shape=(None, 8)
input2 = tf.keras.layers.Input(shape=(32,))
x2 = tf.keras.layers.Dense(8, activation='relu')(input2) #shape=(None, 8)
max_inp=tf.keras.layers.maximum([x1,x2]) #shape=(None, 8)
out = tf.keras.layers.Dense(4)(max_inp)
model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
```

#### Arguments:


* <b>`inputs`</b>: A list of input tensors (at least 2) of same shape.
* <b>`**kwargs`</b>: Standard layer keyword arguments.


#### Returns:

A tensor (of same shape as input tensor) with the element-wise
maximum of the inputs.



#### Raises:


* <b>`ValueError`</b>: If input tensors are of different shape.
