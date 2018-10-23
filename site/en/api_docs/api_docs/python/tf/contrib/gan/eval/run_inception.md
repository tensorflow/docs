

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.eval.run_inception

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.run_inception`
* `tf.contrib.gan.eval.run_inception`

``` python
run_inception(
    images,
    graph_def=None,
    default_graph_def_fn=_default_graph_def_fn,
    image_size=INCEPTION_V3_DEFAULT_IMG_SIZE,
    input_tensor=INCEPTION_V3_INPUT,
    output_tensor=INCEPTION_V3_OUTPUT
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Run images through a pretrained Inception classifier.

#### Args:

* <b>`images`</b>: Input tensors. Must be [batch, height, width, channels]. Input shape
    and values must be in [-1, 1], which can be achieved using
    `preprocess_image`.
* <b>`graph_def`</b>: A GraphDef proto of a pretrained Inception graph. If `None`,
    call `default_graph_def_fn` to get GraphDef.
* <b>`default_graph_def_fn`</b>: A function that returns a GraphDef. Used if
    `graph_def` is `None. By default, returns a pretrained InceptionV3 graph.
* <b>`image_size`</b>: Required image width and height. See unit tests for the default
    values.
* <b>`input_tensor`</b>: Name of input Tensor.
* <b>`output_tensor`</b>: Name of output Tensor. This function will compute activations
    at the specified layer. Examples include INCEPTION_V3_OUTPUT and
    INCEPTION_V3_FINAL_POOL which would result in this function computing
    the final logits or the penultimate pooling layer.


#### Returns:

Logits.


#### Raises:

* <b>`ValueError`</b>: If images are not the correct size.
* <b>`ValueError`</b>: If neither `graph_def` nor `default_graph_def_fn` are provided.