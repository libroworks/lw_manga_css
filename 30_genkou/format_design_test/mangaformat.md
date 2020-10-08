@div:coverpage

<div class="chap_num">X</div>

# マンガフォーマット

@div:chap_lead
ここでは記述ルールをまとめます
@divend

@divend

<p id="pagetitle">試作　マンガフォーマット</a>


## マンガ組み合わせ例
=======
@「starting fwide
雪ちゃんいるー？

＃はい、ここに
@」


@アリス「doya fslim
雪ちゃん、「ほにゃらら」って知ってる？
@」

@雪「iyada fslim
心得はございますが、なにゆえほにゃららに興味を？
@」

@アリス「shibu fslim
この間「ほにゃらら」を知らなくて恥をかいたのよ
@」

@雪「jito fslim
そんなことが……
@」

@アリス「centering fuan back001
次までにほにゃららをマスターしてギャフンといわせてやるわ
@」

@divend

---


### コマ幅の指定
===========
@アリス「doya
省略時デフォルト幅
@」

@雪「jito
省略時デフォルト幅
@」

@アリス「doya fslim
fslim
@」

@アリス「doya fwide
fwide
@」

@アリス「doya ffull
ffull
@」

@divend

![](img0/zuhan0/zuhan0-1.svg?svgimg=30,,30)

ショートカットとして、＠frameを＠「、＠fendを＠」としてもよいことにしました（＠は半角）。

### 背景と中央揃え
無指定の場合、アリスは左、雪は右に寄ります。**centering指定で中央に寄せる**ことができます（コマ幅によってはうまくいかないことも）

====
@雪「centering kohon back000
centering
@」

@雪「kohon back000
default

＃あいてますね
@」

@divend

![](img0/zuhan0/zuhan0-2.svg?svgimg=30,,38)


TODO：背景パターンを増やすかどうか要検討

### マンガ全体の囲み
マンガ全体の囲み（＠div:container～＠divend）は、css flexboxを使って**コマを横に並べる**ために使います。これで囲まない場合、コマは通常の文章や画像などと同じく縦に並びます。

![](img0/zuhan0/zuhan0-3.svg?svgimg=30,,25)


### 特殊なパターン（章冒頭に置くスタートコマ）

@「starting fwide
雪ちゃん、雪ちゃん、雪ちゃーん！

＃そんなに呼ばなく<br>
てもいますよ
@」

![](img0/zuhan0/zuhan0-4.svg?svgimg=30,,32)



### 特殊なパターン（フルサイズで1画面に2人）
二人の向きが決まっているので、吹き出しの尻尾を付けないとどっち向きかわからない。TODO：吹き出しのafter要素でSVG画像のシッポを付ける。

====
@雪「soreda ffull
画像も入る。拡張してても基本はMarkdownだから
![](img0/chap4zu5.JPG?svgimg=30)
@」

@アリス「yatta fleft
すごーい
@」

@divend

![](img0/zuhan0/zuhan0-5.svg?svgimg=30,,32)

---

---
### 表情パターンと指定

@negative:4

#### アリス

@negative:4

====
@アリス「namida fslim fshort
namida
@」

@アリス「shibu fslim fshort
shibu
@」

@アリス「hatena fslim fshort
hatena
@」

@アリス「gyao fslim fshort
gyao
@」

@アリス「doya fslim fshort
doya
@」

@アリス「fuan fslim fshort
fuan
@」

@アリス「yatta fslim fshort
yatta
@」

@アリス「sumashi fslim fshort
sumashi
@」

@frame:blank fslim fshort
@」

@divend


@アリス「fuan back000 fshort
こんなに覚えられるかな……

＃印刷して貼って<br>おこうかしら
@」


#### 雪
=====
@雪「jito fslim fshort
jito
@」

@雪「shock fslim fshort
shock
@」

@雪「anone fslim fshort
anone
@」

@雪「kohon fslim fshort
kohon
@」

@雪「gohoubi fslim fshort
gohoubi
@」

@雪「iyada fslim fshort
iyada
@」

@雪「soreda fslim fshort
soreda
@」

@雪「desuyo fslim fshort
desuyo
@」

@frame:blank fslim fshort
@」

@divend

<!---
@雪「jito back000 fshort
単純な番号のほうがよいかも……？

＃「y001」とか
@」 -->


---

### 背景設定

====
@アリス「yatta back001 fslim
back001
@」

@アリス「yatta back002 fslim
back002
@」

@アリス「yatta back003 fslim
back003
@」

@アリス「yatta back004 fslim
back004
@」

@アリス「yatta back005 fslim
back005
@」

@アリス「yatta back006 fslim
back006
@」

@アリス「yatta back007 fslim
back007
@」

@アリス「yatta back008 fslim
back008
@」

@アリス「yatta back009 fslim
back009
@」

@divend

---

====

@アリス「yatta back010 fslim
back010
@」

@アリス「yatta back011 fslim
back011
@」

@アリス「yatta back012 fslim
back012
@」


@アリス「yatta back013 fslim
back013
@」

@アリス「yatta back014 fslim
back014
@」

@アリス「yatta back015 fslim
back015
@」

@divend


@div:column
#### 特殊指定
＜sp＞（実際には半角で入力）という擬似タグで、6mmの空きを作ることができます。格好悪いですが、吹き出しの文字の位置を微調整するために使います。

＠frame:blankは空きのコマ（枠線なし）を入れます。マンガのコンテナは均等空き設定なので、コマが足りないときは空きのコマで詰め物します。

@divend


---

### 背景設定（幅広版）

=====
@雪「jito centering back001
back001
@」

@雪「jito centering back002
back002
@」

@雪「jito centering back003
back003
@」

@雪「jito centering back004
back004
@」

@雪「jito centering back005
back005
@」


@雪「jito centering back006
back006
@」

@divend

---
====

@雪「jito centering back007
back007
@」

@雪「jito centering back008
back008
@」

@雪「jito centering back009
back009
@」

@雪「jito centering back010
back010
@」

@雪「jito centering back011
back011
@」

@雪「jito centering back012
back012
@」

@divend

---


===

@雪「jito centering back013
back013
@」

@雪「jito centering back014
back014
@」

@雪「jito centering back015
back015
@」

@divend

---

---

## 分割テスト
=======
@「starting fwide
雪ちゃんいるー？

＃はい、ここに
@」


@アリス「doya fslim
雪ちゃん、「ほにゃらら」って知ってる？
@」

@雪「iyada fslim
心得はございますが、なにゆえほにゃららに興味を？
@」

@アリス「shibu fslim
この間「ほにゃらら」を知らなくて恥をかいたのよ
@」

@雪「jito fslim
そんなことが……
@」

@アリス「doya fslim
雪ちゃん、「ほにゃらら」って知ってる？
@」

@雪「iyada fslim
心得はございますが、なにゆえほにゃららに興味を？
@」

@アリス「shibu fslim
この間「ほにゃらら」を知らなくて恥をかいたのよ
@」

@divend

=======

@雪「jito fslim
そんなことが……
@」

@アリス「doya fslim
雪ちゃん、「ほにゃらら」って知ってる？
@」

@雪「iyada fslim
心得はございますが、なにゆえほにゃららに興味を？
@」

@アリス「shibu fslim
この間「ほにゃらら」を知らなくて恥をかいたのよ
@」

@雪「jito fslim
そんなことが……
@」

@アリス「doya fslim
雪ちゃん、「ほにゃらら」って知ってる？
@」

@雪「iyada fslim
心得はございますが、なにゆえほにゃららに興味を？
@」

@アリス「shibu fslim
この間「ほにゃらら」を知らなくて恥をかいたのよ
@」

@雪「jito fslim
そんなことが……
@」



@divend
