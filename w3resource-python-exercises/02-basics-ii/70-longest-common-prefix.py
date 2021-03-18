
def longest_common_prefix(values):
    substring_len = 0
    while substring_len <= max([len(x) for x in values]):
        substring_len += 1
        loop_prefixes = set()
        for value in values:
            loop_prefixes.add(value[:substring_len])
        if len(loop_prefixes) > 1:
            substring_len -= 1
            break
    if (substring_len == 0):
        print(None)
        return
    print(value[:substring_len])
    

longest_common_prefix(["abcdefgh","abcefgh"])
longest_common_prefix(["w3r","w3resource"])
longest_common_prefix(["Python","PHP", "Perl"])
longest_common_prefix(["Python","PHP", "Java"])
