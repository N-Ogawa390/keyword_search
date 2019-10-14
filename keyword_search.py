from self_mod.init_mods import *

# keyword = input('検索したいキーワードを入力してください：')
keyword = ('ダンススクール')

print('ありがとうございます。それでは知恵袋の上位5記事を検索します！')

br.get('https://chiebukuro.yahoo.co.jp/')

br.find_element_by_xpath('//*[@id="searchForm"]/div/input[1]').click()
br.find_element_by_xpath('//*[@id="searchForm"]/div/input[1]').send_keys('%s' % keyword)
br.find_element_by_xpath('//*[@id="searchForm"]/div/p[1]/input').click()

key_elm = br.find_elements_by_xpath('//*[@class="listSearchResults__listItem___nYuqC"]/h3/a')
csvlist = []

for i in key_elm:
    j = i.text
    k = i.get_attribute('href')
    # print(j + '\t' + k)
    csvlist.append(j + k)

# print(csvlist)

with open('list_key.csv', 'w') as file:
    for l in csvlist:
        file.write(l + '\n')
# 基本系：https://teratail.com/questions/47153

# with open('keyword.csv','w') as f:
#     writelist = csv.writer(f, lineterminator='\n')
#     writelist.writerow(csvlist) writerowは配列すべてを1行に書き込む
#だから、[[タイトル1,URL1],[タイトル2,URL2],…]の2次元配列を作る必要がある

quit()
