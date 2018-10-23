

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.AggregationMethod

## Class `AggregationMethod`





Defined in [`tensorflow/python/ops/gradients_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/gradients_impl.py).

See the guide: [Training > Gradient Computation](../../../api_guides/python/train#Gradient_Computation)

A class listing aggregation methods used to combine gradients.

Computing partial derivatives can require aggregating gradient
contributions. This class lists the various methods that can
be used to combine gradients in the graph:

*  `ADD_N`: All of the gradient terms are summed as part of one
   operation using the "AddN" op. It has the property that all
   gradients must be ready before any aggregation is performed.
*  `DEFAULT`: The system-chosen default aggregation method.

## Class Members

<h3 id="ADD_N"><code>ADD_N</code></h3>

<h3 id="DEFAULT"><code>DEFAULT</code></h3>

<h3 id="EXPERIMENTAL_ACCUMULATE_N"><code>EXPERIMENTAL_ACCUMULATE_N</code></h3>

<h3 id="EXPERIMENTAL_TREE"><code>EXPERIMENTAL_TREE</code></h3>

