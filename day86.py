# day 86 - read clipboard
# open the sample_clip.xlsx file
# copy the data
# run this info!
# voila a pandas df out the box!

import pandas as pd
df = pd.read_clipboard(na_values = [None], parse_dates=['d'])
df.dtypes
