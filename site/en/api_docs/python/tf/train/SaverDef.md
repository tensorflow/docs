page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.SaverDef

## Class `SaverDef`





### Aliases:

* Class `tf.compat.v1.train.SaverDef`
* Class `tf.train.SaverDef`



Defined in [`core/protobuf/saver.proto`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/core/protobuf/saver.proto).

<!-- Placeholder for "Used in" -->


## Properties

<h3 id="filename_tensor_name"><code>filename_tensor_name</code></h3>

`string filename_tensor_name`


<h3 id="keep_checkpoint_every_n_hours"><code>keep_checkpoint_every_n_hours</code></h3>

`float keep_checkpoint_every_n_hours`


<h3 id="max_to_keep"><code>max_to_keep</code></h3>

`int32 max_to_keep`


<h3 id="restore_op_name"><code>restore_op_name</code></h3>

`string restore_op_name`


<h3 id="save_tensor_name"><code>save_tensor_name</code></h3>

`string save_tensor_name`


<h3 id="sharded"><code>sharded</code></h3>

`bool sharded`


<h3 id="version"><code>version</code></h3>

`CheckpointFormatVersion version`




## Class Members

* `CheckpointFormatVersion` <a id="CheckpointFormatVersion"></a>
* `LEGACY = 0` <a id="LEGACY"></a>
* `V1 = 1` <a id="V1"></a>
* `V2 = 2` <a id="V2"></a>
