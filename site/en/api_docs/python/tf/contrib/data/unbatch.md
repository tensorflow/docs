

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.unbatch

``` python
unbatch()
```



Defined in [`tensorflow/contrib/data/python/ops/batching.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/data/python/ops/batching.py).

See the guide: [Dataset Input Pipeline > Transformations on existing datasets](../../../../../api_guides/python/input_dataset#Transformations_on_existing_datasets)

A Transformation which splits the elements of a dataset.

For example, if elements of the dataset are shaped `[B, a0, a1, ...]`,
where `B` may vary from element to element, then for each element in
the dataset, the unbatched dataset will contain `B` consecutive elements
of shape `[a0, a1, ...]`.

#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.