page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.cifar100.load_data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/datasets/cifar100.py#L31-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads CIFAR100 dataset.

### Aliases:

* `tf.compat.v1.keras.datasets.cifar100.load_data`
* `tf.compat.v2.keras.datasets.cifar100.load_data`


``` python
tf.keras.datasets.cifar100.load_data(label_mode='fine')
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`label_mode`</b>: one of "fine", "coarse".


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.



#### Raises:


* <b>`ValueError`</b>: in case of invalid `label_mode`.
