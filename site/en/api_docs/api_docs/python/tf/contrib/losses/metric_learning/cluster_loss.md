

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.metric_learning.cluster_loss

``` python
tf.contrib.losses.metric_learning.cluster_loss(
    labels,
    embeddings,
    margin_multiplier,
    enable_pam_finetuning=True,
    margin_type='nmi',
    print_losses=False
)
```



Defined in [`tensorflow/contrib/losses/python/metric_learning/metric_loss_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/losses/python/metric_learning/metric_loss_ops.py).

Computes the clustering loss.

The following structured margins are supported:
  nmi: normalized mutual information
  ami: adjusted mutual information
  ari: adjusted random index
  vmeasure: v-measure
  const: indicator checking whether the two clusterings are the same.

#### Args:

* <b>`labels`</b>: 2-D Tensor of labels of shape [batch size, 1]
* <b>`embeddings`</b>: 2-D Tensor of embeddings of shape
    [batch size, embedding dimension]. Embeddings should be l2 normalized.
* <b>`margin_multiplier`</b>: float32 scalar. multiplier on the structured margin term
    See section 3.2 of paper for discussion.
* <b>`enable_pam_finetuning`</b>: Boolean, Whether to run local pam refinement.
    See section 3.4 of paper for discussion.
* <b>`margin_type`</b>: Type of structured margin to use. See section 3.2 of
    paper for discussion. Can be 'nmi', 'ami', 'ari', 'vmeasure', 'const'.
* <b>`print_losses`</b>: Boolean. Option to print the loss.

Paper: https://arxiv.org/abs/1612.01213.


#### Returns:

* <b>`clustering_loss`</b>: A float32 scalar `Tensor`.

#### Raises:

* <b>`ImportError`</b>: If sklearn dependency is not installed.