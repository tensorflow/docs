page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.distribute.cluster_resolver


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/distribute/cluster_resolver">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Library imports for ClusterResolvers.

<!-- Placeholder for "Used in" -->

This library contains all implementations of ClusterResolvers.
ClusterResolvers are a way of specifying cluster information for distributed
execution. Built on top of existing `ClusterSpec` framework, ClusterResolvers
are a way for TensorFlow to communicate with various cluster management
systems (e.g. GCE, AWS, etc...).

## Classes

[`class ClusterResolver`](../../tf/distribute/cluster_resolver/ClusterResolver): Abstract class for all implementations of ClusterResolvers.

[`class GCEClusterResolver`](../../tf/distribute/cluster_resolver/GCEClusterResolver): ClusterResolver for Google Compute Engine.

[`class KubernetesClusterResolver`](../../tf/distribute/cluster_resolver/KubernetesClusterResolver): ClusterResolver for Kubernetes.

[`class SimpleClusterResolver`](../../tf/distribute/cluster_resolver/SimpleClusterResolver): Simple implementation of ClusterResolver that accepts a ClusterSpec.

[`class SlurmClusterResolver`](../../tf/distribute/cluster_resolver/SlurmClusterResolver): ClusterResolver for system with Slurm workload manager.

[`class TFConfigClusterResolver`](../../tf/distribute/cluster_resolver/TFConfigClusterResolver): Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

[`class TPUClusterResolver`](../../tf/distribute/cluster_resolver/TPUClusterResolver): Cluster Resolver for Google Cloud TPUs.

[`class UnionResolver`](../../tf/distribute/cluster_resolver/UnionResolver): Performs a union on underlying ClusterResolvers.
