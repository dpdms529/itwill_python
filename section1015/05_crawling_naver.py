# 네이버 뉴스 중에서 [세계] 카테고리의 본문

from Crawler import crawler
from bs4 import BeautifulSoup

# 1. URL 설정하기
URL = "https://news.naver.com/section/104"

# 2. 수집할 뉴스기사의 URL 조사
link_list = crawler.select(
    URL,
    encoding="utf-8",
    selector=".sa_text > a",
)
# print(len(link_list))
# print(type(link_list))

# for item in link_list:
#     print(item.text, item.get("href"))

# 3. item에서 <a> 태그가 가지고 있는 속성들 중에서 href 속성 값만 추출하기
url_list = [i.get("href") for i in link_list]
# print(url_list)

# 4. 네이버 뉴스기사(세계)에 접속해서 본문 크롤링하기
## <article id="dic_area"> ..... </a>
news_content = ""  # 뉴스기사의 본문을 누적해서 저장할 문자열 변수
for i, url_world in enumerate(url_list):  # url_world : 크롤링할 페이지의 URL주소
    print("%d번째 뉴스기사 수집중...>> %s" % (i + 1, url_world))
    # URL에 접근해서 뉴스기사 가져오기
    news_html = crawler.select(url_world, encoding="utf-8", selector="#dic_area")

    if not news_html:
        print("%d번째 뉴스기사 크롤링 실패" % (i + 1))
    else:
        print("%d번째 뉴스기사 크롤링 성공" % (i + 1))
        for item in news_html:
            crawler.remove(item, "br")
            crawler.remove(item, "div")
            crawler.remove(item, "img")
            crawler.remove(item, "em")
            crawler.remove(item, "strong")
            crawler.remove(item, "span")
            crawler.remove(item, "script")
            news_content += item.text.strip()


print(news_content)


# 텍스트 마이닝
from konlpy.tag import Okt
from collections import Counter

okt = Okt()

nouns = okt.nouns(news_content)

words = []
for n in nouns:
    if len(n) > 1:
        words.append(n)

count = Counter(words)

most = count.most_common(100)

tags = {}
for n, c in most:
    tags[n] = c

from wordcloud import WordCloud
from matplotlib import pyplot

wc = WordCloud(
    font_path="gulim",
    max_font_size=200,
    width=1200,
    height=800,
    scale=2.0,
    background_color="#ffffff",
)

gen = wc.generate_from_frequencies(tags)

pyplot.figure()
pyplot.imshow(gen, interpolation="bilinear")
pyplot.axis("off")
wc.to_file("section1015/naver_worldnews_20251015.png")
pyplot.show()
pyplot.close()

# 정제한 데이터를 엑셀로 저장
from pandas import DataFrame
from pandas import ExcelFile

lists = []
for n, c in most:
    if len(n) > 1:
        lists.append([n, c])

df = DataFrame(lists, columns=["단어", "빈도수"])
df.to_excel(
    "section1015/네이버세계뉴스_20251015.xlsx",
    sheet_name="단어빈도수",
    index=False,
)

print(df)
