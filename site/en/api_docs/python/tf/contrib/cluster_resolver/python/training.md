page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.cluster_resolver.python.training



Defined in [`tensorflow/contrib/cluster_resolver/python/training/__init__.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/cluster_resolver/python/training/__init__.py).

Library Imports for Cluster Resolvers.

## Modules

[`tpu_cluster_resolver`](../../../../tf/contrib/cluster_resolver/python/training/tpu_cluster_resolver) module: Stub file for TPUClusterResolver to maintain backwards compatibility.

## Classes

[`class ClusterResolver`](../../../../tf/contrib/cluster_resolver/ClusterResolver): Abstract class for all implementations of ClusterResolvers.

[`class GceClusterResolver`](../../../../tf/contrib/cluster_resolver/GceClusterResolver): Cluster Resolver for Google Compute Engine.

[`class KubernetesClusterResolver`](../../../../tf/contrib/cluster_resolver/KubernetesClusterResolver): Cluster Resolver for Kubernetes.

[`class SimpleClusterResolver`](../../../../tf/contrib/cluster_resolver/SimpleClusterResolver): Simple implementation of ClusterResolver that accepts a ClusterSpec.

[`class SlurmClusterResolver`](../../../../tf/contrib/cluster_resolver/SlurmClusterResolver): Cluster Resolver for system with Slurm workload manager.

[`class TFConfigClusterResolver`](../../../../tf/contrib/cluster_resolver/TFConfigClusterResolver): Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

[`class TPUClusterResolver`](../../../../tf/contrib/cluster_resolver/TPUClusterResolver): Cluster Resolver for Google Cloud TPUs.

[`class UnionClusterResolver`](../../../../tf/contrib/cluster_resolver/UnionClusterResolver): Performs a union on underlying ClusterResolvers.

