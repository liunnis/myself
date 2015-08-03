import urllib2
url = 'http://m.weather.com.cn/data5/city.xml'
content = (urllib2.urlopen(url).read()).decode('utf8')
print content