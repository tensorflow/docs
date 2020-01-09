page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.metric_learning.contrastive_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/losses/python/metric_learning/metric_loss_ops.py#L86-L119">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the contrastive loss.

``` python
tf.contrib.losses.metric_learning.contrastive_loss(
    labels,
    embeddings_anchor,
    embeddings_positive,
    margin=1.0
)
```



<!-- Placeholder for "Used in" -->

This loss encourages the embedding to be close to each other for
  the samples of the same label and the embedding to be far apart at least
  by the margin constant for the samples of different labels.
See: http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf

#### Args:


* <b>`labels`</b>: 1-D tf.int32 `Tensor` with shape [batch_size] of
  binary labels indicating positive vs negative pair.
* <b>`embeddings_anchor`</b>: 2-D float `Tensor` of embedding vectors for the anchor
  images. Embeddings should be l2 normalized.
* <b>`embeddings_positive`</b>: 2-D float `Tensor` of embedding vectors for the
  positive images. Embeddings should be l2 normalized.
* <b>`margin`</b>: margin term in the loss definition.


#### Returns:


* <b>`contrastive_loss`</b>: tf.float32 scalar.
