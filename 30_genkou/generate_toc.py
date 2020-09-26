from pathlib import Path
from bs4 import BeautifulSoup

result = '<nav role="doc-toc">\n' + (' '*4) + '<ul class="ul_h1">\n'
result += '''    <ul class="ul_h0">
        <li><a href="00_maeduke.html#h2_0"><span class="bg_white">はじめに</span></a>
        <li><a href="00_maeduke.html#h2_2"><span class="bg_white">キャラクター紹介</span></a>
    </ul>
'''
current = Path()
oldelemname = 'h1'
toc_h1_cnt = 1
toc_h2_cnt = 1
for path in current.glob('chap*'):
    if path.is_file():
        continue
    for target in path.glob('*.html'):
        # print(target)
        soup = BeautifulSoup(
                target.read_text(encoding="utf-8"), 'html.parser')
        targetpath = str(target).replace('\\', '/')
        # h1～h3要素を取得
        elems = soup.find_all(['h1','h2','h3'])
        for elem in elems:
            # print(elem)
            # print(elem['id'])
            # print(elem.get_text().strip())
            id = elem['id']
            if elem.name == 'h1':
                if oldelemname == 'h3':
                    result += (' ' * 12) + '</ul>\n'
                    result += (' ' * 8) + '</ul>\n'
                if oldelemname == 'h2':
                    result += (' ' * 8) + '</ul>\n'
                result += (' ' * 8)
                result += f'<li><a class="li_{elem.name}" href="{targetpath}#{id}">'
                result += f'<span class="nav_num">{toc_h1_cnt}</span>' + elem.get_text().strip()
                result += '</a></li>\n'
                toc_h1_cnt += 1
                toc_h2_cnt = 1
            if elem.name == 'h2':
                if oldelemname == 'h1':
                    result += (' ' * 8) + '<ul class="ul_h2">\n'
                if oldelemname == 'h3':
                    result += (' ' * 12) + '</ul>\n'
                result += (' ' * 12)
                result += f'<li><a class="li_{elem.name}" href="{targetpath}#{id}">'
                result += '<span class="bg_white">' + elem.get_text().strip()
                result += '</span></a></li>\n'
                toc_h2_cnt += 1
            if elem.name == 'h3':
                if oldelemname == 'h2':
                    result += (' ' * 12) + '<ul class="ul_h3">\n'
                result += (' ' * 16)
                result += f'<li><a class="li_{elem.name}" href="{targetpath}#{id}">'
                result += '<span class="bg_white">' + elem.get_text().strip()
                result += '</span></a></li>\n'
            oldelemname = elem.name

# 後始末
if oldelemname == 'h3':
    result += (' ' * 12) + '</ul>\n'
    result += (' ' * 8) + '</ul>\n'
if oldelemname == 'h2':
    result += (' ' * 8) + '</ul>\n'

result += '''        <ul class="ul_h0">
            <li><a href="99_atoduke.html#h2_0"><span class="bg_white">索引</span></a>
            <li><a href="99_atoduke.html#h3_0"><span class="bg_white">サンプルファイルについて</span></a>
            <li><a href="99_atoduke.html#h3_2"><span class="bg_white">著者プロフィール</span></a>
        </ul>
    </ul>
    <a href="999_okuduke.html" class="okuduke_link"></a>
</nav>
'''
print(result)
outpath = Path('tocoutput.html')
outpath.write_text(result, encoding = 'utf-8')
