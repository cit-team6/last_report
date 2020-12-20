# 目覚ましロボットアーム
・眠っていたらタンバリンを叩いて起こす  
・起きなかったらお気に入りの人形を叩いたり、重要書類をぐちゃぐちゃにしたり嫌がらせしてきます。  

## システムの起動方法

CRANE-X7の制御信号ケーブルを制御用パソコンへ接続します。
Terminalを開き、`crane_x7_bringup`の`demo.launch`を起動します。
このlaunchファイルには次のオプションが用意されています。

- fake_execution (default: true)

実機を使用する/使用しない

### シミュレータを使う場合

実機無しで動作を確認する場合、
制御信号ケーブルを接続しない状態で次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=true
```

### 実機を使う場合

実機で動作を確認する場合、
制御信号ケーブルを接続した状態で次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=false
```

ケーブルの接続ポート名はデフォルトで`/dev/ttyUSB0`です。
別のポート名(例: /dev/ttyUSB1)を使う場合は次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=false port:=/dev/ttyUSB1
```

### Gazeboを使う場合

次のコマンドで起動します。実機との接続やcrane_x7_bringupの実行は必要ありません。

```sh
roslaunch crane_x7_gazebo crane_x7_with_table.launch
```

# セットアップ方法

## カメラのセットアップ(Realsenseを使用する場合)  
・  カメラのセットアップや動作方法はこちら
https://github.com/cit-team6/last_report/blob/main/RealSense/sensor_setup_manual.md
## プログラムのセットアップ  

・ rt-net様のcrane_x7_rosをインストールしていない方は以下のコマンドを入力してください。(インストール済みの方は飛ばしてください)

```sh
cd /catkin_ws/src
git clone https://github.com/rt-net/crane_x7_ros.git
cd /catkin_ws
catkin_make
source ~/.bashrc
```
・ このリポジトリをインストールします。以下のコマンドを入力してください。

```sh
cd /catkin_ws/src/crane_x7_ros
git clone https://github.com/cit-team6/last_report.git
cd /catkin_ws
catkin_make
source ~/.bashrc
```

# 実行方法
