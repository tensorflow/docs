page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.cluster_resolver


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cluster_resolver/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Standard imports for Cluster Resolvers.

<!-- Placeholder for "Used in" -->


## Classes

[`class ClusterResolver`](../../tf/distribute/cluster_resolver/ClusterResolver): Abstract class for all implementations of ClusterResolvers.

[`class GCEClusterResolver`](../../tf/distribute/cluster_resolver/GCEClusterResolver): ClusterResolver for Google Compute Engine.

[`class KubernetesClusterResolver`](../../tf/distribute/cluster_resolver/KubernetesClusterResolver): ClusterResolver for Kubernetes.

[`class SimpleClusterResolver`](../../tf/distribute/cluster_resolver/SimpleClusterResolver): Simple implementation of ClusterResolver that accepts a ClusterSpec.

[`class SlurmClusterResolver`](../../tf/distribute/cluster_resolver/SlurmClusterResolver): ClusterResolver for system with Slurm workload manager.

[`class TFConfigClusterResolver`](../../tf/distribute/cluster_resolver/TFConfigClusterResolver): Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

[`class TPUClusterResolver`](../../tf/distribute/cluster_resolver/TPUClusterResolver): Cluster Resolver for Google Cloud TPUs.

[`class UnionClusterResolver`](../../tf/distribute/cluster_resolver/UnionResolver): Performs a union on underlying ClusterResolvers.
