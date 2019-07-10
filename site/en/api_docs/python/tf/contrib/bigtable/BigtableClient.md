page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.bigtable.BigtableClient

## Class `BigtableClient`

BigtableClient is the entrypoint for interacting with Cloud Bigtable in TF.



### Aliases:

* Class `tf.contrib.bigtable.BigtableClient`
* Class `tf.contrib.cloud.BigtableClient`



Defined in [`contrib/bigtable/python/ops/bigtable_api.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/bigtable/python/ops/bigtable_api.py).

<!-- Placeholder for "Used in" -->

BigtableClient encapsulates a connection to Cloud Bigtable, and exposes the
`table` method to open a Bigtable table.

<h2 id="__init__"><code>__init__</code></h2>

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

``` python
table(
    name,
    snapshot=None
)
```

Opens a table and returns a <a href="../../../tf/contrib/bigtable/BigtableTable"><code>tf.contrib.bigtable.BigtableTable</code></a> object.


#### Args:


* <b>`name`</b>: A <a href="../../../tf#string"><code>tf.string</code></a> <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> name of the table to open.
* <b>`snapshot`</b>: Either a <a href="../../../tf#string"><code>tf.string</code></a> <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> snapshot id, or `True` to
  request the creation of a snapshot. (Note: currently unimplemented.)


#### Returns:

A <a href="../../../tf/contrib/bigtable/BigtableTable"><code>tf.contrib.bigtable.BigtableTable</code></a> Python object representing the
operations available on the table.




