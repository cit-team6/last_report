# RealSense(TM)を操作する手順

## 概要

* このファイルはRealSenseにとってソースコードを書く時に必要になったライブラリーを入れる方法などをまとめる。
* プロセス：未完成

## 目次

  * [概要](#概要)
  * [環境](#環境)
  * [インストール手順](#インストール手順)
  * [操作手順](#操作手順)
    * [コード](#コード)
  * [ライセンス](#ライセンス)
  
## 環境

* Ubuntu 18.04

## インストール手順

下記は参考するものである

* RoSレポジトリをまだインストールされていない方向け：

[千葉工業大学　上田先生の作成したレポジトリ](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server)

* RealSense(TM)をインストールする必要なドライバーとライブラリ：

[deruma.net](https://demura.net/robot/16525.html?fbclid=IwAR0nOSm6AjqzBr9XKlJBnbOrQo_9WXP6ynvVWw4D2tUS67yDh-SiwgAf6o0)
  
## 操作手順

1. alt+T (ターミナルを開く）

2. `$ roscore` を実行する

3. 新ターミナルを起動して、`$ roslaunch realsense2_camera rs_camera.launch`を実行する

4. 新ターミナルを起動して、`$ cd ~/catkin_ws/src/test/scripts`を実行する

5. 上記のフォルダで`$ python realsense.py`を実行する

### カメラの画像出力を確認する方法（任意）

    $ rosrun rqt_image_view rqt_image_view
    
### コード

リンク：[realsense.py](https://github.com/cit-team6/last_report/blob/main/RealSense/realsense.py)

## ライセンス

[GNU General Public License v3.0](https://github.com/cit-team6/last_report/blob/main/RealSense/LICENSE)
