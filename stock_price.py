import sys
import mechanize

days = 0
amount = 0

br = mechanize.Browser()
resp = br.open("http://api.kibot.com/?action=login&user=guest&password=guest")
resp = br.open("http://api.kibot.com/?action=history&symbol=" + sys.argv[1] + "&interval=daily&startdate=" + sys.argv[2] + "&enddate=" + sys.argv[3])

res = resp.read().split("\n")

for line in res:
  item = line.split(",")
  if len(item) > 4:
    amount += float(item[4])
    days += 1

if days > 0:
  print amount / days
else:
  print "Please specify the correct date"
