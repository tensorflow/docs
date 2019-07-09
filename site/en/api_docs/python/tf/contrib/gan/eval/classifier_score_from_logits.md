

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.classifier_score_from_logits

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.classifier_score_from_logits`
* `tf.contrib.gan.eval.classifier_score_from_logits`

``` python
tf.contrib.gan.eval.classifier_score_from_logits(logits)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Classifier score for evaluating a generative model from logits.

This method computes the classifier score for a set of logits. This can be
used independently of the classifier_score() method, especially in the case
of using large batches during evaluation where we would like precompute all
of the logits before computing the classifier score.

This technique is described in detail in https://arxiv.org/abs/1606.03498. In
summary, this function calculates:

exp( E[ KL(p(y|x) || p(y)) ] )

which captures how different the network's classification prediction is from
the prior distribution over classes.

#### Args:

* <b>`logits`</b>: Precomputed 2D tensor of logits that will be used to
    compute the classifier score.


#### Returns:

The classifier score. A floating-point scalar of the same type as the output
of `logits`.