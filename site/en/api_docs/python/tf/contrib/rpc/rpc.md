page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rpc.rpc

TODO: add doc.

``` python
tf.contrib.rpc.rpc(
    address,
    method,
    request,
    protocol='',
    fail_fast=True,
    timeout_in_ms=0,
    name=None
)
```



Defined in generated file: `contrib/rpc/python/ops/gen_rpc_op.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`address`</b>: A `Tensor` of type `string`.
* <b>`method`</b>: A `Tensor` of type `string`.
* <b>`request`</b>: A `Tensor` of type `string`.
* <b>`protocol`</b>: An optional `string`. Defaults to `""`.
* <b>`fail_fast`</b>: An optional `bool`. Defaults to `True`.
* <b>`timeout_in_ms`</b>: An optional `int`. Defaults to `0`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
