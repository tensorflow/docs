page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.factorization.GmmAlgorithm


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L92-L459">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GmmAlgorithm`

Tensorflow Gaussian mixture model clustering class.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L98-L152">View source</a>

``` python
__init__(
    data,
    num_classes,
    initial_means=None,
    params='wmc',
    covariance_type=FULL_COVARIANCE,
    random_seed=0
)
```

Constructor.


#### Args:


* <b>`data`</b>: a list of Tensors with data, each row is a new example.
* <b>`num_classes`</b>: number of clusters.
* <b>`initial_means`</b>: a Tensor with a matrix of means. If None, means are
  computed by sampling randomly.
* <b>`params`</b>: Controls which parameters are updated in the training
  process. Can contain any combination of "w" for weights, "m" for
  means, and "c" for covariances.
* <b>`covariance_type`</b>: one of "full", "diag".
* <b>`random_seed`</b>: Seed for PRNG used to initialize seeds.


#### Raises:

Exception if covariance type is unknown.




## Methods

<h3 id="alphas"><code>alphas</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L235-L236">View source</a>

``` python
alphas()
```




<h3 id="assignments"><code>assignments</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L246-L251">View source</a>

``` python
assignments()
```

Returns a list of Tensors with the matrix of assignments per shard.


<h3 id="clusters"><code>clusters</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L238-L240">View source</a>

``` python
clusters()
```

Returns the clusters with dimensions num_classes X 1 X num_dimensions.


<h3 id="covariances"><code>covariances</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L242-L244">View source</a>

``` python
covariances()
```

Returns the covariances matrices.


<h3 id="init_ops"><code>init_ops</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L223-L225">View source</a>

``` python
init_ops()
```

Returns the initialization operation.


<h3 id="is_initialized"><code>is_initialized</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L231-L233">View source</a>

``` python
is_initialized()
```

Returns a boolean operation for initialized variables.


<h3 id="log_likelihood_op"><code>log_likelihood_op</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L261-L263">View source</a>

``` python
log_likelihood_op()
```

Returns the log-likelihood operation.


<h3 id="scores"><code>scores</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L253-L259">View source</a>

``` python
scores()
```

Returns the per-sample likelihood fo the data.


#### Returns:

Log probabilities of each data point.


<h3 id="training_ops"><code>training_ops</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/factorization/python/ops/gmm_ops.py#L227-L229">View source</a>

``` python
training_ops()
```

Returns the training operation.




## Class Members

* `CLUSTERS_COVS_VARIABLE = 'clusters_covs'` <a id="CLUSTERS_COVS_VARIABLE"></a>
* `CLUSTERS_VARIABLE = 'clusters'` <a id="CLUSTERS_VARIABLE"></a>
* `CLUSTERS_WEIGHT = 'alphas'` <a id="CLUSTERS_WEIGHT"></a>
