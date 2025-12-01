import streamlit as st
import pandas as pd
import plotly.express as px

# Statistik ringkasan
total_balita = len(data)
avg_birthweight = round(data['I05A'].mean(),2)
avg_birthlength = round(data['I07'].mean(),2)
avg_gest_age = round(data['I04'].mean(),2)

# 1. Tren berat lahir vs usia kehamilan
trends_birthweight = data.groupby('I04')['I05A'].mean().reset_index()
fig_trend = px.line(trends_birthweight, x='I04', y='I05A', 
                    title='Tren Rata-rata Berat Lahir Berdasarkan Usia Kehamilan')

# 2. Histogram panjang lahir
fig_length_dist = px.histogram(data, x='I07', nbins=30, 
                               title='Distribusi Panjang Lahir')

# 3. Berat lahir berdasarkan jenis kelamin
fig_gender_weight = px.box(data, x='B4K4', y='I05A', color='B4K4',
                           title='Berat Lahir Berdasarkan Jenis Kelamin')

# 4. Panjang lahir berdasarkan jenis kelamin
fig_gender_length = px.box(data, x='B4K4', y='I07', color='B4K4',
                           title='Panjang Lahir Berdasarkan Jenis Kelamin')

# 5. Scatter hubungan panjang dan berat lahir
fig_scatter = px.scatter(data, x='I07', y='I05A', color='B4K4',
                         title='Hubungan Panjang & Berat Lahir')

# 6. Distribusi balita per provinsi
prov_summary = data.groupby('B1R1').agg(
    count=('B4K4','count'),
    avg_weight=('I05A','mean'),
    avg_length=('I07','mean')
).reset_index()

fig_prov = px.bar(prov_summary, x='B1R1', y='count',
                  title='Distribusi Balita per Provinsi')
