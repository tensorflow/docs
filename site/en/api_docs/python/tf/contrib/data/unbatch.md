page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.unbatch

``` python
tf.contrib.data.unbatch()
```



Defined in [`tensorflow/contrib/data/python/ops/batching.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/data/python/ops/batching.py).

See the guide: [Dataset Input Pipeline > Transformations on existing datasets](../../../../../api_guides/python/input_dataset#Transformations_on_existing_datasets)

Splits elements of a dataset into multiple elements on the batch dimension.

For example, if elements of the dataset are shaped `[B, a0, a1, ...]`,
where `B` may vary for each input element, then for each element in the
dataset, the unbatched dataset will contain `B` consecutive elements
of shape `[a0, a1, ...]`.

```python
# NOTE: The following example uses `{ ... }` to represent the contents
# of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.apply(tf.contrib.data.unbatch()) == {
    'a', 'b', 'c', 'a', 'b', 'a', 'b', 'c', 'd'}
```

#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.