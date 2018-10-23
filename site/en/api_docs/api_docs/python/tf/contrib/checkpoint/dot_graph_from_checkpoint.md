

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.dot_graph_from_checkpoint

``` python
tf.contrib.checkpoint.dot_graph_from_checkpoint(save_path)
```



Defined in [`tensorflow/contrib/checkpoint/python/visualize.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/checkpoint/python/visualize.py).

Visualizes an object-based checkpoint (from <a href="../../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>).

Useful for inspecting checkpoints and debugging loading issues.

Example usage from Python (requires pydot):

```python
import tensorflow as tf
import pydot

dot_string = tf.contrib.checkpoint.dot_graph_from_checkpoint('/path/to/ckpt')
parsed, = pydot.graph_from_dot_data(dot_string)
parsed.write_svg('/tmp/tensorflow/visualized_checkpoint.svg')
```

Example command line usage:

```sh
python -c "import tensorflow as tf;\
  print(tf.contrib.checkpoint.dot_graph_from_checkpoint('/path/to/ckpt'))"\
  | dot -Tsvg > /tmp/tensorflow/checkpoint_viz.svg
```

#### Args:

* <b>`save_path`</b>: The checkpoint prefix, as returned by <a href="../../../tf/train/Checkpoint#save"><code>tf.train.Checkpoint.save</code></a>
    or <a href="../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a>.

#### Returns:

A graph in DOT format as a string.