# TensorFlow testing best practices

These are the recommended practices for testing code in the
[TensorFlow repository](https://github.com/tensorflow/tensorflow).

## Before you get started

Before you contribute source code to a TensorFlow project, please review the
`CONTRIBUTING.md` file in the GitHub repo of the project. (For example, see the
[CONTRIBUTING.md file for the core TensorFlow repo](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md).)
All code contributors are required to sign a
[Contributor License Agreement](https://cla.developers.google.com/clas) (CLA).

## General principles

### Only depend on what you use in your BUILD rules

TensorFlow is a large library, and depending on the full package when
writing a unit test for its submodules has been a common practice. However, this
disables the `bazel` dependency-based analysis. This means that continuous
integration systems cannot intelligently eliminate unrelated tests for
presubmit/postsubmit runs. If you only depend on the submodules that you are
testing in your `BUILD` file, you will save time for all TensorFlow developers,
and a lot of valuable computation power.

However, modifying your build dependency to omit the full TF targets brings some
limitations for what you can import in your Python code. You will not be able to
use the `import tensorflow as tf` statement in your unit tests anymore. But this
is a worthwhile tradeoff since as it saves all developers from running thousands
of unnecessary tests.

### All code should have unit tests

For any code you write, you should also write its unit tests. If you write a new
file `foo.py`, you should place its unit tests in `foo_test.py` and submit it
within the same change. Aim for >90% incremental test coverage for all your
code.

### Avoid using native bazel test rules in TF

TF has a lot of subtleties when running tests. We have worked to hide all of
those complexities in our bazel macros. To avoid having to deal with those, use
the following instead of the native test rules. Note that all of these are
defined in `tensorflow/tensorflow.bzl`
For CC tests, use `tf_cc_test`, `tf_gpu_cc_test`, `tf_gpu_only_cc_test`.
For python tests, use `tf_py_test` or `gpu_py_test`.
If you need something really close to the native `py_test` rule, please use the
one defined in tensorflow.bzl instead. You just need to add the following line
at the top of the BUILD file: `load(“tensorflow/tensorflow.bzl”, “py_test”)`

### Be aware where the test executes

When you write a test, our test infra can take care of running your tests on
CPU, GPU and accelerators if you write them accordingly. We have automated tests
that run on Linux, macos, windows, that have systems with or without GPUs. You
simply need to pick one of the macros listed above, and then use tags to limit
where they are executed.

* `manual` tag will exclude your test from running anywhere. This includes
manual test executions that use patterns such as `bazel test tensorflow/…`

* `no_oss` will exclude your test from running in the official TF OSS test
infrastructure.

* `no_mac` or `no_windows` tags can be used to exclude your test from relevant
operating system test suites.
* `no_gpu` tag can be used to exclude your test from running in GPU test suites.

### Verify tests run in expected test suites

TF has quite a few test suites. Sometimes, they may be confusing to set up.
There might be different problems that cause your tests to be omitted from
continuous builds. Thus, you should verify your tests are executing as expected.
To do this:

* Wait for your presubmits on your Pull Request(PR) to run to completion.
* Scroll to the bottom of your PR to see the status checks.
* Click the “Details” link at the right side of any Kokoro check.
* Check the “Targets” list to find your newly added targets.

### Each class/unit should have its own unit test file

Separate test classes help us better isolate failures and resources. They lead
to much shorter and easier to read test files. Therefore, all your Python files
should have at least one corresponding test file (For each `foo.py`, it should
have `foo_test.py`). For more elaborate tests, such as integration tests that
require different setups, it is fine to add more test files.

## Speed and running times

### Sharding should be used as little as possible

Instead of sharding please consider:
* Making your tests smaller
* If the above is not possible, split the tests up

Sharding helps reduce the overall latency of a test, but the same can be
achieved by breaking up tests to smaller targets. Splitting tests gives us a
finer level of control on each test, minimizing unnecessary presubmit runs and
reducing the coverage loss from a buildcop disabling an entire target due to a
misbehaving testcase. Moreover, sharding incurs hidden costs that are not so
obvious, such as running all test initialization code for all shards. This issue
has been escalated to us by infra teams as a source that creates extra load.

### Smaller tests are better

The quicker your tests run, the more likely people will be to run your tests.
One extra second for your test can accumulate to hours of extra time spent
running your test by developers and our infrastructure. Try to make your tests
run under 30 seconds (in non-opt mode!), and make them small. Only mark your
tests as medium as a last resort. The infra does not run any large tests as
presubmits or postsubmits! Therefore, only write a large test if you are going
to arrange where it is going to run. Some tips to make tests run faster:

* Run less iterations of training in your test
* Consider using dependency injection to replace heavy dependencies of system
under test with simple fakes.
* Consider using smaller input data in unit tests
* If nothing else works, try splitting up your test file.

### Test times should aim for half of test size timeout to avoid flakes

With `bazel` test targets, small tests have 1 minute timeouts. Medium test
timeouts are 5 minutes. Large tests are just not executed by the TensorFlow test
infra. However, many tests are not deterministic in the amount of time they
take. For various reasons your tests might take more time every now and then.
And, if you mark a test that runs for 50 seconds on the average as small, your
test will flake if it schedules on a machine with an old CPU. Therefore, aim for
30 second average running time for small tests. Aim for 2 minutes 30 seconds of
average running time for medium tests.

### Reduce the number of samples and increase tolerances for training

Slow running tests deter contributors. Running training in tests can be very
slow. Prefer higher tolerances to be able to use less samples in your tests to
keep your tests sufficiently fast (2.5 minutes max).

## Eliminate non-determinism and flakes

### Write deterministic tests

Unit tests should always be deterministic. All tests running on TAP and guitar
should run the same way every single time, if there is no code change affecting
them. To ensure this, below are some points to consider.

### Always seed any source of stochasticity

Any random number generator, or any other sources of stochasticity can cause
flakiness. Therefore, each of these must be seeded. In addition to making tests
less flaky, this makes all tests reproducible. Different ways to set some seeds
you may need to set in TF tests are:

```python
# Python RNG
import random
random.seed(42)

# Numpy RNG
import numpy as np
np.random.seed(42)

# TF RNG
from tensorflow.python.framework import random_seed
random_seed.set_seed(42)
```

### Avoid using `sleep` in multithreaded tests

Using `sleep` function in tests can be a major cause of flakiness. Especially
when using multiple threads, using sleep to wait for another thread will never
be determistic. This is due to system not being able to guarantee any ordering
of execution of different threads or processes. Therefore, prefer deterministic
synchronization constructs such as mutexes.

### Check if the test is flaky

Flakes cause buildcops and developers to lose many hours. They are difficult to
detect, and they are difficult to debug. Even though there are automated systems
to detect flakiness, they need to accumulate hundreds of test runs before they
can accurately denylist tests. Even when they detect, they denylist your tests
and test coverage is lost. Therefore, test authors should check if their tests
are flaky when writing tests. This can be easily done by running your test with
the flag: `--runs_per_test=1000`

### Use TensorFlowTestCase

TensorFlowTestCase takes necessary precautions such as seeding all random number
generators used to reduce flakiness as much as possible. As we discover and fix
more flakiness sources, these all will be added to TensorFlowTestCase.
Therefore, you should use TensorFlowTestCase when writing tests for tensorflow.
TensorFlowTestCase is defined here: `tensorflow/python/framework/test_util.py`

### Write hermetic tests

Hermetic tests do not need any outside resources. They are packed with
everything they need, and they just start any fake services they might need. Any
services other than your tests are sources for non determinism. Even with 99%
availability of other services, network can flake, rpc response can be delayed,
and you might end up with an inexplicable error message.
Outside services may be, but not limited to, GCS, S3 or any website.
