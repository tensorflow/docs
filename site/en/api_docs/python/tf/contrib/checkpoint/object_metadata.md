page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.object_metadata


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/util.py#L442-L476">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retrieves information about the objects in a checkpoint.

``` python
tf.contrib.checkpoint.object_metadata(save_path)
```



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
