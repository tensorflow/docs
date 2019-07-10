page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.object_metadata

Retrieves information about the objects in a checkpoint.

``` python
tf.contrib.checkpoint.object_metadata(save_path)
```



Defined in [`python/training/tracking/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/tracking/util.py).

<!-- Placeholder for "Used in" -->


#### Example usage:



```python
object_graph = tf.contrib.checkpoint.object_metadata(
    tf.train.latest_checkpoint(checkpoint_directory))
ckpt_variable_names = set()
for node in object_graph.nodes:
  for attribute in node.attributes:
    ckpt_variable_names.add(attribute.full_name)
```

#### Args:


* <b>`save_path`</b>: The path to the checkpoint, as returned by `save` or
  <a href="../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a>.


#### Returns:

A parsed `tf.contrib.checkpoint.TrackableObjectGraph` protocol buffer.


#### Raises:


* <b>`ValueError`</b>: If an object graph was not found in the checkpoint.