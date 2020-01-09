page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.cifar100.load_data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/datasets/cifar100/load_data">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/datasets/cifar100.py#L31-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads CIFAR100 dataset.

### Aliases:

* <a href="/api_docs/python/tf/keras/datasets/cifar100/load_data"><code>tf.compat.v1.keras.datasets.cifar100.load_data</code></a>
* <a href="/api_docs/python/tf/keras/datasets/cifar100/load_data"><code>tf.compat.v2.keras.datasets.cifar100.load_data</code></a>


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
