

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.get_cross_tower_context

``` python
tf.contrib.distribute.get_cross_tower_context()
```



Defined in [`tensorflow/python/training/distribute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/distribute.py).

Returns the current DistributionStrategy if in a cross-tower context.

Note that execution:
1. starts in the default (single-tower) tower context;
2. switches to cross-tower context when entering a
   `with DistributionStrategy.scope():` block;
3. switches to a (non-default) tower context inside
   `call_for_each_tower(fn, ...)`;
4. if `fn` calls `get_tower_context()->merge_call(merge_fn, ...)`, then
   inside `merge_fn` you are back in the cross-tower context.

Note that you can also go directly from step 1 to 4 to switch to a
cross-tower context for the default `DistributionStrategy`. You may
also switch from the cross-tower context of 4 to a tower context by
calling `call_for_each_tower()`, jumping back to step 3.

Most `DistributionStrategy` methods may only be executed in
a cross-tower context.

#### Returns:

Returns the current `DistributionStrategy` object in a cross-tower
context, or None.

Exactly one of `get_tower_context()` and `get_cross_tower_context()`
will return None in a particular block.