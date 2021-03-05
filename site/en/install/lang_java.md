# Install TensorFlow Java

[TensorFlow Java](https://github.com/tensorflow/java) can run on any JVM for
building, training and deploying machine learning models. It supports both CPU
and GPU execution, in graph or eager mode, and presents a rich API for using
TensorFlow in a JVM environment. Java and other JVM languages, like Scala and
Kotlin, are frequently used in large and small enterprises all over the world,
which makes TensorFlow Java a strategic choice for adopting machine learning at
a large scale.

Caution: The TensorFlow Java API is *not* covered by the TensorFlow
[API stability guarantees](../guide/versions.md).

## Requirements

TensorFlow Java runs on Java 8 and above, and supports out-of-the-box the
following platforms:

*   Ubuntu 16.04 or higher; 64-bit, x86
*   macOS 10.12.6 (Sierra) or higher; 64-bit, x86
*   Windows 7 or higher; 64-bit, x86

*Note: To use TensorFlow on Android, see
[TensorFlow Lite](https://tensorflow.org/lite)*

## Versions

TensorFlow Java has its own release cycle, independent from the
[TensorFlow runtime](https://github.com/tensorflow/tensorflow). Consequently,
its version does not match the version of TensorFlow runtime it runs on. Consult
the TensorFlow Java
[versioning table](https://github.com/tensorflow/java/#tensorflow-version-support)
to list all versions available and their mapping with the TensorFlow runtime.

## Artifacts

There are
[several ways](https://github.com/tensorflow/java/#using-maven-artifacts) to add
TensorFlow Java to your project. The easiest one is to add a dependency on the
`tensorflow-core-platform` artifact, which includes both the TensorFlow Java
Core API and the native dependencies it requires to run on all supported
platforms.

You can also select one of the following extensions instead of the pure CPU
version:

*   `tensorflow-core-platform-mkl`: Support for Intel® MKL-DNN on all platforms
*   `tensorflow-core-platform-gpu`: Support for CUDA® on Linux and Windows
    platforms
*   `tensorflow-core-platform-mkl-gpu`: Support for Intel® MKL-DNN and CUDA® on
    Linux and Windows platforms.

In addition, a separate dependency on the `tensorflow-framework` library can be
added to benefit from a rich set of utilities for TensorFlow-based machine
learning on the JVM.

## Installing with Maven

To include TensorFlow in your [Maven](http://maven.apache.org) application, add
a dependency on its [artifacts](#artifacts) to your project's `pom.xml` file.
For example,

```xml
<dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>tensorflow-core-platform</artifactId>
  <version>0.2.0</version>
</dependency>
```

### Reducing Number of Dependencies

It is important to note that adding a dependency on a `tensorflow-core-platform`
artifact will import native libraries for all supported platforms, which can
significantly increase the size of your project.

If you wish to target a subset of the available platforms then you can exclude
the unnecessary artifacts from the other platforms using the
[Maven Dependency Exclusion](https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html#dependency-exclusions)
feature.

Another way to select which platforms you want to include in your application is
to set JavaCPP system properties, in your Maven command line or in your
`pom.xml`. Please see JavaCPP
[documentation](https://github.com/bytedeco/javacpp-presets/wiki/Reducing-the-Number-of-Dependencies)
for more details.

### Using Snapshots

The latest TensorFlow Java development snapshots from the TensorFlow Java source
repository are available on the [OSS Sonatype](https://oss.sonatype.org) Nexus
repository. To depend on these artifacts, make sure to configure the OSS
snapshots repository in your `pom.xml`.

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

## Installing with Gradle

To include TensorFlow in your [Gradle](https://gradle.org) application, add a
dependency on its [artifacts](#artifacts) to your project's `build.gradle` file.
For example,

```groovy
repositories {
    mavenCentral()
}

dependencies {
    compile group: 'org.tensorflow', name: 'tensorflow-core-platform', version: '0.2.0'
}
```

### Reducing Number of Dependencies

Excluding native artifacts from TensorFlow Java with Gradle is not as easy as
with Maven. We recommend that you use Gradle JavaCPP plugins to reduce this
number of dependencies.

Please read at Gradle JavaCPP
[documentation](https://github.com/bytedeco/gradle-javacpp) for more details.

## Installing from Sources

To build TensorFlow Java from sources, and possibly customize it, please read
the following
[instructions](https://github.com/tensorflow/java/blob/master/README.md#building-sources).

*Note: Only official builds distributed by TensorFlow are supported by its
maintainers and custom builds should be used at the user's risk.*

# Example Program

This example shows how to build an Apache Maven project with TensorFlow. First,
add the TensorFlow dependency to the project's `pom.xml` file:

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.myorg</groupId>
    <artifactId>hellotensorflow</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <exec.mainClass>HelloTensorFlow</exec.mainClass>
    <!-- Minimal version for compiling TensorFlow Java is JDK 8 -->
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
    <!-- Include TensorFlow (pure CPU only) for all supported platforms -->
        <dependency>
            <groupId>org.tensorflow</groupId>
            <artifactId>tensorflow-core-platform</artifactId>
            <version>0.2.0</version>
        </dependency>
    </dependencies>
</project>
```

Create the source file `src/main/java/HelloTensorFlow.java`:

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
    System.out.println("Hello TensorFlow " + TensorFlow.version());

    try (ConcreteFunction dbl = ConcreteFunction.create(HelloTensorFlow::dbl);
        Tensor<TInt32> x = TInt32.scalarOf(10);
        Tensor<TInt32> dblX = dbl.call(x).expect(TInt32.DTYPE)) {
      System.out.println(x.data().getInt() + " doubled is " + dblX.data().getInt());
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
mvn -q compile exec:java
</pre>

The command prints: <code>TensorFlow version and a simple calculation.</code>

Success! TensorFlow Java is configured.
