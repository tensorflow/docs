page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.ModelFnOps

## Class `ModelFnOps`

Ops returned from a model_fn.





Defined in [`contrib/learn/python/learn/estimators/model_fn.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/estimators/model_fn.py).

<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.tensorflow.org/code/tensorflow/contrib/learn/README.md)
for general migration instructions.

## Properties

<h3 id="predictions"><code>predictions</code></h3>




<h3 id="loss"><code>loss</code></h3>




<h3 id="train_op"><code>train_op</code></h3>




<h3 id="eval_metric_ops"><code>eval_metric_ops</code></h3>




<h3 id="output_alternatives"><code>output_alternatives</code></h3>




<h3 id="training_chief_hooks"><code>training_chief_hooks</code></h3>




<h3 id="training_hooks"><code>training_hooks</code></h3>




<h3 id="scaffold"><code>scaffold</code></h3>




<h3 id="mode"><code>mode</code></h3>






## Methods

<h3 id="estimator_spec"><code>estimator_spec</code></h3>

``` python
estimator_spec(default_serving_output_alternative_key=None)
```

Creates an equivalent `EstimatorSpec`.


#### Args:


* <b>`default_serving_output_alternative_key`</b>: Required for multiple heads. If
  you have multiple entries in `output_alternatives` dict (comparable to
  multiple heads), `EstimatorSpec` requires a default head that will be
  used if a Servo request does not explicitly mention which head to infer
  on. Pass the key of the output alternative here that you want to
  designate as default. A separate ExportOutpout for this default head
  will be added to the export_outputs dict with the special key
  saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY, unless there is
  already an enry in output_alternatives with this special key.


#### Returns:

Instance of `EstimatorSpec` that is equivalent to this `ModelFnOps`



#### Raises:


* <b>`ValueError`</b>: If problem type is unknown.



