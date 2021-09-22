# TF1.x -> TF2 migration overview

TensorFlow 2 is fundamentally different from TF1.x in several ways. You can
still run unmodified TF1.x code
([except for contrib](https://github.com/tensorflow/community/blob/master/rfcs/20180907-contrib-sunset.md))
against TF2 binary installations like so:

```python
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
```

However, this is *not* running TF2 behaviors and APIs, and may not work as
expected with code written for TF2. If you are not running with TF2 behaviors
active, you are effectively running TF1.x on top of a TF2 installation. Read the
[TF1 vs TF2 behaviors guide](./tf1_vs_tf2.ipynb) for more details on how TF2 is
different from TF1.x.

This guide provides an overview of the process to migrate your TF1.x code to
TF2. This enables you to take advantage of new and future feature improvements
and also make your code simpler, more performant, and easier to maintain.

If you are using `tf.keras`'s high level APIs and training exclusively with
`model.fit`, your code should more or less be fully compatible with TF2 except
for the following caveats:

-   TF2 has new
    [default learning rates](../../guide/effective_tf2.ipynb#optimizer_defaults)
    for Keras optimizers.
-   TF2 [may have changed](../../guide/effective_tf2.ipynb#keras_metric_names)
    the "name" that metrics are logged to.

## TF2 migration process

Before migrating, learn about the behavior and API differences between TF1.x and
TF2 by reading the [guide](./tf1_vs_tf2.ipynb).

1.  Run the automated script to convert some of your TF1.x API usage to
    `tf.compat.v1`.
2.  Remove old `tf.contrib` symbols (check
    [TF Addons](https://github.com/tensorflow/addons) and
    [TF-Slim](https://github.com/google-research/tf-slim)).
3.  Make your TF1.x model forward passes run in TF2 with eager execution
    enabled.
4.  Upgrade your TF1.x code for training loops and saving/loading models to TF2
    equivalents.
5.  (Optional) Migrate your TF2-compatible `tf.compat.v1` APIs to idiomatic TF2
    APIs.

The following sections expand upon the steps outlined above.

## Run the symbol conversion script

This executes an initial pass at rewriting your code symbols to run against TF
2.x binaries, but won't make your code idiomatic to TF 2.x nor will it
automatically make your code compatible with TF2 behaviors.

Your code will most likely still make use of `tf.compat.v1` endpoints to access
placeholders, sessions, collections, and other TF1.x-style functionality.

Read the [guide](./upgrade.ipynb) to find out more about the best practices for
using the symbol conversion script.

## Remove usage of `tf.contrib`

The `tf.contrib` module has been sunsetted and several of its submodules have
been integrated into the core TF2 API. The other submodules are now spun-off
into other projects like [TF IO](https://github.com/tensorflow/io) and
[TF Addons](https://www.tensorflow.org/addons/overview).

A large amount of older TF1.x code uses the
[Slim](https://ai.googleblog.com/2016/08/tf-slim-high-level-library-to-define.html)
library, which was packaged with TF1.x as `tf.contrib.layers`. When migrating
your Slim code to TF2, switch your Slim API usages to point to the
[tf-slim pip package](https://pypi.org/project/tf-slim/). Then, read the
[model mapping guide](https://tensorflow.org/guide/migrate/model_mapping#a_note_on_slim_and_contriblayers)
to learn how to convert Slim code.

Alternatively, if you use Slim pre-trained models you may consider trying out
Keras's pre-traimed models from `tf.keras.applications` or
[TF Hub](https://tfhub.dev/s?tf-version=tf2&q=slim)'s TF2 `SavedModel`s exported
from the original Slim code.

## Make TF1.x model forward passes run with TF2 behaviors enabled

### Track variables and losses

[TF2 does not support global collections.](./tf1_vs_tf2.ipynb#no_more_globals)

Eager execution in TF2 does not support `tf.Graph` collection-based APIs. This
affects how you construct and track variables.

For new TF2 code you would use `tf.Variable` instead of `v1.get_variable` and
use Python objects to collect and track variables instead of
`tf.compat.v1.variable_scope`. Typically this would be one of:

*   `tf.keras.layers.Layer`
*   `tf.keras.Model`
*   `tf.Module`

Aggregate lists of variables (like
`tf.Graph.get_collection(tf.GraphKeys.VARIABLES)`) with the `.variables` and
`.trainable_variables` attributes of the `Layer`, `Module`, or `Model` objects.

The `Layer` and `Model` classes implement several other properties that remove
the need for global collections. Their `.losses` property can be a replacement
for using the `tf.GraphKeys.LOSSES` collection.

Read the [model mapping guide](./model_mapping.ipynb) to find out more about
using the TF2 code modeling shims to embed your existing `get_variable` and
`variable_scope` based code inside of `Layers`, `Models`, and `Modules`. This
will let you the execute forward passes with eager execution enabled without
major rewrites.

### Adapting to other behavior changes

If the [model mapping guide](./model_mapping.ipynb) on its own is insufficient
to get your model forward pass running other behavior changes that may be more
details, see the guide on [TF1.x vs TF2 behaviors](./tf1_vs_tf2.ipynb) to learn
about the other behavior changes and how you can adapt to them. Also check out
the
[making new Layers and Models via subclassing guide](https://tensorflow.org/guide/keras/custom_layers_and_models.ipynb)
for details.

### Validating your results

See the [model validation guide](./validate_correctness.ipynb) for easy tools
and guidance around how you can (numerically) validate that your model is
behaving correctly when eager execution is enabled. You may find this especially
useful when paired with the [model mapping guide](./model_mapping.ipynb).

## Upgrade training, evaluation, and import/export code

TF1.x training loops built with `v1.Session`-style `tf.estimator.Estimator`s and
other collections-based approaches are not compatible with the new behaviors of
TF2. It is important you migrate all your TF1.x training code as combining it
with TF2 code can cause unexpected behaviors.

You can choose from among several strategies to do this.

The highest-level approach is to use `tf.keras`. The high level functions in
Keras manage a lot of the low-level details that might be easy to miss if you
write your own training loop. For example, they automatically collect the
regularization losses, and set the `training=True` argument when calling the
model.

Refer to the [Estimator migration guide](./migrating_estimator.ipynb) to learn
how you can migrate `tf.estimator.Estimator`s code to use
[vanilla](./migrating_estimator.ipynb#tf2_keras_training_api) and
[custom](./migrating_estimator.ipynb#tf2_keras_training_api_with_custom_training_step)
`tf.keras` training loops.

Custom training loops give you finer control over your model such as tracking
the weights of individual layers. Read the guide on
[building training loops from scratch](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch)
to learn how to use `tf.GradientTape` to retrieve model weights and use them to
update the model.

### Convert TF1.x optimizers to Keras optimizers

The optimizers in `tf.compat.v1.train`, such as the
[Adam optimizer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/AdamOptimizer)
and the
[gradient descent optimizer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/GradientDescentOptimizer),
have equivalents in `tf.keras.optimizers`.

The table below summarizes how you can convert these legacy optimizers to their
Keras equivalents. You can directly replace the TF1.x version with the TF2
version unless additional steps (such as
[updating the default learning rate](../../guide/effective_tf2.ipynb#optimizer_defaults))
are required.

Note that converting your optimizers
[may make old checkpoints incompatible](./migrating_checkpoints.ipynb).

<table>
  <tr>
    <th>TF1.x</th>
    <th>TF2</th>
    <th>Additional steps</th>
  </tr>
  <tr>
    <td>`tf.v1.train.GradientDescentOptimizer`</td>
    <td>`tf.keras.optimizers.SGD`</td>
    <td>None</td>
  </tr>
  <tr>
    <td>`tf.v1.train.MomentumOptimizer`</td>
    <td>`tf.keras.optimizers.SGD`</td>
    <td>Include the `momentum` argument</td>
  </tr>
  <tr>
    <td>`tf.v1.train.AdamOptimizer`</td>
    <td>`tf.keras.optimizers.Adam`</td>
    <td>Rename `beta1` and `beta2` arguments to `beta_1` and `beta_2`</td>
  </tr>
  <tr>
    <td>`tf.v1.train.RMSPropOptimizer`</td>
    <td>`tf.keras.optimizers.RMSprop`</td>
    <td>Rename the `decay` argument to `rho`</td>
  </tr>
  <tr>
    <td>`tf.v1.train.AdadeltaOptimizer`</td>
    <td>`tf.keras.optimizers.Adadelta`</td>
    <td>None</td>
  </tr>
  <tr>
    <td>`tf.v1.train.AdagradOptimizer`</td>
    <td>`tf.keras.optimizers.Adagrad`</td>
    <td>None</td>
  </tr>
  <tr>
    <td>`tf.v1.train.FtrlOptimizer`</td>
    <td>`tf.keras.optimizers.Ftrl`</td>
    <td>Remove the `accum_name` and `linear_name` arguments</td>
  </tr>
  <tr>
    <td>`tf.contrib.AdamaxOptimizer`</td>
    <td>`tf.keras.optimizers.Adamax`</td>
    <td>Rename the `beta1`, and `beta2` arguments to `beta_1` and `beta_2`</td>
  </tr>
  <tr>
    <td>`tf.contrib.Nadam`</td>
    <td>`tf.keras.optimizers.Nadam`</td>
    <td>Rename the `beta1`, and `beta2` arguments to `beta_1` and `beta_2`</td>
  </tr>
</table>

Note: In TF2, all epsilons (numerical stability constants) now default to `1e-7`
instead of `1e-8`. This difference is negligible in most use cases.

### Upgrade data input pipelines

There are many ways to feed data to a `tf.keras` model. They will accept Python
generators and Numpy arrays as input.

The recommended way to feed data to a model is to use the `tf.data` package,
which contains a collection of high performance classes for manipulating data.
The `dataset`s belonging to `tf.data` are efficient, expressive, and integrate
well with TF2.

They can be passed directly to the `tf.keras.Model.fit` method.

```python
model.fit(dataset, epochs=5)
```

They can be iterated over directly standard Python:

```python
for example_batch, label_batch in dataset:
    break
```

If you are still using `tf.queue`, these are now only supported as
data-structures, not as input pipelines.

You should also migrate all feature preprocessing code that
uses`tf.feature_columns`. Read the
[migration guide](./migrating_feature_columns.ipynb) for more details.

### Saving and loading models

TF2 uses object-based checkpoints. Read the
[checkpoint migration guide](./migrating_checkpoints.ipynb) to learn more about
migrating off name-based TF1.x checkpoints. Also read the
[checkpoints guide](https://www.tensorflow.org/guide/checkpoint) in the core
TensorFlow docs.

There are no significant compatibility concerns for saved models. Read the
[`SavedModel` guide](./saved_model.ipynb) for more information about migrating
`SavedModel`s in TF1.x to TF2. In general,

-   TF1.x saved_models work in TF2.
-   TF2 saved_models work in TF1.x if all the ops are supported.

Also refer to the
[`GraphDef` section](./saved_model.ipynb#graphdef_and_metagraphdef) in the
`SavedModel` migration guide for more information on working with `Graph.pb` and
`Graph.pbtxt` objects.

## (Optional) Migrate off `tf.compat.v1` symbols

The `tf.compat.v1` module contains the complete TF1.x API, with its original
semantics.

Even after following the steps above and ending up with code that is fully
compatible with all TF2 behaviors, it is likely there may be many mentions of
`compat.v1` apis that happen to be compatible with TF2. You should avoid using
these legacy `compat.v1` apis for any new code that you write, though they will
continue working for your already-written code.

However, you may choose to migrate the existing usages to non-legacy TF2 APIs.
The docstrings of individual `compat.v1` symbols will often explain how to
migrate them to non-legacy TF2 APIs. Additionally, the
[model mapping guide's section on incremental migration to idiomatic TF2 APIs](./model_mapping.ipynb#incremental_migration_to_native_tf2)
may help with this as well.

## Resources and further reading

As mentioned previously, it is a good practice to migrate all your TF1.x code to
TF2. Read the guides in the
[Migrate to TF2 section](https://tensorflow.org/guide/migrate) of the TensorFlow
guide to learn more.
