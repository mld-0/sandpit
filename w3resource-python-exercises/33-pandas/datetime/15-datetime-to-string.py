import datetime
import dateutil.parser
import dateparser

_datetime = datetime.datetime(2020,1,1)
print("_datetime:")
print(_datetime)
print()

#   strftime() -> Convert datetime to string
result = _datetime.strftime("%F %H:%M:%S")
print("result:")
print(type(result))
print(result)
print()

_datetime_str = '2020-01-01'
print("_datetime_str:")
print(_datetime_str)
print()

#   Using dateutil.parser.parse() -> built-in Python datetime parser
_datetime = dateutil.parser.parse(_datetime_str)
print("_datetime (dateutil.parser.parse):")
print(type(_datetime))
print(_datetime)
print()

#   Using datetime.strptime() -> requires datetime format
_datetime = datetime.datetime.strptime(_datetime_str, '%Y-%m-%d')
print("_datetime (datetime.datetime.strptime):")
print(type(_datetime))
print(_datetime)
print()

#   Using dateparser (very good datetime parser, not included in python)
_datetime = dateparser.parse(_datetime_str)
print("_datetime (dateparser.parse):")
print(type(_datetime))
print(_datetime)

