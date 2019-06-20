page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.has_distribution_strategy

``` python
tf.contrib.distribute.has_distribution_strategy()
```



Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/distribute.py).

Return if there is a current non-default `DistributionStrategy`.

#### Returns:

True if inside a `with distribution_strategy.scope():`.