# Install TensorFlow for Go

TensorFlow provides a
[Go API](https://pkg.go.dev/github.com/tensorflow/tensorflow/tensorflow/go){:.external}—
particularly useful for loading models created with Python and running them
within a Go application.

Caution: The TensorFlow Go API is *not* covered by the TensorFlow
[API stability guarantees](../guide/versions.md).


## Supported Platforms

TensorFlow for Go is supported on the following systems:

* Linux, 64-bit, x86
* macOS, Version 10.12.6 (Sierra) or higher


## Setup

### TensorFlow C library

Install the [TensorFlow C library](./lang_c.md) which is required for the
TensorFlow Go package.

### Download

Download and install the TensorFlow Go package and its dependencies:

<pre class="devsite-terminal devsite-click-to-copy">
go get github.com/tensorflow/tensorflow/tensorflow/go
</pre>

And validate your installation:

<pre class="devsite-terminal devsite-click-to-copy">
go test github.com/tensorflow/tensorflow/tensorflow/go
</pre>


## Build

### Example program

With the TensorFlow Go package installed, create an example program with the
following source code (`hello_tf.go`):

```go
package main

import (
	tf "github.com/tensorflow/tensorflow/tensorflow/go"
	"github.com/tensorflow/tensorflow/tensorflow/go/op"
	"fmt"
)

func main() {
	// Construct a graph with an operation that produces a string constant.
	s := op.NewScope()
	c := op.Const(s, "Hello from TensorFlow version " + tf.Version())
	graph, err := s.Finalize()
	if err != nil {
		panic(err)
	}

	// Execute the graph in a session.
	sess, err := tf.NewSession(graph, nil)
	if err != nil {
		panic(err)
	}
	output, err := sess.Run(nil, []tf.Output{c}, nil)
	if err != nil {
		panic(err)
	}
	fmt.Println(output[0].Value())
}
```

### Run

Run the example program:

<pre class="devsite-terminal devsite-click-to-copy">
go run hello_tf.go
</pre>

The command outputs: <code>Hello from TensorFlow version <em>number</em></code>

Success: The TensorFlow for Go is configured.

The program may generate the following warning messages, which you can ignore:

<pre>
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library
wasn't compiled to use *Type* instructions, but these are available on your
machine and could speed up CPU computations.
</pre>

## Build from source

TensorFlow is open source. Read
[the instructions](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/go/README.md){:.external}
to build TensorFlow for Go from source code.
