description: Public API for tf.io namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.io

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.io namespace.



## Modules

[`gfile`](../tf/io/gfile.md) module: Public API for tf.io.gfile namespace.

## Classes

[`class FixedLenFeature`](../tf/io/FixedLenFeature.md): Configuration for parsing a fixed-length input feature.

[`class FixedLenSequenceFeature`](../tf/io/FixedLenSequenceFeature.md): Configuration for parsing a variable-length input feature into a `Tensor`.

[`class RaggedFeature`](../tf/io/RaggedFeature.md): Configuration for passing a RaggedTensor input feature.

[`class SparseFeature`](../tf/io/SparseFeature.md): Configuration for parsing a sparse input feature from an `Example`.

[`class TFRecordOptions`](../tf/io/TFRecordOptions.md): Options used for manipulating TFRecord files.

[`class TFRecordWriter`](../tf/io/TFRecordWriter.md): A class to write records to a TFRecords file.

[`class VarLenFeature`](../tf/io/VarLenFeature.md): Configuration for parsing a variable-length input feature.

## Functions

[`decode_and_crop_jpeg(...)`](../tf/io/decode_and_crop_jpeg.md): Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`decode_base64(...)`](../tf/io/decode_base64.md): Decode web-safe base64-encoded strings.

[`decode_bmp(...)`](../tf/io/decode_bmp.md): Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`decode_compressed(...)`](../tf/io/decode_compressed.md): Decompress strings.

[`decode_csv(...)`](../tf/io/decode_csv.md): Convert CSV records to tensors. Each column maps to one tensor.

[`decode_gif(...)`](../tf/io/decode_gif.md): Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

[`decode_image(...)`](../tf/io/decode_image.md): Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

[`decode_jpeg(...)`](../tf/io/decode_jpeg.md): Decode a JPEG-encoded image to a uint8 tensor.

[`decode_json_example(...)`](../tf/io/decode_json_example.md): Convert JSON-encoded Example records to binary protocol buffer strings.

[`decode_png(...)`](../tf/io/decode_png.md): Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`decode_proto(...)`](../tf/io/decode_proto.md): The op extracts fields from a serialized protocol buffers message into tensors.

[`decode_raw(...)`](../tf/io/decode_raw.md): Convert raw byte strings into tensors.

[`deserialize_many_sparse(...)`](../tf/io/deserialize_many_sparse.md): Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`encode_base64(...)`](../tf/io/encode_base64.md): Encode strings into web-safe base64 format.

[`encode_jpeg(...)`](../tf/io/encode_jpeg.md): JPEG-encode an image.

[`encode_proto(...)`](../tf/io/encode_proto.md): The op serializes protobuf messages provided in the input tensors.

[`extract_jpeg_shape(...)`](../tf/io/extract_jpeg_shape.md): Extract the shape information of a JPEG-encoded image.

[`is_jpeg(...)`](../tf/io/is_jpeg.md): Convenience function to check if the 'contents' encodes a JPEG image.

[`match_filenames_once(...)`](../tf/io/match_filenames_once.md): Save the list of files matching pattern, so it is only computed once.

[`matching_files(...)`](../tf/io/matching_files.md): Returns the set of files matching one or more glob patterns.

[`parse_example(...)`](../tf/io/parse_example.md): Parses `Example` protos into a `dict` of tensors.

[`parse_sequence_example(...)`](../tf/io/parse_sequence_example.md): Parses a batch of `SequenceExample` protos.

[`parse_single_example(...)`](../tf/io/parse_single_example.md): Parses a single `Example` proto.

[`parse_single_sequence_example(...)`](../tf/io/parse_single_sequence_example.md): Parses a single `SequenceExample` proto.

[`parse_tensor(...)`](../tf/io/parse_tensor.md): Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`read_file(...)`](../tf/io/read_file.md): Reads and outputs the entire contents of the input filename.

[`serialize_many_sparse(...)`](../tf/io/serialize_many_sparse.md): Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

[`serialize_sparse(...)`](../tf/io/serialize_sparse.md): Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

[`serialize_tensor(...)`](../tf/io/serialize_tensor.md): Transforms a Tensor into a serialized TensorProto proto.

[`write_file(...)`](../tf/io/write_file.md): Writes contents to the file at input filename. Creates file and recursively

[`write_graph(...)`](../tf/io/write_graph.md): Writes a graph proto to a file.

