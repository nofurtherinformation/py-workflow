# %%
import os
import pandas as pd
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))
repo_root = os.path.abspath(os.path.join(dir_path, '..'))

def main():
    try:
        req = requests.get('https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=integrated_county_timeseries_fips_17031_external')
        df = pd.DataFrame(req.json()['integrated_county_timeseries_external_data'])
        print(df.head())
        df.to_csv(os.path.join(repo_root, f'csv/latest_cook_county.csv'),index=False)
    except Exception as e:
        print('!!Error!!')
        print(e)

if __name__ == '__main__':
    main()
# %%
