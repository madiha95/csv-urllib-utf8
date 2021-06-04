import pandas as pd
from urllib.parse import quote

data = pd.read_csv("file_decoded.csv",error_bad_lines=False)


def title_parse(details):
    details = quote(details)
    return details


data['details']= data.details.apply(title_parse)
data.to_csv('file_encoded.csv')
