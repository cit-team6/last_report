## タンバリンを叩く

## インストール方法

次のコマンドを実行します。

```sh
cd ~/catkin_ws/src/crane_x7_ros/crane_x7_gazebo/worlds/
```
table.worldの中身を置き換える。

次のコマンドを実行します。
```sh
 cd ~/catkin_ws/src/crane_x7_ros/crane_x7_examples/scripts/
 vi tambourine.py
```
---

tambourine.pyの中身を置き換える。

次のコマンドを実行します。
```sh
 chmod +x tambourine.py
```

## 実行方法

`demo.launch`を実行している状態で実行できます。

- [tambourine](#tambourine)

---

### tanbarin

マジックの準備をするためのコードです。

表示される指示に従いマジックの準備をしてください。

次のコマンドを実行します。

```sh
rosrun crane_x7_examples tambourine.py
```

実際の動きは　→　[rink](https://github.com/knr2/tanbari_model/blob/main/25BEA4EE-1060-4554-AE39-268258D0E60F.gif)

---