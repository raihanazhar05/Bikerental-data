import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset yang telah dibersihkan
day_df = pd.read_csv('/cleaned_day_data.csv')
hour_df = pd.read_csv('/cleaned_hour_data.csv')

# Judul laman Streamlit
st.title("Analisis Data Bike Sharing (Bike Rental Dataset)")

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
options = st.sidebar.radio("Pilihan", ['Dampak Cuaca', 'Puncak Waktu dan Hari'])

# Dampak cuaca terhadap penyewaan/rental sepeda
if options == 'Dampak Cuaca':
    st.header("Dampak Cuaca terhadap Penyewaan/Rental Sepeda")

    # Scatter plot untuk menunjukkan hubungan antara kondisi cuaca dan jumlah penyewaan/rental sepeda
    st.subheader("Temperatur vs Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(data=day_df, x='temp', y='cnt', ax=ax)
    ax.set_title('Temperatur vs Penyewaan Sepeda')
    st.pyplot(fig)

    st.subheader("Kelembaban vs Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(data=day_df, x='hum', y='cnt', ax=ax)
    ax.set_title('Kelembaban vs Penyewaan Sepeda')
    st.pyplot(fig)

    st.subheader("Kecepatan Angin vs Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(data=day_df, x='windspeed', y='cnt', ax=ax)
    ax.set_title('Kecepatan Angin vs Penyewaan Sepeda')
    st.pyplot(fig)

    # Correlation heatmap untuk korelasi kondisi cuaca dan jumlah penyewaan/rental sepeda
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(day_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

# Puncak Waktu dan Hari untuk Penyewaan/Rental Sepeda
elif options == 'Puncak Waktu dan Hari':
    st.header("Puncak Waktu dan Hari untuk Penyewaan/Rental Sepeda")

    if 'hr' in hour_df.columns:
        hour_df['hour'] = hour_df['hr']
    else:
        hour_df['hour'] = pd.to_datetime(hour_df['dteday']).dt.hour

    # Rata-rata Jumlah Penyewaan/Rental Sepeda dalam 24 jam
    st.subheader("Rata-rata Jumlah Penyewaan/Rental Sepeda dalam 24 jam")
    hourly_rentals = hour_df.groupby('hour')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=hourly_rentals, x='hour', y='cnt', ax=ax)
    ax.set_title('Rata-rata Jumlah Penyewaan/Rental Sepeda dalam 24 jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan/Rental Sepeda')
    st.pyplot(fig)

    # Rata-rata Jumlah Penyewaan/Rental Sepeda tiap hari dalam 1 minggu
    st.subheader("Rata-rata Jumlah Penyewaan/Rental Sepeda Setiap Hari dalam 1 Minggu")
    daily_rentals = day_df.groupby('day')['cnt'].mean().reset_index()
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    daily_rentals['day'] = daily_rentals['day'].apply(lambda x: days[x])
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=daily_rentals, x='day', y='cnt', ax=ax)
    ax.set_title('Rata-rata Jumlah Penyewaan/Rental Sepeda Setiap Hari dalam 1 Minggu')
    ax.set_xlabel('Hari')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan/Rental Sepeda')
    st.pyplot(fig)

    # Rata-rata jumlah Penyewaan/Rental Sepeda tiap Bulannya
    st.subheader("Rata-rata jumlah Penyewaan/Rental Sepeda tiap Bulannya")
    monthly_rentals = day_df.groupby('month')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=monthly_rentals, x='month', y='cnt', ax=ax)
    ax.set_title('Rata-rata jumlah Penyewaan/Rental Sepeda tiap Bulannya')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan/Rental Sepeda')
    st.pyplot(fig)

# Footer
st.sidebar.markdown("""
---
Untuk submission akhir kelas Belajar Analisis Data dengan Python
""")
