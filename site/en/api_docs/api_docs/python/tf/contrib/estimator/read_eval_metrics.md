

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.read_eval_metrics

``` python
tf.contrib.estimator.read_eval_metrics(eval_dir)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/early_stopping.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/estimator/python/estimator/early_stopping.py).

Helper to read eval metrics from eval summary files.

#### Args:

* <b>`eval_dir`</b>: Directory containing summary files with eval metrics.


#### Returns:

A `dict` with global steps mapping to `dict` of metric names and values.