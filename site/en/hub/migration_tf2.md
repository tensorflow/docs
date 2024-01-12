
# Migrating from TF1 to TF2 with TensorFlow Hub

This page explains how to keep using TensorFlow Hub while migrating your
TensorFlow code from TensorFlow 1 to TensorFlow 2. It complements TensorFlow's
general [migration guide](https://www.tensorflow.org/guide/migrate).

For TF2, TF Hub has switched away from the legacy `hub.Module` API for building
a `tf.compat.v1.Graph` like `tf.contrib.v1.layers` do. Instead, there is now a
`hub.KerasLayer` for use alongside other Keras layers for building a
`tf.keras.Model` (typically in TF2's new
[eager execution environment](https://www.tensorflow.org/api_docs/python/tf/executing_eagerly))
and its underlying `hub.load()` method for low-level TensorFlow code.

The `hub.Module` API remains available in the `tensorflow_hub` library for use
in TF1 and in the TF1 compatibility mode of TF2. It can only load models in the
[TF1 Hub format](tf1_hub_module.md).

The new API of `hub.load()` and `hub.KerasLayer` works for TensorFlow 1.15 (in
eager and graph mode) and in TensorFlow 2. This new API can load the new
[TF2 SavedModel](tf2_saved_model.md) assets, and, with the restrictions laid out
in the [model compatibility guide](model_compatibility.md), the legacy models in
TF1 Hub format.

In general, it is recommended to use new API wherever possible.

## Summary of the new API

`hub.load()` is the new low-level function to load a SavedModel from TensorFlow
Hub (or compatible services). It wraps TF2's `tf.saved_model.load()`;
TensorFlow's [SavedModel Guide](https://www.tensorflow.org/guide/saved_model)
describes what you can do with the result.

```python
m = hub.load(handle)
outputs = m(inputs)
```

The `hub.KerasLayer` class calls `hub.load()` and adapts the result for use in
Keras alongside other Keras layers. (It may even be a convenient wrapper for
loaded SavedModels used in other ways.)

```python
model = tf.keras.Sequential([
    hub.KerasLayer(handle),
    ...])
```

Many tutorials show these APIs in action. See in particular

*   [Text classification example notebook](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/tf2_text_classification.ipynb)
*   [Image classification example notebook](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/tf2_image_retraining.ipynb)

### Using the new API in Estimator training

If you use a TF2 SavedModel in an Estimator for training with parameter servers
(or otherwise in a TF1 Session with variables placed on remote devices), you
need to set `experimental.share_cluster_devices_in_session` in the tf.Session's
ConfigProto, or else you will get an error like "Assigned device
'/job:ps/replica:0/task:0/device:CPU:0' does not match any device."

The necessary option can be set like

```python
session_config = tf.compat.v1.ConfigProto()
session_config.experimental.share_cluster_devices_in_session = True
run_config = tf.estimator.RunConfig(..., session_config=session_config)
estimator = tf.estimator.Estimator(..., config=run_config)
```

Starting with TF2.2, this option is no longer experimental, and the
`.experimental` piece can be dropped.

## Loading legacy models in TF1 Hub format

It can happen that a new TF2 SavedModel is not yet available for your use-case
and you need to load an legacy model in TF1 Hub format. Starting in
`tensorflow_hub` release 0.7, you can use legacy model in TF1 Hub format
together with `hub.KerasLayer` as shown below:

```python
m = hub.KerasLayer(handle)
tensor_out = m(tensor_in)
```

Additionally `KerasLayer` exposes the ability to specify `tags`, `signature`,
`output_key` and `signature_outputs_as_dict` for more specific usages of legacy
models in TF1 Hub format and legacy SavedModels.

For more information on TF1 Hub format compatibility see the
[model compatibility guide](model_compatibility.md).

## Using lower level APIs

Legacy TF1 Hub format models can be loaded via `tf.saved_model.load`. Instead of

```python
# DEPRECATED: TensorFlow 1
m = hub.Module(handle, tags={"foo", "bar"})
tensors_out_dict = m(dict(x1=..., x2=...), signature="sig", as_dict=True)
```

it is recommended to use:

```python
# TensorFlow 2
m = hub.load(path, tags={"foo", "bar"})
tensors_out_dict = m.signatures["sig"](x1=..., x2=...)
```

In these examples `m.signatures` is a dict of TensorFlow
[concrete functions](https://www.tensorflow.org/tutorials/customization/performance#tracing)
keyed by signature names. Calling such a function computes all its outputs, even
if unused. (This is different from the lazy evaluation of TF1's graph mode.)
