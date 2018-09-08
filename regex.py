import re

regex = r'ab+'
text = "bababbababbabbab"
pattern = re.compile(regex)

# searchは全ての連続部分文字列を調べ，最初に引っかかったところを返す
matchObj = re.search(pattern, text)
print(matchObj)

# searchは全ての連続部分文字列を調べ，全て返す
matchObjs = re.findall(pattern, text)
print(matchObjs)

# matchはtextそのものがregexの条件を満たすか調べる
matchObj = re.match(regex, text)
print(matchObj)

# findはマッチするところの先頭を返す．なければ-1を返す？
# subは文字列を正規表現で置換する．str.replaceはただの文字列置換

# メールアドレス

regex = r'[A-Za-z0-9\._+]+@[A-Za-z]+\.[A-Za-z]'
re.match(regex), 'sampleaccount@sampledomain.com')