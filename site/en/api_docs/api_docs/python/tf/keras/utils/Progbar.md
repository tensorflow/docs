

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.utils.Progbar

## Class `Progbar`





Defined in [`tensorflow/python/keras/_impl/keras/utils/generic_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/utils/generic_utils.py).

Displays a progress bar.

#### Arguments:

* <b>`target`</b>: Total number of steps expected, None if unknown.
* <b>`interval`</b>: Minimum visual progress update interval (in seconds).

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

* <b>`current`</b>: Index of current step.
* <b>`values`</b>: List of tuples (name, value_for_last_step).
        The progress bar will display averages for these values.
* <b>`force`</b>: Whether to force visual progress update.



