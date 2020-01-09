page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.list_objects


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/util.py#L479-L493">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Traverse the object graph and list all accessible objects.

``` python
tf.contrib.checkpoint.list_objects(root_trackable)
```



<!-- Placeholder for "Used in" -->

Looks for `Trackable` objects which are dependencies of
`root_trackable`. Includes slot variables only if the variable they are
slotting for and the optimizer are dependencies of `root_trackable`
(i.e. if they would be saved with a checkpoint).

#### Args:


* <b>`root_trackable`</b>: A `Trackable` object whose dependencies should be flattened.


#### Returns:

A flat list of objects.
