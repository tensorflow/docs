page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rpc.try_rpc

``` python
tf.contrib.rpc.try_rpc(
    address,
    method,
    request,
    protocol='',
    fail_fast=True,
    timeout_in_ms=0,
    name=None
)
```



Defined in generated file: `tensorflow/contrib/rpc/python/ops/gen_rpc_op.py`.

TODO: add doc.

#### Args:

* <b>`address`</b>: A `Tensor` of type `string`.
* <b>`method`</b>: A `Tensor` of type `string`.
* <b>`request`</b>: A `Tensor` of type `string`.
* <b>`protocol`</b>: An optional `string`. Defaults to `""`.
* <b>`fail_fast`</b>: An optional `bool`. Defaults to `True`.
* <b>`timeout_in_ms`</b>: An optional `int`. Defaults to `0`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (response, status_code, status_message).

* <b>`response`</b>: A `Tensor` of type `string`.
* <b>`status_code`</b>: A `Tensor` of type `int32`.
* <b>`status_message`</b>: A `Tensor` of type `string`.