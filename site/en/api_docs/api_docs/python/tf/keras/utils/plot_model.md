

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.utils.plot_model

``` python
plot_model(
    model,
    to_file='model.png',
    show_shapes=False,
    show_layer_names=True,
    rankdir='TB'
)
```



Defined in [`tensorflow/python/keras/_impl/keras/utils/vis_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/utils/vis_utils.py).

Converts a Keras model to dot format and save to a file.

#### Arguments:

* <b>`model`</b>: A Keras model instance
* <b>`to_file`</b>: File name of the plot image.
* <b>`show_shapes`</b>: whether to display shape information.
* <b>`show_layer_names`</b>: whether to display layer names.
* <b>`rankdir`</b>: `rankdir` argument passed to PyDot,
        a string specifying the format of the plot:
        'TB' creates a vertical plot;
        'LR' creates a horizontal plot.