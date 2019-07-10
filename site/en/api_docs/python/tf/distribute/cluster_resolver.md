page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.distribute.cluster_resolver



<!-- Placeholder for "Used in" -->


## Classes

[`class ClusterResolver`](../../tf/distribute/cluster_resolver/ClusterResolver): Abstract class for all implementations of ClusterResolvers.

[`class GCEClusterResolver`](../../tf/distribute/cluster_resolver/GCEClusterResolver): Cluster Resolver for Google Compute Engine.

[`class KubernetesClusterResolver`](../../tf/distribute/cluster_resolver/KubernetesClusterResolver): Cluster Resolver for Kubernetes.

[`class SimpleClusterResolver`](../../tf/distribute/cluster_resolver/SimpleClusterResolver): Simple implementation of ClusterResolver that accepts a ClusterSpec.

[`class SlurmClusterResolver`](../../tf/distribute/cluster_resolver/SlurmClusterResolver): Cluster Resolver for system with Slurm workload manager.

[`class TFConfigClusterResolver`](../../tf/distribute/cluster_resolver/TFConfigClusterResolver): Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

[`class TPUClusterResolver`](../../tf/distribute/cluster_resolver/TPUClusterResolver): Cluster Resolver for Google Cloud TPUs.

[`class UnionResolver`](../../tf/distribute/cluster_resolver/UnionResolver): Performs a union on underlying ClusterResolvers.

