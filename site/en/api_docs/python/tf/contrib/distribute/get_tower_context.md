

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.get_tower_context

``` python
tf.contrib.distribute.get_tower_context()
```



Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/distribute.py).

Returns the current TowerContext or None if in a cross-tower context.

Note that execution:
1. starts in the default (single-tower) tower context (this function
   will return the default TowerContext object);
2. switches to cross-tower context (in which case this will return
   None) when entering a `with DistributionStrategy.scope():` block;
3. switches to a (non-default) tower context inside
   `call_for_each_tower(fn, ...)`;
4. if `fn` calls `get_tower_context()->merge_call(merge_fn, ...)`, then
   inside `merge_fn` you are back in the cross-tower context (and again
   this function will return None).

Note that you can also go directly from step 1 to 4 to switch to a
cross-tower context for the default `DistributionStrategy`. You may
also switch from the cross-tower context of 4 to a tower context by
calling `call_for_each_tower()`, jumping back to step 3.

Most `DistributionStrategy` methods may only be executed in
a cross-tower context, in a tower context you should use the
`TowerContext` API instead.

#### Returns:

The current `TowerContext` object when in a tower context scope, else None.

Exactly one of `get_tower_context()` and `get_cross_tower_context()`
will return None in a particular block.