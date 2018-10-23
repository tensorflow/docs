

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.callbacks.TensorBoard

### `class tf.contrib.keras.callbacks.TensorBoard`



Defined in [`tensorflow/contrib/keras/python/keras/callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/callbacks.py).

Tensorboard basic visualizations.

This callback writes a log for TensorBoard, which allows
you to visualize dynamic graphs of your training and test
metrics, as well as activation histograms for the different
layers in your model.

#### Arguments:

    log_dir: the path of the directory where to save the log
        files to be parsed by Tensorboard.
    histogram_freq: frequency (in epochs) at which to compute activation
        histograms for the layers of the model. If set to 0,
        histograms won't be computed.
    write_graph: whether to visualize the graph in Tensorboard.
        The log file can become quite large when
        write_graph is set to True.
    write_images: whether to write model weights to visualize as
        image in Tensorboard.
    embeddings_freq: frequency (in epochs) at which selected embedding
        layers will be saved.
    embeddings_layer_names: a list of names of layers to keep eye on. If
        None or empty list all the embedding layer will be watched.
    embeddings_metadata: a dictionary which maps layer name to a file name
        in which metadata for this embedding layer is saved. See the
        [details](https://www.tensorflow.org/how_tos/embedding_viz/#metadata_optional)
        about metadata files format. In case if the same metadata file is
        used for all embedding layers, string can be passed.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    log_dir='./logs',
    histogram_freq=0,
    write_graph=True,
    write_images=False,
    embeddings_freq=0,
    embeddings_layer_names=None,
    embeddings_metadata=None
)
```



<h3 id="on_batch_begin"><code>on_batch_begin</code></h3>

``` python
on_batch_begin(
    batch,
    logs=None
)
```



<h3 id="on_batch_end"><code>on_batch_end</code></h3>

``` python
on_batch_end(
    batch,
    logs=None
)
```



<h3 id="on_epoch_begin"><code>on_epoch_begin</code></h3>

``` python
on_epoch_begin(
    epoch,
    logs=None
)
```



<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end(
    epoch,
    logs=None
)
```



<h3 id="on_train_begin"><code>on_train_begin</code></h3>

``` python
on_train_begin(logs=None)
```



<h3 id="on_train_end"><code>on_train_end</code></h3>

``` python
on_train_end(_)
```



<h3 id="set_model"><code>set_model</code></h3>

``` python
set_model(model)
```



<h3 id="set_params"><code>set_params</code></h3>

``` python
set_params(params)
```





