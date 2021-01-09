
python -m timeit -s "import re" "re.match('hello', 'hello world')"

python -m timeit -s "import re; h=re.compile('hello')" "h.match('hello world')"

python -m timeit -s "import re" "h=re.compile('hello'); h.match('hello world')"

