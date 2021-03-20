
def html_tag_word(tag_lbl, _str):
    result = "<" + tag_lbl + ">" + _str + "</" + tag_lbl + ">"
    print(result)

html_tag_word('i', 'Python')
html_tag_word('b', 'Python Tutorial')

