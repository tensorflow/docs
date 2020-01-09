page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.sliding_window_batch


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/data/python/ops/sliding.py#L66-L129">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A sliding window over a dataset. (deprecated) (deprecated arguments)

``` python
tf.contrib.data.sliding_window_batch(
    window_size,
    stride=None,
    window_shift=None,
    window_stride=1
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(stride)`. They will be removed in a future version.
Instructions for updating:
stride is deprecated, use window_shift instead

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.window(size=window_size, shift=window_shift, stride=window_stride).flat_map(lambda x: x.batch(window_size))` instead.

This transformation passes a sliding window over this dataset. The window size
is `window_size`, the stride of the input elements is `window_stride`, and the
shift between consecutive windows is `window_shift`. If the remaining elements
cannot fill up the sliding window, this transformation will drop the final
smaller element. For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { [1], [2], [3], [4], [5], [6] }

a.apply(sliding_window_batch(window_size=3)) ==
{ [[1], [2], [3]], [[2], [3], [4]], [[3], [4], [5]], [[4], [5], [6]] }

a.apply(sliding_window_batch(window_size=3, window_shift=2)) ==
{ [[1], [2], [3]], [[3], [4], [5]] }

a.apply(sliding_window_batch(window_size=3, window_stride=2)) ==
{ [[1], [3], [5]], [[2], [4], [6]] }
```

#### Args:


* <b>`window_size`</b>: A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
  elements in the sliding window. It must be positive.
* <b>`stride`</b>: (Optional.) A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
  forward shift of the sliding window in each iteration. The default is `1`.
  It must be positive. Deprecated alias for `window_shift`.
* <b>`window_shift`</b>: (Optional.) A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
  forward shift of the sliding window in each iteration. The default is `1`.
  It must be positive.
* <b>`window_stride`</b>: (Optional.) A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
  stride of the input elements in the sliding window. The default is `1`.
  It must be positive.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.



#### Raises:


* <b>`ValueError`</b>: if invalid arguments are provided.
