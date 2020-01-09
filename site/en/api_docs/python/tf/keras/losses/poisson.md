page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.poisson


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/losses.py#L1035-L1061">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the Poisson loss between y_true and y_pred.

### Aliases:

* `tf.compat.v1.keras.losses.poisson`
* `tf.compat.v1.keras.metrics.poisson`
* `tf.compat.v2.keras.losses.poisson`
* `tf.compat.v2.keras.metrics.poisson`
* `tf.compat.v2.losses.poisson`
* `tf.compat.v2.metrics.poisson`
* `tf.keras.metrics.poisson`
* `tf.losses.poisson`
* `tf.metrics.poisson`


``` python
tf.keras.losses.poisson(
    y_true,
    y_pred
)
```



<!-- Placeholder for "Used in" -->

The Poisson loss is the mean of the elements of the `Tensor`
`y_pred - y_true * log(y_pred)`.

#### Usage:



```python
loss = tf.keras.losses.poisson([1.4, 9.3, 2.2], [4.3, 8.2, 12.2])
print('Loss: ', loss.numpy())  # Loss: -0.8045559
```

#### Args:


* <b>`y_true`</b>: Tensor of true targets.
* <b>`y_pred`</b>: Tensor of predicted targets.


#### Returns:

A `Tensor` with the mean Poisson loss.



#### Raises:


* <b>`InvalidArgumentError`</b>: If `y_true` and `y_pred` have incompatible shapes.
