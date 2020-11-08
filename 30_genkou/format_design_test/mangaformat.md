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

<!-- ![](img0/zuhan0/zuhan0-1.svg?svgimg=30,,30) -->

---


###### マンガコマ表記の基本形
```
＠雪「kohon fslim
セリフ
＠」

＠アリス「doya fslim
セリフ
＠」
```

以降も含めて＠はすべて半角です。

### 背景と中央揃え
無指定の場合、アリスは左、雪は右に寄ります。**centering指定で中央に寄せる**ことができます（基本fwideと組み合わせて使います）

====
@雪「centering kohon back000
centering
@」

@雪「kohon back000
default

＃あいてますね
@」

@divend

```
＠雪「kohon fwide centering back000
セリフ

＃心の声
＠」
```

心の声は空きがさみしいときに使います。


### マンガ全体の囲み
マンガ全体の囲み（＠div:container～＠divend）は、css flexboxを使って**コマを横に並べる**ために使います。これで囲まない場合、コマは通常の文章や画像などと同じく縦に並びます。＠div:containerは4つ以上の半角=で代用できます。

```
＝＝＝＝

マンガコマの指定を並べる

＠divend
```

<!-- ![](img0/zuhan0/zuhan0-3.svg?svgimg=30,,25) -->


### 特殊なパターン（章冒頭に置くスタートコマ）

@「starting fwide
雪ちゃん、雪ちゃん、雪ちゃーん！

＃そんなに呼ばなく<br>
てもいますよ
@」


```
＠「starting fwide
雪ちゃん、雪ちゃん、雪ちゃーん！

＃そんなに呼ばなく<br>
てもいますよ
＠」
```

<!-- ![](img0/zuhan0/zuhan0-4.svg?svgimg=30,,32) -->


---

### 特殊なパターン（フルサイズで1画面に2人）
＠fleftまたは＠frightを指定した場合、コマ幅をゼロにして前のコマに入ります。

====
@雪「soreda ffull
画像も入る。拡張してても基本はMarkdownだから
@」

@アリス「yatta fleft
すごーい
@」

@divend

```
＝＝＝＝
＠雪「soreda ffull
画像も入る。拡張してても基本はMarkdownだから
＠」

＠アリス「yatta fleft
すごーい
＠」

＠divend
````

====
@アリス「doya fwide
＠fwideと組み合わせるときは、fslimで埋める
@」

@雪「soreda fright
ですよー　
@」

@div:blank fslim

@divend

@divend


```
＝＝＝＝
＠アリス「doya fwide
＠fwideと組み合わせるときは、fslimで埋める
＠」

＠雪「soreda fright
ですよー　
＠」

＠div:blank fslim

＠divend

＠divend
```

<!-- ![](img0/zuhan0/zuhan0-5.svg?svgimg=30,,32) -->

---

### コマの隙間に図版を入れる

====

@雪「kohon fwide back001
セリフだけでは間が持たない

@div:inlinefigure
![](img0/zuhan0/chap1zu3.svg?svgimg=40,80,35,-6,12)
@divend

@」

@divend

```
＠雪「kohon fwide back001
セリフだけでは間が持たない

＠div:inlinefigure
！[](img0/zuhan0/chap1zu3.svg?svgimg=40,80,35,-6,12)
＠divend

＠」
```

セリフの中に図版を入れた場合、普通なら吹き出しの中に入ります。それを＠div:inlinefigure～＠divendで囲むと、絶対配置（position:aboslute）によって外に出します。

- 背景を透過する必要があります。
- 図版の位置とサイズはMDBPのsvgimg指定で指定します。

```
?svgimg=拡大率,幅,高さ,xシフト,yシフト
```

---

### 高さの指定
どうしてもコマがうまく入らないときに使うftallという指定があります。

===

@雪「kohon fslim
通常は46mm
@」

@雪「kohon fslim ftall
ftallは54mm
@」

@雪「kohon fslim ftall7
ftall7は73mm
@」

@divend

```
＠雪「kohon fslim ftall
ftallは54mm
＠」
```

|指定| 高さ
|--|--
|ftall | 54mm
|ftall7 | 73mm
|ftall40 | 40mm
|ftall43 | 43mm
|ftall48 | 48mm


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

## 会話


【雪kohon】たいていの場合、先生役のセリフは長く、生徒役のセリフは短いです

【アリスdoya】そうなんだよね。だから右寄せ

【アリスdoya】でも生徒が長いセリフをしゃべることもあるわけで、その場合、右寄せだと変なことに

【アリスdoya hidariyose】仕方がないので左寄せ指定を加えます。これを指定すると左寄せになるので


会話は墨付きカッコ（【】）の中にキャラと表情指定を書きます。複数段落にすることはできません。
```
【雪kohon】たいていの場合、先生役のセリフは長く、生徒役のセリフは短いです

【アリスdoya】そうなんだよね。だから右寄せ

【アリスdoya】でも生徒が長いセリフをしゃべることもあるわけで、その場合、右寄せだと変なことに

【アリスdoya hidariyose】仕方がないので左寄せ指定を加えます。これを指定すると左寄せになるので
```
