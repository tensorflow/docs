page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.cloud


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cloud/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Module for cloud ops.

<!-- Placeholder for "Used in" -->


## Classes

[`class BigQueryReader`](../../tf/contrib/cloud/BigQueryReader): A Reader that outputs keys and tf.Example values from a BigQuery table.

[`class BigtableClient`](../../tf/contrib/cloud/BigtableClient): BigtableClient is the entrypoint for interacting with Cloud Bigtable in TF.

[`class BigtableTable`](../../tf/contrib/cloud/BigtableTable): Entry point for reading and writing data in Cloud Bigtable.

[`class BlockCacheParams`](../../tf/contrib/cloud/BlockCacheParams): BlockCacheParams is a struct used for configuring the GCS Block Cache.

[`class ConfigureGcsHook`](../../tf/contrib/cloud/ConfigureGcsHook): ConfigureGcsHook configures GCS when used with Estimator/TPUEstimator.

## Functions

[`configure_colab_session(...)`](../../tf/contrib/cloud/configure_colab_session): ConfigureColabSession configures the GCS file system in Colab.

[`configure_gcs(...)`](../../tf/contrib/cloud/configure_gcs): Configures the GCS file system for a given a session.
