# lw_manga_css～Vivliostyle用マンガスタイルCSS

## 概要
リブロワークスが制作した『そろそろ常識？ マンガでわかる「正規表現」』から、原稿とイラストを除き、CSSとダミー原稿をまとめたものです。

[Vivliostyle](https://vivliostyle.org/ja/)を利用して、印刷可能なPDFを作成することができます。

https://libroworks.co.jp/?p=3271

https://www.c-r.com/book/detail/1360

![編集中のイメージ](sampleimg1.png)

出力結果については、「40_pdf/fullpage_sample.pdf」をご覧ください。

## とりあえず見る方法
1. ローカルにCloneして個々のHTMLをwebブラウザで開く。ページングはされないがとりあえず見ることができます。
2. ローカルでWebサーバーを立ち上げてルートにファイルを配置し、「`http://localhost/30_genkou/viewer/#src=../00_maeduke.html&bookMode=true`」のような指定で開く。
3. 当社製のAtomエディタ用パッケージ[MDBP](https://atom.io/packages/mdbp-markdown-book-preview)で、00_maeduke.mdを開く。


## CSSについて
CSSは「30_genkou/_css」フォルダに収録されています。ページ設定にはCSS Paged Meidaを使用しています。

|CSSファイル | 役割
|--|--
|1_main.css  |h1～h6やpなど、標準的なタグ用のスタイルを定義
|2_kaiwa.css |会話表現用のスタイルを定義
|3_manga.css |マンガ表現用のスタイルを定義
|00_maeduke.css |目次、前書きなどの前付けのスタイルを定義
|chap1.css～chap6.css |1～6章のツメのスタイルを定義
|chap7_applendix.css |付録章のスタイルを定義
|99_atodule.css  |索引、プロフィールなどのスタイルを定義
|999_okuduke.css |奥付のスタイルの定義

### 画像ファイル
このCSSでは、background-imageによる画像ファイルでデザインを設定しています。画像ファイルを置き換えることで、デザインを変えることができます。画像ファイルは「30_genkou/_css/img」に収録されています。

|画像ファイル | 用途
|--|--
|manga_charaフォルダ | マンガ用のキャラクター画像
|manga_backフォルダ |コマの背景画像
|kaiwa_faceフォルダ | 会話用のキャラクター画像（マンガ用画像を左右反転して使用）
|3frame_fukidashi_c/l/r.svg |吹き出しのしっぽ
|chara_mame.png | マメ知識用画像
|comic_regex_bg2.png | 本文の背景画像
|comic_regex_circle01.png |キャラクター紹介の背景画像
|comic_regex_h3_bg.svg |h3見出しの背景画像
|comic_regex_lace01.svg |セクションタイトルの背景画像
|comic_regex_mae_h2_bg.svg |前付けの見出しの背景画像
|comic_regex_mae_mokuji01.svg |目次の見出し背景画像
|comic_regex_mae_mokuji02.svg |目次の見出し背景画像
|comic_regex_tobira_bg.png |章扉の背景画像
|plate_icon.svg |黒板用のアイコン
|soro_seiki_soutobira.png |総扉の背景画像

※装飾部分はなるべくSVG画像を使用していますが、サイズが大きいと粗くレンダリングされる現象があるため、一部はPNG画像にしています。


## HTML構成について
複数のHTMLで構成されており、VivliostyleのbookModeで連結しています。




## aaaa


説明作成中……
