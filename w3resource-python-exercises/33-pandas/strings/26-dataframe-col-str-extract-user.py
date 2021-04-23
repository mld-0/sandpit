import re
import pandas as pd

pd.set_option('display.max_columns', 10)

values = pd.DataFrame({
    'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in @Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
    })

print("values:")
print(values)

_delim = ", "
_find_user = lambda x: _delim.join(re.findall(r'(?<=@)\w+', x))

values['extract_user'] = values['tweets'].apply(_find_user)
print("extract_user:")
print(values)

