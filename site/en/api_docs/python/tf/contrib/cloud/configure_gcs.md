page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cloud.configure_gcs

``` python
tf.contrib.cloud.configure_gcs(
    session,
    credentials=None,
    block_cache=None,
    device=None
)
```



Defined in [`tensorflow/contrib/cloud/python/ops/gcs_config_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/cloud/python/ops/gcs_config_ops.py).

Configures the GCS file system for a given a session.

Warning: GCS `credentials` may be transmitted over the network unencrypted.
Please ensure that the network is trusted before using this function. For
users running code entirely within Google Cloud, your data is protected by
encryption in between data centers. For more information, please take a look
at https://cloud.google.com/security/encryption-in-transit/.

#### Args:

* <b>`session`</b>: A <a href="../../../tf/Session"><code>tf.Session</code></a> session that should be used to configure the GCS
    file system.
* <b>`credentials`</b>: [Optional.] A JSON string
* <b>`block_cache`</b>: [Optional.] A BlockCacheParams to configure the block cache .
* <b>`device`</b>: [Optional.] The device to place the configure ops.