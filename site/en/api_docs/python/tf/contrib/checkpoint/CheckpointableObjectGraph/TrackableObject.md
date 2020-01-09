page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.CheckpointableObjectGraph.TrackableObject


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/core/protobuf/trackable_object_graph.proto">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TrackableObject`

A ProtocolMessage



<!-- Placeholder for "Used in" -->


## Child Classes
[`class ObjectReference`](../../../../tf/contrib/checkpoint/CheckpointableObjectGraph/TrackableObject/ObjectReference)

[`class SerializedTensor`](../../../../tf/contrib/checkpoint/CheckpointableObjectGraph/TrackableObject/SerializedTensor)

[`class SlotVariableReference`](../../../../tf/contrib/checkpoint/CheckpointableObjectGraph/TrackableObject/SlotVariableReference)

## Properties

<h3 id="attributes"><code>attributes</code></h3>

`repeated SerializedTensor attributes`


<h3 id="children"><code>children</code></h3>

`repeated ObjectReference children`


<h3 id="slot_variables"><code>slot_variables</code></h3>

`repeated SlotVariableReference slot_variables`
