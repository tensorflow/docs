page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.RunMode

## Class `RunMode`

Specifies the way a converted function or method should be executed in TF.





Defined in [`python/autograph/impl/api.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/autograph/impl/api.py).

<!-- Placeholder for "Used in" -->


#### Attributes:

* GRAPH: Call this function directly, as-is. This is suitable for functions
  that were already designed for TF graphs and contain ops.
* PY_FUNC: Wrap this function into a py_func op. This is suitable for code
  that will only run correctly in Python, for example code that renders to
  the display, reads keyboard input, etc.


## Class Members

* `GRAPH` <a id="GRAPH"></a>
* `PY_FUNC` <a id="PY_FUNC"></a>
