

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.factorization.KMeans

## Class `KMeans`





Defined in [`tensorflow/contrib/factorization/python/ops/clustering_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/factorization/python/ops/clustering_ops.py).

Creates the graph for k-means clustering.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    inputs,
    num_clusters,
    initial_clusters=RANDOM_INIT,
    distance_metric=SQUARED_EUCLIDEAN_DISTANCE,
    use_mini_batch=False,
    mini_batch_steps_per_iteration=1,
    random_seed=0,
    kmeans_plus_plus_num_retries=2,
    kmc2_chain_length=200
)
```

Creates an object for generating KMeans clustering graph.

This class implements the following variants of K-means algorithm:

If use_mini_batch is False, it runs standard full batch K-means. Each step
runs a single iteration of K-Means. This step can be run sharded across
multiple workers by passing a list of sharded inputs to this class. Note
however that a single step needs to process the full input at once.

If use_mini_batch is True, it runs a generalization of the mini-batch
K-means algorithm. It runs multiple iterations, where each iteration is
composed of mini_batch_steps_per_iteration steps. Two copies of cluster
centers are maintained: one that is updated at the end of each iteration,
and one that is updated every step. The first copy is used to compute
cluster allocations for each step, and for inference, while the second copy
is the one updated each step using the mini-batch update rule. After each
iteration is complete, this second copy is copied back the first copy.

Note that for use_mini_batch=True, when mini_batch_steps_per_iteration=1,
the algorithm reduces to the standard mini-batch algorithm. Also by setting
mini_batch_steps_per_iteration = num_inputs / batch_size, the algorithm
becomes an asynchronous version of the full-batch algorithm. Note however
that there is no guarantee by this implementation that each input is seen
exactly once per iteration. Also, different updates are applied
asynchronously without locking. So this asynchronous version may not behave
exactly like a full-batch version.

#### Args:

* <b>`inputs`</b>: An input tensor or list of input tensors. It is assumed that the
    data points have been previously randomly permuted.
* <b>`num_clusters`</b>: An integer tensor specifying the number of clusters. This
    argument is ignored if initial_clusters is a tensor or numpy array.
* <b>`initial_clusters`</b>: Specifies the clusters used during initialization. One
    of the following:
    - a tensor or numpy array with the initial cluster centers.
    - a function f(inputs, k) that returns up to k centers from `inputs`.
    - "random": Choose centers randomly from `inputs`.
    - "kmeans_plus_plus": Use kmeans++ to choose centers from `inputs`.
    - "kmc2": Use the fast k-MC2 algorithm to choose centers from `inputs`.
    In the last three cases, one batch of `inputs` may not yield
    `num_clusters` centers, in which case initialization will require
    multiple batches until enough centers are chosen. In the case of
    "random" or "kmeans_plus_plus", if the input size is <= `num_clusters`
    then the entire batch is chosen to be cluster centers.
* <b>`distance_metric`</b>: Distance metric used for clustering. Supported options:
    "squared_euclidean", "cosine".
* <b>`use_mini_batch`</b>: If true, use the mini-batch k-means algorithm. Else assume
    full batch.
* <b>`mini_batch_steps_per_iteration`</b>: Number of steps after which the updated
    cluster centers are synced back to a master copy.
* <b>`random_seed`</b>: Seed for PRNG used to initialize seeds.
* <b>`kmeans_plus_plus_num_retries`</b>: For each point that is sampled during
    kmeans++ initialization, this parameter specifies the number of
    additional points to draw from the current distribution before selecting
    the best. If a negative value is specified, a heuristic is used to
    sample O(log(num_to_sample)) additional points.
* <b>`kmc2_chain_length`</b>: Determines how many candidate points are used by the
    k-MC2 algorithm to produce one new cluster centers. If a (mini-)batch
    contains less points, one new cluster center is generated from the
    (mini-)batch.


#### Raises:

* <b>`ValueError`</b>: An invalid argument was passed to initial_clusters or
    distance_metric.

<h3 id="training_graph"><code>training_graph</code></h3>

``` python
training_graph()
```

Generate a training graph for kmeans algorithm.

This returns, among other things, an op that chooses initial centers
(init_op), a boolean variable that is set to True when the initial centers
are chosen (cluster_centers_initialized), and an op to perform either an
entire Lloyd iteration or a mini-batch of a Lloyd iteration (training_op).
The caller should use these components as follows. A single worker should
execute init_op multiple times until cluster_centers_initialized becomes
True. Then multiple workers may execute training_op any number of times.

#### Returns:

A tuple consisting of:
* <b>`all_scores`</b>: A matrix (or list of matrices) of dimensions (num_input,
    num_clusters) where the value is the distance of an input vector and a
    cluster center.
* <b>`cluster_idx`</b>: A vector (or list of vectors). Each element in the vector
    corresponds to an input row in 'inp' and specifies the cluster id
    corresponding to the input.
* <b>`scores`</b>: Similar to cluster_idx but specifies the distance to the
    assigned cluster instead.
* <b>`cluster_centers_initialized`</b>: scalar indicating whether clusters have been
    initialized.
* <b>`init_op`</b>: an op to initialize the clusters.
* <b>`training_op`</b>: an op that runs an iteration of training.



