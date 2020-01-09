page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.boston_housing.load_data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/datasets/boston_housing/load_data">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/datasets/boston_housing.py#L27-L62">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads the Boston Housing dataset.

### Aliases:

* <a href="/api_docs/python/tf/keras/datasets/boston_housing/load_data"><code>tf.compat.v1.keras.datasets.boston_housing.load_data</code></a>
* <a href="/api_docs/python/tf/keras/datasets/boston_housing/load_data"><code>tf.compat.v2.keras.datasets.boston_housing.load_data</code></a>


``` python
tf.keras.datasets.boston_housing.load_data(
    path='boston_housing.npz',
    test_split=0.2,
    seed=113
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`path`</b>: path where to cache the dataset locally
    (relative to ~/.keras/datasets).
* <b>`test_split`</b>: fraction of the data to reserve as test set.
* <b>`seed`</b>: Random seed for shuffling the data
    before computing the test split.


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
