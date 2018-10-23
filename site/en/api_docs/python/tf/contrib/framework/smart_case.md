

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.smart_case

``` python
tf.contrib.framework.smart_case(
    pred_fn_pairs,
    default=None,
    exclusive=False,
    name='smart_case'
)
```



Defined in [`tensorflow/python/framework/smart_cond.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/framework/smart_cond.py).

Like tf.case, except attempts to statically evaluate predicates.

If any predicate in `pred_fn_pairs` is a bool or has a constant value, the
associated callable will be called or omitted depending on its value.
Otherwise this functions like tf.case.

#### Args:

* <b>`pred_fn_pairs`</b>: Dict or list of pairs of a boolean scalar tensor and a
                 callable which returns a list of tensors.
* <b>`default`</b>: Optional callable that returns a list of tensors.
* <b>`exclusive`</b>: True iff at most one predicate is allowed to evaluate to `True`.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

The tensors returned by the first pair whose predicate evaluated to True, or
those returned by `default` if none does.


#### Raises:

* <b>`TypeError`</b>: If `pred_fn_pairs` is not a list/dictionary.
* <b>`TypeError`</b>: If `pred_fn_pairs` is a list but does not contain 2-tuples.
* <b>`TypeError`</b>: If `fns[i]` is not callable for any i, or `default` is not
             callable.