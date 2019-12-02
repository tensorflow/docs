# 연산 생성하기

Note: C++로 작성한 사용자 정의 연산이 텐서플로 공식 pip 패키지와 ABI 호환되도록 하기 위해서,
[사용자 정의 연산 저장소](https://github.com/tensorflow/custom-op)의 가이드를 따르세요.
저장소에는 사용자 정의 연산 생성과 배포에 필요한 도커 이미지뿐만 아니라 전체(end-to-end) 코드 예제가 있습니다.

기존 텐서플로 라이브러리에서 제공하지 않는 연산을 만들고 싶다면,
먼저, 파이썬 연산이나 함수를 조합해서 파이썬으로 연산을 작성하는 것을 추천합니다.
만약에 그것이 불가능하다면, C++로 사용자 정의 연산을 작성하세요.
다음은 C++로 연산을 작성해야만 하는 몇 가지 이유입니다:

* 기존 연산을 조합해서 연산을 표현하기 쉽지않거나 불가능한 경우
* 기존 기본 연산을 조합해서 연산을 표현하는 것이 효율적이지 않은 경우
* 향후 컴파일러가 융합(fusing)하기 어려운 기본 연산의 조합을 수동으로 하기 원하는 경우

예를 들어, "MaxPool" 연산과 비슷한 "median pooling"과 같은 것을 구현한다고 했을 때,
최대값을 찾는 대신 이동하는 윈도우 안에 포함된 값의 중간값을 찾는 연산을 해야 합니다.
이러한 연산은 다른 연산의 조합(예를 들어, ExtractImagePatches 와 TopK를 사용)으로 해결 할 수 있지만,
그 방식은 단일하고 잘 융합된 연산으로 작성된 네이티브 연산보다는 성능과 메모리 사용에 있어 효율적이지 않을 수 있습니다.
당연히 연산자 조합을 통해서 원하는 것을 표현하려고 시도하는 것이 좋지만,
그것이 어렵고 비효율적인 경우에는 새로운 연산을 추가하는 것이 좋습니다.

사용자 정의 연산을 사용하려면 다음이 필요합니다:

1.  C++파일에 새로운 연산을 등록하세요.
    연산 등록은 구현과 독립적인 연산의 기능에 대한 인터페이스(상세 사양)을 정의하는 것입니다.
    예를 들어, 연산 등록은 연산 이름과 입력 및 출력을 정의하는 것입니다.
    또한, 텐서 형태 추론에 사용될 수 있는 형태 함수를 정의합니다.
2.  C++로 연산을 구현하세요.
    연산 구현은 커널로 알려져 있고 1단계에서 등록한 상세 사양을 충실하게 구현하는 것입니다.
    입/출력 형태 또는 아키텍쳐(예를 들어 CPU, GPU)에 따라 다양한 커널이 있을 수 있습니다.
3.  파이썬 래퍼(wrapper)를 만드세요 (선택).
    이 래퍼는 작성한 연산을 파이썬에서 사용하기 위한 공개용 API입니다.
    기본 래퍼는 연산 등록 과정에서 자동으로 생성되고 그것을 바로 사용하거나 내용을 추가할 수 있습니다.
4.  연산을 위한 그래디언트를 계산할 함수를 작성하세요 (선택).
5.  연산을 테스트하세요.
    편의상 파이썬에서 테스트를 하지만 C++에서 테스트를 할 수 있습니다.
    그래디언트를 정의했다면, 파이썬 `tf.test.compute_gradient_error`를 활용해 검증할 수 있습니다.
    렐루(Relu)와 유사한 연산자의 정방향 함수와 그들의 그래디언트를 테스트하는 예인
    [`relu_op_test.py`](https://www.tensorflow.org/code/tensorflow/python/kernel_tests/relu_op_test.py)를 참고하세요.

### 선행조건

* C++에 익숙
* [텐서플로 실행파일](../../install)이 설치되어 있거나
  [텐서플로 소스를 다운로드](../../install/source.md)해서 그 소스를 설치할 수 있어야 함

## 연산 인터페이스 정의하기

연산 인터페이스를 정의하기 위해서 그 인터페이스를 텐서플로 시스템에 등록해야 합니다.
등록을 위해서는 연산의 이름과 입력(변수형 및 이름), 출력(변수형 및 이름)과 함께
docstrings 및 연산이 요구하는 [속성](#속성)을 명시해야 합니다.

이 동작 과정을 알기 위해, `int32`인 텐서를 입력 받아
첫 번째 원소를 제외한 모든 값을 0으로 설정한 복제본을 출력하는 함수를 만든다고 가정해 봅시다.
이를 위해, `zero_out.cc` 파일을 생성합니다.
그리고 나서 연산 인터페이스를 정의한 `REGISTER_OP` 매크로를 호출하는 소스를 추가합니다:

```c++
#include "tensorflow/core/framework/op.h"
#include "tensorflow/core/framework/shape_inference.h"

using namespace tensorflow;

REGISTER_OP("ZeroOut")
    .Input("to_zero: int32")
    .Output("zeroed: int32")
    .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
      c->set_output(0, c->input(0));
      return Status::OK();
    });
```

`ZeroOut`라는 연산은 32비트 정수형 텐서 `to_zero`를 입력받아서, 32비트 정수형 텐서 `zeroed`를 출력합니다.
또한 연산은 출력 텐서와 입력 텐서가 동일한 형태임을 보장하기 위해 형태 함수를 사용합니다.
예를 들어, 입력이 [10, 20] 형태의 텐서이라면, 형태 함수에서 출력 역시 [10, 20] 형태의 텐서이라고 명시합니다.


> 함수명 관련 주의: 연산 이름은 낙타대문자(CamelCase) 표현식이어야 하고,
> 실행 파일에 등록된 다른 연산과 중복되지 않아야 합니다.

## 연산을 위한 커널 구현하기

인터페이스를 정의한 후, 1개 이상의 연산 구현을 제공해야 합니다.
이런 커널 중 하나를 생성하기 위해서 `Compute` 메서드를 오버라이드한 `OpKernel` 확장 클래스를 생성해야 합니다.
`Compute` 메서드는 `OpKernelContext*` 형태의 `context` 변수를 제공하고,
이 변수를 통해서 입력과 출력 텐서에 대한 유용한 정보에 접근할 수 있습니다.

위에서 생성한 파일에 작성한 커널을 추가하면 그 커널은 다음과 같은 형태일 것입니다:

```c++
#include "tensorflow/core/framework/op_kernel.h"

using namespace tensorflow;

class ZeroOutOp : public OpKernel {
 public:
  explicit ZeroOutOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // 입력 텐서 얻어오기
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<int32>();

    // 출력 텐서 생성하기
    Tensor* output_tensor = NULL;
    OP_REQUIRES_OK(context, context->allocate_output(0, input_tensor.shape(),
                                                     &output_tensor));
    auto output_flat = output_tensor->flat<int32>();

    // 출력 텐서에 첫값만 제외한 나머지 값을 0으로 설정
    const int N = input.size();
    for (int i = 1; i < N; i++) {
      output_flat(i) = 0;
    }

    // 가능하다면, 입력 텐서 첫값을 출력 텐서에 쓰기
    if (N > 0) output_flat(0) = input(0);
  }
};
```

커널을 구현한 후, 텐서플로 시스템에 등록해야 합니다.
등록과정에서 커널을 실행할 수 있는 제한조건을 명시해야 합니다.
예를 들어, 하나의 커널은 CPU에서 동작하도록 만들고 GPU를 위한 커널은 별개로 만들 수 있습니다.

`ZeroOut` 연산에서 이를 위해 다음을 `zero_out.cc`에 추가하세요:

```c++
REGISTER_KERNEL_BUILDER(Name("ZeroOut").Device(DEVICE_CPU), ZeroOutOp);
```

>   중요: OpKernal 인스턴스는 동시에(concurrently) 접근될 수 있습니다.
>   `Compute`는 스레드에 안전(thread-safe) 해야합니다.
>   뮤텍스(mutex)로 클래스 변수에 대한 모든 접근을 보호해야 합니다.
>   아니면 클래스 변수를 통해 상태를 공유하지 마세요!
>   연산 상태를 계속 확인하기 위해서 [`ResourceMgr`](https://www.tensorflow.org/code/tensorflow/core/framework/resource_mgr.h) 사용을 검토해보세요.

### 멀티 쓰레드 CPU 커널

멀티 쓰레드 CPU 커널을 작성하기 위해, [`work_sharder.h`](https://www.tensorflow.org/code/tensorflow/core/util/work_sharder.h)에 있는 Shard 함수를 사용할 수 있습니다.
이 함수는 내부-연산 스레딩을 사용할 수 있도록 설정된 스레드에 계산 함수를 분배합니다
([`config.proto`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config.proto)의 intra_op_parallelism_threads를 참고하세요).

### GPU 커널

GPU 커널 구현은 두 부분으로 구성되어 있습니다: OpKernel과 CUDA 커널 및 관련 실행 코드

OpKernel 구현에서 입력값 검사나 출력을 할당하는 부분은
CPU 커널과 GPU 커널에서 공통적으로 활용되기도 합니다.
이런 경우 제안하는 구현 방식은:

1. 기기와 텐서 변수형을 이용한 템플릿 클래스로 OpKernel을 정의합니다.
2. 실제 결과를 계산하기 위해 Compute 함수는 템플릿 인자로 호출합니다.
3. CPUDevice를 인자로 사용하는 구현은 같은 파일에 정의하지만,
   GPUDevice를 인자로 사용하는 구현은 CUDA 컴파일러에 의해 컴파일되도록 .cu.cc 파일에 정의합니다.

다음은 구현의 예입니다.

```c++
// kernel_example.h
#ifndef KERNEL_EXAMPLE_H_
#define KERNEL_EXAMPLE_H_

template <typename Device, typename T>
struct ExampleFunctor {
  void operator()(const Device& d, int size, const T* in, T* out);
};

#if GOOGLE_CUDA
// 일부에 특화된 GpuDevice를 인자로 사용
template <typename Eigen::GpuDevice, typename T>
struct ExampleFunctor {
  void operator()(const Eigen::GpuDevice& d, int size, const T* in, T* out);
};
#endif

#endif KERNEL_EXAMPLE_H_
```

```c++
// kernel_example.cc
#include "kernel_example.h"
#include "tensorflow/core/framework/op_kernel.h"

using namespace tensorflow;

using CPUDevice = Eigen::ThreadPoolDevice;
using GPUDevice = Eigen::GpuDevice;

// CPU에 특화된 실제 계산
template <typename T>
struct ExampleFunctor<CPUDevice, T> {
  void operator()(const CPUDevice& d, int size, const T* in, T* out) {
    for (int i = 0; i < size; ++i) {
      out[i] = 2 * in[i];
    }
  }
};

// OpKernel 정의
// 템플릿 매개변수 <T>은 텐서 형태
template <typename Device, typename T>
class ExampleOp : public OpKernel {
 public:
  explicit ExampleOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // 입력 텐서 얻어오기
    const Tensor& input_tensor = context->input(0);

    // 출력 텐서 생성하기
    Tensor* output_tensor = NULL;
    OP_REQUIRES_OK(context, context->allocate_output(0, input_tensor.shape(),
                                                     &output_tensor));

    // 계산하기
    OP_REQUIRES(context, input_tensor.NumElements() <= tensorflow::kint32max,
                errors::InvalidArgument("텐서에 데이터 개수가 너무 많음"));
    ExampleFunctor<Device, T>()(
        context->eigen_device<Device>(),
        static_cast<int>(input_tensor.NumElements()),
        input_tensor.flat<T>().data(),
        output_tensor->flat<T>().data());
  }
};

// CPU 커널 등록하기
#define REGISTER_CPU(T)                                          \
  REGISTER_KERNEL_BUILDER(                                       \
      Name("예제").Device(DEVICE_CPU).TypeConstraint<T>("T"),    \
      ExampleOp<CPUDevice, T>);
REGISTER_CPU(float);
REGISTER_CPU(int32);

// GPU 커널 등록하기
#ifdef GOOGLE_CUDA
#define REGISTER_GPU(T)                                          \
  /* kernel_example.cu.cc 에서 명시적 인스턴스화를 선언 */       \
  extern template ExampleFunctor<GPUDevice, T>;                  \
  REGISTER_KERNEL_BUILDER(                                       \
      Name("예제").Device(DEVICE_GPU).TypeConstraint<T>("T"),    \
      ExampleOp<GPUDevice, T>);
REGISTER_GPU(float);
REGISTER_GPU(int32);
#endif  // GOOGLE_CUDA
```

```c++
// kernel_example.cu.cc
#ifdef GOOGLE_CUDA
#define EIGEN_USE_GPU
#include "example.h"
#include "tensorflow/core/util/gpu_kernel_helper.h"

using namespace tensorflow;

using GPUDevice = Eigen::GpuDevice;

// CUDA 커널 정의
template <typename T>
__global__ void ExampleCudaKernel(const int size, const T* in, T* out) {
  for (int i = blockIdx.x * blockDim.x + threadIdx.x; i < size;
       i += blockDim.x * gridDim.x) {
    out[i] = 2 * ldg(in + i);
  }
}

// CUDA 커널을 실행시킬 GPU 구현 정의
template <typename T>
void ExampleFunctor<GPUDevice, T>::operator()(
    const GPUDevice& d, int size, const T* in, T* out) {
  // CUDA 커널 실행
  //
  // 블럭 개수와 블럭당 스레드 개수 계산 예제는
  // core/util/gpu_kernel_helper.h 에서 확인하세요.
  int block_count = 1024;
  int thread_per_block = 20;
  ExampleCudaKernel<T>
      <<<block_count, thread_per_block, 0, d.stream()>>>(size, in, out);
}

// OpKernal에 등록된 변수형에 따른 명시적 인스턴스화
template struct ExampleFunctor<GPUDevice, float>;
template struct ExampleFunctor<GPUDevice, int32>;

#endif  // GOOGLE_CUDA
```

## 연산 라이브러리 빌드하기

### 설치된 컴파일러로 연산 컴파일하기 (텐서플로 실행파일로 설치한 경우)

시스템에 설치된 `g++`이나 `clang`과 같은 `C++` 컴파일러로 `zero_out.cc`을 컴파일 할 수 있습니다.
PIP 패키지 실행 파일은 작성된 연산 컴파일에 필요한 헤더 파일과 라이브러리를 시스템마다 별도의 위치에 설치합니다.
그러나 텐서플로 파이썬 라이브러리는 헤더 파일 저장 경로를 위해 `get_include` 함수를 제공하고,
`get_lib`으로 연결가능한 공유 객체가 포함된 경로를 얻을 수 있습니다.
다음은 우분투가 설치된 기기에서 이 함수들을 실행한 결과입니다.

```bash
$ python
>>> import tensorflow as tf
>>> tf.sysconfig.get_include()
'/usr/local/lib/python2.7/site-packages/tensorflow/include'
>>> tf.sysconfig.get_lib()
'/usr/local/lib/python2.7/site-packages/tensorflow'
```

다음은 `g++`가 설치되어 있을 때 작성한 연산을 동적 라이브러리로 컴파일하는 일련의 명령어입니다.

```bash
TF_CFLAGS=( $(python -c 'import tensorflow as tf; print(" ".join(tf.sysconfig.get_compile_flags()))') )
TF_LFLAGS=( $(python -c 'import tensorflow as tf; print(" ".join(tf.sysconfig.get_link_flags()))') )
g++ -std=c++11 -shared zero_out.cc -o zero_out.so -fPIC ${TF_CFLAGS[@]} ${TF_LFLAGS[@]} -O2
```

Max OS X에서 `.so`을 생성할 때 "-undefined dynamic_lookup"이라는 추가적인 플래그가 필요합니다.

>   `gcc` 버젼이 `>=5`인 경우 주의사항:
>    gcc는 버젼 `5`부터 새로운 C++ [ABI](https://gcc.gnu.org/gcc-5/changes.html#libstdcxx)를 사용합니다.
>    텐서플로 웹사이트에 있는 PIP 패키지 실행 파일은 이전 ABI를 사용하는 `gcc4`로 만들어졌습니다.
>    연산 라이브러리를 `gcc>=5`로 컴파일할 때,
>    이전 ABI와 호환되도록 하기 위해서 명령줄에 `-D_GLIBCXX_USE_CXX11_ABI=0`를 포함해야 합니다.

### 바젤(bazel)로 연산 컴파일하기 (텐서플로 소스로부터 설치한 경우)

텐서플로를 소스로부터 설치했다면, 연산 컴파일을 위한 텐서플로 빌드 시스템을 사용할 수 있습니다.
이를 위해 [`tensorflow/core/user_ops`][user_ops] 디렉토리에 있는 바젤 빌드 규칙에 따라 작성된 BUILD 파일을 생성하세요.

```python
load("//tensorflow:tensorflow.bzl", "tf_custom_op_library")

tf_custom_op_library(
    name = "zero_out.so",
    srcs = ["zero_out.cc"],
)
```

`zero_out.so`를 만들기 위해서 다음 명령어를 실행하세요.

```bash
$ bazel build --config opt //tensorflow/core/user_ops:zero_out.so
```
>   위에서 설명했듯이, gcc>=5로 컴파일하려면 바젤 명령줄에 `--cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"`을 추가하세요.

>   Note: 공유 라이브러리(`.so` 파일)를 만들기 위해 표준인 `cc_library` 방식을 사용할 수 있지만,
>   `tf_custom_op_library` 매크로 사용을 강력히 추천합니다.
>   `tf_custom_op_library`는 추가적으로 요구되는 의존성을 포함하고 있고,
>   생성된 공유 라이브러리가 텐서플로의 플러그인 적재 매커니즘과 호환성을 갖는지 검증합니다.

## 파이썬에서 연산 사용하기

텐서플로 파이썬 API는 동적 라이브러리를 적재하고 텐서플로 프레임워크에 연산을 등록하기 위한
`tf.load_op_library` 함수를 제공합니다.
`load_op_library`는 커널과 연산을 위한 파이썬 랩퍼를 포함한 파이썬 모듈을 돌려줍니다.
그래서, 연산을 만든 후에 파이썬에서 그것을 실행하려면 다음과 같이 할 수 있습니다:

```python
import tensorflow as tf
zero_out_module = tf.load_op_library('./zero_out.so')
with tf.Session(''):
  zero_out_module.zero_out([[1, 2], [3, 4]]).eval()

# 출력
array([[1, 0], [0, 0]], dtype=int32)
```

생성된 함수는 스네이크_케이스(snake\_case)형태 이름으로 주어집니다
([PEP8](https://www.python.org/dev/peps/pep-0008/)를 준수하기 위해).
그래서 작성한 연산 이름이 C++ 파일에서 `ZeroOut`이라면 파이썬 함수는 `zero_out`라는 이름으로 호출됩니다.

연산을 파이썬 모듈에서 불러올 수 있는 일반적인 함수처럼 만들기 위해,
파이썬 소스 파일에서 다음과 같이 `load_op_library`를 호출하는 것이 유용할 수 있습니다:

```python
import tensorflow as tf

zero_out_module = tf.load_op_library('./zero_out.so')
zero_out = zero_out_module.zero_out
```

## 연산 작동 검증하기

작성한 연산이 올바르게 구현됐는지 검증하기 위한 좋은 방법은 테스트를 작성하는 것입니다.
다음 내용과 함께 `zero_out_op_test.py`를 생성하세요:

```python
import tensorflow as tf

class ZeroOutTest(tf.test.TestCase):
  def testZeroOut(self):
    zero_out_module = tf.load_op_library('./zero_out.so')
    with self.test_session():
      result = zero_out_module.zero_out([5, 4, 3, 2, 1])
      self.assertAllEqual(result.eval(), [5, 0, 0, 0, 0])

if __name__ == "__main__":
  tf.test.main()
```

그리고 나서 테스트를 실행하세요(텐서플로는 설치되어 있다고 가정):

```sh
$ python zero_out_op_test.py
```

## 연산에서 고급 기능을 작성하기

이제 기본적인(일부 제약은 있지만) 연산을 만들고 구현하는 법을 알게 됐습니다.
지금부터 연산을 작성하는데 필요한 좀 더 복잡한 기능의 일부를 살펴보려고 합니다.
포함된 내용은 다음과 같습니다:

*   [조건부 검사와 검증](#조건부-검사와-검증)
*   [연산 등록](#연산-등록)
    *   [속성](#속성)
    *   [속성 자료형](#속성-자료형)
    *   [다형성](#다형성)
    *   [입력과 출력](#입력과-출력)
    *   [하위 호환성](#하위-호환성)
*   [GPU 지원](#GPU-지원)
    *   [GPU를 위한 커널 컴파일하기](#GPU를-위한-커널-컴파일하기)
*   [파이썬에서 그래디언트 구현하기](#파이썬에서-그래디언트-구현하기)
*   [C++에서 형태 함수](#C에서-형태-함수)

### 조건부 검사와 검증

위의 예제는 연산을 어떤 형태 텐서에도 활용 가능하다고 가정했습니다.
만약 오직 벡터에만 적용 가능하다면 어떻게 해야할까요?
그것은 다음처럼 OpKernel 구현에 벡터 여부를 확인하는 부분을 추가해야함을 의미합니다.

```c++
  void Compute(OpKernelContext* context) override {
    // 입력 텐서 가져오기
    const Tensor& input_tensor = context->input(0);

    OP_REQUIRES(context, TensorShapeUtils::IsVector(input_tensor.shape()),
                errors::InvalidArgument("ZeroOut는 1-D 벡터이어야 함"));
    // ...
  }
```

추가된 부분은 입력값이 벡터임을 확인하고 벡터가 아니라면 `InvalidArgument`인 상태를 반환합니다.
추가된 [`OP_REQUIRES` 매크로][validation-macros]는 입력값으로 3개를 받습니다:

*   `컨텍스트`, `SetStatus()` 메소드를 위해서 `OpKernelContext` 혹은 `OpKernelConstruction`의 포인터
    ([`tensorflow/core/framework/op_kernel.h`](https://www.tensorflow.org/code/tensorflow/core/framework/op_kernel.h) 참조)
*   상태. 예를 들어, 텐서 형태를 확인하는 함수들은
    [`tensorflow/core/framework/tensor_shape.h`](https://www.tensorflow.org/code/tensorflow/core/framework/tensor_shape.h)에서 확인할 수 있습니다.
*   에러, `Status` 객체로 표현됩니다,
    [`tensorflow/core/lib/core/status.h`](https://www.tensorflow.org/code/tensorflow/core/lib/core/status.h) 참조하세요.
    `Status`는 타입(주로 `InvalidArgument`이지만 타입 종류는 확인하세요)과 메시지를 둘 다 가지고 있습니다.
    에러를 생성하기 위한 함수는
    [`tensorflow/core/lib/core/errors.h`][validation-macros]에서 확인가능합니다.

다른 방법으로 함수에서 반환된 `Status` 객체가 에러인지 확인하고 그것을 반환하기 원한다면
[`OP_REQUIRES_OK`][validation-macros]를 사용하세요.
이 매크로 둘 다 오류시 함수에서 에러를 반환합니다.

### 연산 등록

#### 속성

연산은 그래프에 추가될 때 설정되는 값인 속성을 가질 수 있습니다.
속성은 연산을 설정하는 데 사용되는데, 커널 구현에서 활용되거나
연산 등록에서 입력과 출력의 자료형으로 사용될 수 있습니다.
입력값은 다양하기 때문에 가능하다면 속성 대신에 입력값을 사용하는 것을 선호합니다.
속성은 고정값이고 그래프가 생성되는 시점에 정의되어져야 하기 때문입니다.
반대로 입력은 입력할 때마다 매번 변경될 수 있고 사용자에 의해서 설정할 수 있는 동적으로 변경되는 텐서입니다.
속성은 입력을 활용할 수 없는 경우에 사용됩니다:
서명(입력과 출력의 개수와 자료형)에 영향을 미치거나 매번 변경될 수 없는 어떤 구성.

연산을 등록할 때, `Attr` 메서드를 사용해 다음과 같은 형태로 속성 이름과 자료형을 명시해서 속성을 정의합니다:

```
<name>: <attr-type-expr>
```

`<name>`은 문자로 시작하고 영문자와 밑줄로 구성되고,
`<attr-type-expr>`는 [아래 설명한](#속성-자료형) 형태의 표현식입니다.

예를 들어, `ZeroOut`라는 연산이 0번째 원소가 아닌 사용자 지정 색인에 있는 원소를 보존하고 싶다면,
연산을 다음과 같이 등록할 수 있습니다:
```c++
REGISTER_OP("ZeroOut")
    .Attr("preserve_index: int")
    .Input("to_zero: int32")
    .Output("zeroed: int32");
```

([속성 자료형](#속성-자료형)은 입력과 출력에서 사용하는 `tf.DType`과는 다르다는 것에 주의하세요.)

작성한 커널에서는 생성자의 입력 매개변수인 `context`를 통해서 속성에 접근할 수 있습니다:
```c++
class ZeroOutOp : public OpKernel {
 public:
  explicit ZeroOutOp(OpKernelConstruction* context) : OpKernel(context) {
    // 보존할 원소의 색인 가져오기
    OP_REQUIRES_OK(context,
                   context->GetAttr("preserve_index", &preserve_index_));
    // preserve_index가 양수 인지 확인하기
    OP_REQUIRES(context, preserve_index_ >= 0,
                errors::InvalidArgument("preserve_index >= 0 이어야 함, got ",
                                        preserve_index_));
  }
  void Compute(OpKernelContext* context) override {
    // ...
  }
 private:
  int preserve_index_;
};
```

속성은 `Compute` 메서드에서 다음과 같이 사용됩니다:
```c++
  void Compute(OpKernelContext* context) override {
    // ...

    // 동적으로 변경될 수 있는 입력값을 검증하기 위해서 저장된 속성을 사용합니다
    // 그리고 preserve_index가 입력값 범위안에 있는지 확인합니다
    OP_REQUIRES(context, preserve_index_ < input.dimension(0),
                errors::InvalidArgument("preserve_index 범위 초과"));

    // 출력 텐서의 모든 원소값을 0으로 설정합
    const int N = input.size();
    for (int i = 0; i < N; i++) {
      output_flat(i) = 0;
    }

    // 요청된 입력값을 보존
    output_flat(preserve_index_) = input(preserve_index_);
  }
```

#### 속성 자료형

다음은 속성에서 지원하는 자료형입니다:

* `string`: 바이트(byte)의 연속(UTF8이 필수는 아님).
* `int`: 부호있는 정수.
* `float`: 부동 소수점 숫자.
* `bool`: 참 혹은 거짓.
* `type`: [`DataType`][DataTypeString]의 값(참조가 아닌)중에 하나.
* `shape`: [`TensorShapeProto`][TensorShapeProto].
* `tensor`: [`TensorProto`][TensorProto].
* `list(<type>)`: `<type>` 리스트, `<type>`은 위의 어떤 자료형중 하나.
  `list(list(<type>))`는 유효하지 않습니다 주의하세요.

추가: 최종적인 리스트는 [`op_def_builder.cc:FinalizeAttr`][FinalizeAttr]을 참고하세요.

##### 기본값과 제약사항

속성은 기본값을 가질 수 있고, 일부 속성은 제약사항을 가지고 있습니다.
제약사항이 있는 속성을 정의하기 위해서, 아래의 `<attr-type-expr>`를 사용할 수 있습니다:

* `{'<string1>', '<string2>'}`: 값은 `<string1>` 혹은 `<string2>` 둘 중 하나를 가지는 `string`이여야 합니다.
  이 문법을 사용했을 때 자료형 이름 `string`은 자료형은 암시합니다.
  이러한 문법은 열거형을 모방합니다:

  ```c++
  REGISTER_OP("EnumExample")
      .Attr("e: {'apple', 'orange'}");
  ```

* `{<type1>, <type2>}`: 값은 `type` 자료형이고 `tf.DType`에서 지원하는 `<type1>` 또는 `<type2>` 중에 하나여야 합니다.
  속성 자료형에 `type`을 명시하지 않습니다. 그것은 `{...}`안의 자료형 리스트를 통해 암시됩니다.
  예를 들어, 아래와 같은 경우에 속성 `t`의 자료형은 `int32`과 `float`, `bool` 중에 하나입니다:

  ```c++
  REGISTER_OP("RestrictedTypeExample")
      .Attr("t: {int32, float, bool}");
  ```

* 일반적인 자료형에 대한 제약사항에 대한 몇 가지 단축형이 있습니다:
    * `numbertype`: 숫자(문자나 부울(boolean)형이 아닌)로 제한된 자료형 `type`
    * `realnumbertype`: 복잡한 자료형이 없는 `numbertype`
    * `quantizedtype`: 정량화된(quantized) 숫자 자료형인 `numbertype`

    이러한 것들로 허용된 구체적인 자료형 리스트는
    [`tensorflow/core/framework/types.h`](https://www.tensorflow.org/code/tensorflow/core/framework/types.h)
    에 있는 `NumberTypes()`와 같은 함수에 의해 정의됩니다.
    이 예제에서 속성 `t`는 반드시 숫자 자료형중에 하나여야 합니다.

    ```c++
    REGISTER_OP("NumberType")
        .Attr("t: numbertype");
    ```

    이 연산을 사용하면:

    ```python
    tf.number_type(t=tf.int32)  # 유효
    tf.number_type(t=tf.bool)   # 유효하지 않음
    ```

    리스트는 다른 리스트와 단일 자료형을 결합할 수 있습니다.
    다음 연산은 속성 `t`가 숫자 자료형이나 부울 자료형 중 하나만을 허용합니다:

    ```c++
    REGISTER_OP("NumberOrBooleanType")
        .Attr("t: {numbertype, bool}");
    ```

    이 연산을 사용하면:

    ```python
    tf.number_or_boolean_type(t=tf.int32)  # 유효
    tf.number_or_boolean_type(t=tf.bool)   # 유효
    tf.number_or_boolean_type(t=tf.string) # 유효하지 않음
    ```

* `int >= <n>`: 값은 자연수 `<n>`보다 크거나 같은 정수 자료형이어야 합니다.

  예를 들어, 다음 연산 등록은 속성 `a`가 최소한 `2`보다 큰 값임을 명시합니다:

  ```c++
  REGISTER_OP("MinIntExample")
      .Attr("a: int >= 2");
  ```

* `list(<type>) >= <n>`: `<n>`보다 크거나 같은 길이를 가진 `<type>`의 리스트입니다.

  예를 들어, 다음 연산 등록은 속성 `a`가 `int32` 혹은 `float`의 리스트이고 그 값이 최소한 3보다 큰 값임을 명시합니다:

  ```c++
  REGISTER_OP("TypeListExample")
      .Attr("a: list({int32, float}) >= 3");
  ```

속성에 기본값을 할당하려면(이를 통해 생성된 코드에서 속성을 옵셔널(optional)으로 만들어줌),
다음과 같이 `= <default>`를 끝부분에 추가하세요:

```c++
REGISTER_OP("AttrDefaultExample")
    .Attr("i: int = 0");
```

기본값을 위한 문법은 GraphDef 정의를 결과로 만들어내는 프로토(proto) 표현에 사용될 것입니다.

전체 자료형의 기본값을 명시하는 예:

```c++
REGISTER_OP("AttrDefaultExampleForAllTypes")
   .Attr("s: string = 'foo'")
   .Attr("i: int = 0")
   .Attr("f: float = 1.0")
   .Attr("b: bool = true")
   .Attr("ty: type = DT_INT32")
   .Attr("sh: shape = { dim { size: 1 } dim { size: 2 } }")
   .Attr("te: tensor = { dtype: DT_INT32 int_val: 5 }")
   .Attr("l_empty: list(int) = []")
   .Attr("l_int: list(int) = [2, 3, 5, 7]");
```

특히 `tf.DType`을 사용하는 `type`의 값에 주의하세요.

#### 다형성

##### 자료형 다형성

다양한 자료형을 입력으로 받거나 출력으로 생성하는 연산을 위해,
연산을 등록할 때 [입력과 출력 자료형](#입력과-출력)에 있는 [속성](#속성)을 명시할 수 있습니다.
일반적으로 그런 다음 지원하는 자료형에 맞는 `OpKernel`을 등록할 수 있습니다.

예를 들어 `ZeroOut` 연산이 `float`과 `int32`을 지원하게 하려면, 연산 등록은 다음과 같을 것 입니다:
```c++
REGISTER_OP("ZeroOut")
    .Attr("T: {float, int32}")
    .Input("to_zero: T")
    .Output("zeroed: T");
```

연산 등록에서 입력 자료형은 `float` 혹은 `int32`이어야 한다고 명시했고,
둘 다 `T`인 자료형이기 때문에 출력 자료형은 입력 자료형과 같을 것입니다.

> <a id="naming"></a>명명(naming)에 관한 메모:
> 입력과 출력 그리고 속성 이름은 일반적으로 스네이크_케이스(snake_case)여야 합니다.
> 한가지 예외인 경우는 속성이 입력과 출력의 자료형으로 사용되는 경우입니다.
> 해당 속성의 자료형은 연산이 그래프로 추가될 때 추론될 수 있으므로 연산 함수에서 나타나지 않습니다.
> 예를 들어 최종적으로 정의된 ZeroOut는 다음과 같은 파이썬 함수를 생성할 것입니다:
>
> ```python
> def zero_out(to_zero, name=None):
>   """...
>   Args:
>     to_zero: `Tensor` 다음 자료형 중에 하나여야 함:
>         `float32`, `int32`.
>     name: 작업 이름 (선택).
>
>   Returns:
>     `to_zero`와 같은 자료형인 `Tensor`
>   """
> ```
>
> 만약 `to_zero`로 `int32`인 텐서가 전달된다면 `T`는 자동적으로 `int32`(실제는 `DT_INT32`)로 설정됩니다.
> 이 추론된 속성은 대문자화된 혹은 카멜케이스(CamelCase) 형식의 이름이 사용됩니다.
>
> 이것을 속성 자료형으로 출력 자료형을 결정하는 연산과 비교해 보세요:
>
> ```c++
> REGISTER_OP("StringToNumber")
>     .Input("string_tensor: string")
>     .Output("output: out_type")
>     .Attr("out_type: {float, int32} = DT_FLOAT");
>     .Doc(R"doc(
> 입력 텐서에 있는 문자열을 숫자 자료형으로 변환
> )doc");
> ```
>
> 이 경우, 생성된 파이썬 코드에 사용자가 직접 출력 자료형을 명시해야 합니다:
>
> ```python
> def string_to_number(string_tensor, out_type=None, name=None):
>   """입력 텐서에 있는 문자열을 숫자 자료형으로 변환
>
>   Args:
>     string_tensor: `string` 자료형인 `Tensor`.
>     out_type: `tf.float32, tf.int32` 중에 하나인 `tf.DType` (선택).
>       기본값은 `tf.float32`.
>     name: 작업 이름 (선택).
>
>   Returns:
>     `out_type`로 정의된 자료형인 `Tensor`
>   """
> ```

```c++
#include "tensorflow/core/framework/op_kernel.h"

class ZeroOutInt32Op : public OpKernel {
  // 이전과 같음
};

class ZeroOutFloatOp : public OpKernel {
 public:
  explicit ZeroOutFloatOp(OpKernelConstruction* context)
      : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // 입력 텐서 얻어오기
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<float>();

    // 출력 텐서 생성하기
    Tensor* output = NULL;
    OP_REQUIRES_OK(context,
                   context->allocate_output(0, input_tensor.shape(), &output));
    auto output_flat = output->template flat<float>();

    // 출력 텐서의 모든 값을 0으로 설정하기
    const int N = input.size();
    for (int i = 0; i < N; i++) {
      output_flat(i) = 0;
    }

    // 첫 입력값을 보존하기
    if (N > 0) output_flat(0) = input(0);
  }
};

// 아래 템플릿을 활용한 인스턴스를 생성할 때,
// TypeConstraint<int32>("T")는 속성 "T" (위의 연산 등록에서 정의된)가
// "int32"이여야 함을 나타냅니다
REGISTER_KERNEL_BUILDER(
    Name("ZeroOut")
    .Device(DEVICE_CPU)
    .TypeConstraint<int32>("T"),
    ZeroOutInt32Op);
REGISTER_KERNEL_BUILDER(
    Name("ZeroOut")
    .Device(DEVICE_CPU)
    .TypeConstraint<float>("T"),
    ZeroOutFloatOp);
```

> [하위 호환성](#하위-호환성)을 위해서
> 이미 존재하는 연산의 속성을 추가할 때 [기본값](#기본값과-제약사항) 명시하세요:
>
> ```c++
> REGISTER_OP("ZeroOut")
>   .Attr("T: {float, int32} = DT_INT32")
>   .Input("to_zero: T")
>   .Output("zeroed: T")
> ```

추가 자료형인 `double`을 지원하기 원한다면:
```c++
REGISTER_OP("ZeroOut")
    .Attr("T: {float, double, int32}")
    .Input("to_zero: T")
    .Output("zeroed: T");
```

중복된 구현을 포함한 추가 `OpKernel`을 작성하는 대신에 C++ 템플릿을 주로 사용할 것입니다.
그런 경우라도 오버로드된 자료형마다 커널 등록(`REGISTER_KERNEL_BUILDER` 호출)을 해야합니다.
```c++
template <typename T>
class ZeroOutOp : public OpKernel {
 public:
  explicit ZeroOutOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // 입력 텐서 얻어오기
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<T>();

    // 출력 텐서 생성하기
    Tensor* output = NULL;
    OP_REQUIRES_OK(context,
                   context->allocate_output(0, input_tensor.shape(), &output));
    auto output_flat = output->template flat<T>();

    // 출력 텐서의 모든 값을 0으로 설정하기
    const int N = input.size();
    for (int i = 0; i < N; i++) {
      output_flat(i) = 0;
    }

    // 첫 입력값을 보존하기
    if (N > 0) output_flat(0) = input(0);
  }
};

// 아래 템플릿을 활용한 인스턴스를 생성할 때,
// TypeConstraint<int32>("T")는 속성 "T" (위의 연산 등록에서 정의된)가
// "int32"이여야 함을 나타냅니다
REGISTER_KERNEL_BUILDER(
    Name("ZeroOut")
    .Device(DEVICE_CPU)
    .TypeConstraint<int32>("T"),
    ZeroOutOp<int32>);
REGISTER_KERNEL_BUILDER(
    Name("ZeroOut")
    .Device(DEVICE_CPU)
    .TypeConstraint<float>("T"),
    ZeroOutOp<float>);
REGISTER_KERNEL_BUILDER(
    Name("ZeroOut")
    .Device(DEVICE_CPU)
    .TypeConstraint<double>("T"),
    ZeroOutOp<double>);
```

여러 개의 오버로드가 있다면 매크로로 등록할 수도 있습니다.

```c++
#include "tensorflow/core/framework/op_kernel.h"

#define REGISTER_KERNEL(type)                                       \
  REGISTER_KERNEL_BUILDER(                                          \
      Name("ZeroOut").Device(DEVICE_CPU).TypeConstraint<type>("T"), \
      ZeroOutOp<type>)

REGISTER_KERNEL(int32);
REGISTER_KERNEL(float);
REGISTER_KERNEL(double);

#undef REGISTER_KERNEL
```

커널에 등록하려는 자료형 리스트에 따라,
[`tensorflow/core/framework/register_types.h`][register_types]에서 제공하는 매크로를 사용할 수 있습니다:

```c++
#include "tensorflow/core/framework/op_kernel.h"
#include "tensorflow/core/framework/register_types.h"

REGISTER_OP("ZeroOut")
    .Attr("T: realnumbertype")
    .Input("to_zero: T")
    .Output("zeroed: T");

template <typename T>
class ZeroOutOp : public OpKernel { ... };

#define REGISTER_KERNEL(type)                                       \
  REGISTER_KERNEL_BUILDER(                                          \
      Name("ZeroOut").Device(DEVICE_CPU).TypeConstraint<type>("T"), \
      ZeroOutOp<type>)

TF_CALL_REAL_NUMBER_TYPES(REGISTER_KERNEL);

#undef REGISTER_KERNEL
```

##### 입/출력으로 리스트 사용

다양한 자료형을 수용하거나 생성할 수 있도록 하는 것 뿐만 아니라,
연산은 다양한 개수의 텐서를 사용하거나 생성할 수 있습니다.

다음 예에서, 속성 `T`는 리스트이고 입력 `in`과 출력 `out`의 자료형으로 사용됩니다.
입력과 출력은 텐서의 리스트입니다
(그리고 입력과 출력 모두 자료형이 `T`이기 때문에 출력 텐서 개수와 자료형은 입력과 동일합니다).

```c++
REGISTER_OP("PolymorphicListExample")
    .Attr("T: list(type)")
    .Input("in: T")
    .Output("out: T");
```

리스트에서 사용될 수 있는 자료형을 제한할 수 있습니다.
다음 예에서 입력은 `float`과 `double` 텐서의 리스트입니다.
예를 들어, 연산에 입력에 들어있는 자료형이 `(float, double, float)`이라면
출력 자료형도 `(float, double, float)`이어야 합니다.

```c++
REGISTER_OP("ListTypeRestrictionExample")
    .Attr("T: list({float, double})")
    .Input("in: T")
    .Output("out: T");
```

만약에 리스트안의 모든 텐서 값이 같은 자료형이기 원한다면,
다음과 같이 작성할 수 있습니다:

```c++
REGISTER_OP("IntListInputExample")
    .Attr("N: int")
    .Input("in: N * int32")
    .Output("out: int32");
```

이 예제에서는 `int32`형인 텐서 리스트를 입력받고,
그 리스트의 길이를 명시하기 위해서 `int`형의 속성 `N`을 사용합니다.

이것은 [자료형 다형성](#자료형-다형성)으로도 만들 수 있습니다.
다음 예에서, 입력은 동일한(그러나 명시되지 않은) 자료형(`"T"`)을 가진 텐서 리스트(길이 `"N"`)이고,
출력은 동일한 자료형인 단일 텐서입니다:

```c++
REGISTER_OP("SameListInputExample")
    .Attr("N: int")
    .Attr("T: type")
    .Input("in: N * T")
    .Output("out: T");
```

기본값으로 텐서 리스트는 최소 길이가 1입니다.
[해당 속성에 `">="`제한](#기본값과-제약사항)을 사용해 기본값을 변경할 수 있습니다.
다음 예에서 입력은 길이가 최소 2이상인 `int32` 텐서입니다:

```c++
REGISTER_OP("MinLengthIntListExample")
    .Attr("N: int >= 2")
    .Input("in: N * int32")
    .Output("out: int32");
```

이러한 문법은 `"list(type)"` 속성에도 적용가능합니다:

```c++
REGISTER_OP("MinimumLengthPolymorphicListExample")
    .Attr("T: list(type) >= 3")
    .Input("in: T")
    .Output("out: T");
```

#### 입력과 출력

위의 내용을 요약하자면, 다양한 입력과 출력을 대해서 연산을 등록할 수 있습니다.

```c++
REGISTER_OP("MultipleInsAndOuts")
    .Input("y: int32")
    .Input("z: float")
    .Output("a: string")
    .Output("b: int32");
```

각각의 입력 혹은 출력의 표현식은 다음과 같습니다:

```
<name>: <io-type-expr>
```

위의 `<name>`은 소문자로 시작하고 알파벳 문자와 밑줄로 구성할 수 있습니다.
`<io-type-expr>`는 다음과 같은 자료형 표현식중 하나입니다:

* `<type>`, `<type>`는 지원가능한 입력 자료형 (예 `float`, `int32`, `string`).
  이 경우에는 주어진 자료형의 단일 텐서임을 의미합니다.

  `tf.DType`을 확인하세요.

  ```c++
  REGISTER_OP("BuiltInTypesExample")
      .Input("integers: int32")
      .Input("complex_numbers: complex64");
  ```

* `<attr-type>`, `<attr-type>`은 `type` 혹은 `list(type)` 자료형인 [속성](#속성)의 이름입니다
   (자료형 제한이 가능함). 이 문법에서는 [연산 다형성](#다형성)을 허용합니다.

  ```c++
  REGISTER_OP("PolymorphicSingleInput")
      .Attr("T: type")
      .Input("in: T");

  REGISTER_OP("RestrictedPolymorphicSingleInput")
      .Attr("T: {int32, int64}")
      .Input("in: T");
  ```

  속성이 `list(type)`인 경우에는 텐서 시퀀스임을 의미합니다.

  ```c++
  REGISTER_OP("ArbitraryTensorSequenceExample")
      .Attr("T: list(type)")
      .Input("in: T")
      .Output("out: T");

  REGISTER_OP("RestrictedTensorSequenceExample")
      .Attr("T: list({int32, int64})")
      .Input("in: T")
      .Output("out: T");
  ```

  입력과 출력 모두 자료형이 `T`이기 때문에 출력의 텐서 개수와 자료형은 입력과 동일함을 유의하세요.

* 동일한 자료형을 가지는 텐서 시퀀스:
  `<number> * <type>`으로 표현하고 `<number>`는 `int`형인 [속성](#속성)의 이름입니다.
  `<type>`는 `tf.DType` 혹은 `type`을 표현한 속성 이름일 수 있습니다.
  첫 번째 예처럼, 이 연산은 `int32` 텐서 리스트를 입력받습니다:

  ```c++
  REGISTER_OP("Int32SequenceExample")
      .Attr("NumTensors: int")
      .Input("in: NumTensors * int32")
  ```

  반면에 다음 연산은 동일 자료형만 담을 수 있는 텐서 리스트를 입력받습니다:

  ```c++
  REGISTER_OP("SameTypeSequenceExample")
      .Attr("NumTensors: int")
      .Attr("T: type")
      .Input("in: NumTensors * T")
  ```

* 텐서 참조: `Ref(<type>)`으로 표현하고 `<type>`는 기존 자료형중에 하나입니다.

> 명명시 참고: 입력의 자료형으로 사용된 모든 속성은 유추되어질 것입니다.
> 관습적으로 유추될 속성은 대문자(`T` 혹은 `N`과 같은)를 사용합니다.
> 반면에 입력과 출력, 속성은 함수 매개변수와 같은 이름으로 표현합니다(예 `num_outputs`).
> 자세한 내용은 [명명에 대한 이전 노트](#naming)를 참고하세요.

자세한 내용을 알고 싶다면,
[`tensorflow/core/framework/op_def_builder.h`][op_def_builder]을 참고하세요.

#### 하위 호환성

사용자 정의 연산을 잘 만들었고 다른 사용자에게 공유해 그 연산을 사용하는 고객이 있다고 가정하겠습니다.
그러나, 어떤 식으로든 연산을 변경하고 싶습니다.

일반적으로, 기존에 검토된 사양을 변경하려면 이전 버전과 호환돠어야 합니다:
연산의 명세를 변경하는 것이 이전 명세로 이미 생성된 직렬화 `GraphDef` 프로토콜 버퍼를 깨면 안됩니다.
`GraphDef` 호환성에 대한 상세 내용은 [여기서 확인하세요](./versions.md#compatibility_of_graphs_and_checkpoints).

하위 호환성을 지키기 위한 몇 가지 방법이 있습니다.

1. 연산에 추가되는 어떤 새로운 속성도 정의된 기본값을 가지고 있어야하고,
   연산은 기본값을 사용해 변경 전에 정의된 작동을 해야합니다.
   연산이 다형성을 가지도록 변경하는 경우에도 이전에 정의된 특징을 보존하기 위해 새로운 자료형 속성에 기본값을 주어야 합니다.
   예를 들어 기존 연산이 다음과 같다면:

       REGISTER_OP("MyGeneralUnaryOp")
           .Input("in: float")
           .Output("out: float");

   하위 호환성을 지키면서 다형성을 지원하도록 바꾸려면 다음과 같이 할 수 있습니다:

       REGISTER_OP("MyGeneralUnaryOp")
           .Input("in: T")
           .Output("out: T")
           .Attr("T: numerictype = DT_FLOAT");

2. 속성에 대한 제약을 줄여서 안전하게 만들 수 있습니다.
   예를 들어, `{int32, int64}`을 `{int32, int64, float}` 혹은 `type`으로 변경가능합니다.
   또는, `{"apple", "orange"}`을 `{"apple", "banana", "orange"}` 혹은 `string`으로 변경할 수 있습니다.

3. 리스트의 기본값을 변경 이전과 동일하게 맞춘다면,
   단일 입력/출력을 리스트로된 입력/출력으로 변경할 수 있습니다.

4. 기본값이 없다면, 새로운 입력/출력 리스트룰 추가할 수 있습니다.

5. 새롭게 작성한 연산 이름에 프로젝트마다 고유한 접두어를 붇여서 네임스페이스를 만드세요.
   이를 통해 향후 텐서플로에 포함될 수 있는 연산과 이름이 겹치는 것을 막을 수 있습니다.

6. 계획을 먼저하세요. 연산에 대한 향후 사용을 예측해 보세요.
   어떤 특징은 호환성을 지키면서 변경하기 어려울 수 있습니다.
   (예를 들어, 같은 자료형인 리스트를 다양한 자료형을 가지는 리스트로 만들기)

안전하거나 안전하지 않는 변경에 대한 전체 내용은
[`tensorflow/core/framework/op_compatibility_test.cc`](https://www.tensorflow.org/code/tensorflow/core/framework/op_compatibility_test.cc)에서
찾을 수 있습니다.
만약에 하위 호환성을 확보하기 어렵다면, 그때는 새로운 이름과 의미를 갖는 새로운 연산을 만드세요.

또한 이러한 변경을 `GraphDef` 호환성을 지키면서 유지할 수 있는 동안,
생성되는 파이썬 코드는 이전 버전과 호환되지 않는 방식으로 변경될 수 있음을 주의하세요.
새로운 선택형 파라미터를 추가하는 것을 제외하고 이전 버전의 특징을 유지함으로써,
파이썬 API는 사용자가 파이썬 랩퍼를 신중하게 변경하여 호환성을 유지할 수 있습니다.
일반적으로 호환되지 않는 변경은 텐서플로 메이저 버젼이 변경되고,
[`GraphDef` 버전 의미](./versions.md#compatibility_of_graphs_and_checkpoints)를 준수해야 하는 경우에만 발생합니다.

### GPU 지원

OpKernel을 구현할 때 CPU를 지원하는 것과 GPU를 지원하는 것으로 다르게 구현을 할 수 있고,
이를 [다른 자료형을 위한 커널 등록](#다형성)과 같이 처리할 수 있습니다.
[`tensorflow/core/kernels/`](https://www.tensorflow.org/code/tensorflow/core/kernels/)는
GPU를 지원하는 커널의 예입니다.
어떤 커널은 `.cc`로 끝나는 파일이 CPU버젼이고 `_gpu.cu.cc`로 끝나는 파일이 GPU버젼이고
공통으로 사용하는 코드는 `.h`에서 공유합니다.

예를 들어, `tf.pad`는 GPU 커널을 위한 부분을 제외하고 [`tensorflow/core/kernels/pad_op.cc`][pad_op]에 모든 구현되어 있습니다.
[`tensorflow/core/kernels/pad_op_gpu.cu.cc`](https://www.tensorflow.org/code/tensorflow/core/kernels/pad_op_gpu.cu.cc)에
GPU커널에 관련된 부분이 있고, 공유하는 코드는 템플릿 클래스 형태로
[`tensorflow/core/kernels/pad_op.h`](https://www.tensorflow.org/code/tensorflow/core/kernels/pad_op.h)에 정의되어 있습니다.
코드를 이처럼 관리하는 이유는 2가지입니다:
CPU를 위한 구현과 GPU를 위한 구현에 필요한 공통 코드를 공유할 수 있고
GPU 컴파일러가 컴파일하는 GPU구현 부분만 다른 파일로 분리할 수 있습니다.

추가적으로 알아야할 것은, `pad`의 GPU 커널 버젼이 사용되는 경우에도,
CPU 메모리에 있는 입력인 `"paddings"`이 여전히 필요합니다.
입력과 출력이 CPU에 있다는 것을 표시하기 위해, 커널 등록에서 `HostMemory()` 호출을 추가하세요, 예를 들어:

```c++
#define REGISTER_GPU_KERNEL(T)                         \
  REGISTER_KERNEL_BUILDER(Name("Pad")                  \
                              .Device(DEVICE_GPU)      \
                              .TypeConstraint<T>("T")  \
                              .HostMemory("paddings"), \
                          PadOp<GPUDevice, T>)
```

#### GPU를 위한 커널 컴파일하기

연산을 구현하기 위해 CUDA 커널을 사용하는 예제는
[cuda_op_kernel.cu.cc](https://www.tensorflow.org/code/tensorflow/examples/adding_an_op/cuda_op_kernel.cu.cc)에서 볼 수 있습니다.
`tf_custom_op_library`에는 쿠다 커널(`*.cu.cc` 파일)을 포함하고 있는 소스 파일 리스트를 명시할 수 있는 `gpu_srcs` 매개변수가 있습니다.
텐서플로 설치 파일로 설치한 경우 쿠타 커널은 엔비디아의 `nvcc` 컴파일러로 컴파일 되어야 합니다.
다음은 [cuda_op_kernel.cu.cc](https://www.tensorflow.org/code/tensorflow/examples/adding_an_op/cuda_op_kernel.cu.cc)과
[cuda_op_kernel.cc](https://www.tensorflow.org/code/tensorflow/examples/adding_an_op/cuda_op_kernel.cc)를
한개의 동적 적재 라이브러리로 컴파일하기 위해서 사용된 일련의 명령어입니다:

```bash
nvcc -std=c++11 -c -o cuda_op_kernel.cu.o cuda_op_kernel.cu.cc \
  ${TF_CFLAGS[@]} -D GOOGLE_CUDA=1 -x cu -Xcompiler -fPIC

g++ -std=c++11 -shared -o cuda_op_kernel.so cuda_op_kernel.cc \
  cuda_op_kernel.cu.o ${TF_CFLAGS[@]} -fPIC -lcudart ${TF_LFLAGS[@]}
```

위에서 생성된 `cuda_op_kernel.so`는 파이썬에서 보통 `tf.load_op_library` 함수로 적재할 수 있습니다.

만약에 쿠다 라이브러리가 `/usr/local/lib64`에 설치되어 있지 않다면,
위의 2번째 명령어(g++)에 라이브러리 경로를 명시적으로 추가할 수 있습니다.
예를 들어, 쿠다가 `/usr/local/cuda-8.0`에 설치되어 있다면 `-L /usr/local/cuda-8.0/lib64/`를 추가하세요.

>   일부 리눅스에서는, `nvcc` 컴파일 단계에서 추가적인 설정이 필요합니다.
>   `nvcc` 명령어에서 `mwaitxintrin.h`때문에 생길 수 있는 에러를 피하기 위해 `-D_MWAITXINTRIN_H_INCLUDED`를 추가하세요.

### 파이썬에서 그래디언트 구현하기

연산 그래프가 주어지면, 텐서플로는 기존 연산에 대한 그래디언트를 표현하는 새로운 연산을 추가하기 위해서 자동미분(역전파) 사용합니다.
새로운 연산을 위한 자동 미분 작업을 만들기 위해,
연산 출력에 대한 그래디언트로 주어진 연산 입력에 대한 그래디언트를 계산하기 위한 그래디언트 함수를 등록해야 합니다.

수학적으로, 만약에 연산이 등록된 그래디언트 \\(y = f(x)\\)를 계산하면
연산은 \\(y\\)에 대한 손실 \\(L\\)의 그래디언트 \\(\partial L/ \partial y\\)를
체인룰을 통해 \\(x\\)에 대한 그래디언트 \\(\partial L/ \partial x\\)로 변환합니다:

$$\frac{\partial L}{\partial x}
    = \frac{\partial L}{\partial y} \frac{\partial y}{\partial x}
    = \frac{\partial L}{\partial y} \frac{\partial f}{\partial x}.$$

`ZeroOut`의 경우, 입력에 있는 오직 하나의 값만이 출력에 영향을 미치고,
그래서 입력에 대한 그래디언트는 엉성한 "원 핫" 텐서입니다.
이는 다음과 같이 표현됩니다:

```python
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import sparse_ops

@ops.RegisterGradient("ZeroOut")
def _zero_out_grad(op, grad):
  """`zero_out`의 그래디언트

  매개변수:
    op: 미분하려고 하는 `zero_out` `Operation`,
      원래 연산의 입력과 출력을 찾기 위해서 사용할 수 있음
    grad: `zero_out` 연산의 출력에 대한 그래디언트

  반환:
    `zero_out`의 입력에 대한 그래디언트
  """
  to_zero = op.inputs[0]
  shape = array_ops.shape(to_zero)
  index = array_ops.zeros_like(shape)
  first_grad = array_ops.reshape(grad, [-1])[0]
  to_zero_grad = sparse_ops.sparse_to_dense([index], shape, first_grad, 0)
  return [to_zero_grad]  # 입력이 하나이기 때문에, 한개 텐서로 이뤄진 리스트
```

그래디언트 함수를 등록하기 위한 함수 `tf.RegisterGradient`에 대한 상세내용:

* 하나의 출력을 가지는 연산의 경우, 그래디언트 함수는
  `tf.Operation` `op`과 `tf.Tensor` `grad`을 받아들일 것이고,
  새로운 연산을 텐서 [`op.inputs[i]`](../../api_docs/python/framework.md#Operation.inputs)과
  [`op.outputs[i]`](../../api_docs/python/framework.md#Operation.outputs), `grad`를
  사용하지 않고 생성합니다.
  속성에 대한 정보는 `tf.Operation.get_attr`에서 찾을 수 있습니다.

* 만약 연산 출력이 여러 개라면, 그래디언트 함수는 `op`과 각각 출력에 대한 그래디언트 리스트를 가지는 `grads`을 받아들입니다.
  그래디언트 함수 출력은 각 입력의 그래디언트를 표현하는 텐서 객체 리스트이어야 합니다.

* 만약 어떤 입력에 대해 잘 정의된 그래디언트가 없다면, 인덱스로 사용되는 정수 입력 같은,
  반환되어야 하는 그래디언트는 `None`이어야 합니다.
  예를 들어, 실수형 텐서 `x`와 정수 인덱스 `i`를 입력으로 받아들이는 연산인 경우
  그래디언트 함수는 `return [x_grad, None]`일 것입니다.

* 연산을 위해 의미가 있는 그래디언트가 없다면, 보통 어떤 그래디언트도 등록하지 않을 것이고,
  연산의 그래디언트가 전혀 필요없는 한 그 것은 괜찮을 것입니다.
  어떤 경우에, 연산은 잘 정의된 그래디언트를 가지고 있지 않지만 그래디언트의 계산에 관여될 수 있습니다.
  그런 경우 자동적으로 0을 역전파하기 위해서 `ops.NotDifferentiable`를 사용할 수 있습니다.

그 때 그래디언트 함수가 호출 될 때 텐서 그 자체가 아니라 연산 데이터 흐름 그래프만 사용할 수 있음을 유의하세요.
그래서, 모든 계산은 그래프 실행시간에 실행되기 위해서 다른 텐스플로 연산을 사용해서 수행해야 합니다.

### C++에서 형태 함수

텐서플로 API는 그래프를 실행하지 않아도 텐서 형태에 대한 정보를 제공하는 "형태 추론"이라 불리는 기능을 가지고 있습니다.
형태 추론은 C++ `REGISTER_OP` 선언문에서 각 연산 자료형 등록을 위한 "형태 함수"을 통해서 가능하고,
2가지 규칙을 수행합니다:
그래프 생성하는 동안 입력 형태가 호환되는지 확인하고
출력 형태를 지정합니다.

형태 함수는 `shape_inference::InferenceContext` 클래스에 있는 연산으로 정의되어 있습니다.
예를 들어 ZeroOut을 위한 형태 함수안에는:

```c++
    .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
      c->set_output(0, c->input(0));
      return Status::OK();
    });
```

`c->set_output(0, c->input(0));`가 첫번째 출력 형태는 첫번째 입력의 형태로 설정되어야 함을 선언합니다.
만약에 출력이 위의 예처럼 인덱스에 의해 선택된다면, `set_output`의 두번째 매개변수는 `ShapeHandle` 객체여야 합니다.
기본 생성자로 빈 `ShapeHandle` 객체를 생성할 수 있습니다.
인덱스 `idx`를 갖는 입력을 위한 `ShapeHandle`객체는 `c->input(idx)`에 의해서 얻을 수 있습니다.

많은 연산에서 사용 가능한 몇 가지 공통 형태 함수가 있습니다.
그 중 하나인 `shape_inference::UnchangedShape`는
[common_shape_fns.h](https://www.tensorflow.org/code/tensorflow/core/framework/common_shape_fns.h)에서 찾을 수 있고
다음과 같이 사용됩니다:

```c++
REGISTER_OP("ZeroOut")
    .Input("to_zero: int32")
    .Output("zeroed: int32")
    .SetShapeFn(::tensorflow::shape_inference::UnchangedShape);
```

형태 함수는 입력을 형태를 제한할 수 있습니다.
[`ZeroOut`의 입력을 벡터 형태로 제한한](#조건부-검사와-검증) 버젼의 경우, 형태 함수는 다음과 같을 것입니다:

```c++
    .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
      ::tensorflow::shape_inference::ShapeHandle input;
      TF_RETURN_IF_ERROR(c->WithRank(c->input(0), 1, &input));
      c->set_output(0, input);
      return Status::OK();
    });
```

`WithRank` 호출은 입력 형태 `c->input(0)`가 정확히 1차원인 형태를 가지는지 검증합니다
(또는 만약 입력 형태가 알려지지 않았다면, 출력 형태는 알려지지 않은 차원의 벡터가 될 것입니다).

만약 작성한 연산이 [다양한 입력을 지원하는 다형성](#다형성)을 가진다면,
검사할 형태의 개수를 정하기 위해서 `InferenceContext`의 멤버와
모든 형태가 호환되는지를 검증하기 위해서 `Merge`를 사용할 수 있습니다
(추가로 연산 속성에 접근할 수 있도록 해주는 `InferenceContext::GetAttr`로 길이를 가르키는 속성을 접근할 수 있습니다).

```c++
    .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
      ::tensorflow::shape_inference::ShapeHandle input;
      ::tensorflow::shape_inference::ShapeHandle output;
      for (size_t i = 0; i < c->num_inputs(); ++i) {
        TF_RETURN_IF_ERROR(c->WithRank(c->input(i), 2, &input));
        TF_RETURN_IF_ERROR(c->Merge(output, input, &output));
      }
      c->set_output(0, output);
      return Status::OK();
    });
```

형태 추론은 선택적인 특징이고 텐서의 형태는 매우 다양하기 때문에,
형태 함수는 어떤 입력에 대한 불완전한 형태 정보에도 단단해야(robust) 합니다.
[`InferenceContext`](https://www.tensorflow.org/code/tensorflow/core/framework/shape_inference.h)의
`Merge` 메서드는 둘 중 어느 하나라도 불완전한 정보를 가지더라도 호출자가 두 형태가 같은지 점검할 수 있도록 합니다.
형태 함수는 모든 핵심 텐서플로 연산에 정의되어 있고 다양한 사용 예를 제공합니다.

`InferenceContext` 클래스는 형태 함수 조작을 하는데 사용될 수 있는 다양한 멤버 함수를 가지고 있습니다.
예를 들어, `InferenceContext::Dim`과 `InferenceContext::WithValue`를 이용해서 특정 차원이 매우 특정한 값을 갖는지 검증 할 수 있습니다;
`InferenceContext::Add`과 `InferenceContext::Multiply`를 이용해서 출력 차원이 두 입력 차원의 합/곱인지 검증할 수 있습니다.
다양한 모든 형태 조작을 위한 `InferenceContext` 클래스를 확인하세요.
다음 예는 첫 입력의 형태가 (n, ...)인 경우 첫 출력의 형태를 (n, 3)으로 설정합니다.

```c++
.SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
    c->set_output(0, c->Matrix(c->Dim(c->input(0), 0), 3));
    return Status::OK();
});
```

만약 복잡한 형태 함수가 있다면,
다양한 입력 형태 조합이 기대한 출력 형태 조합을 만들어 내는지 검증하기 위한 테스트를 추가하는 것을 고려해야 합니다.
그러한 테스트를 어떻게 작성하는지에 대한 예는
[core ops tests](https://www.tensorflow.org/code/tensorflow/core/ops/array_ops_test.cc)에서 볼 수 있습니다
(`INFER_OK`과 `INFER_ERROR`의 문법은 약간 애매하지만,
테스트에서 입력과 출력 형태 정의에 대한 표현을 간결하게 하려고 노력해야 합니다.
우선은, 형태의 문자열 사양을 이해하기 위해서 테스트문 주변 주석을 참조하세요).

## 사용자 정의 연산을 위한 pip 패키지 생성하기

작성한 연산으로 `pip` 패키지를 생성히기 위해서,
[tensorflow/custom-op](https://github.com/tensorflow/custom-op) 예를 참고하세요.
이 가이드는 소스로 부터 텐서플로를 생성하는 대신에
텐서플로 pip 패키지로 부터 사용자 정의 연산을 만드는 법을 보여줍니다.

[core-array_ops]:https://www.tensorflow.org/code/tensorflow/core/ops/array_ops.cc
[python-user_ops]:https://www.tensorflow.org/code/tensorflow/python/user_ops/user_ops.py
[tf-kernels]:https://www.tensorflow.org/code/tensorflow/core/kernels/
[user_ops]:https://www.tensorflow.org/code/tensorflow/core/user_ops/
[pad_op]:https://www.tensorflow.org/code/tensorflow/core/kernels/pad_op.cc
[standard_ops-py]:https://www.tensorflow.org/code/tensorflow/python/ops/standard_ops.py
[standard_ops-cc]:https://www.tensorflow.org/code/tensorflow/cc/ops/standard_ops.h
[python-BUILD]:https://www.tensorflow.org/code/tensorflow/python/BUILD
[validation-macros]:https://www.tensorflow.org/code/tensorflow/core/lib/core/errors.h
[op_def_builder]:https://www.tensorflow.org/code/tensorflow/core/framework/op_def_builder.h
[register_types]:https://www.tensorflow.org/code/tensorflow/core/framework/register_types.h
[FinalizeAttr]:https://www.tensorflow.org/code/tensorflow/core/framework/op_def_builder.cc
[DataTypeString]:https://www.tensorflow.org/code/tensorflow/core/framework/types.cc
[python-BUILD]:https://www.tensorflow.org/code/tensorflow/python/BUILD
[types-proto]:https://www.tensorflow.org/code/tensorflow/core/framework/types.proto
[TensorShapeProto]:https://www.tensorflow.org/code/tensorflow/core/framework/tensor_shape.proto
[TensorProto]:https://www.tensorflow.org/code/tensorflow/core/framework/tensor.proto
