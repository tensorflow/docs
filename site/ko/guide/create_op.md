# op 생성하기

Note: 사용자 정의 op가 텐서플로 공식 pip 패키지를 위한 ABI 호환성을 보장하기 위해서,
[사용자 정의 op 저장소](https://github.com/tensorflow/custom-op)의 설명을 따르세요.
저장소에는 사용자 정의 op를 생성하고 배포하기 위해 필요한 도커 이미지뿐만 아니라, 전체(end-to-end) 코드 예제가 있습니다.

기존 텐서플로 라이브러리에서 제공하지 않는 op를 만들고 싶다면,
먼저, 파이썬 op나 함수를 조합해서 파이썬으로 op를 작성하는 것을 추천합니다.
만약에 그것이 불가능하다면, C++로 사용자 정의 op를 작성하세요.
다음은 C++로 op를 작성해야만 하는 몇 가지 이유입니다:

* 작업이 기존 op를 조합해서 표현하기 쉽지않거나 불가능한 경우
* 작업이 기존 기본 연산을 조합해서 사용하는 것이 효율적이지 않은 경우
* 미래의 컴파일러가 어려운 융합(fusing)을 찾기 위해서 기본 연산의 수동 조합하려는 경우

예를 들어, "MaxPool" 연산과 비슷한 "median pooling"과 같은 것을 구현한다고 했을 때,
최대값을 찾는 대신에 이동하는 윈도우안에 포함된 값의 중간값을 찾는 연산을 해야 합니다.
이러한 작업을 다른 연산의 조합(예를 들어, ExtractImagePatches 와 TopK를 사용)으로 해결 할 수 있지만,
그것은 하나의 융합된 연산으로 좀 더 잘 작성된 네이티브 연산처럼 성능이나 메모리 사용에 있어 효율적이지 않을 수 있습니다.
항상 그렇듯, 연산자 조합을 활용해서 원하는 것을 표현하려고 시도하는 것이 좋고,
그것이 어렵고 비효율적인 경우에만 새로운 연산을 추가하는 것이 좋습니다.

사용자 정의 op를 사용하려면 다음이 필요합니다:

1.  C++파일에 새로운 op를 등록하세요.
    Op 등록은 구현과 독립적인 op 기능에 대한 인터페이스(상세 사양)을 정의하는 것입니다.
    예를 들어, op 등록은 op 이름과 입력 및 출력을 정의하는 것입니다.
    또한, 텐서 형태 추론에 사용될 수 있는 형태 함수를 정의합니다.
2.  C++로 op를 구현하세요.
    Op 구현은 커널로 알려져 있고 1단계에서 등록한 상세 사양의 충실한 구현입니다.
    다른 입/출력 형태 또는 아키텍쳐(예를 들어 CPU, GPU)에 따라 다양한 커널이 있을 수 있습니다.
3.  파이썬 래퍼(wrapper)를 만드세요(선택).
    이 래퍼는 파이썬에서 작성된 op를 사용하기 위한 공개용 API 입니다.
    기본 래퍼는 op 등록과정에서 자동으로 생성되고 그것을 바로 사용하거나 내용을 추가할 수 있습니다.
4.  op를 위한 그래디언트를 계산할 함수를 작성하세요(선택).
5.  op를 테스트하세요.
    편의상 파이썬에서 테스트를 하지만 C++에서 테스트를 할 수 있습니다.
    그래디언트를 정의했다면, 파이썬 `tf.test.compute_gradient_error`를 활용해 검증할 수 있습니다.
    렐루(Relu)와 유사한 연산자의 정방향 함수와 그들의 그래디언트를 테스트하는 예인
    [`relu_op_test.py`](https://www.tensorflow.org/code/tensorflow/python/kernel_tests/relu_op_test.py)를 참고하세요.

### 선행조건

* C++에 익숙
* [텐서플로 실행파일](../../install)이 설치되어 있거나
  [텐서플로 소스를 다운로드](../../install/source.md)해서 그 소스를 설치할 수 있어야 함

## op 인터페이스 정의하기

op 인터페이스를 정의하기 위해서는 그 인터페이스를 텐서플로 시스템에 등록해야 합니다.
등록을 위해서는 op의 이름과 입력(변수형 및 이름), 출력(변수형 및 이름)과 함께
docstrings 및 op가 요구하는 [속성](#attrs)을 명시해야합니다.

이 동작과정을 알기 위해, 입력으로 `int32`인 텐서를 받아서
첫번째 요소를 제외한 모든 값을 0으로 설정한 복제본을 춢력하는 함수를 만든다고 가정해 봅시다.
이를 위해, `zero_out.cc` 파일을 생성합니다.
그리고 나서 op 인터페이스를 정의한 `REGISTER_OP` 매크로를 호출하는 소스를 추가합니다:

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

`ZeroOut`라는 op는 32비트 정수형 텐서 `to_zero`를 입력받아서, 32비트 정수형 텐서 `zeroed` 를 출력합니다.
또한 출력 텐서가 입력 텐서와 동일한 형태임을 보장하기 위해서 형태 함수를 사용합니다.
예를 들어, 입력이 [10, 20] 형태의 텐서이라면, 형태 함수에서 출력 역시 [10, 20] 형태의 텐서이라고 명시합니다.


> 함수명 관련 주의: op 이름은 낙타대문자(CamelCase) 표현식이어야 하고,
> 실행 파일에 등록된 다른 op와 중복되지 않아야 합니다.

## op를 위한 커널 구현하기

인터페이스를 정의한 후, 1개 이상의 op 구현를 제공해야 합니다.
이런 커널 중 하나를 생성하기 위해서 `Compute` 메서드를 오버라이드한 `OpKernel` 확장 클래스를 생성해야 합니다.
`Compute` 메서드는 `OpKernelContext*` 형태의 `context` 변수를 제공하고,
이 변수를 통해서 입력과 출력 텐서와 같은 유용한 정보에 접근할 수 있습니다.

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
예를 들어, 커널 하나를 CPU에서 동작하도록 만들고 GPU를 위한 커널은 별개로 만들 수 있습니다.

`ZeroOut` op에서 이를 위해 `zero_out.cc`에 다음을 추가하세요:

```c++
REGISTER_KERNEL_BUILDER(Name("ZeroOut").Device(DEVICE_CPU), ZeroOutOp);
```

>   중요: OpKernal 인스턴스는 동시에(concurrently) 접근될 수 있습니다.
>   `Compute`는 스레드에 안전(thread-safe) 해야합니다.
>   뮤텍스(mutex)로 클래스 변수에 대한 어떤 접근도 보호해야합니다.
>   아니면 클래스 변수를 통해 상태를 공유하지 마세요!
>   op 상태를 계속 확인하기 위해서 [`ResourceMgr`](https://www.tensorflow.org/code/tensorflow/core/framework/resource_mgr.h) 사용을 검토해보세요.

### 멀티 쓰레드 CPU 커널

멀티 쓰레드 CPU 커널을 작성하기 위해, [`work_sharder.h`](https://www.tensorflow.org/code/tensorflow/core/util/work_sharder.h)에 있는 Shard 함수를 사용할 수 있습니다.
이 함수는 내부-op 스레딩을 사용할 수 있도록 설정된 스레드에 계산 함수를 분배합니다
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

## op 라이브러리 빌드하기

### 설치된 컴파일러로 op 컴파일하기 (텐서플로 실행파일을 설치한 경우)

시스템에 설치된 `g++`이나 `clang`과 같은 `C++` 컴파일러로 `zero_out.cc`을 컴파일 할 수 있습니다.
PIP 패키지 실행 파일은 작성된 op를 컴파일하기 위해 필요한 헤더 파일과 라이브러리를 시스템마다 별도의 위치에 설치합니다.
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

`g++`가 설치되어 있다면, 다음은 작성한 op를 동적 라이브러리와 함께 컴파일하는 일련의 명령어입니다.

```bash
TF_CFLAGS=( $(python -c 'import tensorflow as tf; print(" ".join(tf.sysconfig.get_compile_flags()))') )
TF_LFLAGS=( $(python -c 'import tensorflow as tf; print(" ".join(tf.sysconfig.get_link_flags()))') )
g++ -std=c++11 -shared zero_out.cc -o zero_out.so -fPIC ${TF_CFLAGS[@]} ${TF_LFLAGS[@]} -O2
```

Max OS X에서는 `.so`을 생성할 때 "-undefined dynamic_lookup"이라는 추가적인 플래그가 필요합니다.

>   `gcc` 버젼이 `>=5`인 경우 주의사항:
>    gcc는 버젼 `5`부터 새로운 C++ [ABI](https://gcc.gnu.org/gcc-5/changes.html#libstdcxx)를 사용합니다.
>    텐서플로 웹사이트에 있는 PIP 패키지 실행 파일은 이전 ABI를 사용하는 `gcc4`로 만들어졌습니다.
>    op 라이브러리를 `gcc>=5`로 컴파일할 때,
>    이전 ABI와 호환되기 위해서는 `-D_GLIBCXX_USE_CXX11_ABI=0`를 명령 줄에 포함해야 합니다.

### 바젤(bazel)로 op 컴파일하기 (텐서플로 소스로부터 설치한 경우)

텐서플로를 소스로부터 설치했다면, op 컴파일을 위해 텐서플로 빌드 시스템을 사용할 수 있습니다.
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

## 파이썬에서 op 사용하기

텐서플로 파이썬 API는 동적 라이브러리를 적재하고 텐서플로 프레임워크에 op를 등록하기 위한
`tf.load_op_library` 함수를 제공합니다.
`load_op_library`는 커널과 op를 위한 파이썬 랩퍼를 포함한 파이썬 모듈을 돌려줍니다.
그래서, op를 만들었고 파이썬에서 그것을 실행하려면 다음과 같이 할 수 있습니다:

```python
import tensorflow as tf
zero_out_module = tf.load_op_library('./zero_out.so')
with tf.Session(''):
  zero_out_module.zero_out([[1, 2], [3, 4]]).eval()

# 출력
array([[1, 0], [0, 0]], dtype=int32)
```

생성된 함수는 스네이크 케이스(snake\_case)형태 이름으로 주어집니다.
([PEP8](https://www.python.org/dev/peps/pep-0008/)를 준수하기 위해서).
그래서 작성한 op 이름이 C++ 파일에서 `ZeroOut`이라면 파이썬 함수는 `zero_out`라는 이름으로 호출됩니다.

op를 파이썬 모듈에서 임포트(import)할 수 있는 일반적인 함수처럼 만들기 위해,
파이썬 소스 파일에서 다음과 같이 `load_op_library`를 호출하는 것이 유용할 수 있습니다:

```python
import tensorflow as tf

zero_out_module = tf.load_op_library('./zero_out.so')
zero_out = zero_out_module.zero_out
```

## op 작동 검증하기

작성한 op가 올바르게 구현됐는지 검증하기 위한 좋은 방법은 테스트를 작성하는 것입니다.
테스트를 위한 내용과 함께 `zero_out_op_test.py`를 생성하세요:

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

## op에서 고급 기능을 작성하기

이제 기본적인(일부 제약은 있지만) op와 구현을 작성하는 방법을 알게됐습니다.
지금부터 op를 작성하는데 필요한 좀 더 복잡한 기능의 일부를 살펴보려고 합니다.
다음을 포함합니다:

*   [조건부 검사와 검증](#conditional-checks-and-validation)
*   [Op 등록](#op-registration)
    *   [속성](#attrs)
    *   [속성 형태](#attr-types)
    *   [다형성](#polymorphism)
    *   [입력과 출력](#inputs-and-outputs)
    *   [이전 버전과의 호환성](#backwards-compatibility)
*   [GPU 지원](#gpu-support)
    *   [GPU기기를 위한 커널 컴파일하기](#compiling-the-kernel-for-the-gpu-device)
*   [파이썬에서 그래디언크 구현하기](#implement-the-gradient-in-python)
*   [C++에서 형태 함수](#shape-functions-in-c)

### 조건부 검사와 검증

다음 예제는 op가 어떤 형태 텐서에도 적용 가능하다고 가정했습니다.
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

*   `컨텍스트`, `SetStatus()` 메소드를 위해서 `OpKernelContext` 혹은 `OpKernelConstruction`의 포인터 (
    [`tensorflow/core/framework/op_kernel.h`](https://www.tensorflow.org/code/tensorflow/core/framework/op_kernel.h) 참조)
*   상태. 예를 들어, 텐서 형태를 확인하는 함수들은
    [`tensorflow/core/framework/tensor_shape.h`](https://www.tensorflow.org/code/tensorflow/core/framework/tensor_shape.h)에서 확인할 수 있습니다.
*   에러, `Status` 객체로 표현됩니다,
    [`tensorflow/core/lib/core/status.h`](https://www.tensorflow.org/code/tensorflow/core/lib/core/status.h) 참조하세요.
    `Status`는 타입(주로 `InvalidArgument` 이지만 타입 종류는 확인하세요)과 메시지를 둘 다 가지고 있습니다.
    에러를 생성하기 위한 함수는
    [`tensorflow/core/lib/core/errors.h`][validation-macros]에서 확인가능합니다.

다른 방법으로 함수에서 반환된 `Status` 객체가 에러인지 확인하고 그것을 반환하기 원한다면
[`OP_REQUIRES_OK`][validation-macros]를 사용하세요.
이 매크로 둘 다 오류시 함수에서 에러를 반환합니다.

### Op 등록

#### 속성

Op는 그래프에 추가될 때 설정되는 값인 속성을 가질 수 있습니다.
속성은 op를 설정하는 데 사용되고, 그 값은 커널 구현에서 활용되거나
op 등록에서 입력과 출력의 자료형으로 사용될 수 있습니다.
입력값은 다양하기 때문에 가능하다면 속성 대신에 입력값을 사용하는 것을 선호합니다.
속성은 고정값이고 그래프가 생성되는 시점에 정의되어야 하기 때문입니다.
반대로 입력인 텐서는 동적으로 변할 수 있습니다.
즉, 입력이 매번 변경될 수 있고 사용자에 의해서 설정할 수 있습니다.
속성은 입력을 활용할 수 없는 경우에 사용됩니다:
서명(입력과 출력의 개수와 자료형)에 영향을 미치거나 매번 변경될 수 없는 어떤 구성.

op를 등록할 때, `Attr` 메서드를 사용해 다음과 같은 형태로 속성 이름과 자료형을 명시해서 속성을 정의합니다:

```
<이름>: <속성-자료형-표현식>
```

`<이름>`은 문자로 시작하고 영문자와 밑줄로 구성되고,
`<속성-타입-표현식>`는 [아래 설명한](#attr_types) 형태의 표현식입니다.

예를 들어, `ZeroOut`라는 op가 0번째 원소가 아닌 사용자 지정 색인에 있는 원소를 보존하고 싶다면,
op를 다음과 같이 등록할 수 있습니다:
```c++
REGISTER_OP("ZeroOut")
    .Attr("preserve_index: int")
    .Input("to_zero: int32")
    .Output("zeroed: int32");
```

([속성 자료형](#attr_types)은 입력과 출력에서 사용하는 `tf.DType`과는 다르다는 것에 주의하세요.)

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
제약사항이 있는 속성을 정의하기 위해서, 아래의 `<속성-자료형-표현식>`를 사용할 수 있습니다:

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

* 공통의 자료형 제약사항을 위한 몇 가지 단축형이 있습니다:
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

    이 op를 사용하면:

    ```python
    tf.number_type(t=tf.int32)  # 유효
    tf.number_type(t=tf.bool)   # 유효하지 않음
    ```

    리스트는 다른 리스트와 단일 자료형을 결합할 수 있습니다.
    다음 op는 속성 `t`가 숫자 자료형이나 부울 자료형 중 하나만을 허용합니다:

    ```c++
    REGISTER_OP("NumberOrBooleanType")
        .Attr("t: {numbertype, bool}");
    ```

    이 op를 사용하면:

    ```python
    tf.number_or_boolean_type(t=tf.int32)  # 유효
    tf.number_or_boolean_type(t=tf.bool)   # 유효
    tf.number_or_boolean_type(t=tf.string) # 유효하지 않음
    ```

* `int >= <n>`: 값은 자연수 `<n>`보다 크거나 같은 정수 자료형이어야 합니다.

  예를 들어, 다음 op 등록은 속성 `a`가 최소한 `2`보다 큰 값임을 명시합니다:

  ```c++
  REGISTER_OP("MinIntExample")
      .Attr("a: int >= 2");
  ```

* `list(<type>) >= <n>`: `<n>`보다 크거나 같은 길이를 가진 `<type>`의 리스트입니다.

  예를 들어, 다음 op 등록은 속성 `a`가 `int32` 혹은 `float`의 리스트이고 그값이 최소한 3보다 큰 값임을 명시합니다:

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

#### Polymorphism

##### Type polymorphism

For ops that can take different types as input or produce different output
types, you can specify [an attr](#attrs) in
[an input or output type](#inputs-and-outputs) in the op registration.  Typically
you would then register an `OpKernel` for each supported type.

For instance, if you'd like the `ZeroOut` op to work on `float`s
in addition to `int32`s, your op registration might look like:
```c++
REGISTER_OP("ZeroOut")
    .Attr("T: {float, int32}")
    .Input("to_zero: T")
    .Output("zeroed: T");
```

Your op registration now specifies that the input's type must be `float`, or
`int32`, and that its output will be the same type, since both have type `T`.

> <a id="naming"></a>A note on naming: Inputs, outputs, and attrs generally should be
> given snake\_case names.  The one exception is attrs that are used as the type
> of an input or in the type of an input. Those attrs can be inferred when the
> op is added to the graph and so don't appear in the op's function.  For
> example, this last definition of ZeroOut will generate a Python function that
> looks like:
>
> ```python
> def zero_out(to_zero, name=None):
>   """...
>   Args:
>     to_zero: A `Tensor`. Must be one of the following types:
>         `float32`, `int32`.
>     name: A name for the operation (optional).
>
>   Returns:
>     A `Tensor`. Has the same type as `to_zero`.
>   """
> ```
>
> If `to_zero` is passed an `int32` tensor, then `T` is automatically set to
> `int32` (well, actually `DT_INT32`). Those inferred attrs are given
> Capitalized or CamelCase names.
>
> Compare this with an op that has a type attr that determines the output
> type:
>
> ```c++
> REGISTER_OP("StringToNumber")
>     .Input("string_tensor: string")
>     .Output("output: out_type")
>     .Attr("out_type: {float, int32} = DT_FLOAT");
>     .Doc(R"doc(
> Converts each string in the input Tensor to the specified numeric type.
> )doc");
> ```
>
> In this case, the user has to specify the output type, as in the generated
> Python:
>
> ```python
> def string_to_number(string_tensor, out_type=None, name=None):
>   """Converts each string in the input Tensor to the specified numeric type.
>
>   Args:
>     string_tensor: A `Tensor` of type `string`.
>     out_type: An optional `tf.DType` from: `tf.float32, tf.int32`.
>       Defaults to `tf.float32`.
>     name: A name for the operation (optional).
>
>   Returns:
>     A `Tensor` of type `out_type`.
>   """
> ```

```c++
#include "tensorflow/core/framework/op_kernel.h"

class ZeroOutInt32Op : public OpKernel {
  // as before
};

class ZeroOutFloatOp : public OpKernel {
 public:
  explicit ZeroOutFloatOp(OpKernelConstruction* context)
      : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // Grab the input tensor
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<float>();

    // Create an output tensor
    Tensor* output = NULL;
    OP_REQUIRES_OK(context,
                   context->allocate_output(0, input_tensor.shape(), &output));
    auto output_flat = output->template flat<float>();

    // Set all the elements of the output tensor to 0
    const int N = input.size();
    for (int i = 0; i < N; i++) {
      output_flat(i) = 0;
    }

    // Preserve the first input value
    if (N > 0) output_flat(0) = input(0);
  }
};

// Note that TypeConstraint<int32>("T") means that attr "T" (defined
// in the op registration above) must be "int32" to use this template
// instantiation.
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

> To preserve [backwards compatibility](#backwards-compatibility), you should
> specify a [default value](#default-values-constraints) when adding an attr to
> an existing op:
>
> ```c++
> REGISTER_OP("ZeroOut")
>   .Attr("T: {float, int32} = DT_INT32")
>   .Input("to_zero: T")
>   .Output("zeroed: T")
> ```

Let's say you wanted to add more types, say `double`:
```c++
REGISTER_OP("ZeroOut")
    .Attr("T: {float, double, int32}")
    .Input("to_zero: T")
    .Output("zeroed: T");
```

Instead of writing another `OpKernel` with redundant code as above, often you
will be able to use a C++ template instead.  You will still have one kernel
registration (`REGISTER_KERNEL_BUILDER` call) per overload.
```c++
template <typename T>
class ZeroOutOp : public OpKernel {
 public:
  explicit ZeroOutOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // Grab the input tensor
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<T>();

    // Create an output tensor
    Tensor* output = NULL;
    OP_REQUIRES_OK(context,
                   context->allocate_output(0, input_tensor.shape(), &output));
    auto output_flat = output->template flat<T>();

    // Set all the elements of the output tensor to 0
    const int N = input.size();
    for (int i = 0; i < N; i++) {
      output_flat(i) = 0;
    }

    // Preserve the first input value
    if (N > 0) output_flat(0) = input(0);
  }
};

// Note that TypeConstraint<int32>("T") means that attr "T" (defined
// in the op registration above) must be "int32" to use this template
// instantiation.
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

If you have more than a couple overloads, you can put the registration in a
macro.

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

Depending on the list of types you are registering the kernel for, you may be
able to use a macro provided by
[`tensorflow/core/framework/register_types.h`][register_types]:

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

##### List inputs and outputs

In addition to being able to accept or produce different types, ops can consume
or produce a variable number of tensors.

In the next example, the attr `T` holds a *list* of types, and is used as the
type of both the input `in` and the output `out`.  The input and output are
lists of tensors of that type (and the number and types of tensors in the output
are the same as the input, since both have type `T`).

```c++
REGISTER_OP("PolymorphicListExample")
    .Attr("T: list(type)")
    .Input("in: T")
    .Output("out: T");
```

You can also place restrictions on what types can be specified in the list. In
this next case, the input is a list of `float` and `double` tensors. The op
accepts, for example, input types `(float, double, float)` and in that case the
output type would also be `(float, double, float)`.

```c++
REGISTER_OP("ListTypeRestrictionExample")
    .Attr("T: list({float, double})")
    .Input("in: T")
    .Output("out: T");
```

If you want all the tensors in a list to be of the same type, you might do
something like:

```c++
REGISTER_OP("IntListInputExample")
    .Attr("N: int")
    .Input("in: N * int32")
    .Output("out: int32");
```

This accepts a list of `int32` tensors, and uses an `int` attr `N` to
specify the length of the list.

This can be made [type polymorphic](#type-polymorphism) as well.  In the next
example, the input is a list of tensors (with length `"N"`) of the same (but
unspecified) type (`"T"`), and the output is a single tensor of matching type:

```c++
REGISTER_OP("SameListInputExample")
    .Attr("N: int")
    .Attr("T: type")
    .Input("in: N * T")
    .Output("out: T");
```

By default, tensor lists have a minimum length of 1. You can change that default
using
[a `">="` constraint on the corresponding attr](#default-values-constraints).
In this next example, the input is a list of at least 2 `int32` tensors:

```c++
REGISTER_OP("MinLengthIntListExample")
    .Attr("N: int >= 2")
    .Input("in: N * int32")
    .Output("out: int32");
```

The same syntax works with `"list(type)"` attrs:

```c++
REGISTER_OP("MinimumLengthPolymorphicListExample")
    .Attr("T: list(type) >= 3")
    .Input("in: T")
    .Output("out: T");
```

#### Inputs and outputs

To summarize the above, an op registration can have multiple inputs and outputs:

```c++
REGISTER_OP("MultipleInsAndOuts")
    .Input("y: int32")
    .Input("z: float")
    .Output("a: string")
    .Output("b: int32");
```

Each input or output spec is of the form:

```
<name>: <io-type-expr>
```

where `<name>` begins with a letter and can be composed of alphanumeric
characters and underscores. `<io-type-expr>` is one of the following type
expressions:

* `<type>`, where `<type>` is a supported input type (e.g. `float`, `int32`,
  `string`). This specifies a single tensor of the given type.

  See
  `tf.DType`.

  ```c++
  REGISTER_OP("BuiltInTypesExample")
      .Input("integers: int32")
      .Input("complex_numbers: complex64");
  ```

* `<attr-type>`, where `<attr-type>` is the name of an [Attr](#attrs) with type
  `type` or `list(type)` (with a possible type restriction). This syntax allows
  for [polymorphic ops](#polymorphism).

  ```c++
  REGISTER_OP("PolymorphicSingleInput")
      .Attr("T: type")
      .Input("in: T");

  REGISTER_OP("RestrictedPolymorphicSingleInput")
      .Attr("T: {int32, int64}")
      .Input("in: T");
  ```

  Referencing an attr of type `list(type)` allows you to accept a sequence of
  tensors.

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

  Note that the number and types of tensors in the output `out` is the same as
  in the input `in`, since both are of type `T`.

* For a sequence of tensors with the same type: `<number> * <type>`, where
  `<number>` is the name of an [Attr](#attrs) with type `int`.  The `<type>` can
  either be a `tf.DType`,
  or the name of an attr with type `type`.  As an example of the first, this
  op accepts a list of `int32` tensors:

  ```c++
  REGISTER_OP("Int32SequenceExample")
      .Attr("NumTensors: int")
      .Input("in: NumTensors * int32")
  ```

  Whereas this op accepts a list of tensors of any type, as long as they are all
  the same:

  ```c++
  REGISTER_OP("SameTypeSequenceExample")
      .Attr("NumTensors: int")
      .Attr("T: type")
      .Input("in: NumTensors * T")
  ```

* For a reference to a tensor: `Ref(<type>)`, where `<type>` is one of the
  previous types.

> A note on naming: Any attr used in the type of an input will be inferred.  By
> convention those inferred attrs use capital names (like `T` or `N`).
> Otherwise inputs, outputs, and attrs have names like function parameters
> (e.g. `num_outputs`).  For more details, see the
> [earlier note on naming](#naming).

For more details, see
[`tensorflow/core/framework/op_def_builder.h`][op_def_builder].

#### Backwards compatibility

Let's assume you have written a nice, custom op and shared it with others, so
you have happy customers using your operation.  However, you'd like to make
changes to the op in some way.

In general, changes to existing, checked-in specifications must be
backwards-compatible: changing the specification of an op must not break prior
serialized `GraphDef` protocol buffers constructed from older specifications.
The details of `GraphDef` compatibility are
[described here](./versions.md#compatibility_of_graphs_and_checkpoints).

There are several ways to preserve backwards-compatibility.

1. Any new attrs added to an operation must have default values defined, and
   with that default value the op must have the original behavior. To change an
   operation from not polymorphic to polymorphic, you *must* give a default
   value to the new type attr to preserve the original signature by default. For
   example, if your operation was:

       REGISTER_OP("MyGeneralUnaryOp")
           .Input("in: float")
           .Output("out: float");

   you can make it polymorphic in a backwards-compatible way using:

       REGISTER_OP("MyGeneralUnaryOp")
           .Input("in: T")
           .Output("out: T")
           .Attr("T: numerictype = DT_FLOAT");

2. You can safely make a constraint on an attr less restrictive.  For example,
   you can change from `{int32, int64}` to `{int32, int64, float}` or `type`.
   Or you may change from `{"apple", "orange"}` to `{"apple", "banana",
   "orange"}` or `string`.

3. You can change single inputs / outputs into list inputs / outputs, as long as
   the default for the list type matches the old signature.

4. You can add a new list input / output, if it defaults to empty.

5. Namespace any new ops you create, by prefixing the op names with something
   unique to your project. This avoids having your op colliding with any ops
   that might be included in future versions of TensorFlow.

6. Plan ahead! Try to anticipate future uses for the op. Some signature changes
   can't be done in a compatible way (for example, making a list of the same
   type into a list of varying types).

The full list of safe and unsafe changes can be found in
[`tensorflow/core/framework/op_compatibility_test.cc`](https://www.tensorflow.org/code/tensorflow/core/framework/op_compatibility_test.cc).
If you cannot make your change to an operation backwards compatible, then create
a new operation with a new name with the new semantics.

Also note that while these changes can maintain `GraphDef` compatibility, the
generated Python code may change in a way that isn't compatible with old
callers.  The Python API may be kept compatible by careful changes in a
hand-written Python wrapper, by keeping the old signature except possibly adding
new optional arguments to the end.  Generally incompatible changes may only be
made when TensorFlow's changes major versions, and must conform to the
[`GraphDef` version semantics](./versions.md#compatibility_of_graphs_and_checkpoints).

### GPU support

You can implement different OpKernels and register one for CPU and another for
GPU, just like you can [register kernels for different types](#polymorphism).
There are several examples of kernels with GPU support in
[`tensorflow/core/kernels/`](https://www.tensorflow.org/code/tensorflow/core/kernels/).
Notice some kernels have a CPU version in a `.cc` file, a GPU version in a file
ending in `_gpu.cu.cc`, and some code shared in common in a `.h` file.

For example, the `tf.pad` has
everything but the GPU kernel in [`tensorflow/core/kernels/pad_op.cc`][pad_op].
The GPU kernel is in
[`tensorflow/core/kernels/pad_op_gpu.cu.cc`](https://www.tensorflow.org/code/tensorflow/core/kernels/pad_op_gpu.cu.cc),
and the shared code is a templated class defined in
[`tensorflow/core/kernels/pad_op.h`](https://www.tensorflow.org/code/tensorflow/core/kernels/pad_op.h).
We organize the code this way for two reasons: it allows you to share common
code among the CPU and GPU implementations, and it puts the GPU implementation
into a separate file so that it can be compiled only by the GPU compiler.

One thing to note, even when the GPU kernel version of `pad` is used, it still
needs its `"paddings"` input in CPU memory.  To mark that inputs or outputs are
kept on the CPU, add a `HostMemory()` call to the kernel registration, e.g.:

```c++
#define REGISTER_GPU_KERNEL(T)                         \
  REGISTER_KERNEL_BUILDER(Name("Pad")                  \
                              .Device(DEVICE_GPU)      \
                              .TypeConstraint<T>("T")  \
                              .HostMemory("paddings"), \
                          PadOp<GPUDevice, T>)
```

#### Compiling the kernel for the GPU device

Look at
[cuda_op_kernel.cu.cc](https://www.tensorflow.org/code/tensorflow/examples/adding_an_op/cuda_op_kernel.cu.cc)
for an example that uses a CUDA kernel to implement an op. The
`tf_custom_op_library` accepts a `gpu_srcs` argument in which the list of source
files containing the CUDA kernels (`*.cu.cc` files) can be specified. For use
with a binary installation of TensorFlow, the CUDA kernels have to be compiled
with NVIDIA's `nvcc` compiler. Here is the sequence of commands you can use to
compile the
[cuda_op_kernel.cu.cc](https://www.tensorflow.org/code/tensorflow/examples/adding_an_op/cuda_op_kernel.cu.cc)
and
[cuda_op_kernel.cc](https://www.tensorflow.org/code/tensorflow/examples/adding_an_op/cuda_op_kernel.cc)
into a single dynamically loadable library:

```bash
nvcc -std=c++11 -c -o cuda_op_kernel.cu.o cuda_op_kernel.cu.cc \
  ${TF_CFLAGS[@]} -D GOOGLE_CUDA=1 -x cu -Xcompiler -fPIC

g++ -std=c++11 -shared -o cuda_op_kernel.so cuda_op_kernel.cc \
  cuda_op_kernel.cu.o ${TF_CFLAGS[@]} -fPIC -lcudart ${TF_LFLAGS[@]}
```

`cuda_op_kernel.so` produced above can be loaded as usual in Python, using the
`tf.load_op_library` function.

Note that if your CUDA libraries are not installed in `/usr/local/lib64`,
you'll need to specify the path explicitly in the second (g++) command above.
For example, add `-L /usr/local/cuda-8.0/lib64/` if your CUDA is installed in
`/usr/local/cuda-8.0`.

>   Note in some linux settings, additional options to `nvcc` compiling step are needed. Add `-D_MWAITXINTRIN_H_INCLUDED` to the `nvcc` command line to avoid errors from `mwaitxintrin.h`.

### Implement the gradient in Python

Given a graph of ops, TensorFlow uses automatic differentiation
(backpropagation) to add new ops representing gradients with respect to the
existing ops.
To make automatic differentiation work for new ops, you must register a gradient
function which computes gradients with respect to the ops' inputs given
gradients with respect to the ops' outputs.

Mathematically, if an op computes \\(y = f(x)\\) the registered gradient op
converts gradients \\(\partial L/ \partial y\\) of loss \\(L\\) with respect to
\\(y\\) into gradients \\(\partial L/ \partial x\\) with respect to \\(x\\) via
the chain rule:

$$\frac{\partial L}{\partial x}
    = \frac{\partial L}{\partial y} \frac{\partial y}{\partial x}
    = \frac{\partial L}{\partial y} \frac{\partial f}{\partial x}.$$

In the case of `ZeroOut`, only one entry in the input affects the output, so the
gradient with respect to the input is a sparse "one hot" tensor.  This is
expressed as follows:

```python
from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import sparse_ops

@ops.RegisterGradient("ZeroOut")
def _zero_out_grad(op, grad):
  """The gradients for `zero_out`.

  Args:
    op: The `zero_out` `Operation` that we are differentiating, which we can use
      to find the inputs and outputs of the original op.
    grad: Gradient with respect to the output of the `zero_out` op.

  Returns:
    Gradients with respect to the input of `zero_out`.
  """
  to_zero = op.inputs[0]
  shape = array_ops.shape(to_zero)
  index = array_ops.zeros_like(shape)
  first_grad = array_ops.reshape(grad, [-1])[0]
  to_zero_grad = sparse_ops.sparse_to_dense([index], shape, first_grad, 0)
  return [to_zero_grad]  # List of one Tensor, since we have one input
```

Details about registering gradient functions with
`tf.RegisterGradient`:

* For an op with one output, the gradient function will take an
  `tf.Operation` `op` and a
  `tf.Tensor` `grad` and build new ops
  out of the tensors
  [`op.inputs[i]`](../../api_docs/python/framework.md#Operation.inputs),
  [`op.outputs[i]`](../../api_docs/python/framework.md#Operation.outputs), and `grad`.  Information
  about any attrs can be found via
  `tf.Operation.get_attr`.

* If the op has multiple outputs, the gradient function will take `op` and
  `grads`, where `grads` is a list of gradients with respect to each output.
  The result of the gradient function must be a list of `Tensor` objects
  representing the gradients with respect to each input.

* If there is no well-defined gradient for some input, such as for integer
  inputs used as indices, the corresponding returned gradient should be
  `None`.  For example, for an op taking a floating point tensor `x` and an
  integer index `i`, the gradient function would `return [x_grad, None]`.

* If there is no meaningful gradient for the op at all, you often will not have
  to register any gradient, and as long as the op's gradient is never needed,
  you will be fine. In some cases, an op has no well-defined gradient but can
  be involved in the computation of the gradient. Here you can use
  `ops.NotDifferentiable` to automatically propagate zeros backwards.

Note that at the time the gradient function is called, only the data flow graph
of ops is available, not the tensor data itself.  Thus, all computation must be
performed using other tensorflow ops, to be run at graph execution time.

### Shape functions in C++

The TensorFlow API has a feature called "shape inference" that provides
information about the shapes of tensors without having to execute the
graph. Shape inference is supported by "shape functions" that are registered for
each op type in the C++ `REGISTER_OP` declaration, and perform two roles:
asserting that the shapes of the inputs are compatible during graph
construction, and specifying the shapes for the outputs.

Shape functions are defined as operations on the
`shape_inference::InferenceContext` class. For example, in the shape function
for ZeroOut:

```c++
    .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
      c->set_output(0, c->input(0));
      return Status::OK();
    });
```

`c->set_output(0, c->input(0));` declares that the first output's shape should
be set to the first input's shape. If the output is selected by its index as in the above example, the second parameter of `set_output` should be a `ShapeHandle` object. You can create an empty `ShapeHandle` object by its default constructor. The `ShapeHandle` object for an input with index `idx` can be obtained by `c->input(idx)`.

There are a number of common shape functions
that apply to many ops, such as `shape_inference::UnchangedShape` which can be
found in [common_shape_fns.h](https://www.tensorflow.org/code/tensorflow/core/framework/common_shape_fns.h) and used as follows:

```c++
REGISTER_OP("ZeroOut")
    .Input("to_zero: int32")
    .Output("zeroed: int32")
    .SetShapeFn(::tensorflow::shape_inference::UnchangedShape);
```

A shape function can also constrain the shape of an input. For the version of
[`ZeroOut` with a vector shape constraint](#validation), the shape function
would be as follows:

```c++
    .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
      ::tensorflow::shape_inference::ShapeHandle input;
      TF_RETURN_IF_ERROR(c->WithRank(c->input(0), 1, &input));
      c->set_output(0, input);
      return Status::OK();
    });
```

The `WithRank` call validates that the input shape `c->input(0)` has
a shape with exactly one dimension (or if the input shape is unknown,
the output shape will be a vector with one unknown dimension).

If your op is [polymorphic with multiple inputs](#polymorphism), you can use
members of `InferenceContext` to determine the number of shapes to check, and
`Merge` to validate that the shapes are all compatible (alternatively, access
attributes that indicate the lengths, with `InferenceContext::GetAttr`, which
provides access to the attributes of the op).

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

Since shape inference is an optional feature, and the shapes of tensors may vary
dynamically, shape functions must be robust to incomplete shape information for
any of the inputs. The `Merge` method in [`InferenceContext`](https://www.tensorflow.org/code/tensorflow/core/framework/shape_inference.h)
allows the caller to assert that two shapes are the same, even if either
or both of them do not have complete information. Shape functions are defined
for all of the core TensorFlow ops and provide many different usage examples.

The `InferenceContext` class has a number of functions that can be used to
define shape function manipulations.  For example, you can validate that a
particular dimension has a very specific value using `InferenceContext::Dim` and
`InferenceContext::WithValue`; you can specify that an output dimension is the
sum / product of two input dimensions using `InferenceContext::Add` and
`InferenceContext::Multiply`. See the `InferenceContext` class for
all of the various shape manipulations you can specify. The following example sets
shape of the first output to (n, 3), where first input has shape (n, ...)

```c++
.SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
    c->set_output(0, c->Matrix(c->Dim(c->input(0), 0), 3));
    return Status::OK();
});
```

If you have a complicated shape function, you should consider adding a test for
validating that various input shape combinations produce the expected output
shape combinations.  You can see examples of how to write these tests in some
our
[core ops tests](https://www.tensorflow.org/code/tensorflow/core/ops/array_ops_test.cc).
(The syntax of `INFER_OK` and `INFER_ERROR` are a little cryptic, but try to be
compact in representing input and output shape specifications in tests.  For
now, see the surrounding comments in those tests to get a sense of the shape
string specification).

## Build a pip package for your custom op

To build a `pip` package for your op, see the
[tensorflow/custom-op](https://github.com/tensorflow/custom-op) example. This
guide shows how to build custom ops from the TensorFlow pip package instead
of building TensorFlow from source.

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
