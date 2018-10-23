

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.utils.plot_model

``` python
plot_model(
    model,
    to_file='model.png',
    show_shapes=False,
    show_layer_names=True,
    rankdir='TB'
)
```



Defined in [`tensorflow/contrib/keras/python/keras/utils/vis_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/utils/vis_utils.py).

Converts a Keras model to dot format and save to a file.

#### Arguments:

    model: A Keras model instance
    to_file: File name of the plot image.
    show_shapes: whether to display shape information.
    show_layer_names: whether to display layer names.
    rankdir: `rankdir` argument passed to PyDot,
        a string specifying the format of the plot:
        'TB' creates a vertical plot;
        'LR' creates a horizontal plot.