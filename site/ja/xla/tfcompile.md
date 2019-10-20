# AOTコンパイルの利用

## tfcompileとは？

`tfcompile` は、TensorFlowのグラフを実行コードへ事前に(AOT)コンパイルするための標準ツールです。
全体のバイナリサイズを減らすことに加えて、いくつかの実行時オーバヘッドを無くすことができます。
`tfcompile` の典型的な使い方は、推論用の計算グラフをモバイルデバイス向けの実行コードへコンパイルすることです。

TensorFlowのグラフは、通常TensorFlowのランタイムによって実行されます。
これは、グラフの各ノードを実行することになるため、実行時オーバヘッドを招きます。
TensorFlowのグラフやランタイムのコードが必要になるため、全体のバイナリサイズも大きくなります。
`tfcompile` よって生成される実行コードは、TensorFlowのランタイムを使わず、実際に計算で使用するカーネルのみに依存します。

コンパイラは、XLAフレームワークの上に作られています。
TensorFlowとXLAフレームワークをつなぐコードは、[tensorflow/compiler](https://www.tensorflow.org/code/tensorflow/compiler/) に存在します。


## tfcompileは何をするか？

`tfcompile` は、TensorFlowの概念であるfeedとfetchによって形作られるサブグラフを受け取り、サブグラフを満たすファンクションを生成します。
`feeds` はファンクションの入力引数、`fetches` はファンクションの出力引数です。
刈り込んだ結果のサブグラフは、PlaceholderとVariableノードを含めることができないため、すべての入力はfeedによって指定される必要があります。
すべてのPlacerholderとVariableは、feedとして指定されるのは共通であり、最終的なサブグラフはこれらのノードを一切含みません。
生成されたファンクションは、ファンクションのシグネチャをエクスポートするヘッダファイルと、実装を含むオブジェクトファイルからなる `cc_library` としてパッケージ化されます。
ユーザーは、生成されたファンクションを適切に呼び出すコードを書きます。


## tfcompileの利用

このセクションでは、`tfcompile` を使ってTensorFlowのサブグラフから実行可能バイナリを生成するための、高レベルのステップを詳しく述べます。
ステップは、以下からなります。

* ステップ1: コンパイルするサブグラフを構成する
* ステップ2: サブグラフをコンパイルするための `tf_library` ビルドマクロを利用する
* ステップ3: サブグラフを呼び出すコードを書く
* ステップ4: 最終的なバイナリを作成する


### ステップ1: コンパイルするサブグラフを構成する

生成されたファンクションの入力および出力引数に相当する、feedとfetchを決めます。
そして、[`tensorflow.tf2xla.Config`](https://www.tensorflow.org/code/tensorflow/compiler/tf2xla/tf2xla.proto) の `feeds` および `fetches` を設定します。

```textproto
# 各feedは、生成されたファンクションにおける入力の位置指定引数です。
# エントリの順序と入力引数の順序は一致します。
# ここで "x_hold" と "y_hold" は、グラフ上に定義されたPlaceholderノードの名前を指します。
feed {
  id { node_name: "x_hold" }
  shape {
    dim { size: 2 }
    dim { size: 3 }
  }
}
feed {
  id { node_name: "y_hold" }
  shape {
    dim { size: 3 }
    dim { size: 2 }
  }
}

# 各fetchは、生成されたファンクションにおける出力の位置指定引数です。
# エントリの順序と出力引数の順序は一致します。
# ここで "x_y_prod" は、グラフ上に定義されたMatmulノードの名前を指します。
fetch {
  id { node_name: "x_y_prod" }
}
```


### ステップ2: サブグラフをコンパイルするためのtf_libraryビルドマクロを利用する

このステップでは、`tf_library` ビルドマクロを利用して、グラフを `cc_library` に変換します。
`cc_library` は、グラフから生成されたコードを含んだオブジェクトファイルと、生成されたコードにアクセスするためのヘッダファイルから構成されます。
`tf_library` は、TensorFlowのグラフを実行コードにコンパイルするための `tfcompile` を利用しています。

```build
load("//tensorflow/compiler/aot:tfcompile.bzl", "tf_library")

# グラフを実行コードにコンパイルするために、tf_libraryマクロを使用します。
tf_library(
    # nameは、以下のビルドルールを生成するために使用します。
    # <name>           : cc_libraryは、生成されたヘッダとオブジェクトファイルをパッケージ化します。
    # <name>_test      : cc_testは、簡単なテストとベンチマークを含みます。
    # <name>_benchmark : cc_binaryは、最小限の依存関係を持つスタンドアロンなベンチマークを含み、
    #                    モバイルデバイスで実行できます。
    name = "test_graph_tfmatmul",
    # cpp_classには、名前空間を含む生成後のC++のクラス名を指定します。
    # クラスは、与えられた名前空間、もし名前空間が与えられていない場合はグローバルな名前空間に生成されます。
    cpp_class = "foo::bar::MatMulComp",
    # graphには、入力となるGraphDefを指定しますが、デフォルトではバイナリフォーマットを期待しています。
    # テキストフォーマットを使用する場合、接尾辞 '.pbtex' を使ってください。
    # 入力のfeedと出力のfetchを含んだこの入力グラフから、サブグラフが生成されます。
    # PlaceholderやVariableのOperationは、このサブグラフには存在しません。
    graph = "test_graph_tfmatmul.pb",
    # configには、入力となるConfigを指定しますが、デフォルトではバイナリフォーマットを期待しています。
    # テキストフォーマットを使用する場合、接尾辞 '.pbtex' を使ってください。
    # これは前のステップにおいて、feedとfetchを指定したところになります。
    config = "test_graph_tfmatmul.config.pbtxt",
)
```

> この例で使用するGraphDef (test_graph_tfmatmul.pb)を生成するためには、--out_dirフラグを使って出力場所を指定した状態で [make_test_graphs.py](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/make_test_graphs.py) を実行してください。

典型的なグラフとして、学習時に学習される重みを表現する [`Variables`](https://www.tensorflow.org/guide/variables) を含んだものがありますが、`tfcompile` は `Variables` を含んだサブグラフをコンパイルできません。
ツール [freeze_graph.py](https://www.tensorflow.org/code/tensorflow/python/tools/freeze_graph.py) は、チェックポイントファイルに保存された値を使って、Variablesを定数に変換します。
`tf_library` マクロは便宜上、このツールを実行する `freeze_checkpoint` 引数をサポートします。
[tensorflow/compiler/aot/tests/BUILD](https://www.tensorflow.org/code/tensorflow/compiler/aot/tests/BUILD) には、より多くの例があります。

> コンパイルされたサブグラフに現れた定数は、直接生成されるコードへコンパイルされます。生成されたファンクションに定数を渡すためには、これらをコンパイルしてしまうのではなく、単にfeedとして渡します。

`tf_library` ビルドマクロに関する詳細は、[tfcompile.bzl](https://www.tensorflow.org/code/tensorflow/compiler/aot/tfcompile.bzl) を参照してください。

基本となる `tfcompile` ツールの詳細については、[tfcompile_main.cc](https://www.tensorflow.org/code/tensorflow/compiler/aot/tfcompile_main.cc) を参照してください。


### ステップ3: サブグラフを呼び出すコードを書く

このステップでは、生成されたコードを呼び出すために、前ステップにおける `tf_library` ビルドマクロによって生成されたヘッダファイル(`test_graph_tfmatmul.h`) を使います。
ヘッダファイルは、ビルドパッケージとおなじく `bazel-genfiles` に配置され、`tf_library` ビルドマクロに設定されたnameアトリビュートに基づいて命名されます。
たとえば、`test_graph_tfmatmul` のために生成されるヘッダは、`test_graph_tfmatmul.h` になるでしょう。
以下は、生成されたものに関する省略版です。
`bazel-genfiles` に生成されたファイルは、役立つ付加的なコメントを含みます。

```c++
namespace foo {
namespace bar {

// MatMulCompは、事前にTensorFlowのグラフとして指定された計算を表現し、
// 実行コードへコンパイルされました。
class MatMulComp {
 public:
  // AllocModeは、バッファの割り当てモードを制御します。
  enum class AllocMode {
    ARGS_RESULTS_AND_TEMPS,  // 引数と結果、そして一時的に使用するバッファを割り当てます。
    RESULTS_AND_TEMPS_ONLY,  // 結果と一時的に使用するバッファのみを割り当てます。
  };

  MatMulComp(AllocMode mode = AllocMode::ARGS_RESULTS_AND_TEMPS);
  ~MatMulComp();

  // 引数のバッファから入力を読み込んで計算を実行し、出力結果をバッファに書き込みます。
  // 成功時にはtrueを返し、失敗時にはfalseを返します。
  bool Run();

  // 入力バッファを管理するメソッドです。バッファは、行優先のデータ順序となります。
  // それぞれの位置指定引数のためのメソッド群があります。
  void** args();

  void set_arg0_data(float* data);
  float* arg0_data();
  float& arg0(size_t dim0, size_t dim1);

  void set_arg1_data(float* data);
  float* arg1_data();
  float& arg1(size_t dim0, size_t dim1);

  // 出力バッファを管理するメソッドです。バッファは、行優先のデータ順序となります。
  // Runの呼び出しが成功したあとに呼ぶ必要があります。
  // それぞれの位置指定結果のためのメソッド群があります。
  void** results();


  float* result0_data();
  float& result0(size_t dim0, size_t dim1);
};

}  // end namespace bar
}  // end namespace foo
```

生成されたC++クラスは、`tf_library` マクロの `cpp_class` に指定したとおり、名前空間 `foo::bar` における `MatMulComp` になります。
生成されたすべてのクラスは、引数と結果のためのバッファを扱うメソッドが異なるのみで、おなじAPIを持ちます。
これらのメソッドは、`tf_library` マクロの引数である `feed` と `fetch` に指定するバッファの数や型によって違いが発生します。

生成されたクラスでは、3つのバッファが管理されます。
`args` は入力、`results` は出力、`temps` は計算を実行するために内部で利用する一時的なバッファを表しています。
デフォルトでは、生成されたクラスのそれぞれのインスタンスは、これらのすべてのバッファを確保して管理します。
コンストラクタの引数 `AllocMode` はこの振る舞いを変えるために使うことができます。
すべてのバッファは、64バイトの境界にアライメントされています。

生成されたC++クラスは、XLAによって生成された低レベルのコードを単にラッパするクラスです。

`tfcompile_test.cc` をもとに生成されたファンクションを呼び出す例：

```c++
#define EIGEN_USE_THREADS
#define EIGEN_USE_CUSTOM_THREAD_POOL

#include <iostream>
#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/compiler/aot/tests/test_graph_tfmatmul.h" // 生成される

int main(int argc, char** argv) {
  Eigen::ThreadPool tp(2);  // 必要に応じたスレッドプールのサイズ
  Eigen::ThreadPoolDevice device(&tp, tp.NumThreads());


  foo::bar::MatMulComp matmul;
  matmul.set_thread_pool(&device);

  // 引数を設定し、計算を実行する
  const float args[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
  std::copy(args + 0, args + 6, matmul.arg0_data());
  std::copy(args + 6, args + 12, matmul.arg1_data());
  matmul.Run();

  // 結果を確認する
  if (matmul.result0(0, 0) == 58) {
    std::cout << "Success" << std::endl;
  } else {
    std::cout << "Failed. Expected value 58 at 0,0. Got:"
              << matmul.result0(0, 0) << std::endl;
  }

  return 0;
}
```


### ステップ4: 最終的なバイナリを作る

このステップでは、ステップ2における `tf_library` によって生成されたライブラリと、ステップ3で書いたコードを組み合わせて最終的なバイナリを作ります。
以下は、`bazel` BUILDファイルの例です。

```build
# あなたのバイナリをリンクする例
# //tensorflow/compiler/aot/tests/BUILDも参照
load("//tensorflow/compiler/aot:tfcompile.bzl", "tf_library")

# ステップ2におけるtf_libraryの呼び出しとおなじ
tf_library(
    name = "test_graph_tfmatmul",
    ...
)

# tf_libraryによって生成された実行コードは、あなたのコードへリンクすることができます
cc_binary(
    name = "my_binary",
    srcs = [
        "my_code.cc",  # 生成されたヘッダにアクセスするために、test_graph_tfmatmul.hをインクルードします
    ],
    deps = [
        ":test_graph_tfmatmul",  # 生成されたオブジェクトファイルへリンクします
        "//third_party/eigen3",
    ],
    linkopts = [
          "-lpthread",
    ]
)
```
