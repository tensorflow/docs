

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.eval.run_image_classifier

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.run_image_classifier`
* `tf.contrib.gan.eval.run_image_classifier`

``` python
run_image_classifier(
    tensor,
    graph_def,
    input_tensor,
    output_tensor,
    scope='RunClassifier'
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Runs a network from a frozen graph.

#### Args:

* <b>`tensor`</b>: An Input tensor.
* <b>`graph_def`</b>: A GraphDef proto.
* <b>`input_tensor`</b>: Name of input tensor in graph def.
* <b>`output_tensor`</b>: Name of output tensor in graph def.
* <b>`scope`</b>: Name scope for classifier.


#### Returns:

Classifier output. Shape depends on the classifier used, but is often
[batch, classes].


#### Raises:

* <b>`ValueError`</b>: If `image_size` is not `None`, and `tensor` are not the correct
    size.