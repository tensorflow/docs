page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.io





Public API for tf.io namespace.

## Classes

[`class FixedLenFeature`](../tf/io/FixedLenFeature): Configuration for parsing a fixed-length input feature.

[`class FixedLenSequenceFeature`](../tf/io/FixedLenSequenceFeature): Configuration for parsing a variable-length input feature into a `Tensor`.

[`class PaddingFIFOQueue`](../tf/io/PaddingFIFOQueue): A FIFOQueue that supports batching variable-sized tensors by padding.

[`class PriorityQueue`](../tf/io/PriorityQueue): A queue implementation that dequeues elements in prioritized order.

[`class QueueBase`](../tf/io/QueueBase): Base class for queue implementations.

[`class RandomShuffleQueue`](../tf/io/RandomShuffleQueue): A queue implementation that dequeues elements in a random order.

[`class SparseFeature`](../tf/io/SparseFeature): Configuration for parsing a sparse input feature from an `Example`.

[`class TFRecordCompressionType`](../tf/io/TFRecordCompressionType): The type of compression for the record.

[`class TFRecordOptions`](../tf/io/TFRecordOptions): Options used for manipulating TFRecord files.

[`class TFRecordWriter`](../tf/io/TFRecordWriter): A class to write records to a TFRecords file.

[`class VarLenFeature`](../tf/io/VarLenFeature): Configuration for parsing a variable-length input feature.

## Functions

[`decode_base64(...)`](../tf/io/decode_base64): Decode web-safe base64-encoded strings.

[`decode_compressed(...)`](../tf/io/decode_compressed): Decompress strings.

[`decode_csv(...)`](../tf/io/decode_csv): Convert CSV records to tensors. Each column maps to one tensor.

[`decode_json_example(...)`](../tf/io/decode_json_example): Convert JSON-encoded Example records to binary protocol buffer strings.

[`decode_raw(...)`](../tf/io/decode_raw): Reinterpret the bytes of a string as a vector of numbers.

[`deserialize_many_sparse(...)`](../tf/io/deserialize_many_sparse): Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`encode_base64(...)`](../tf/io/encode_base64): Encode strings into web-safe base64 format.

[`match_filenames_once(...)`](../tf/io/match_filenames_once): Save the list of files matching pattern, so it is only computed once.

[`matching_files(...)`](../tf/io/matching_files): Returns the set of files matching one or more glob patterns.

[`parse_example(...)`](../tf/io/parse_example): Parses `Example` protos into a `dict` of tensors.

[`parse_sequence_example(...)`](../tf/io/parse_sequence_example): Parses a batch of `SequenceExample` protos.

[`parse_single_example(...)`](../tf/io/parse_single_example): Parses a single `Example` proto.

[`parse_single_sequence_example(...)`](../tf/io/parse_single_sequence_example): Parses a single `SequenceExample` proto.

[`parse_tensor(...)`](../tf/io/parse_tensor): Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`read_file(...)`](../tf/io/read_file): Reads and outputs the entire contents of the input filename.

[`serialize_many_sparse(...)`](../tf/io/serialize_many_sparse): Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

[`serialize_sparse(...)`](../tf/io/serialize_sparse): Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

[`tf_record_iterator(...)`](../tf/io/tf_record_iterator): An iterator that read the records from a TFRecords file.

[`write_file(...)`](../tf/io/write_file): Writes contents to the file at input filename. Creates file and recursively

[`write_graph(...)`](../tf/io/write_graph): Writes a graph proto to a file.

