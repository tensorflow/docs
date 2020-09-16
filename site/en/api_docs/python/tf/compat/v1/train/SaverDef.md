description: A ProtocolMessage

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.SaverDef" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="CheckpointFormatVersion"/>
<meta itemprop="property" content="LEGACY"/>
<meta itemprop="property" content="V1"/>
<meta itemprop="property" content="V2"/>
</div>

# tf.compat.v1.train.SaverDef

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/core/protobuf/saver.proto">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A ProtocolMessage

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`filename_tensor_name`
</td>
<td>
`string filename_tensor_name`
</td>
</tr><tr>
<td>
`keep_checkpoint_every_n_hours`
</td>
<td>
`float keep_checkpoint_every_n_hours`
</td>
</tr><tr>
<td>
`max_to_keep`
</td>
<td>
`int32 max_to_keep`
</td>
</tr><tr>
<td>
`restore_op_name`
</td>
<td>
`string restore_op_name`
</td>
</tr><tr>
<td>
`save_tensor_name`
</td>
<td>
`string save_tensor_name`
</td>
</tr><tr>
<td>
`sharded`
</td>
<td>
`bool sharded`
</td>
</tr><tr>
<td>
`version`
</td>
<td>
`CheckpointFormatVersion version`
</td>
</tr>
</table>



## Class Variables

* `CheckpointFormatVersion` <a id="CheckpointFormatVersion"></a>
* `LEGACY = 0` <a id="LEGACY"></a>
* `V1 = 1` <a id="V1"></a>
* `V2 = 2` <a id="V2"></a>
