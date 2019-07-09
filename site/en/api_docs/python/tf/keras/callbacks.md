page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.keras.callbacks



Defined in [`tensorflow/keras/callbacks/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/keras/callbacks/__init__.py).

Callbacks: utilities called at certain points during model training.

## Classes

[`class BaseLogger`](../../tf/keras/callbacks/BaseLogger): Callback that accumulates epoch averages of metrics.

[`class CSVLogger`](../../tf/keras/callbacks/CSVLogger): Callback that streams epoch results to a csv file.

[`class Callback`](../../tf/keras/callbacks/Callback): Abstract base class used to build new callbacks.

[`class EarlyStopping`](../../tf/keras/callbacks/EarlyStopping): Stop training when a monitored quantity has stopped improving.

[`class History`](../../tf/keras/callbacks/History): Callback that records events into a `History` object.

[`class LambdaCallback`](../../tf/keras/callbacks/LambdaCallback): Callback for creating simple, custom callbacks on-the-fly.

[`class LearningRateScheduler`](../../tf/keras/callbacks/LearningRateScheduler): Learning rate scheduler.

[`class ModelCheckpoint`](../../tf/keras/callbacks/ModelCheckpoint): Save the model after every epoch.

[`class ProgbarLogger`](../../tf/keras/callbacks/ProgbarLogger): Callback that prints metrics to stdout.

[`class ReduceLROnPlateau`](../../tf/keras/callbacks/ReduceLROnPlateau): Reduce learning rate when a metric has stopped improving.

[`class RemoteMonitor`](../../tf/keras/callbacks/RemoteMonitor): Callback used to stream events to a server.

[`class TensorBoard`](../../tf/keras/callbacks/TensorBoard): Tensorboard basic visualizations.

[`class TerminateOnNaN`](../../tf/keras/callbacks/TerminateOnNaN): Callback that terminates training when a NaN loss is encountered.

