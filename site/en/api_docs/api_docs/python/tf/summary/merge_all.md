

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.summary.merge_all

``` python
merge_all(key=tf.GraphKeys.SUMMARIES)
```



Defined in [`tensorflow/python/summary/summary.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/summary/summary.py).

See the guide: [Summary Operations > Generation of Summaries](../../../../api_guides/python/summary#Generation_of_Summaries)

Merges all summaries collected in the default graph.

#### Args:

* <b>`key`</b>: `GraphKey` used to collect the summaries.  Defaults to
    `GraphKeys.SUMMARIES`.


#### Returns:

  If no summaries were collected, returns None.  Otherwise returns a scalar
  `Tensor` of type `string` containing the serialized `Summary` protocol
  buffer resulting from the merging.