import re
import json

import utils


df = utils.load_and_prepare_data(csv_path="coffee_sales.csv")

print(df.sample(5))