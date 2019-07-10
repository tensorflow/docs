page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.unbatch

Splits elements of a dataset into multiple elements on the batch dimension.

### Aliases:

* `tf.compat.v1.data.experimental.unbatch`
* `tf.compat.v2.data.experimental.unbatch`
* `tf.data.experimental.unbatch`

``` python
tf.data.experimental.unbatch()
```



Defined in [`python/data/experimental/ops/batching.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/batching.py).

<!-- Placeholder for "Used in" -->

For example, if elements of the dataset are shaped `[B, a0, a1, ...]`,
where `B` may vary for each input element, then for each element in the
dataset, the unbatched dataset will contain `B` consecutive elements
of shape `[a0, a1, ...]`.

```python
# NOTE: The following example uses `{ ... }` to represent the contents
# of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.apply(tf.data.experimental.unbatch()) == {
    'a', 'b', 'c', 'a', 'b', 'a', 'b', 'c', 'd'}
```

#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
