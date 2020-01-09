page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.DistributeConfig


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_config.py#L24-L45">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `DistributeConfig`

A config tuple for distribution strategies.



<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`train_distribute`</b>: a `DistributionStrategy` object for training.
* <b>`eval_distribute`</b>: an optional `DistributionStrategy` object for
  evaluation.
* <b>`remote_cluster`</b>: a dict, `ClusterDef` or `ClusterSpec` object specifying
  the cluster configurations. If this is given, the `train_and_evaluate`
  method will be running as a standalone client which connects to the
  cluster for training.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_config.py#L40-L45">View source</a>

``` python
@staticmethod
__new__(
    cls,
    train_distribute=None,
    eval_distribute=None,
    remote_cluster=None
)
```

Create new instance of DistributeConfig(train_distribute, eval_distribute, remote_cluster)




## Properties

<h3 id="train_distribute"><code>train_distribute</code></h3>




<h3 id="eval_distribute"><code>eval_distribute</code></h3>




<h3 id="remote_cluster"><code>remote_cluster</code></h3>
