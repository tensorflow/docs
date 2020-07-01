# TensorFlow version compatibility

This document is for users who need backwards compatibility across different
versions of TensorFlow (either for code or data), and for developers who want
to modify TensorFlow while preserving compatibility.

## Semantic versioning 2.0

TensorFlow follows Semantic Versioning 2.0 ([semver](http://semver.org)) for its
public API. Each release version of TensorFlow has the form `MAJOR.MINOR.PATCH`.
For example, TensorFlow version 1.2.3 has `MAJOR` version 1, `MINOR` version 2,
and `PATCH` version 3. Changes to each number have the following meaning:

* **MAJOR**:  Potentially backwards incompatible changes.  Code and data that
  worked with a previous major release will not necessarily work with the new
  release. However, in some cases existing TensorFlow graphs and checkpoints
  may be migratable to the newer release; see
  [Compatibility of graphs and checkpoints](#compatibility_of_graphs_and_checkpoints)
  for details on data compatibility.

* **MINOR**: Backwards compatible features, speed improvements, etc. Code and
  data that worked with a previous minor release *and* which depends only on the
  non-experimental public API will continue to work unchanged.  For details on
  what is and is not the public API, see [What is covered](#what_is_covered).

* **PATCH**: Backwards compatible bug fixes.

For example, release 1.0.0 introduced backwards *incompatible* changes from
release 0.12.1.  However, release 1.1.1 was backwards *compatible* with release
1.0.0.
<a name="what_is_covered"></a>
## What is covered

Only the public APIs of TensorFlow are backwards compatible across minor and
patch versions.  The public APIs consist of

* All the documented [Python](../api_docs/python) functions and classes in the
  `tensorflow` module and its submodules, except for

    * Private symbols: any function, class, etc., whose name start with `_`
    * Experimental and `tf.contrib` symbols, see [below](#not_covered) for
      details.

  Note that the code in the `examples/` and `tools/` directories is not
  reachable through the `tensorflow` Python module and is thus not covered by
  the compatibility guarantee.

  If a symbol is available through the `tensorflow` Python module or its
  submodules, but is not documented, then it is **not** considered part of the
  public API.

* The compatibility API (in Python, the `tf.compat` module). At major versions,
  we may release utilities and additional endpoints to help users with the
  transition to a new major version. These API symbols are deprecated and not
  supported (i.e., we will not add any features, and we will not fix bugs
  other than to fix vulnerabilities), but they do fall under our compatibility
  guarantees.

* The [C API](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/c/c_api.h).

* The following protocol buffer files:

    * [`attr_value`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/attr_value.proto)
    * [`config`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/protobuf/config.proto)
    * [`event`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/util/event.proto)
    * [`graph`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/graph.proto)
    * [`op_def`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/op_def.proto)
    * [`reader_base`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/reader_base.proto)
    * [`summary`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/summary.proto)
    * [`tensor`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/tensor.proto)
    * [`tensor_shape`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/tensor_shape.proto)
    * [`types`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/types.proto)

<a name="not_covered"></a>
## What is *not* covered

Some parts of TensorFlow can change in backward incompatible ways at any point.
These include:

*   **Experimental APIs**: To facilitate development, we exempt some API symbols
    clearly marked as experimental from the compatibility guarantees. In
    particular, the following are not covered by any compatibility guarantees:

    -   any symbol in the `tf.contrib` module or its submodules;
    -   any symbol (module, function, argument, property, class, or constant)
        whose name contains `experimental` or `Experimental`; or
    -   any symbol whose fully qualified name includes a module or class which
        is itself experimental. This includes fields and submessages of any
        protocol buffer called `experimental`.

*   **Other languages**: TensorFlow APIs in languages other than Python and C,
    such as:

    -   [C++](../install/lang_c.md) (exposed through header files in
        [`tensorflow/cc`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/cc)).
    -   [Java](../install/lang_java.md),
    -   [Go](../install/lang_go.md)
    -   [JavaScript](https://www.tensorflow.org/js)

*   **Details of composite ops:** Many public functions in Python expand to
    several primitive ops in the graph, and these details will be part of any
    graphs saved to disk as `GraphDef`s. These details may change for minor
    releases. In particular, regression tests that check for exact matching
    between graphs are likely to break across minor releases, even though the
    behavior of the graph should be unchanged and existing checkpoints will
    still work.

*   **Floating point numerical details:** The specific floating point values
    computed by ops may change at any time. Users should rely only on
    approximate accuracy and numerical stability, not on the specific bits
    computed. Changes to numerical formulas in minor and patch releases should
    result in comparable or improved accuracy, with the caveat that in machine
    learning improved accuracy of specific formulas may result in decreased
    accuracy for the overall system.

*   **Random numbers:** The specific random numbers computed may change at any
    time. Users should rely only on approximately correct distributions and
    statistical strength, not the specific bits computed. See the
    [random number generation](random_numbers.ipynb) guide for details.

*   **Version skew in distributed Tensorflow:** Running two different versions
    of TensorFlow in a single cluster is unsupported. There are no guarantees
    about backwards compatibility of the wire protocol.

*   **Bugs:** We reserve the right to make backwards incompatible behavior
    (though not API) changes if the current implementation is clearly broken,
    that is, if it contradicts the documentation or if a well-known and
    well-defined intended behavior is not properly implemented due to a bug. For
    example, if an optimizer claims to implement a well-known optimization
    algorithm but does not match that algorithm due to a bug, then we will fix
    the optimizer. Our fix may break code relying on the wrong behavior for
    convergence. We will note such changes in the release notes.

*   **Unused API:** We reserve the right to make backwards incompatible changes
    to APIs for which we find no documented uses (by performing audit of
    TensorFlow usage through GitHub search). Before making any such changes, we
    will announce our intention to make the change on the
    [announce@ mailing list](https://groups.google.com/a/tensorflow.org/forum/#!forum/announce),
    providing instructions for how to address any breakages (if applicable), and
    wait for two weeks to give our community a chance to share their feedback.

*   **Error behavior:** We may replace errors with non-error behavior. For
    instance, we may change a function to compute a result instead of raising an
    error, even if that error is documented. We also reserve the right to change
    the text of error messages. In addition, the type of an error may change
    unless the exception type for a specific error condition is specified in the
    documentation.

<a name="compatibility_of_graphs_and_checkpoints"></a>
## Compatibility of SavedModels, graphs and checkpoints

SavedModel is the preferred serialization format to use in TensorFlow programs.
SavedModels contain two parts: One or more graphs encoded as `GraphDefs` and a
Checkpoint. The graphs describe the data flow of ops to be run, and checkpoints
contain the saved tensor values of variables in a graph.

Many TensorFlow users create SavedModels, and load and execute them with a
later release of TensorFlow. In compliance with [semver](https://semver.org),
SavedModels written with one version of TensorFlow can be loaded and evaluated
with a later version of TensorFlow with the same major release.

We make additional guarantees for *supported* SavedModels. We call a SavedModel
which was created using **only non-deprecated, non-experimental,
non-compatibility APIs** in TensorFlow major version `N` a *SavedModel supported
in version `N`*. Any SavedModel supported in TensorFlow major version `N` can be
loaded and executed with TensorFlow major version `N+1`. However, the
functionality required to build or modify such a model may not be available any
more, so this guarantee only applies to the unmodified SavedModel.

We will endeavor to preserve backwards compatibility as long as possible, so
that the serialized files are usable over long periods of time.

### GraphDef compatibility

Graphs are serialized via the `GraphDef` protocol buffer.  To facilitate
backwards incompatible changes to graphs, each `GraphDef` has a version number
separate from the TensorFlow version.  For example, `GraphDef` version 17
deprecated the `inv` op in favor of `reciprocal`.  The semantics are:

* Each version of TensorFlow supports an interval of `GraphDef` versions. This
  interval will be constant across patch releases, and will only grow across
  minor releases.  Dropping support for a `GraphDef` version will only occur
  for a major release of TensorFlow (and only aligned with the version support
  guaranteed for SavedModels).

* Newly created graphs are assigned the latest `GraphDef` version number.

* If a given version of TensorFlow supports the `GraphDef` version of a graph,
  it will load and evaluate with the same behavior as the TensorFlow version
  used to generate it (except for floating point numerical details and random
  numbers as outlined above), regardless of the major version of TensorFlow.
  In particular, a GraphDef which is compatible with a checkpoint file in one
  version of TensorFlow (such as is the case in a SavedModel) will remain
  compatible with that checkpoint in subsequent versions, as long as the
  GraphDef is supported.

  Note that this applies only to serialized Graphs in GraphDefs (and
  SavedModels): *Code* which reads a checkpoint may not be able to read
  checkpoints generated by the same code running a different version of
  TensorFlow.

* If the `GraphDef` *upper* bound is increased to X in a (minor) release, there
  will be at least six months before the *lower* bound is increased to X.  For
  example (we're using hypothetical version numbers here):

    * TensorFlow 1.2 might support `GraphDef` versions 4 to 7.
    * TensorFlow 1.3 could add `GraphDef` version 8 and support versions 4 to 8.
    * At least six months later, TensorFlow 2.0.0 could drop support for
      versions 4 to 7, leaving version 8 only.

  Note that because major versions of TensorFlow are usually published more than
  6 months apart, the guarantees for supported SavedModels detailed above are
  much stronger than the 6 months guarantee for GraphDefs.

Finally, when support for a `GraphDef` version is dropped, we will attempt to
provide tools for automatically converting graphs to a newer supported
`GraphDef` version.

## Graph and checkpoint compatibility when extending TensorFlow

This section is relevant only when making incompatible changes to the `GraphDef`
format, such as when adding ops, removing ops, or changing the functionality
of existing ops.  The previous section should suffice for most users.

<a id="backward_forward"/>

### Backward and partial forward compatibility

Our versioning scheme has three requirements:

*   **Backward compatibility** to support loading graphs and checkpoints
    created with older versions of TensorFlow.
*   **Forward compatibility** to support scenarios where the producer of a
    graph or checkpoint is upgraded to a newer version of TensorFlow before
    the consumer.
*   Enable evolving TensorFlow in incompatible ways. For example, removing ops,
    adding attributes, and removing attributes.

Note that while the `GraphDef` version mechanism is separate from the TensorFlow
version, backwards incompatible changes to the `GraphDef` format are still
restricted by Semantic Versioning.  This means functionality can only be removed
or changed between `MAJOR` versions of TensorFlow (such as `1.7` to `2.0`).
Additionally, forward compatibility is enforced within Patch releases (`1.x.1`
to `1.x.2` for example).

To achieve backward and forward compatibility and to know when to enforce changes
in formats, graphs and checkpoints have metadata that describes when they
were produced. The sections below detail the TensorFlow implementation and
guidelines for evolving `GraphDef` versions.

### Independent data version schemes

There are different data versions for graphs and checkpoints. The two data
formats evolve at different rates from each other and also at different rates
from TensorFlow. Both versioning systems are defined in
[`core/public/version.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/public/version.h).
Whenever a new version is added, a note is added to the header detailing what
changed and the date.

### Data, producers, and consumers

We distinguish between the following kinds of data version information:
* **producers**: binaries that produce data.  Producers have a version
  (`producer`) and a minimum consumer version that they are compatible with
  (`min_consumer`).
* **consumers**: binaries that consume data.  Consumers have a version
  (`consumer`) and a minimum producer version that they are compatible with
  (`min_producer`).

Each piece of versioned data has a [`VersionDef
versions`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/versions.proto)
field which records the `producer` that made the data, the `min_consumer`
that it is compatible with, and a list of `bad_consumers` versions that are
disallowed.

By default, when a producer makes some data, the data inherits the producer's
`producer` and `min_consumer` versions. `bad_consumers` can be set if specific
consumer versions are known to contain bugs and must be avoided. A consumer can
accept a piece of data if the following are all true:

*   `consumer` >= data's `min_consumer`
*   data's `producer` >= consumer's `min_producer`
*   `consumer` not in data's `bad_consumers`

Since both producers and consumers come from the same TensorFlow code base,
[`core/public/version.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/public/version.h)
contains a main data version which is treated as either `producer` or
`consumer` depending on context and both `min_consumer` and `min_producer`
(needed by producers and consumers, respectively). Specifically,

*   For `GraphDef` versions, we have `TF_GRAPH_DEF_VERSION`,
    `TF_GRAPH_DEF_VERSION_MIN_CONSUMER`, and
    `TF_GRAPH_DEF_VERSION_MIN_PRODUCER`.
*   For checkpoint versions, we have `TF_CHECKPOINT_VERSION`,
    `TF_CHECKPOINT_VERSION_MIN_CONSUMER`, and
    `TF_CHECKPOINT_VERSION_MIN_PRODUCER`.

### Add a new attribute with default to an existing op

Following the guidance below gives you forward compatibility only if the set of
ops has not changed:

1. If forward compatibility is desired, set `strip_default_attrs` to `True`
   while exporting the model using either the
   `tf.saved_model.SavedModelBuilder.add_meta_graph_and_variables`
   and `tf.saved_model.SavedModelBuilder.add_meta_graph`
   methods of the `SavedModelBuilder` class, or
   `tf.estimator.Estimator.export_saved_model`
2. This strips off the default valued attributes at the time of
   producing/exporting the models. This makes sure that the exported
   `tf.MetaGraphDef` does not contain the new op-attribute when the default
   value is used.
3. Having this control could allow out-of-date consumers (for example, serving
   binaries that lag behind training binaries) to continue loading the models
   and prevent interruptions in model serving.

### Evolving GraphDef versions

This section explains how to use this versioning mechanism to make different
types of changes to the `GraphDef` format.

#### Add an op

Add the new op to both consumers and producers at the same time, and do not
change any `GraphDef` versions. This type of change is automatically
backward compatible, and does not impact forward compatibility plan since
existing producer scripts will not suddenly use the new functionality.

#### Add an op and switch existing Python wrappers to use it

1.  Implement new consumer functionality and increment the `GraphDef` version.
2.  If it is possible to make the wrappers use the new functionality only in
    cases that did not work before, the wrappers can be updated now.
3.  Change Python wrappers to use the new functionality. Do not increment
    `min_consumer`, since models that do not use this op should not break.

#### Remove or restrict an op's functionality

1.  Fix all producer scripts (not TensorFlow itself) to not use the banned op or
    functionality.
2.  Increment the `GraphDef` version and implement new consumer functionality
    that bans the removed op or functionality for GraphDefs at the new version
    and above. If possible, make TensorFlow stop producing `GraphDefs` with the
    banned functionality. To do so, add the
    [`REGISTER_OP(...).Deprecated(deprecated_at_version,
    message)`](https://github.com/tensorflow/tensorflow/blob/b289bc7a50fc0254970c60aaeba01c33de61a728/tensorflow/core/ops/array_ops.cc#L1009).
3.  Wait for a major release for backward compatibility purposes.
4.  Increase `min_producer` to the GraphDef version from (2) and remove the
    functionality entirely.

#### Change an op's functionality

1.  Add a new similar op named `SomethingV2` or similar and go through the
    process of adding it and switching existing Python wrappers to use it.
    To ensure forward compatibility use the checks suggested in
    [compat.py](https://www.tensorflow.org/code/tensorflow/python/compat/compat.py)
    when changing the Python wrappers.
2.  Remove the old op (Can only take place with a major version change due to
    backward compatibility).
3.  Increase `min_consumer` to rule out consumers with the old op, add back the
    old op as an alias for `SomethingV2`, and go through the process to switch
    existing Python wrappers to use it.
4.  Go through the process to remove `SomethingV2`.

#### Ban a single unsafe consumer version

1.  Bump the `GraphDef` version and add the bad version to `bad_consumers` for
    all new GraphDefs. If possible, add to `bad_consumers` only for GraphDefs
    which contain a certain op or similar.
2.  If existing consumers have the bad version, push them out as soon as
    possible.
