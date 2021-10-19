import pandas as pd

raw_data = pd.read_csv(r'D:\AGH\Semestr_7\AiBD\Lab1\lab2\data\tb.csv')

raw_data = raw_data.drop(columns=['new_sp', 'new_sp_mu', 'new_sp_fu', 'new_sp_m04', 'new_sp_m514', 'new_sp_f04',
                                  'new_sp_f514'])
new_data = pd.melt(raw_data, id_vars=['iso2', 'year'], value_vars=list(raw_data.columns)[2:],
                   var_name='column', value_name='cases')

new_data = new_data.dropna(subset=['cases'])

new_data['cases'] = new_data['cases'].astype(int)
new_data['sex'] = new_data['column'].str[7]
new_data['age'] = new_data['column'].str[8:].map({
    '014': '0-14',
    '1524': '15-24',
    '2534': '25-34',
    '3544': '35-44',
    '4554': '45-54',
    '5564': '55-64',
    '65': '65+'
})
new_data = new_data[['iso2', 'year', 'age', 'cases', 'sex']]

new_data.to_csv(r'D:\AGH\Semestr_7\AiBD\Lab1\lab2\output\clean_data.csv')
