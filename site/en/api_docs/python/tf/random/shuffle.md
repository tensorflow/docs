page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.shuffle


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/random_ops.py#L258-L287">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Randomly shuffles a tensor along its first dimension.

### Aliases:

* `tf.compat.v1.random.shuffle`
* `tf.compat.v1.random_shuffle`
* `tf.compat.v2.random.shuffle`


``` python
tf.random.shuffle(
    value,
    seed=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
to one and only one `output[i]`. For example, a mapping that might occur for a
3x2 tensor is:

```python
[[1, 2],       [[5, 6],
 [3, 4],  ==>   [1, 2],
 [5, 6]]        [3, 4]]
```

#### Args:


* <b>`value`</b>: A Tensor to be shuffled.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
  See
  <a href="../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of same shape and type as `value`, shuffled along its first
dimension.
