

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.eval.classifier_score

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.classifier_score`
* `tf.contrib.gan.eval.classifier_score`

``` python
classifier_score(
    images,
    classifier_fn,
    num_batches=1
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Classifier score for evaluating a conditional generative model.

This is based on the Inception Score, but for an arbitrary classifier.

This technique is described in detail in https://arxiv.org/abs/1606.03498. In
summary, this function calculates

exp( E[ KL(p(y|x) || p(y)) ] )

which captures how different the network's classification prediction is from
the prior distribution over classes.

#### Args:

* <b>`images`</b>: Images to calculate the classifier score for.
* <b>`classifier_fn`</b>: A function that takes images and produces logits based on a
    classifier.
* <b>`num_batches`</b>: Number of batches to split `generated_images` in to in order to
    efficiently run them through the classifier network.


#### Returns:

The classifier score. A floating-point scalar.