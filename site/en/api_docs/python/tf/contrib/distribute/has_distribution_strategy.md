page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.has_distribution_strategy

``` python
tf.contrib.distribute.has_distribution_strategy()
```



Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/distribute.py).

Return if there is a current non-default `DistributionStrategy`.

#### Returns:

True if inside a `with distribution_strategy.scope():`.