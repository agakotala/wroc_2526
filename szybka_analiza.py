import pandas as pd

df = pd.read_csv('wynagrodzenia.csv')

#print(df.head())
#print(df.info())
#print(df.describe())
#flitorwanie wiek, dochod
wiek_i_dochod = df[['wiek', 'dochód']]
#print(wiek_i_dochod.head())
powyzej_30 = df[df['wiek'] > 30]
#print(powyzej_30.head())
powyzej_30_kobiety = df[(df['wiek'] > 30) & (df['płeć'] == 'K')] #dwa warunki łączone za pomocą &
#print(powyzej_30_kobiety.head())
sredni_dochod = df.groupby('płeć')['dochód'].mean()
#print(sredni_dochod)
agregaty = df.groupby('płeć').agg({
    'dochód': ['mean', 'median', 'std'],
    'wiek': ['min', 'max', 'count']
})

agregaty = agregaty.round(2) #zaokrąglenie do 2 miejsc po przecinku
#print(agregaty)
mapa_stanu = {
    'żonaty': 'zy',
    'zamężna': 'za',
    'wolny': 'wy',
    'wolna': 'wa',
    'wdowa': "wda",
    'wdowiec': 'wdc',
    'rozwiedziony': 'ry',
    'rozwiedziona': 'ra'
}
df['stan_cywilny_skrot'] = df['stan_cywilny'].map(mapa_stanu) #mapuje czyli zmienia dane z calych
#print(df.stan_cywilny_skrot)




