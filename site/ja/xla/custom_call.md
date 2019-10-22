# XLAのカスタムコール

このドキュメントでは、XLA「カスタムコール」の書き方と使い方について説明します。
カスタムコールは、C++やCUDAなどのプログラミング言語で書かれたコードを、XLAプログラムから呼び出すことができます。

警告： カスタムコールは、パワーユーザ用の低レベル機能です。
カスタムコールを使うと、デバッグしにくい（そして気づきにくい）状態の中で、あなたのプログラムが壊れやすくなります。
何かおかしくなったとき、あなた自身でXLAをデバッグできる準備ができていないなら、カスタムコールを使うべきではありません。
トラブルに遭遇したとしても、XLA開発者から支援はあまりもらえないと思っているべきです。

警告： カスタムコールのAPI/ABIは、現時点では固まっていません。
きまぐれに変更するつもりはありませんが、変更する可能性はあります。
将来可能性があるいくつかの変更については以下で説明します。

## CPUでのカスタムコール

XLAクライアントAPI経由で、カスタムコールを表すHLO命令を作ることができます。
これは、執筆時点ではTensorFlow経由では公開されていません。

例えば、以下のコードはCPU上で `A[i] = B[i % 128] + C[i]` をカスタムコールを使用して計算します（もちろん、通常のHLOを使って計算できますし、すべきです！）。

```c++
#include "tensorflow/compiler/xla/client/xla_builder.h"
#include "tensorflow/compiler/xla/service/custom_call_target_registry.h"

void do_it() {
  xla::XlaBuilder b("do_it");
  xla::XlaOp param0 =
      xla::Parameter(0, xla::ShapeUtil::CreateShape(F32, {128}), "p0");
  xla::XlaOp param1 =
      xla::Parameter(1, xla::ShapeUtil::CreateShape(F32, {2048}), "p1");
  xla::XlaOp custom_call =
      xla::CustomCall(&b, "do_custom_call", /*operands=*/{param0, param1},
                      /*output_shape=*/ShapeUtil::CreateShape(F32, {2048}));
}

void do_custom_call(void* out, const void** in) {
  float* out_buf = reinterpret_cast<float*>(out);
  const float* in0 = reinterpret_cast<const float*>(in[0]);
  const float* in1 = reinterpret_cast<const float*>(in[1]);
  for (int i = 0; i < 2048; ++i) {
    out_buf[i] = in0[i % 128] + in1[i];
  }
}
XLA_REGISTER_CUSTOM_CALL_TARGET(do_custom_call, "Host");
```

関数 `do_custom_call` は、処理を実行するバッファの次元情報を知っている必要があります。
この例では、サイズ128と2048を直書きしています。
もし、これをしたくない場合には、パラメータとして次元情報を関数に渡すことができます。

## GPUでのカスタムコール

GPUのカスタムコールのフレームワークは、CPUのフレームワークと多少異なります。
ここでは、上記のCPUコードと同じ `A[i] = B[i % 128] + C[i]` の計算を行うCUDAの例をあげます。

```c++
void do_it() { /* 上と同じ実装 */ }

__global__ custom_call_kernel(const float* in0, const float* in1, float* out) {
  size_t idx = threadIdx.x * blockSize.x + gridIdx.x;
  out[idx] = in0[idx % 128] + in1[idx];
}

void do_custom_call(CUstream stream, void** buffers,
                    const char* opaque, size_t opaque_len) {
  const float* in0 = reinterpret_cast<const float*>(buffers[0]);
  const float* in1 = reinterpret_cast<const float*>(buffers[1]);
  float* out = reinterpret_cast<float*>(buffers[2]);

  const int64 block_dim = 64;
  const int64 grid_dim = 2048 / block_dim;
  custom_call_kernel<<<grid_dim, block_dim,
                       /*dynamic_shared_mem_bytes=*/0, stream>>>(in0, in1, out);
}
XLA_REGISTER_CUSTOM_CALL_TARGET(do_custom_call, "CUDA");
```

最初にGPUカスタムコール関数が、*CPU上で実行される関数である*ことに注意してください。
CPU用 `do_custom_call` 関数は、GPU上での作業をキューに入れる役割を果たします。
ここではCUDAカーネルを起動していますが、cublasを呼び出すような他のこともできます。

`buffers` はホスト上にあるポインタの配列で、各要素はデバイス（つまりGPU）メモリを指しています。
パラメータが最初に来て、そのあと出力の値が来ます。
これは、CPUの呼び出し規則とは大きく異なり、２つのパラメータ、`ins` と `out` があります。
違う実装をした主な理由は、タプル型の入出力を効率的に処理するためです。
以下の章をごらんください。

CPUの例のように、入出力バッファの大きさをカスタムコールに直書きしました。
しかし、CPUの場合とは異なり、オペランドとしてバッファの大きさを渡してもうまく動きません。
通常、CPU上でバッファの大きさが分かっている必要があります。例えば、カーネルを起動するとき、block/gridの次元情報が必要です。
しかし、カスタムコールにオペランドとしてバッファサイズが渡されると、この値はGPUメモリ上にあります。
処理の開始時に、この値を読むためのだけに処理が重い同期的なデバイスからホストへのメモリコピーを実行する必要があります。

これを回避するために `opaque` パラメータを用意しています。
カスタムコールをつくるときに、任意のバイト文字列をセットできます。

```c++
std::string opaque = "...";
xla::CustomCall(&b, "do_custom_call", /*operands=*/{param0, param1},
                /*output_shape=*/ShapeUtil::CreateShape(F32, {2048}),
                opaque);
```

`xla::Shape` はプロトコルバッファ表現を持つので、 `opaque` の内部にこのシリアライズされた表現を保存してGPUカスタムコールの内部でデシリアライズできます。
ただし、 `xla::ShapeProto` は頻繁には変更されませんが、 `xla::Shape` は*変更されます*。
gitログをチェックして、過去にどのような変更が行われたか確認してください。

## カスタムコールにタプルを渡す

以下のカスタムコール呼び出しを考えます。

```c++
using xla::ShapeUtil;
Shape p0_shape = ShapeUtil::MakeTuple({
    ShapeUtil::MakeShape(F32, {32}),
    ShapeUtil::MakeTuple({
        ShapeUtil::MakeShape(F32, {64}),
        ShapeUtil::MakeShape(F32, {128}),
    }),
    ShapeUtil::MakeShape(F32, {256}),
});
xla::XlaOp p0 = xla::Parameter(0, p0_shape, "p0");

Shape out_shape = ShapeUtil::MakeTuple({
  ShapeUtil::MakeShape(F32, {512}),
  ShapeUtil::MakeShape(F32, {1024}),
});
xla::CustomCall(&b, "do_custom_call", /*operands=*/{p0}, out_shape);
```

CPUとGPUの両方で、タプルはポインタの配列としてメモリ内で表現されます。
C++擬似コードでは、上記のパラメータ0は以下のように配置されます。

```c++
// 上記のカスタムコールのパラメータ0のメモリ内レイアウト
// CPUとGPUの両方で有効です。
float* subbuf0 = new float[32];
float* subbuf1 = new float[64];
float* subbuf2 = new float[128]
float* subbuf3 = new float[256];

void* subtuple = new void*[2];
(*subtuple)[0] = subbuf1;
(*subtuple)[1] = subbuf2;

void* p0 = new void*[3];
(*p0)[0] = subbuf0;
(*p0)[1] = subtuple;
(*p0)[2] = subbuf3;
```

CPUとGPUでメモリ内表現は同じですが、CPUとGPUのカスタムコール呼び出し規約では処理方法が異なります。

### 一時バッファとしてのタプル出力

カスタムコールへのタプル入力は便利ですが、厳密には必須ではありません。
カスタムコールへのタプル入力がサポートされていないなら、カスタムコールにタプルを渡す前にget-tuple-elementを使ってタプルを分解できます。

一方、タプル*出力*は、他の方法ではできないことができます。

タプル出力を持つ明確な理由は、それがカスタムコール（または、他のXLA命令）が複数の独立な配列を返す方法だからです。

しかし、あまり明確ではないですが、タプル出力はカスタムコールに一時メモリを提供する方法でもあります。
ええ、*出力*は一時バッファを表現できます。
出力バッファはオペレーションが書き込めるという性質を持っていて、書き込まれたあとに読み出すことができます。
これこそが、まさに一時バッファに必要なものです。

上の例で、 `F32[1024]` を一時バッファとして使いたいとします。
上記のようにHLOを記述して、単にカスタムコールのタプルインデックス1を決して読まないようにします。

### CPUカスタムコールでのタプル

CPUコードには、 `do_custom_call(const void** ins, void* out)` 関数があります。
`ins` は `param0` を指す要素が１つだけの配列です。
`param0` のサブバッファは、そのポインタをデリファレンスしてアクセスできます。
`output_tuple` のサブバッファは、`out` をデリファレンスしてアクセスできます。

### GPUカスタムコールでのタプル

GPUコードには、 `do_custom_call(..., void** buffers, ...)` 関数があります。
この場合 `buffers` は、入出力の各末端のバッファが一要素に対応する、*６つ*のデバイスポインタを持つホストの配列です。
フラットリストを生成するために、パラメータと出力に対して反復処理をおこない、それぞれについてその形状を行きがけ順に走査します。
具体的には:

```c++
// 上記のカスタムコールのための、GPUカスタムコール関数への 
// `buffers` パラメータのレイアウト。
buffers[0] == subbuf0
buffers[1] == subbuf1
buffers[2] == subbuf2
buffers[3] == subbuf3
buffers[4] == output_subbuf0
buffers[5] == output_subbuf1
```
