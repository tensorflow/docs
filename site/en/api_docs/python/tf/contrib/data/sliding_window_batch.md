

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.sliding_window_batch

``` python
tf.contrib.data.sliding_window_batch(
    window_size,
    stride=1
)
```



Defined in [`tensorflow/contrib/data/python/ops/sliding.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/data/python/ops/sliding.py).

A sliding window with size of `window_size` and step of `stride`.

This transformation passes a sliding window over this dataset. The
window size is `window_size` and step size is `stride`. If the left
elements cannot fill up the sliding window, this transformation will
drop the final smaller element. For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { [1], [2], [3], [4], [5], [6] }

a.apply(tf.contrib.data.sliding_window_batch(window_size=3, stride=2)) ==
{
    [[1], [2], [3]],
    [[3], [4], [5]],
}
```

#### Args:

* <b>`window_size`</b>: A <a href="../../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    elements in the sliding window.
* <b>`stride`</b>: (Optional.) A <a href="../../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
    steps moving the sliding window forward for one iteration. The default
    is `1`. It must be in `[1, window_size)`.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.