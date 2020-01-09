page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cloud.configure_gcs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cloud/python/ops/gcs_config_ops.py#L147-L182">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Configures the GCS file system for a given a session.

``` python
tf.contrib.cloud.configure_gcs(
    session,
    credentials=None,
    block_cache=None,
    device=None
)
```



<!-- Placeholder for "Used in" -->

Warning: GCS `credentials` may be transmitted over the network unencrypted.
Please ensure that the network is trusted before using this function. For
users running code entirely within Google Cloud, your data is protected by
encryption in between data centers. For more information, please take a look
at https://cloud.google.com/security/encryption-in-transit/.

#### Args:


* <b>`session`</b>: A <a href="../../../tf/Session"><code>tf.compat.v1.Session</code></a> session that should be used to configure
  the GCS file system.
* <b>`credentials`</b>: [Optional.] A JSON string
* <b>`block_cache`</b>: [Optional.] A BlockCacheParams to configure the block cache .
* <b>`device`</b>: [Optional.] The device to place the configure ops.
