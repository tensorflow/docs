page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.WatchOptions

## Class `WatchOptions`





Defined in [`tensorflow/python/debug/wrappers/framework.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/debug/wrappers/framework.py).

Type for return values of watch_fn.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    debug_ops=None,
    node_name_regex_whitelist=None,
    op_type_regex_whitelist=None,
    tensor_dtype_regex_whitelist=None,
    tolerate_debug_op_creation_failures=False
)
```

Constructor of WatchOptions: Debug watch options.

Used as return values of `watch_fn`s.

#### Args:

* <b>`debug_ops`</b>: (`str` or `list of str`) Debug ops to be used.
* <b>`node_name_regex_whitelist`</b>: Regular-expression whitelist for node_name,
    e.g., `"(weight_[0-9]+|bias_.*)"`
* <b>`op_type_regex_whitelist`</b>: Regular-expression whitelist for the op type of
    nodes, e.g., `"(Variable|Add)"`.
    If both `node_name_regex_whitelist` and `op_type_regex_whitelist`
    are set, the two filtering operations will occur in a logical `AND`
    relation. In other words, a node will be included if and only if it
    hits both whitelists.
* <b>`tensor_dtype_regex_whitelist`</b>: Regular-expression whitelist for Tensor
    data type, e.g., `"^int.*"`.
    This whitelist operates in logical `AND` relations to the two whitelists
    above.
* <b>`tolerate_debug_op_creation_failures`</b>: (`bool`) whether debug op creation
    failures (e.g., due to dtype incompatibility) are to be tolerated by not
    throwing exceptions.



