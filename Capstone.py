#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import plotly.express as px


# In[100]:


st.title("Memberantas Korupsi Melalui *E-Government*")


# In[ ]:


st.image('korupsi.jpg')


# In[ ]:


st.subheader("Korupsi, pencucian uang, dan penghindaran pajak merupakan masalah global, tidak hanya tantangan bagi negara berkembang. - Sri Mulyani")


# In[ ]:


st.write("Definisi korupsi berdasarkan World Bank tahun 2000 (definisi standar internasional) merujuk pada penyalahgunaan kekuasaan publik untuk keuntungan pribadi. Melalui definisi tersebut maka sudah dipastikan terdapat kerugian yang terjadi atas korupsi sehingga sebisa mungkin praktik tersebut diberantas hingga tingkat global.")


# In[ ]:


st.subheader("Apa masalah besarnya?")


# In[ ]:


st.write("Tahukah kalian bahwa lembaga Transparency International mengestimasi korupsi telah menyebabkan kerugian finansial secara global sebanyak 5% GDP dunia atau 3.6 Triliun USD setiap tahunnya? Jika dibagikan secara merata ke 7.9 Miliar orang di dunia maka setiap orang bisa mendapatkan 456 USD atau sekitar 7 Juta Rupiah setiap tahunnya dari kerugian tersebut. Melalui kondisi ini maka pemberantasan korupsi harus menjadi agenda dunia untuk mencegah kerugian yang lebih besar.")


# In[59]:


df1=pd.read_excel('Data_Boxplot.xlsx') 
means=df1.groupby('Tahun')['Skor'].mean() 
fig, ax=plt.subplots(figsize=(15,6)) 
sns.pointplot(x=means.index,y=means.values, color='green', ax=ax) 
plt.legend(labels=['Rata-rata Skor CPI'],title="Keterangan") 
sns.boxplot(data=df1,x='Tahun', y='Skor', ax=ax, showfliers=False) 
plt.title("Distribusi Nilai CPI Tahun 1995-2021") 
st.pyplot(plt)


# In[ ]:


#Eksplanasi CPI
with st.expander("Penjelasan CPI"):
    st.write("""
       Indeks Persepsi Korupsi (IPK)/Corruption Perception Index (CPI) adalah index hasil survei yang dipublikasikan oleh organisasi non-pemerintah internasional Transparency International yang memeringkat 180 negara berdasarkan tingkat korupsi sektor publik yang mereka rasakan. 
       Rentang skor Indeks Persepsi Korupsi berada di antara 0 hingga 100, yang berarti 0-19 Sangat Korup, 20-39 Cenderung Korup, 40-59 Rentan Korup, 60 – 79 Cenderung Bersih, 80-100 Sangat bersih.
       """)
    st.write("akses data: https://www.transparency.org/en/cpi/2021")


# In[23]:


st.write("Namun begitu korupsi menjadi salah satu permasalahan tata kelola negara yang dinilai cukup sulit untuk diberantas. Data terkait skor Corruption Perception Index/CPI menunjukkan bahwa nilai rata-rata skor CPI di 10 tahun terakhir berada di sekitar angka 42-43 (dalam skala 100). Angka tersebut menunjukkan bahwa upaya dunia dalam memberantas korupsi berada pada posisi yang stagnan. Melalui fakta ini maka dibutuhkan solusi yang tepat untuk memberantas korupsi mulai dari akarnya.")


# In[4]:


df2=pd.read_excel('Plot2.xlsx')
fig = px.scatter(df2, x="T-Index", y="CPI 2021",hover_name='Negara',marginal_y="box",
           marginal_x="box", trendline="ols",title="Hubungan antara Index Transparansi dengan CPI Tahun 2021")
cor_plot2 = np.round_(np.corrcoef(df2['T-Index'], df2['CPI 2021'])[0,1],2)
fig.add_annotation(x=30, y=85,
            text='Nilai korelasi: %.2f' % cor_plot2,
            showarrow=False)
st.plotly_chart(fig)


# In[ ]:


#Eksplanasi T-Index
with st.expander("Penjelasan T-Index"):
    st.write("""
        Index Transparansi/Transparency Index/T-Index merupakan suatu index yang dipublikasikan oleh European Research Centre for Anti-corruption and State-Building. 
        Tujuan perhitungan T-Index adalah untuk menyediakan alat yang dapat mengukur transparansi secara aktual, dengan fokus pada menangkap dimensi yang relevan untuk mengendalikan korupsi.
        Konsep transparansi adalah informasi publik minimal yang tersedia dan dapat diakses (bebas biaya) yang diperlukan untuk mencegah korupsi dan memungkinkan akuntabilitas publik dalam masyarakat.
    """)
    st.write("akses data: https://www.againstcorruption.eu/ercas-projects/transparencyindex/")


# In[ ]:


st.write("Salah satu akar permasalahan terjadinya praktik korupsi adalah sistem yang tidak transparan. Hubungan antara data Indeks transparansi/T-Index dengan skor CPI dimana pada tahun 2021 menunjukkan adanya hubungan positif diantara kedua indeks tersebut. Dengan kata lain, semakin rendah transparansi negara maka negara tersebut akan semakin rendah nilai CPInya atau dapat dikatakan akan semakin tinggi tingkat korupsinya. Berangkat dari data tersebut maka diperlukan suatu sistem yang mendukung peningkatan transparansi.")


# In[ ]:


st.subheader("Peran E-Government")


# In[ ]:


st.write("E-Government merupakan salah satu sistem yang dapat diterapkan untuk meningkatkan transparansi suatu instansi. Simarmata (2017) menyampaikan bahwa pemanfaatan  internet, dalam hal ini e-government, sebagai  alat  transparansi tidak hanya meningkatkan kejujuran aparat pemerintah namun lebih jauh dari itu telah menyumbangkan efektifitas dan efisiensi kinerja pemerintah dalam upaya meningkatkan akuntabilitas dan mencegah terjadinya korupsi. Melalui argumen tersebut maka perlu didalami bagaimana hubungan pengembangan E-government dengan tingkat korupsi.")


# In[48]:


df3=pd.read_excel('Plot EGDI CPI.xlsx')
fig3 = px.scatter(df3, x="EGDI", y="CPI", animation_frame="Tahun", hover_name='Negara', size_max=10, title="Hubungan EGDI dengan CPI")
fig3.update_traces(marker={'size': 10})
st.plotly_chart(fig3)


# In[ ]:


#Eksplanasi EGDI
with st.expander("Penjelasan EGDI"):
    st.write("""
        Indeks Pembangunan E-Government/E-Government Development Index/EGDI menyajikan keadaan Pembangunan E-Government pada negara-negara Anggota Perserikatan Bangsa-Bangsa (PBB). 
        Seiring dengan penilaian pola pengembangan situs web di suatu negara, indeks Pengembangan E-Government menggabungkan karakteristik akses, seperti infrastruktur dan tingkat pendidikan, untuk mencerminkan bagaimana suatu negara menggunakan teknologi informasi dalam rangka mempromosikan akses dan inklusi masyarakatnya. 
        EGDI adalah ukuran gabungan dari tiga dimensi penting e-government, yaitu: penyediaan layanan online, konektivitas telekomunikasi, dan kapasitas manusia. 
    """)
    st.write("akses data: https://publicadministration.un.org/egovkb/en-us/Data-Center")


# In[114]:


st.write("Hubungan antara indeks pengembangan E-Government/EGDI dengan skor CPI di setiap tahun menyatakan bahwa ada hubungan positif diantara keduanya. Hal ini menunjukkan bahwa negara yang mengembangkan e-government dengan baik memiliki tingkat transparansi yang tinggi dan tingkat korupsi yang rendah.")


# In[60]:


df4=pd.read_excel('Plot EGDI.xlsx')
means=df4.groupby('Tahun')['Index'].mean() 
fig, ax=plt.subplots(figsize=(15,6)) 
sns.pointplot(x=means.index,y=means.values, color='green', ax=ax) 
plt.legend(labels=['Rata-rata Skor EGDI'],title="Keterangan") 
sns.boxplot(data=df4,x='Tahun', y='Index', ax=ax, showfliers=False) 
plt.title("Distribusi Nilai EGDI") 
st.pyplot(plt)


# In[ ]:


st.write("Pengembangan E-Government dinilai bisa menjadi harapan bagi upaya pemberantasan korupsi. Berdasarkan data indeks EGDI pada tiap tahun pengukurannya dapat dilihat bahwa tingkat pengembangan E-Government di dunia cenderung mengalami peningkatan. Hal ini tentu memberikan harapan bagi dunia bahwa semua negara sedang berusaha meningkatkan tingkat pemanfaatan teknologi dalam tata kelola negaranya. Dimana pada akhirnya memberikan jalan untuk menurunkan praktik korupsi.")


# In[ ]:


st.subheader("Apa yang perlu dipersiapkan oleh setiap negara?")


# In[21]:


st.write("Setelah kita mengetahui bahwa kondisi E-Government membukakan harapan bagi pemberantasan korupsi, hal selanjutnya yang perlu kita pahami adalah cara untuk mendukung pengembangan E-Government pada suatu negara. Analisis ini akan membedah bagaimana partisipasi publik dalam menggunakan sistem elektronik, tingkat penetrasi internet mobile-broadband dan komitmen pemerintah dalam memberikan layanan publik dapat memengaruhi tingkat EGDI")


# In[51]:


fig5 = px.scatter(df3, title="Hubungan antara E-Participation, EGDI, dan CPI", x="E-Participation", y="EGDI", color="CPI", animation_frame="Tahun", hover_name='Negara', size_max=20)
fig5.update_traces(marker={'size': 20})
st.plotly_chart(fig5)


# In[ ]:


#Eksplanasi E-Participation
with st.expander("Penjelasan E-Participation"):
    st.write("""
        Indeks E-Participation adalah indeks tambahan untuk United Nations E-Government Survey. 
        Indeks E-Participation suatu negara mencerminkan mekanisme e-partisipasi yang diterapkan oleh pemerintah dibandingkan dengan semua negara lain. Tujuan dari perhitungan indeks ini ditujukan untuk menawarkan wawasan tentang bagaimana berbagai negara menggunakan alat online dalam mempromosikan interaksi antara pemerintah dan rakyatnya, serta di antara rakyat, untuk kepentingan semua. 
        Komponen dalam indeks E-Participation adalah E-Information, E-Consultation, dan E-Decision-Making.
    """)
    st.write("Akses data: https://publicadministration.un.org/egovkb/Data-Center")


# In[ ]:


st.write("Berdasarkan grafik diatas dapat dilihat bahwa saat ini penduduk di suatu negara sudah mulai terbiasa untuk menggunakan sistem elektronik yang disediakan oleh pemerintah. Nilai E-participation terus bertumbuh ke arah kanan sumbu x dan diikuti dengan pola garis lurus yang semakin terbentuk terhadap EGDI. Hal ini menunjukkan bahwa saat ini peningkatan E-Participation terhadap EGDI semakin menuju pada tingkat korelasi yang lebih kuat sehingga semakin penduduk terlibat dalam menggunakan sistem elektronik semakin baik pula tingkat pengembangan E-Government.")


# In[52]:


df5=pd.read_excel('Internet Broadband.xlsx')
fig6 = px.scatter(df5, title="Hubungan antara Active mobile-broadband subscriptions per 100 inhabitants, EGDI, dan CPI", x="Active mobile-broadband subscriptions per 100 inhabitants", y="EGDI", color="CPI", animation_frame="Tahun", range_x=[0,160], range_y=[0,1], hover_name='Negara', size_max=20)
fig6.update_traces(marker={'size': 20})
st.plotly_chart(fig6)


# In[ ]:


#Eksplanasi Mobile Internet Broadband 
with st.expander("Penjelasan Active mobile-broadband subscriptions per 100 inhabitants"):
    st.write("""
        Infrastruktur komunikasi mendukung penggunaan teknologi digital. Mobile broadband adalah infrastruktur utama yang memungkinkan tidak hanya konektivitas tetapi juga perangkat yang terhubung. Indikator ini mengukur penyerapan teknologi mobile broadband oleh penduduk, dinyatakan sebagai jumlah langganan per 100 penduduk ke layanan jaringan seluler yang menawarkan kecepatan 256 Kbps atau lebih (seperti akses paket kecepatan tinggi (HSPA) dan evolusi jangka panjang (LTE)).
    """)
    st.write("Akses data: https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx")


# In[ ]:


st.write("Sama seperti indeks E-Participation, jumlah langganan mobile-broadband terus meningkat setiap tahunnya. Bahkan mulai tahun 2012 mulai terdapat seseorang yang berlangganan lebih dari 1 layanan mobile-broadband. Adapun saat ini korelasi antara pelanggan aktif mobile-broadband dan EGDI semakin membentuk garis lurus sehingga menunjukkan bahwa semakin tinggi proporsi pelanggan aktif mobile broadband memungkinkan tinggi indeks EGDI suatu negara.")


# In[54]:


fig7 = px.scatter(df3, title="Hubungan antara Government Effectiveness, EGDI, dengan CPI", x="Government Effectiveness", y="EGDI", color="CPI", animation_frame="Tahun", hover_name='Negara', size_max=20)
fig7.update_traces(marker={'size': 20})
st.plotly_chart(fig7)


# In[ ]:


#Eksplanasi Government Effectiveness
with st.expander("Penjelasan Government Effectiveness"):
    st.write("""
        Indeks efektivitas pemerintah adalah indeks yang dielaborasi oleh Grup Bank Dunia dalam mengukur kualitas layanan publik, layanan sipil, perumusan kebijakan, implementasi kebijakan, dan kredibilitas komitmen pemerintah untuk meningkatkan atau mempertahankan kualitas tersebut.
    """)
    st.write("Akses data: https://info.worldbank.org/governance/wgi/")


# In[ ]:


st.write("Dibalik keterlibatan warga dan infrastruktur internet yang memadai, komitmen pemerintah dalam memberikan layanan publik yang bersih turut menjadi faktor dalam peningkatan EGDI. Hal ini dapat terlihat bahwa setiap tahun hubungan antara Government Effectiveness dengan EGDI membentuk garis lurus yang solid. Hal ini menunjukkan bahwa tingkat pengembangan E-Government turut ditentukan oleh bagaimana lembaga pemerintahan berkomitmen untuk memberikan layanan yang berkualitas.")


# In[21]:


st.subheader("Kesimpulan")


# In[ ]:


st.write("Berdasarkan hasil analisis dapat disampaikan bahwa pemberantasan korupsi melalui pengembangan E-Government merupakan agenda setiap pemangku kepentingan. Tidak hanya komitmen pemerintah tetapi kesediaan warga negara menjadi hal penting untuk meningkatkan pendayagunaan sistem elektronik. Adapun tingginya penetrasi internet broadband mobile harus menjadi peluang yang dimanfaatkan oleh pemerintah dalam pengembangan E-Government. Terlebih pada masa pasca covid ini warga negara dinilai telah terbiasa untuk melakukan kegiatan secara virtual. Pada akhirnya saat ini dapat dinilai sebagai momentum yang tepat untuk mengembangkan E-Government sehingga diharapkan menghasilkan peningkatan dalam skor persepsi korupsi secara global.")

