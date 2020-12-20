# 目覚ましロボットアーム
・眠っていたらタンバリンを叩いて起こす  
・起きなかったらお気に入りの人形を叩いたり、重要書類をぐちゃぐちゃにしたり嫌がらせしてきます。  
# セットアップ方法
## カメラのセットアップ(Realsenseを使用する場合)  
・  
## プログラムのセットアップ  

・ rt-net様のcrane_x7_rosをインストールしていない方は以下のパッケージをインストールしてください。(インストール済みの方は飛ばしてください)

```sh
cd /catkin_ws/src
git clone https://github.com/rt-net/crane_x7_ros.git
cd /catkin_ws
catkin_make
source ~/.bashrc
```
・ このリポジトリをインストールします。

```sh
cd /catkin_ws/src/crane_x7_ros
git clone https://github.com/cit-team6/last_report.git
cd /catkin_ws
catkin_make
source ~/.bashrc
```
