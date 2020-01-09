page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.CheckpointableBase


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/tracking/base.py#L498-L990">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CheckpointableBase`

Base class for `Trackable` objects without automatic dependencies.



<!-- Placeholder for "Used in" -->

This class has no __setattr__ override for performance reasons. Dependencies
must be added explicitly. Unless attribute assignment is performance-critical,
use `AutoTrackable` instead. Use `Trackable` for `isinstance`
checks.
