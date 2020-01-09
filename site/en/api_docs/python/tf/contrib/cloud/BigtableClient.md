page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cloud.BigtableClient


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/bigtable/python/ops/bigtable_api.py#L47-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `BigtableClient`

BigtableClient is the entrypoint for interacting with Cloud Bigtable in TF.



<!-- Placeholder for "Used in" -->

BigtableClient encapsulates a connection to Cloud Bigtable, and exposes the
`table` method to open a Bigtable table.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/bigtable/python/ops/bigtable_api.py#L54-L94">View source</a>

``` python
__init__(
    project_id,
    instance_id,
    connection_pool_size=None,
    max_receive_message_size=None
)
```

Creates a BigtableClient that can be used to open connections to tables.


#### Args:


* <b>`project_id`</b>: A string representing the GCP project id to connect to.
* <b>`instance_id`</b>: A string representing the Bigtable instance to connect to.
* <b>`connection_pool_size`</b>: (Optional.) A number representing the number of
  concurrent connections to the Cloud Bigtable service to make.
* <b>`max_receive_message_size`</b>: (Optional.) The maximum bytes received in a
  single gRPC response.


#### Raises:


* <b>`ValueError`</b>: if the arguments are invalid (e.g. wrong type, or out of
  expected ranges (e.g. negative).)



## Methods

<h3 id="table"><code>table</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/bigtable/python/ops/bigtable_api.py#L96-L110">View source</a>

``` python
table(
    name,
    snapshot=None
)
```

Opens a table and returns a `tf.contrib.bigtable.BigtableTable` object.


#### Args:


* <b>`name`</b>: A <a href="../../../tf#string"><code>tf.string</code></a> <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> name of the table to open.
* <b>`snapshot`</b>: Either a <a href="../../../tf#string"><code>tf.string</code></a> <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> snapshot id, or `True` to
  request the creation of a snapshot. (Note: currently unimplemented.)


#### Returns:

A `tf.contrib.bigtable.BigtableTable` Python object representing the
operations available on the table.
