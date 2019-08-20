# TFX ユーザーガイド

## イントロダクション

TFX は TensorFlow 上で動作する、Google のプロダクションスケールの機械学習プラットフォームです。
これは機械学習システムを定義、起動、監視するために必要な設定フレームワークと共有ライブラリを提供し、
それらを機械学習システムに統合できるようにします。

## インストール

[![Python](https://img.shields.io/pypi/pyversions/tfx.svg?style=plastic)](https://github.com/tensorflow/tfx)
[![PyPI](https://badge.fury.io/py/tfx.svg)](https://badge.fury.io/py/tfx)

```
pip install tensorflow
pip install tfx
```

Note: [TensorFlow Serving](https://www.tensorflow.org/serving/),
[TensorFlow JS](https://js.tensorflow.org/),
[TensorFlow Lite](https://www.tensorflow.org/lite) オプションのコンポーネントです。これらのインストールについては、それぞれのドキュメントを確認してください。

Note: このコマンドは [Apache Beam](beam.md) を Direct runner と同時にインストールします。
別途、[Flink](https://flink.apache.org/)のようなストリーミングランナーをインストールする必要があります。

## コアコンポーネント

### TFX パイプライン

TFX パイプラインはいくつかのコンポーネントを用いて、特定の機械学習タスク (たとえば、
特定のデータを用いた回帰モデルの構築とデプロイ) を最終的に実行するためのデータフローを定義します。
パイプラインのコンポーネントは TFX のライブラリを用いて構築されます。
パイプラインの最終結果は、推論を要求する TFX デプロイメントターゲットかサービス、またはその両方です。

## TFX パイプライン コンポーネント

TFX パイプラインは一連のコンポーネントを連結したもので、スケーラブルでハイパフォーマンスな機械学習を実現するように設計されています。
これにはモデリング、訓練、推論のサービング、そしてオンライン、ネイティブモバイルアプリ、JavaScript へのデプロイの管理が含まれています。

TFX パイプラインには典型的には次のコンポーネントが含まれます :

- [**ExampleGen**](examplegen.md) はパイプラインの先頭に来るコンポーネントで、
  データセットの取り込みと、必要な場合には分割を行います。

- [**StatisticsGen**](statsgen.md) はデータセットの統計量を計算します。

- [**SchemaGen**](schemagen.md) は統計量を確認し、データのスキーマを生成します。

- [**ExampleValidator**](exampleval.md) はデータセットに異常値や欠損値が含まれないかを検査します。

- [**Transform**](transform.md) はデータセットに対して特徴量エンジニアリングを行います。

- [**Trainer**](trainer.md) はモデルを訓練します。

- [**Evaluator**](evaluator.md) は訓練させた結果について深く分析を行います。

- [**ModelValidator**](modelval.md) は出力されたモデルのバリデーションを手助けし、
  プロダクション環境に適用するのに「十分良さそう」であることを保証します。

- [**Pusher**](pusher.md) はサービスを提供するインフラストラクチャにモデルをデプロイします。

次の図はこれらのコンポーネント間でのデータのやり取りをあらわしています。

![Component Flow](diag_all.svg)

### コンポーネントの内部構造

TFX のコンポーネントは次の3つの主要な部分から成り立ちます。

- Driver
- Executor
- Publisher

<img src="images/component.svg" alt="Component Anatomy" style="width:40%" />

#### Driver と Publisher

Driver はメタデータストアに対してクエリを発行し、 Executor にメタデータを提供します。
一方、Publisher は Executor の出力を受け取りメタデータとして保存します。
典型的には、開発者は Driver や Publisher を直接扱う必要はありませんが、Driver や Publisher が提供するログメッセージはデバッグの役に立つでしょう。
詳細は [トラブルシューティング](#トラブルシューティング) で改めて取り上げます。

#### Executor

Executor はコンポーネントが処理を行う箇所です。
開発者はそれぞれのコンポーネントを実装しているクラスの仕様に従ったコードを記述することで、Executor の内部で実行される処理を記述できます。
たとえば [Transform コンポーネント](transform.md) を利用する場合、 `preprocessing_fn` を実装する必要が生じるでしょう。

## TFX ライブラリ

TFX はライブラリとパイプラインのコンポーネントの両方を含んでいます。次の図は TFX の提供するライブラリとコンポーネントの関係を表しています。

![Libraries and Components](libraries_components.svg)

TFX はパイプラインのコンポーネントを作成するために必要ないくつかのライブラリを Python パッケージとして提供します。
これらのライブラリは、実装したいパイプラインに特有な側面に集中できるように、パイプラインのコンポーネントを作成するときに利用できます。

TFX のライブラリは次のものを含んでいます:

- [**TensorFlow Data Validation (TFDV)**](tfdv.md) は機械学習で用いるデータの解析や検証のためのライブラリです。
  これは高いスケーラビリティを持ち、 TensorFlow 及び TFX とうまく連携できるように設計されています。
  TFDV は次の内容を含みます:

    * 学習データとテストデータの要約統計量のスケーラブルな算出
    * データの分布や統計量、データセットの組み合わせに対する多面的な比較を行うビューワーとの統合
    * 必須になる値、値域、語彙などのデータに期待できる内容を説明する、データのスキーマを自動的に生成
    * スキーマの検査を補助するためのスキーマビューワー
    * 欠損値、値域を超えた値、誤った特徴量の型といった異常値を特定するための異常値検知
    * どの特徴量で異常値が生じたのか確認し、それを修正するのに必要な知見を得るための異常値ビューワー

- [**TensorFlow Transform (TFT)**](tft.md) は TensorFlow でデータの前処理を行うためのライブラリです。
  TensorFlow Transform はデータセット全体を通じた処理が必要な特徴量の算出に役立ちます。たとえば次のような処理です:

    * 平均と標準偏差を用いた入力値の正規化
    * すべての入力値から語彙を生成し、文字列を整数に変換
    * 観測されたデータの分布をもとにして区間を設定し、実数値 (float) をそれぞれの区間を表す整数値に変換

- [**TensorFlow**](train.md) は TFX のモデルを学習させるために利用されます。
  これは学習データとモデルのコードを入力すると、 SaveModel を出力します。
  また、TFT で作成された特徴量エンジニアリングのパイプラインを用いて、入力値の前処理を行うこともできます。

- [**TensorFlow Model Analysis (TFMA)**](tfma.md) は TensorFlow のモデルを評価するためのライブラリです。
  これは TensorFlow と同時に利用することで EvalSavedModel を生成することもできます。これは TFMA の分析の基本になります。
  TFMA を用いることで、作成したモデルを大量のデータに対して分散処理を行い、学習時に定義したものとおなじ指標で評価することができます。
  これらの指標をデータの異なるスライスに対して計算し、Jupyter notebook を用いて可視化できます。

- [**TensorFlow Metadata (TFMD)**](https://github.com/tensorflow/metadata) は
  機械学習モデルを TensorFlow で学習させるときに役立つメタデータについての標準的な表現形式を提供します。
  メタデータは手動で作成することも、入力データの解析を通じて自動的に生成されることもあるでしょう。
  また、データの検証、探索、変形に使われるかもしれません。
  メタデータのシリアライズ形式は次のものを含みます。

    * 表形式のデータに対するスキーマの記述 (たとえば tf.Example)
    * データセット全体に対する要約統計量の一式

- [**ML Metadata (MLMD)**](mlmd.md) は機械学習デベロッパーとデータサイエンティストのワークフローに関係するメタデータを記録・検索するためのライブラリです。
  大概の場合、メタデータは TFMD の表現を利用します。
  MLMD は [SQL-Lite](https://www.sqlite.org/index.html) や [MySQL](https://www.mysql.com/)、その他の類似した永続的なデータストアの管理を行います。

### TFX を支える技術

#### 必須なもの

- [**Apache Beam**](beam.md) はオープンソースで、バッチ処理とストリーミング処理の両方に対し統一的なデータ並列処理パイプラインのモデルとなるものです。
  TFX は Beam をデータ並列なパイプラインを実装するために利用しています。
  パイプラインは Beam がサポートする分散処理基盤をバックエンドに利用して動作します。
  サポートする分散処理基盤には Apache Flink, Google Cloud Dataflow などが含まれます。

#### オプション

Apache Airflow, Kubeflow のようなオーケストレーターは機械学習パイプラインの設定、オペレーション、監視、メンテナンスをより簡易にします。

- [**Apache Airflow**](orchestra.md) はワークフローをプログラムで記述し、ワークフローのスケジューリング、監視を行うプラットフォームです。
  TFX は Airflow をワークフローをタスクの有向非巡回グラフ (directed acyclic graphs: DAGs) で書き表すために利用しています。
  Airflow のスケジューラーは指定された依存関係にしたがって、ワーカー上でタスクを実行していきます。
  豊富なコマンドラインユーティリティは DAG の複雑な "手術" を簡単に実行できるようにします。
  リッチなユーザーインターフェイスはパイプラインのプロダクション環境での実行状況の可視化、進行状況の監視、また問題が発生したときのトラブルシューティングを容易にします。
  ワークフローがコードで定義されている場合、保守やバージョン管理、テスト、コラボレーションがよりよいものになるでしょう。

- [**Kubeflow**](https://www.kubeflow.org/) はシンプルでポータブルかつスケーラブルであり、
  Kubernetes 上での機械学習ワークフローの作成に特化しています。
  Kubeflow の目的はほかのサービスを再作成することなく、オープンソースのベスト・オブ・ブリードな
  機械学習システムを多様なインフラストラクチャ上で展開するための、単純な方法を提供することです。
  [Kubeflow Pipelines](https://www.kubeflow.org/docs/pipelines/pipelines-overview/)
  は Kubeflow 上で再現性のあるワークフローを実験や Notebook ベースの経験と統合された形で
  構築・実行することを可能にします。
  Kubernetes 上に構築された Kubeflow Pipeline にはホスティングされたメタデータストア、
  コンテナベースのオーケストレーションエンジン、ノートブックサーバー、そしてユーザーが複雑なパイプラインを
  開発、実行、管理するのを助ける UI が含まれています。
  Kubeflow Pipeline SDK はコンポーネントの作成や共有、パイプラインの構築をプログラムで実行できるようにします。

### オーケストレーションとポータビリティ

TFX は Apache Airflow や Kubeflow といった複数の環境やオーケストレーションフレームワークの間で
の移植性が高くなるように設計されています。また、ベアメタル環境や Google Cloud Platform (GCP)
のような異なるコンピューティングプラットフォームの間でも移植可能です。

Note: 現在のバージョンのユーザーガイドではベアメタルシステムのうち、
主に Apache Airflow をオーケストレーションに用いた場合について述べています。

### Model vs. SavedModel

#### Model

モデル (Model) は学習プロセスの成果物で、学習プロセスを通じて得られた重みがシリアライズされたレコードです。
重みはその後、新たな入力に対する予測を計算するために利用されます。
TFX と TensorFlow において、「モデル」はある時点で学習された重みを含むチェックポイントを指します。

「モデル」は予測がどのように行われるか書き表した TensorFlow のコンピュテーショングラフの定義
(別の言い方をすると Python ファイル) を指す場合もあることに注意してください。
この2つの意味のどちらを指すかは文脈に応じて変わります。

#### SavedModel

- **[SavedModel](https://www.tensorflow.org/api_docs/python/tf/saved_model)とは**
  普遍的で、言語に依存しない、密閉された、元の状態に回復可能な TensorFlow モデルのシリアライゼーションです。
- **なぜ重要なのか** : SavedModel は高水準なシステムで単一の抽象を利用して、
  TensorFlow のモデルを作成し、変形し、利用することを可能にするためです。

SavedModel は TensorFlow のモデルのシリアライゼーション形式です。
これはモデルをプロダクション環境でサービス提供する、または訓練したモデルをネイティブモバイルや JavaScript で利用する場合に推奨されます。
たとえば、モデルから推論結果を提供する REST サービスを作成する場合、モデルを SavedModel に
シリアライズし、 TensorFlow Serving でサービス提供できます。詳細は [Serving a TensorFlow
Model](https://www.tensorflow.org/serving/tutorials/Serving_REST_simple) をご確認ください。

### スキーマ

TFX のコンポーネントのうちのいくつかは、_スキーマ_ と呼ばれる入力データについての記述を扱います。
スキーマは [schema.proto](https://github.com/tensorflow/metadata/tree/master/tensorflow_metadata/proto/v0) のインスタンスです。
スキーマは [protocol buffer](https://developers.google.com/protocol-buffers/) 、より一般には "protobuf" として知られているものの一種です。
スキーマは特徴量のデータ型、その特徴量が必ず含まれなければならないかどうか、入力値の許される範囲、などの事柄を指定できます。
TensorFlow Data Validation (TFDV) を利用する利点の一つは、型やカテゴリ、入力値の範囲を推論し、
自動的にスキーマを推測してくれることです。

schema protobuf からの抜粋を次に示します。:

```proto
...
feature {
  name: "age"
  value_count {
    min: 1
    max: 1
  }
  type: FLOAT
  presence {
    min_fraction: 1
    min_count: 1
  }
}
feature {
  name: "capital-gain"
  value_count {
    min: 1
    max: 1
  }
  type: FLOAT
  presence {
    min_fraction: 1
    min_count: 1
  }
}
...
```

スキーマを利用しているコンポーネントを次に示します :

- TensorFlow Data Validation
- TensorFlow Transform

典型的な TFX のパイプラインでは TensorFlow Data Validation がスキーマを生成し、
ほかのコンポーネントはそれを利用します。

Note: 自動生成されたスキーマは「ベストエフォート」のものであり、単にデータの基本的な特徴の推測を試みるものです。
生成されたスキーマについては、開発者が確認し、必要な場合は修正を加えることが期待されています。

## TFX を使った開発

TFX は機械学習のプロジェクトやリサーチ、実験、ローカルのマシン上での開発、デプロイを行うまでのすべてのフェーズにおいて、強力なプラットフォームを提供します。
コードの重複を避け、[学習時とサービス提供時の歪み](#training-serving-skew-detection) の可能性を排除するために、
学習時と学習済みモデルのデプロイ時の両方で TFX のパイプラインを実装し、[TensorFlow Transform](tft.md) ライブラリを
を活用するために [Transform](transform.md) コンポーネントを学習時と推論時の両方で利用することを強く推奨します。
このようにすることで、前処理や解析を行う同一のコードを一貫して利用することができ、
学習に利用するデータとプロダクション環境で学習済みモデルに与えられるデータの間で差異が生じることを避けられます。
また、コードの記述も一度で済みます。

### データ探索、可視化、クリーニング

![Data Exploration, Visualization, and Cleaning](wrangling.svg)

TFX パイプラインは典型的には [ExampleGen](examplegen.md) コンポーネントから始まります。
ExampleGen コンポーネントは入力されたデータを受け付け、 tf.Examples の形式に整形します。
これはデータセットが学習用と評価用に分割されたあとで実行されることもよくあるため、学習用と評価用に、2つの ExampleGen コンポーネントのコピーが存在する場合もあります。
また、一般的には次に [StatisticsGen](statsgen.md) コンポーネントと [SchemaGen](schemagen.md)
コンポーネントが続きます。
これらのコンポーネントはデータを確認し、データのスキーマと統計量を推定します。
スキーマと統計量は [ExampleValidator](exampleval.md) コンポーネントに入力されます。
このコンポーネントはデータの中に異常値や欠損値、誤ったデータ型が存在しないか検査します。
これらのコンポーネントは [TensorFlow Data Validation](tfdv.md) の能力を活用しています。

[TensorFlow Data Validation (TFDV)](tfdv.md) はデータセットの探索、可視化、クリーニングを
行う際に役に立つツールです。
TFDV はデータを確認してデータの型、カテゴリ、値域を推定し、その後、自動的に異常値や欠損値を特定するのを手助けします。
また、可視化ツールも用意されており、データセットの内容理解に役立つでしょう。
パイプラインのコンポーネントの処理が完了したあと、 [MLMD](mlmd.md) からメタデータを読み込み、
データを分析するために TFDV の可視化ツールを Jupyter ノートブック上で利用できます。

一度モデルをデプロイしたあとであれば、TFDV をデプロイされたモデルへの推論リクエストに含まれる
新たなデータを監視し、異常値や傾向の変化を検出するために利用できます。
これは時系列データでトレンドや季節性があり、時間の経過にしたがって変化するものに対してはとくに有効で、
データの問題やモデルを新しいデータで再学習させる必要があるときに、通知を行う手助けになります。

### データの可視化

パイプラインのうち、TFDV を利用するコンポーネント (典型的には StatisticsGen, SchemaGen, ExampleValidator) では、データを処理した結果を Jupyter notebook で可視化できます。
データがモデルやアプリケーションに最適化されるまで何度も実行して結果を比較し、調整を行うことも可能です。

これらのコンポーネントの出力結果を [**ML Metadata (MLMD)**](mlmd.md) にクエリを発行して取得したあと notebook で可視化するために、 TFDV の可視化をサポートする API を利用できます。
これには [tfdv.load_statistics()](`tfdv.load_statistics`) や [tfdv.visualize_statistics()](`tfdv.visualize_statistics`) が含まれます。
これらの可視化を利用することで、データセットの特徴についてよりよい理解を得ることや、もし必要な場合は要求にそって修正することもできます。

### モデルの開発と学習

![Feature Engineering](feature_eng.svg)

典型的な TFX パイプラインは [Transform](transform.md) コンポーネントを含みます。
これは [TensorFlow Transform (TFT)](tft.md) ライブラリを活用して特徴量エンジニアリングを行います。
Transform コンポーネントは SchemaGen コンポーネントの作成したスキーマを入力とし、[data transformations](https://www.tensorflow.org/tfx/transform/api_docs/python/tft) を適用してモデルの学習に利用する特徴量の作成、組み合わせ、変換を行います。
欠損値の除去や型の変換についても、それらが推論時のリクエストにも含まれる可能性のある場合、 Transform コンポーネントで実行すべきです。
TensorFlow のコードを TFX で学習させるよう設計するときには[いくつか重要な検討事項があります。](train.md)

![Modeling and Training](train.svg)

Transform コンポーネントは SavedModel を生成します。
これは [Trainer](trainer.md) コンポーネントの中で TensorFlow にインポートされ、モデルを記述するコードで利用されます。
この SavedModel には Transform コンポーネントの作成した、データエンジニアリングで行う変換がすべて含まれています。
このため、学習時と推論時でまったくおなじコードを用いた同一の変換がなされます。
Transform コンポーネントで生成された SavedModel を含む、モデルを記述するコードを利用することで、学習用と評価用、両方のデータを利用し、モデルの訓練ができるようになります。

モデルを記述するコードの最後のセクションで、モデルを SavedModel と EvalSavedModel の両方の形式で保存すべきです。 EvalSavedModel 形式で保存するためには Trainer コンポーネントで [TensorFlow Model Analysis (TFMA)](tfma.md) ライブラリをインポートして適用することが必要になるでしょう。

```python
import tensorflow_model_analysis as tfma
...

tfma.export.export_eval_savedmodel(
        estimator=estimator,
        export_dir_base=eval_model_dir,
        eval_input_receiver_fn=receiver_fn)
```

### モデルの振る舞いの分析と理解

![Model Analysis](analysis.svg)

モデルの開発を始め学習させる場合、モデルの振る舞いについて分析し、真に理解することは極めて重要です。
典型的な TFX パイプラインは [Evaluator](evaluator.md) コンポーネントを含みます。
このコンポーネントは開発のこのフェーズにおける強力なツールセットを提供する [TensorFlow Model Analysis (TFMA)](tfma.md) ライブラリの能力を活用します。
Evaluator コンポーネントは保存した EvalSavedModel を入力として受け付けます。また、モデルの振る舞いを可視化し分析する際に利用する `SliceSpecs` のリストを指定できます。
それぞれの SliceSpec は学習データ中の、カテゴリカルな特徴量における特定のカテゴリ、数値的な特徴量における特定の値域といった、確認したい学習データの切り口を定義します。

たとえば、年間購入金額や地域データ、年齢層、性別といった異なるセグメントの顧客に対するモデルの振る舞いを理解しようと試みることは重要になりえるでしょう。
データセットがロングテールな分布をしる場合に、これはとくに重要になりえます。少数でも重要なグループに対する容認できない振る舞いが、多数派に対する振る舞いによって覆い隠されてしまう場合があるためです。
たとえば、モデルが平均的な従業員に対してはうまく機能するものの、企業の幹部に対しては本当にひどい過ちを犯すような場合、それを知っておくことは重要になるかもしれません。

### モデルの分析と可視化

モデルの学習を終え、学習結果を [Evaluator](evaluator.md) コンポーネント (これは [TFMA](tfma.md) を活用しています) に入力して処理が完了したあと、結果を Jupyter スタイルのノートブックで可視化できます。
2回目以降であれば、これまでの結果を比較して、結果がモデルとアプリケーションにとって最適化されるまで何度も調整できます。

ノートブック上で可視化を行うためには、まず[**ML Metadata (MLMD)**](mlmd.md) にクエリを発行し、コンポーネント群の実行結果を取得します。
次に、 TFMA の可視化用 API を利用すると結果の可視化ができます。
可視化用 API には [tfma.load_eval_results()](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/load_eval_results)や [tfma.view.render_slicing_metrics()](`tfma/view/render_slicing_metrics`) が含まれます。
可視化を行うことでモデルの特徴についてよりよい理解を得ることができ、必要な場合には修正もできるようになるでしょう。

## デプロイメントターゲット

モデルの開発と学習を終えてその結果に満足しているなら、推論リクエストを受け付ける場所である、1つまたは複数のデプロイメントターゲットにモデルをデプロイするタイミングです。
TFX は3つのクラスのデプロイメントターゲットをサポートしています。
学習済みモデルを SavedModel としてエクスポートすると、これら3つのうちのどれか、またはすべてのデプロイメントターゲットにモデルをデプロイできます。

![Component Flow](diag_all.svg)

### 推論: TensorFlow Serving

[TensorFlow Serving (TFS)](serving.md) はプロダクション環境向けに設計された、柔軟でハイパフォーマンスな機械学習モデルのサービングシステムです。
これは SavedModel を読み込むと、REST や gRPC インターフェースでの推論リクエストを受け付けるようになります。
また、複数のプロセスを同期・分散処理のためのいくつかの高度なアーキテクチャを用いて、1つないしは複数のネットワークサーバー上で走らせます。
TFS の開発やデプロイに関する詳細については [TFS のドキュメント](serving.md)を参照してください。

典型的なパイプラインでは [Pusher](pusher.md) コンポーネントが Trainer コンポーネントで訓練された SavedModel を読み込み、TFS のインフラストラクチャにデプロイします。
これは複数のバージョンやモデルのアップデートの処理を含みます。

### モバイルネイティブや IoT アプリケーションでの推論: TensorFlow Lite

[TensorFlow Lite](https://www.tensorflow.org/lite) は学習済みの TensorFlow モデルをネイティブモバイルや IoT アプリケーションで使うためのツール一式をデベロッパーに提供します。
TensorFlow Serving と同様に、これは SavedModel を読み込み、量子化や枝刈りのような最適化手法を用いて、モバイルや IoT デバイスで動作するようにサイズとパフォーマンスの最適化を試みます。
TensorFlow Lite の利用についての詳細は TensorFlow Lite のドキュメントを参照してください。

### JavaScript での推論: TensorFlow JS

[TensorFlow JS](https://js.tensorflow.org/) は機械学習モデルの学習とデプロイをブラウザや Node.js 上で行う JavaScript ライブラリです。
これは TensorFlow Serving や TensorFlow Lite と同様に SavedModel を読み込み、それを TensorFlow.js Web フォーマットに変換します。
TensorFlow JS の利用についての詳細は TensorFlow JS のドキュメントを参照してください。

## Airflow を用いた TFX パイプラインの作成

### インストール

Airflow は PyPI からインストールできます:

```python
# Airflow
# set this to avoid the GPL version; no functionality difference either way
export SLUGIFY_USES_TEXT_UNIDECODE=yes
pip install apache-airflow
```

### DAG の作成

Python を用いて TFX パイプラインを作成するためには、`tfx.runtimes.tfx_airflow.PipelineDecorator` でデコレートされた関数を定義して、
パイプラインで利用するコンポーネントを作成し、パイプラインに合わせてそれらをつなぎ合わせる必要があります。
その後、ファイルのグローバルコンテキストで `create_pipeline()` を呼び出します。
たとえば、典型的なパイプラインは次のようになるでしょう :

```python
@PipelineDecorator(
    pipeline_name='tfx_example_solution',
    schedule_interval=None,
    start_date=datetime.datetime(2018, 1, 1),
    enable_cache=True,
    additional_pipeline_args={'logger_args': logging_utils.LoggerConfig(
        log_root='/var/tmp/tfx/logs', log_level=logging.INFO)},
    metadata_db_root=os.path.join(home_dir, 'data/tfx/metadata'),
    pipeline_root=pipeline_root)
def create_pipeline():
  """Implements the example pipeline with TFX."""
  examples = csv_input(os.path.join(base_dir, 'no_split/span_1'))
  example_gen = CsvExampleGen(input_data=examples)
  statistics_gen = StatisticsGen(input_data=example_gen.outputs.output)
  infer_schema = SchemaGen(stats=statistics_gen.outputs.output)
  validate_stats = ExampleValidator(  # pylint: disable=unused-variable
      stats=statistics_gen.outputs.output,
      schema=infer_schema.outputs.output)
  transform = Transform(
      input_data=example_gen.outputs.output,
      schema=infer_schema.outputs.output,
      module_file=transforms)
  trainer = Trainer(
      module_file=model,
      transformed_examples=transform.outputs.transformed_examples,
      schema=infer_schema.outputs.output,
      transform_output=transform.outputs.transform_output,
      train_steps=10000,
      eval_steps=5000,
      warm_starting=True)
  model_analyzer = Evaluator(
      examples=example_gen.outputs.output,
      model_exports=trainer.outputs.output)
  model_validator = ModelValidator(
      examples=example_gen.outputs.output,
      model=trainer.outputs.output)
  pusher = Pusher(
      model_export=trainer.outputs.output,
      model_blessing=model_validator.outputs.blessing,
      serving_model_dir=serving_model_dir)

  return [
      example_gen, statistics_gen, infer_schema, validate_stats, transform,
      trainer, model_analyzer, model_validator, pusher
  ]

pipeline = TfxRunner().run(create_pipeline())
```

### Airflow を用いる場合の TFX パイプラインの初期化

[Apache Airflow](orchestra.md) のインストールの際に、パイプラインが作成される `$AIRFLOW_HOME` ディレクトリ (デフォルトでは `~/airflow`) が初期化されます。
完了後、パイプラインのコードを保持するためのディレクトリを作成する必要があります:

```bash
mkdir -p ~/airflow/dags     # or $AIRFLOW_HOME/dags
mkdir -p ~/airflow/data     # or $AIRFLOW_HOME/data
mkdir -p ~/airflow/plugins  # or $AIRFLOW_HOME/plugins
```

#### パイプラインの設定

実際のコードの構造に対する唯一の要件は、`create_pipeline()` 関数 (これは "パイプラインの設定" そのものです) が記された Python ファイルは `dags` フォルダ配下に置かれていなければいけない、というものです。
Python ファイルの名前は DAG の名前と一致させることを推奨します。DAG が `taxi` という名前のときには、そのファイル名も `taxi` とすべきです。

パイプラインの設定ファイル中の `create_pipeline()` 関数は `PipelineDecorator` でデコレートされ、`pipeline_name` などの値が設定されます。
これらは Airflow の web UI を用いてパイプラインを名前で識別する際や、パイプラインのログファイルを配置する際に重要となります。

#### パイプラインのコードのデプロイ

上記のセクションで記述しているようにパイプラインの設定ファイルを配置し、ファイル名を変更します。

`data` フォルダーと `plugins` フォルダー配下に新しくフォルダーを作成しパイプラインのコードを配置することで、パイプラインコードの残りのコードをデプロイしましょう。
これらの出力先フォルダーの名前をパイプラインで設定した名前 (`PipelineDecorator` で設定したもの) と一致させることはグッドプラクティスです。
たとえば、パイプラインの名前が `taxi` のとき、出力フォルダーの名前は次のようになります:

```bash
mkdir -p ~/airflow/data/taxi     # or $AIRFLOW_HOME/data/taxi
mkdir -p ~/airflow/plugins/taxi  # or $AIRFLOW_HOME/plugins/taxi

```

```python
home_dir = os.path.join(os.environ['HOME'], 'airflow/')
base_dir = os.path.join(home_dir, 'data/taxi/')
output_dir = os.path.join(base_dir, 'pipelines/')
```

データセットをファイルとして保存し利用する場合、 `data` フォルダー配下にファイルをコピーすべきです:

```bash
cp data.csv ~/airflow/data/taxi     # or $AIRFLOW_HOME/data/taxi
```

### サンプルコード

慣習的に、パイプラインの設定の記述にはパイプラインの設定に必要な最小限のコードのみを含むべきです。[これはそのようなコードのサンプルです](https://github.com/tensorflow/tfx/blob/master/tfx/examples/chicago_taxi_pipeline/taxi_pipeline_simple.py)。

コードで呼び出している、TensorFlow のモデルや Transform の `preprocessing_fn` などの処理の記述はすべて単一のファイルに含めるべきです。
[これはそのようなコードのサンプルです](https://github.com/tensorflow/tfx/blob/master/tfx/examples/chicago_taxi_pipeline/taxi_utils.py)。

## TFX パイプラインのデプロイとオペレーション

新しいパイプラインの処理を開始させるためには Airflow の web UI でパイプラインを有効にしなければいけません。
多くの場合、web UI から処理を開始する必要もあるでしょう。
もし実行を止めたい場合は、パイプラインを無効にすることも web UI から可能です。
また、パイプラインの現在の状態や、過去の履歴の確認、ログの閲覧も web UI で可能です。

### パイプラインの開始と更新

もしパイプラインをまだ実行していない場合、 Airflow をコマンドラインから実行する必要があります:

```bash
airflow webserver -p 8080
airflow scheduler
```

#### コードの更新

パイプラインのデプロイを行ったあとでも、パイプラインのコードに変更を加えることができます。
変更を加えた場合、 Airflow がリフレッシュを行う次のタイミング (デフォルトは1分です) まで待ち、Airflow の web UI ページを更新して変更を確認する必要があります。
パイプラインの `pipeline_name` を変更した場合には、古い名前が残るかもしれませんが、そのうち "missing" (行方不明) と表示されるようになります。

#### ノートブックを用いた可視化

パイプラインに含まれる TFX のコンポーネントの入力と出力を調べ、実行結果の比較を行うために、Jupyter スタイルのノートブックはとても有用なツールです。
加えて、TFDV と TFMA はどちらも強力な可視化のサポートを備えており、開発者がデータセットを探索し、モデルの出力結果を詳細に解析できるようになっています。

## トラブルシューティング

### Log ファイル中のエラーの探し方

TFX はログを PipelineDecotator の追加の引数である LoggerConfig で設定された場所に出力します。
デフォルトは `/var/tmp/tfx/logs/tfx.log` です。
加えて、オーケストレーター (たとえば Airflow や Kubeflow) もまたログファイルを出力します。
パイプラインのエラーの分析を試みるときには、これらのログファイルがとても有効です。
`taxi` という名前のパイプラインで特に LoggerConfig が設定されていない場合、TFX のログは `/var/tmp/tfx/logs/tfx.log` に出力されます。
これは [logging_utils.LoggerConfig](https://github.com/tensorflow/tfx/blob/master/tfx/utils/logging_utils.py) オブジェクトを生成し、パイプラインの設定の `logger_args` と呼ばれるパラメータに与えることで、設定の変更が可能です。

```python
@PipelineDecorator(
    pipeline_name='tfx_example_solution',
    schedule_interval=None,
    start_date=datetime.datetime(2018, 1, 1),
    enable_cache=True,
    additional_pipeline_args={'logger_args': logging_utils.LoggerConfig(
        log_root='/var/tmp/tfx/logs', log_level=logging.INFO)},
    metadata_db_root=os.path.join(home_dir, 'data/tfx/metadata'),
    pipeline_root=pipeline_root)
```

Note: Docker や Kubeflow のリモート環境上で Executor を動かしている場合、Executor のログはリモートワーカー上に出力されます。

Airflow を利用している場合、ログは Airflow が出力するログにも記録されます。
デフォルトの Airflow のログの出力先は `$AIRFLOW_HOME/logs` で、次のファイルが含まれます:

```
$AIRFLOW_HOME/logs/scheduler/{DATE}/taxi.py.log
$AIRFLOW_HOME/logs/scheduler/latest/taxi.py.log
$AIRFLOW_HOME/logs/taxi
$AIRFLOW_HOME/logs/taxi.COMPONENT_NAME
```

### パイプラインは表示されているが、Airflow で実行しようとするとみつからない

ウェブサーバーとスケジューラーを再起動してみてください。

## Kubeflow を用いた TFX パイプラインの作成

### セットアップ

Kubeflow はパイプラインを大規模に実行するために Kubernetes クラスタを必要とします。
Kubeflow のデプロイを行うための一連の手引については次のデプロイメントガイドラインを参照してください ([deplopying the Kubeflow cluster.](https://www.kubeflow.org/docs/started/getting-started-gke/))

### TFX パイプラインの設定と実行

Kubeflow 上で TFX のサンプルパイプラインを実行するためには Kubeflow パイプラインの[手順書](https://github.com/kubeflow/pipelines/tree/master/samples/tfx-oss)にしたがってください。
TFX コンポーネントは Kubeflow pipeline を構築するためにコンテナ化されています。
また、サンプルは大規模なパブリックのデータセットを読み込み、学習を行って、クラウド上で大規模にデータを処理するステップを解説しています。
