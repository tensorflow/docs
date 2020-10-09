# Install TensorFlow Java

[TensorFlow Java](https://github.com/tensorflow/java) can run on any JVM for building, training and 
running machine learning models. It comes with a series of utilities and frameworks that help achieve 
most of the tasks common to data scientists and developers working in this domain. Java and other JVM 
languages, such as Scala or Kotlin, are frequently used in small-to-large enterprises all over the world, 
which makes TensorFlow a strategic choice for adopting machine learning at a large scale.

Caution: The TensorFlow Java API is *not* covered by the TensorFlow
[API stability guarantees](../guide/versions.md).

## Supported Platforms

TensorFlow Java is supported on the following systems:

* Ubuntu 16.04 or higher; 64-bit, x86
* macOS 10.12.6 (Sierra) or higher
* Windows 7 or higher; 64-bit, x86

*Note: To use TensorFlow on Android, see [TensorFlow Lite](https://tensorflow.org/lite)*

## Maven Dependencies

To include TensorFlow in your [Maven](http://maven.apache.org) application, you first need to add in
your project's `pom.xml` file a dependency on a `tensorflow-core-platform` artifact.
```xml
<dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>tensorflow-core-platform${extension}</artifactId>
  <version>0.2.0</version>
</dependency>
```
You can leave the `extension` variable empty to use a vanilla version of TensorFlow or set it to one
of the supported variant:
* `-mkl`: Support for Intel® MKL-DNN on all platforms
* `-gpu`: Support for CUDA® on Linux and Windows platforms
* `-mkl-gpu`: Support for Intel® MKL-DNN and CUDA® on Linux and Windows platforms.

Optionally, you can also add a dependency to the `tensorflow-framework` library, which provides a rich
set of high-level utilities to improve the developer experience with machine learning on the JVM.
```xml
<dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>tensorflow-framework</artifactId>
  <version>0.2.0</version>
</dependency>
```

### Reducing Number of Dependencies

It is important to note that adding a dependency to a `tensorflow-core-platform` artifact will import native 
libraries for all supported platforms, which can increase significantly the size of your project.

When it is already known that your project will only run on a subset of the supported platforms, it is possible
to exclude the artifacts of other platforms using the [Maven Dependency Exclusion](https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html#dependency-exclusions) feature.


### Using Snapshots

TensorFlow Java is also available as snapshots, which reflects that latest changes of the 
[TensorFlow Java Repository](https://github.com/tensorflow/java). To depend on these artifacts, 
you need to make sure that [OSS Sonatype](https://oss.sonatype.org/) Snapshots repository is 
configured in your `pom.xml` as well:

```xml
<repositories>
    <repository>
        <id>tensorflow-snapshots</id>
        <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>org.tensorflow</groupId>
        <artifactId>tensorflow-core-platform</artifactId>
        <version>0.3.0-SNAPSHOT</version>
    </dependency>
</dependencies>
```

## Example Program

This example shows how to build an Apache Maven project with TensorFlow. First,
add the TensorFlow dependency to the project's `pom.xml` file:

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.myorg</groupId>
    <artifactId>hellotensorflow</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
	<!-- Minimal version for compiling with TensorFlow Java is JDK 8 -->
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.tensorflow</groupId>
            <artifactId>tensorflow-core-platform</artifactId>
            <version>0.2.0</version>
        </dependency>
    </dependencies>
</project>
```

Create the source file (`src/main/java/HelloTensorFlow.java`):

```java
import org.tensorflow.ConcreteFunction;
import org.tensorflow.Signature;
import org.tensorflow.Tensor;
import org.tensorflow.TensorFlow;
import org.tensorflow.op.Ops;
import org.tensorflow.op.core.Placeholder;
import org.tensorflow.op.math.Add;
import org.tensorflow.types.TInt32;

public class HelloTensorFlow {

  public static void main(String[] args) throws Exception {
    System.out.println("Running on TensorFlow " + TensorFlow.version());

    try (ConcreteFunction dbl = ConcreteFunction.create(HelloTensorFlow::dbl);
        Tensor<TInt32> x = TInt32.scalarOf(10);
        Tensor<TInt32> dblX = dbl.call(x).expect(TInt32.DTYPE)) {
      System.out.println("Double of " + x.data().getInt() + " is " + dblX.data().getInt());
    }
  }

  private static Signature dbl(Ops tf) {
    Placeholder<TInt32> x = tf.placeholder(TInt32.DTYPE);
    Add<TInt32> dblX = tf.math.add(x, x);
    return Signature.builder().input("x", x).output("dbl", dblX).build();
  }
}
```

Compile and execute:

<pre class="devsite-terminal prettyprint lang-bsh">
mvn -q compile exec:java  # Use -q to hide logging
</pre>

The command outputs: 
```
Running on TensorFlow 2.3.1
Double of 10 is 20
```

Success: TensorFlow Java is configured.

## Building from Source

To build TensorFlow Java from source and possibly customize it, please read the following [instructions](https://github.com/tensorflow/java/blob/master/README.md#building-sources).
