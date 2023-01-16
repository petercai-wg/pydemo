# https://github.com/sharmasw/DjangoDashboardCorona/tree/master/coronaDash

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
# Create your views here.


def index(request):

    countryName = "US"

    if request.method == 'POST':
        countryName = request.POST.get('countryName')

    global_data = pd.read_csv(
        'C:/pynotebook/data/covid_data.csv', encoding='utf-8', na_values=None)
# 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', encoding='utf-8', na_values=None)

    global_data.drop('Province/State', axis=1, inplace=True)
    global_data.rename(columns={'Country/Region': 'Country'}, inplace=True)
    last_value_column = global_data.columns[-1]
    # get latest count and country, select top 10  by latest count
    df1 = global_data.groupby(['Country']).agg(
        {last_value_column: sum}).reset_index()
    df1.rename(columns={last_value_column: 'last_value'}, inplace=True)

    df2 = df1.sort_values(by='last_value', ascending=False).head(10)
    uniqueCountryNames = list(df2['Country'].values)
    countsVal = list(df2['last_value'].values)

    overallCount = sum(countsVal)

    # print(f"countries: {uniqueCountryNames}, {countsVal}, {overallCount} ")

    countryDataSpe = pd.DataFrame(
        global_data[global_data['Country'] == countryName][global_data.columns[4:-1]].sum()).reset_index()
    countryDataSpe.columns = ['country', 'values']
    countryDataSpe['lagVal'] = countryDataSpe['values'].shift(1).fillna(0)
    countryDataSpe['incrementVal'] = countryDataSpe['values'] - \
        countryDataSpe['lagVal']
    countryDataSpe['rollingMean'] = countryDataSpe['incrementVal'].rolling(
        window=4).mean()
    countryDataSpe = countryDataSpe.fillna(0)
    datasetsForLine = [{'yAxisID': 'y-axis-1', 'label': 'Daily Cumulated Data', 'data': countryDataSpe['values'].values.tolist(), 'borderColor':'#03a9fc', 'backgroundColor':'#03a9fc', 'fill':'false'},
                       {'yAxisID': 'y-axis-2', 'label': 'Rolling Mean 4 days', 'data': countryDataSpe['rollingMean'].values.tolist(), 'borderColor':'#fc5203', 'backgroundColor':'#fc5203', 'fill':'false'}]
    axisvalues = countryDataSpe.index.tolist()

    context = {'countryName': countryName, 'contryNames': uniqueCountryNames,
               'countsVal': countsVal,  'overallCount': overallCount,
               'axisvalues': axisvalues, 'datasetsForLine': datasetsForLine}

    return render(request, 'mychart/dashboard.html', context)
