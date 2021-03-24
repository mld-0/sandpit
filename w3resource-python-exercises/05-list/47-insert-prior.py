
def insert_prior_each(values, n):
    result = []
    for x in values:
        result.append(n)
        result.append(x)
    print(result)

color = ['Red', 'Green', 'Black']
insert_prior_each(color, 'c')
