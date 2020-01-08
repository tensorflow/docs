page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.callbacks.TensorBoard

## Class `TensorBoard`

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback)



Defined in [`tensorflow/python/keras/callbacks.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/callbacks.py).

Tensorboard basic visualizations.

This callback writes a log for TensorBoard, which allows
you to visualize dynamic graphs of your training and test
metrics, as well as activation histograms for the different
layers in your model.

TensorBoard is a visualization tool provided with TensorFlow.

If you have installed TensorFlow with pip, you should be able
to launch TensorBoard from the command line:

```sh
tensorboard --logdir=/full_path_to_your_logs
```

You can find more information about TensorBoard
[here](https://www.tensorflow.org/get_started/summaries_and_tensorboard).

#### Arguments:

* <b>`log_dir`</b>: the path of the directory where to save the log
        files to be parsed by TensorBoard.
* <b>`histogram_freq`</b>: frequency (in epochs) at which to compute activation
        and weight histograms for the layers of the model. If set to 0,
        histograms won't be computed. Validation data (or split) must be
        specified for histogram visualizations.
* <b>`write_graph`</b>: whether to visualize the graph in TensorBoard.
        The log file can become quite large when
        write_graph is set to True.
* <b>`write_grads`</b>: whether to visualize gradient histograms in TensorBoard.
        `histogram_freq` must be greater than 0.
* <b>`batch_size`</b>: size of batch of inputs to feed to the network
        for histograms computation.
* <b>`write_images`</b>: whether to write model weights to visualize as
        image in TensorBoard.
* <b>`embeddings_freq`</b>: frequency (in epochs) at which selected embedding
        layers will be saved. If set to 0, embeddings won't be computed.
        Data to be visualized in TensorBoard's Embedding tab must be passed
        as `embeddings_data`.
* <b>`embeddings_layer_names`</b>: a list of names of layers to keep eye on. If
        None or empty list all the embedding layer will be watched.
* <b>`embeddings_metadata`</b>: a dictionary which maps layer name to a file name
        in which metadata for this embedding layer is saved. See the
        [details](https://www.tensorflow.org/how_tos/embedding_viz/#metadata_optional)
        about metadata files format. In case if the same metadata file is
        used for all embedding layers, string can be passed.
* <b>`embeddings_data`</b>: data to be embedded at layers specified in
        `embeddings_layer_names`. Numpy array (if the model has a single
        input) or list of Numpy arrays (if the model has multiple inputs).
        Learn [more about embeddings](https://www.tensorflow.org/programmers_guide/embedding)


#### Raises:

* <b>`ValueError`</b>: If histogram_freq is set and no validation data is provided.



#### Eager Compatibility
Using `Tensorboard` callback will work while eager execution is enabled,
however outputting histogram summaries of weights and gradients is not
supported, and thus `histogram_freq` will be ignored.



<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    log_dir='./logs',
    histogram_freq=0,
    batch_size=32,
    write_graph=True,
    write_grads=False,
    write_images=False,
    embeddings_freq=0,
    embeddings_layer_names=None,
    embeddings_metadata=None,
    embeddings_data=None
)
```





## Methods

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

Writes scalar summaries for metrics on every training batch.

<h3 id="on_epoch_begin"><code>on_epoch_begin</code></h3>

``` python
on_epoch_begin(
    epoch,
    logs=None
)
```

Add histogram op to Model test_function callbacks, reset batch count.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

``` python
on_epoch_end(
    epoch,
    logs=None
)
```

Checks if summary ops should run next epoch, logs scalar summaries.

<h3 id="on_train_begin"><code>on_train_begin</code></h3>

``` python
on_train_begin(logs=None)
```

Checks if histogram summaries can be run.

<h3 id="on_train_end"><code>on_train_end</code></h3>

``` python
on_train_end(logs=None)
```



<h3 id="set_model"><code>set_model</code></h3>

``` python
set_model(model)
```

Sets Keras model and creates summary ops.

<h3 id="set_params"><code>set_params</code></h3>

``` python
set_params(params)
```





