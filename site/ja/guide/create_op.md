# オペレーションを作成する

Note: あなたのC++のカスタムオペレーションがTensorFlow公式のpipパッケージとABI互換になることを保証するため、[Custom opリポジトリ](https://github.com/tensorflow/custom-op) のガイドに従ってください。
あなたのカスタムオペレーションをビルドし配布するためのDockerのイメージはもちろんのこと、端から端までのコード例が示されています。

既存のTensorFlowのライブラリに存在しないオペレーションを作りたい場合、既存のPythonのオペレーションや関数を組み合わせて、Pythonでオペレーションを書くことを推奨します。
もしそれが不可能なら、C++のカスタムオペレーションを作ってもよいです。
C++のカスタムオペレーションを作りたいと思う理由は、いくつかあります。

* 既存のオペレーションの組み合わせでオペレーションを表現するのが、不可能または簡単ではない
* 既存のプリミティブの組み合わせでオペレーションを表現するのは、効率的ではない
* 将来コンパイラが融合することが難しいプリミティブの組み合わせを、自前で融合したい

例えば、"MaxPool" オペレーションと似ているが、最大値のかわりにウィンドウをスライドさせて中央値を計算する、"median pooling" のようなものを実装したいとしましょう。
これは、オペレーションの組み合わせ（例えば、ExtraImagePatchesとTopKを使う）でも可能ですが、1つの融合したオペレーションとしてより賢明に実装したネイティブなオペレーションと比較して、性能とメモリ効率の面で劣るかもしれません。
オペレーションの組み合わせで、あなたがやりたいことを表現する試みは価値があります。
もしそれが難しいまたは非効率であることが証明されたときのみ、新しいオペレーションを追加することを検討しましょう。

あなたのカスタムオペレーションを組み込むために必要なことを次に示します。

1. C++ファイル内で新しいオペレーションを登録します。オペレーションの登録では、オペレーションの実装とは独立であるオペレーションの機能のためのインターフェース（仕様）を定義します。例えば、オペレーションの登録では、オペレーション名やオペレーションの入出力を定義します。また、テンソルのシェイプ推論に使用されるシェイプ関数を定義します。
2. C++でオペレーションを実装します。オペレーションの実装はカーネルとして知られ、Step 1で登録した仕様の実装を具体化します。異なる入出力型、アーキテクチャ（例えば、CPUやGPU）のために複数のカーネルが存在することもあり得ます。
3. Pythonのラッパーを作成する（任意）。このラッパーは、Pythonでオペレーションを作るときに使われるパブリックなAPIです。デフォルトのラッパーは、オペレーションの登録から生成され、直接利用することもできますし、追加することもできます。
4. オペレーションの勾配を計算するための関数を書きます。（任意）
5. オペレーションをテストします。便宜上、たいていはPythonで行いますが、C++でオペレーションをテストすることも可能です。勾配を定義した場合、Python からは `tf.test.compute_gradient_error` を使って確認できます。Reluのような順伝搬の関数とその勾配をテストするための例については、[`relu_op_test.py`](https://www.tensorflow.org/code/tensorflow/python/kernel_tests/relu_op_test.py) を見てください。


## 前提条件

* C++に精通していること
* [TensorFlowのバイナリ](../../install) がインストールされていること。もしくは、[ダウンロードされたTensorFlowのソースコード](../../install/source.md) があり、ビルドできること


## オペレーションのインターフェースを定義する

TensorFlowのシステムを使って、オペレーションのインターフェースを登録して定義します。
登録にあたり、オペレーションの名前と入出力（型と名前）、オペレーションが必要とする場合があるdocstringsと [アトリビュート](#attrs) を指定します。

どのように取り組むのかを見るために、`int32` のテンソルを受け取り、最初以外のすべての要素が0であるコピーされたテンソルを出力するオペレーションを作ることを考えます。
これを行うために、`zero_out.cc` と命名されたファイルを作成します。
続いて、オペレーションのインターフェースを定義するための `REGISTER_OP` マクロ呼び出しを追加します。

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

この `ZeroOut` オペレーションは、入力として32bit整数のテンソル `to_zero` を受け取り、32bit整数のテンソル `zeroed` を出力します。
このオペレーションは、出力テンソルが入力テンソルと同じシェイプであることを保証するために、シェイプ関数を使っています。
例えば、入力テンソルのシェイプが [10, 20] であるならば、このシェイプ関数は出力のシェイプも [10, 20] であることを明示します。

> 命名に関する注釈: オペレーションの名前はCamelCaseで、かつバイナリに登録されている全てのオペレーションの中で唯一のものである必要があります。


## オペレーションのカーネルお実装する

インターフェースを定義したあとは、1つ以上のオペレーションの実装を提供する必要があります。
これらのカーネルを作成するためには、`OpKernel` を継承したクラスを作成し、`Compute` メソッドをオーバーライドします。
`Compute` メソッドは、`OpKernelContext*` 型である1つの `context` 引数を提供し、ここから入力や出力テンソルのような便利なものにアクセスできます。

上記で作成したファイルにカーネルを追加します。
カーネルは例えば次のようなものになるかもしれません。

```c++
#include "tensorflow/core/framework/op_kernel.h"

using namespace tensorflow;

class ZeroOutOp : public OpKernel {
 public:
  explicit ZeroOutOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // 入力テンソルを取得する。
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<int32>();

    // 出力テンソルを作成する。
    Tensor* output_tensor = NULL;
    OP_REQUIRES_OK(context, context->allocate_output(0, input_tensor.shape(),
                                                     &output_tensor));
    auto output_flat = output_tensor->flat<int32>();

    // 最初以外のすべての要素を0にする。
    const int N = input.size();
    for (int i = 1; i < N; i++) {
      output_flat(i) = 0;
    }

    // 可能なら、最初の入力値は維持する。
    if (N > 0) output_flat(0) = input(0);
  }
};
```

カーネルを実装したあと、TensorFlowのシステムに登録します。
登録時には、このカーネルが動作するいろいろな制約を指定します。
例えば、CPU向けに作成した1つのカーネルと、GPU向けの別のカーネルがあるとしましょう。

これを `ZeroOut` オペレーションで実現するためには、次を `zero_out.cc` に追加します。

```c++
REGISTER_KERNEL_BUILDER(Name("ZeroOut").Device(DEVICE_CPU), ZeroOutOp);
```

> 重要: OpKernelのインスタンスは、同時にアクセスされることがあります。`Compute` メソッドは、スレッドセーフにしなければなりません。クラスメンバへのアクセスはmutexでガードしてください。いっそのこと、クラスメンバ経由で状態を共有しないようにしてください！オペレーションの状態を追跡するためには、[`ResourceMgr](https://www.tensorflow.org/code/tensorflow/core/framework/resource_mgr.h) を使用することを検討してください。
