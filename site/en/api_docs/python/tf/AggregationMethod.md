page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.AggregationMethod


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/gradients_util.py#L881-L917">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AggregationMethod`

A class listing aggregation methods used to combine gradients.



### Aliases:

* Class `tf.compat.v1.AggregationMethod`
* Class `tf.compat.v2.AggregationMethod`


<!-- Placeholder for "Used in" -->

Computing partial derivatives can require aggregating gradient
contributions. This class lists the various methods that can
be used to combine gradients in the graph.

The following aggregation methods are part of the stable API for
aggregating gradients:

*  `ADD_N`: All of the gradient terms are summed as part of one
   operation using the "AddN" op (see <a href="../tf/math/add_n"><code>tf.add_n</code></a>). This
   method has the property that all gradients must be ready and
   buffered separately in memory before any aggregation is performed.
*  `DEFAULT`: The system-chosen default aggregation method.

The following aggregation methods are experimental and may not
be supported in future releases:

* `EXPERIMENTAL_TREE`: Gradient terms are summed in pairs using
  using the "AddN" op. This method of summing gradients may reduce
  performance, but it can improve memory utilization because the
  gradients can be released earlier.

* `EXPERIMENTAL_ACCUMULATE_N`: Gradient terms are summed using the
  "AccumulateN" op (see `tf.accumulate_n`), which accumulates the
  overall sum in a single buffer that is shared across threads.
  This method of summing gradients can result in a lower memory footprint
  and lower latency at the expense of higher CPU/GPU utilization.
  For gradients of types that "AccumulateN" does not support, this
  summation method falls back on the behavior of `EXPERIMENTAL_TREE`

## Class Members

* `ADD_N = 0` <a id="ADD_N"></a>
* `DEFAULT = 0` <a id="DEFAULT"></a>
* `EXPERIMENTAL_ACCUMULATE_N = 2` <a id="EXPERIMENTAL_ACCUMULATE_N"></a>
* `EXPERIMENTAL_TREE = 1` <a id="EXPERIMENTAL_TREE"></a>
