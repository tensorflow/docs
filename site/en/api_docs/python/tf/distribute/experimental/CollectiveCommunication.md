page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.experimental.CollectiveCommunication


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/distribute/experimental/CollectiveCommunication">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/cross_device_ops.py#L975-L986">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CollectiveCommunication`

Communication choices for CollectiveOps.



### Aliases:

* Class <a href="/api_docs/python/tf/distribute/experimental/CollectiveCommunication"><code>tf.compat.v1.distribute.experimental.CollectiveCommunication</code></a>
* Class <a href="/api_docs/python/tf/distribute/experimental/CollectiveCommunication"><code>tf.compat.v2.distribute.experimental.CollectiveCommunication</code></a>


<!-- Placeholder for "Used in" -->

* `AUTO`: Default to runtime's automatic choices.
* `RING`: TensorFlow's ring algorithms for all-reduce and
  all-gather.
* `NCCL`: Use ncclAllReduce for all-reduce, and ring algorithms for
  all-gather.

## Class Members

* `AUTO` <a id="AUTO"></a>
* `NCCL` <a id="NCCL"></a>
* `RING` <a id="RING"></a>
