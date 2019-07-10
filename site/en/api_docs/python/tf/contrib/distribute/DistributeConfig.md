page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.DistributeConfig

## Class `DistributeConfig`

A config tuple for distribution strategies.





Defined in [`python/distribute/distribute_config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/distribute_config.py).

<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`train_distribute`</b>: a `DistributionStrategy` object for training.
* <b>`eval_distribute`</b>: an optional `DistributionStrategy` object for
  evaluation.
* <b>`remote_cluster`</b>: a dict, `ClusterDef` or `ClusterSpec` object specifying
  the cluster configurations. If this is given, the `train_and_evaluate`
  method will be running as a standalone client which connects to the
  cluster for training.

## Properties

<h3 id="train_distribute"><code>train_distribute</code></h3>




<h3 id="eval_distribute"><code>eval_distribute</code></h3>




<h3 id="remote_cluster"><code>remote_cluster</code></h3>






