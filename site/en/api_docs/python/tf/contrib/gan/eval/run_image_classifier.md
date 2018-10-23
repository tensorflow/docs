

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.run_image_classifier

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.run_image_classifier`
* `tf.contrib.gan.eval.run_image_classifier`

``` python
tf.contrib.gan.eval.run_image_classifier(
    tensor,
    graph_def,
    input_tensor,
    output_tensor,
    scope='RunClassifier'
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Runs a network from a frozen graph.

#### Args:

* <b>`tensor`</b>: An Input tensor.
* <b>`graph_def`</b>: A GraphDef proto.
* <b>`input_tensor`</b>: Name of input tensor in graph def.
* <b>`output_tensor`</b>: A tensor name or list of tensor names in graph def.
* <b>`scope`</b>: Name scope for classifier.


#### Returns:

Classifier output if `output_tensor` is a string, or a list of outputs if
`output_tensor` is a list.


#### Raises:

* <b>`ValueError`</b>: If `input_tensor` or `output_tensor` aren't in the graph_def.