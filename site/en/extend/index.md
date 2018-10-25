# Extend

This section explains how developers can add functionality to TensorFlow's
capabilities. Begin by reading the following architectural overview:

* [TensorFlow Architecture](architecture.md)

The following guides explain how to extend particular aspects of
TensorFlow:

* [Adding a New Op](adding_an_op.md), which explains how to create your own
  operations.
* [Adding a Custom Filesystem Plugin](add_filesys.md), which explains how to
  add support for your own shared or distributed filesystem.
* [Custom Data Readers](new_data_formats.md), which details how to add support
  for your own file and record formats.

Python is currently the only language supported by TensorFlow's API stability
promises. However, TensorFlow also provides functionality in C++, Go, Java and
[JavaScript](https://js.tensorflow.org) (including
[Node.js](https://github.com/tensorflow/tfjs-node)),
plus community support for [Haskell](https://github.com/tensorflow/haskell) and
[Rust](https://github.com/tensorflow/rust). If you'd like to create or
develop TensorFlow features in a language other than these languages, read the
following guide:

* [TensorFlow in Other Languages](language_bindings.md)

To create tools compatible with TensorFlow's model format, read the following
guide:

* [A Tool Developer's Guide to TensorFlow Model Files](./tool_developers/index.md)

XLA (Accelerated Linear Algebra) is an experimental compiler for linear
algebra that optimizes TensorFlow computations. The following guides explore
XLA:

* [XLA Overview](./xla/index.md), which introduces XLA.
* [Broadcasting Semantics](./xla/broadcasting.md), which describes XLA's
  broadcasting semantics.
* [Developing a new back end for XLA](./xla/developing_new_backend.md), which
  explains how to re-target TensorFlow in order to optimize the performance
  of the computational graph for particular hardware.
* [Using JIT Compilation](./xla/jit.md), which describes the XLA JIT compiler that
  compiles and runs parts of TensorFlow graphs via XLA in order to optimize performance.
* [Operation Semantics](./xla/operation_semantics.md), which is a reference manual
  describing the semantics of operations in the `ComputationBuilder` interface.
* [Shapes and Layout](./xla/shapes.md), which details the `Shape` protocol buffer.
* [Using AOT compilation](./xla/tfcompile.md), which explains `tfcompile`, a
  standalone tool that compiles TensorFlow graphs into executable code in order to optimize performance.
