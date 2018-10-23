

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.utils.Progbar

### `class tf.contrib.keras.utils.Progbar`



Defined in [`tensorflow/contrib/keras/python/keras/utils/generic_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/utils/generic_utils.py).

Displays a progress bar.

#### Arguments:

    target: Total number of steps expected.
    interval: Minimum visual progress update interval (in seconds).

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    target,
    width=30,
    verbose=1,
    interval=0.05
)
```



<h3 id="add"><code>add</code></h3>

``` python
add(
    n,
    values=None
)
```



<h3 id="update"><code>update</code></h3>

``` python
update(
    current,
    values=None,
    force=False
)
```

Updates the progress bar.

#### Arguments:

    current: Index of current step.
    values: List of tuples (name, value_for_last_step).
        The progress bar will display averages for these values.
    force: Whether to force visual progress update.



