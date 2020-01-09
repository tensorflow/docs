page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.make_initializable_iterator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/ops/dataset_ops.py#L2084-L2115">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.

### Aliases:

* <a href="/api_docs/python/tf/data/make_initializable_iterator"><code>tf.compat.v1.data.make_initializable_iterator</code></a>


``` python
tf.data.make_initializable_iterator(
    dataset,
    shared_name=None
)
```



<!-- Placeholder for "Used in" -->

Note: The returned iterator will be in an uninitialized state,
and you must run the `iterator.initializer` operation before using it:

```python
dataset = ...
iterator = tf.compat.v1.data.make_initializable_iterator(dataset)
# ...
sess.run(iterator.initializer)
```

#### Args:


* <b>`dataset`</b>: A <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.
* <b>`shared_name`</b>: (Optional.) If non-empty, the returned iterator will be shared
  under the given name across multiple sessions that share the same devices
  (e.g. when using a remote server).


#### Returns:

A <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> over the elements of `dataset`.



#### Raises:


* <b>`RuntimeError`</b>: If eager execution is enabled.
