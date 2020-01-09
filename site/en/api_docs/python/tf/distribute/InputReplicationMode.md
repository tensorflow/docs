page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.InputReplicationMode


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/distribute_lib.py#L330-L339">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `InputReplicationMode`

Replication mode for input function.



### Aliases:

* Class `tf.compat.v1.distribute.InputReplicationMode`
* Class `tf.compat.v2.distribute.InputReplicationMode`


<!-- Placeholder for "Used in" -->

* `PER_WORKER`: The input function will be called on each worker
  independently, creating as many input pipelines as number of workers.
  Replicas will dequeue from the local Dataset on their worker.
  <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> doesn't manage any state sharing between such
  separate input pipelines.

## Class Members

* `PER_WORKER` <a id="PER_WORKER"></a>
