

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.Progbar

## Class `Progbar`





Defined in [`tensorflow/python/keras/utils/generic_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/utils/generic_utils.py).

Displays a progress bar.

#### Arguments:

* <b>`target`</b>: Total number of steps expected, None if unknown.
* <b>`width`</b>: Progress bar width on screen.
* <b>`verbose`</b>: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
* <b>`stateful_metrics`</b>: Iterable of string names of metrics that
        should *not* be averaged over time. Metrics in this list
        will be displayed as-is. All others will be averaged
        by the progbar before display.
* <b>`interval`</b>: Minimum visual progress update interval (in seconds).

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    target,
    width=30,
    verbose=1,
    interval=0.05,
    stateful_metrics=None
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
    values=None
)
```

Updates the progress bar.

#### Arguments:

* <b>`current`</b>: Index of current step.
* <b>`values`</b>: List of tuples:
        `(name, value_for_last_step)`.
        If `name` is in `stateful_metrics`,
        `value_for_last_step` will be displayed as-is.
        Else, an average of the metric over time will be displayed.



