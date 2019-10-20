# 新しいXLAのバックエンド開発

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

本予備ガイドは、効率的な方法でTensorFlowをハードウェアに容易に対応させたいと考えている、アーリーアダプターのためのものです。
本ガイドは1つ1つ丁寧に説明したものではなく、LLVM、Bazel、TensorFlowの知識を前提としています。

XLAは、新しいアーキテクチャやアクセラレータが、TensorFlowのグラフを処理するバックエンドを実装するための抽象的なインターフェースを提供します。
XLAへの対応は、新しいハードウェア向けに既存のすべてのTensorFlowのオペレーションを実装するのと比べて、はるかに簡潔でスケーラブルです。


実装のほとんどは、以下のシナリオのうちの1つに分類されます。

1. LLVMのバックエンドが存在するかしないかにかかわらず、公式にXLAでサポートされていない既存のCPUアーキテクチャ
2. LLVMのバックエンドが存在する、CPUではないハードウェア
3. LLVMのバックエンドが存在しない、CPUではないハードウェア

Note: LLVMのバックエンドとは、公式にリリースされたLLVMのバックエンド、または企業内で開発されたカスタマイズ版LLVMのバックエンドのことを指します。


## シナリオ1: 公式にXLAでサポートされていない既存のCPUアーキテクチャ

このシナリオの場合、既存の [XLA CPUバックエンド](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/cpu) を見ることから始めてください。
XLAのCPUバックエンド間の主な違いは、LLVMによって生成されるコードであることから、XLAではLLVMを使って異なるCPUをTensorFlowに簡単に対応できます。
Googleは、x64とARM64のアーキテクチャに対してXLAを試験しています。

もしハードウェア企業がハードウェア向けのLLVMのバックエンドをもつ場合、ビルドされたLLVMのバックエンドをXLAに接続することは簡単です。
JITモードでは、XLAのCPUバックエンドはホスト側のCPUのコードを生成します。
Ahead-Of-Timeコンパイルでは、[`xla::AotCompilationOptions`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/compiler.h) が対象とするアーキテクチャに対して設定するLLVM Tripleを提供します。

もし既存のLLVMのバックエンドがなくてもコード生成器が違う形で存在するならば、既存のCPUバックエンドの大部分を再利用できる可能性があります。


## シナリオ2: LLVMのバックエンドが存在する、CPUではないハードウェア

LLVM IRを出力する既存の [`xla::CPUCompiler`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/cpu/cpu_compiler.cc) や [`xla::GPUCompiler`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/gpu/nvptx_compiler.cc) クラスをベースとして、新しい [`xla::Compiler`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/compiler.h) の実装を作ることが可能です。
ハードウェアの性質によりLLVM IRの生成方法は異なりますが、多くのコードは既存のバックエンドと共有できるでしょう。

よい参考例は、XLAの [GPUバックエンド](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/gpu) です。
GPUのバックエンドはCPUとは異なるISAをターゲットとするため、GPUドメイン固有なコードの生成方法になります。
ほかの種類のハードウェア、たとえば（アップストリームのLLVMのバックエンドをもつ）HexagonのようなDSPは、LLVM IRの生成のしくみを再利用することができますが、ほかの部分は固有のものになるでしょう


## シナリオ3: LLVMのバックエンドが存在しない、CPUではないハードウェア

LLVMを利用できない場合、対象のハードウェア向けに新しいバックエンドを実装することが最良の選択肢となります。
この選択肢は、多大な労力を必要とします。
実装しなければならないクラスは次に示すとおりです。

* [StreamExecutor](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/stream_executor/stream_executor.h): 多くのデバイスでは、`StreamExecutor` のすべてのメソッドが必要になることはありません。詳細は既存の `StreamExecutor` の実装を見てください。
* [xla::Compiler](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/compiler.h): 本クラスは、HLO Computationから `xla::Executable` へのコンパイル処理を隠蔽します。
* [xla::Executable](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/executable.h): 本クラスは、コンパイル済みのComputationをプラットフォーム上で実行するために使用されます。
* [xla::TransferManager](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/xla/service/transfer_manager.h): 本クラスは、与えられたデバイスメモリのハンドルからXLAのリテラルデータを構築するための、プラットフォーム特有のしくみを提供することを可能にします。言い換えれば、ホストからデバイスまたはその反対のデータ転送処理を隠蔽します。
