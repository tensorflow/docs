page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.Progbar


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L311-L478">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Progbar`

Displays a progress bar.



### Aliases:

* Class `tf.compat.v1.keras.utils.Progbar`
* Class `tf.compat.v2.keras.utils.Progbar`


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`target`</b>: Total number of steps expected, None if unknown.
* <b>`width`</b>: Progress bar width on screen.
* <b>`verbose`</b>: Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose)
* <b>`stateful_metrics`</b>: Iterable of string names of metrics that
    should *not* be averaged over time. Metrics in this list
    will be displayed as-is. All others will be averaged
    by the progbar before display.
* <b>`interval`</b>: Minimum visual progress update interval (in seconds).
* <b>`unit_name`</b>: Display name for step counts (usually "step" or "sample").

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L326-L349">View source</a>

``` python
__init__(
    target,
    width=30,
    verbose=1,
    interval=0.05,
    stateful_metrics=None,
    unit_name='step'
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="add"><code>add</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L477-L478">View source</a>

``` python
add(
    n,
    values=None
)
```




<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/generic_utils.py#L351-L475">View source</a>

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
