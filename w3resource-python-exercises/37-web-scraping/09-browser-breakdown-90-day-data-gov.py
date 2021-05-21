import requests

_url = 'https://analytics.usa.gov/data/live/browsers.json'
print("_url:")
print(_url)
print()

r = requests.get(_url)
print("r:")
print(type(r))
print(r)
print()

result = r.json()
print("result:")
print(type(result))
help(r.json)
print()

result_visits = result['totals']['visits']
print("result_visits:")
print(result_visits)
print()


#   Get browser totals as sorted dictionary
result_browsers = result['totals']['browser']
result_browsers = dict(sorted(result_browsers.items(), key=lambda x: x[1], reverse=True))
print("result_browsers:")
print(result_browsers)
print()

#   Verify result_visits is equal to sum of visits from each browser
result_browser_sum = sum(result_browsers.values())
print("result_browser_sum:")
print(result_browser_sum)
print()

#   Get percentage share of each broswer as sorted dictionary, for results with percentage share > 0.01
result_browsers_share = {k: v/result_visits*100 for k, v in result_browsers.items() if v/result_visits*100 > 0.01}
print("result_browsers_share:")
print(result_browsers_share)


