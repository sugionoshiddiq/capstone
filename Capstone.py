#!/usr/bin/env python
# coding: utf-8

# In[15]:


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


st.write("Tahukah kalian bahwa lembaga Transparency International mengestimasi korupsi telah menyebabkan kerugian finansial secara global sebanyak 5% GDP dunia atau 3.6 Triliun USD setiap tahunnya? Jika dibagikan secara merata ke 7.9 Miliar orang di dunia maka setiap orang harus menanggung 456 USD atau sekitar 7 Juta Rupiah setiap tahunnya. Melalui kondisi ini maka pemberantasan korupsi harus menjadi agenda dunia untuk mencegah kerugian yang lebih besar.")


# In[25]:


df1=pd.read_excel('Data_Boxplot.xlsx') 
means=df1.groupby('Tahun')['Skor'].mean() 
fig, ax=plt.subplots(figsize=(15,6)) 
sns.pointplot(x=means.index,y=means.values, color='green', ax=ax) 
plt.legend(labels=['Rata-rata Skor CPI'],title="Keterangan")
my_pal = {1995:"skyblue", 1996:"skyblue",1997:"skyblue",1998:"skyblue",1999:"skyblue",2000:"skyblue",2001:"skyblue",2002:"skyblue",2003:"skyblue",2004:"skyblue",2005:"skyblue",2006:"skyblue",2007:"skyblue",2008:"skyblue",2009:"skyblue",2010:"skyblue",2011:"skyblue",2012:"m",2013:"m",2014:"m",2015:"m",2016:"m",2017:"m",2018:"m",2019:"m",2019:"m",2020:"m",2021:"m"}
sns.boxplot(data=df1,x='Tahun', y='Skor', ax=ax, showfliers=False, palette=my_pal) 
plt.title("Terdapat Stagnansi Distribusi Skor CPI pada 10 tahun terakhir") 
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
fig = px.scatter(df2, x="T-Index", y="CPI 2021",hover_name='Negara', trendline="ols",title="Terdapat Hubungan Moderat Antara EGDI dengan Indeks Transparansi di Tahun 2021")
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


st.write("Salah satu akar permasalahan terjadinya praktik korupsi adalah sistem yang tidak transparan. Hubungan antara data Indeks transparansi/T-Index dengan skor CPI dimana pada tahun 2021 menunjukkan adanya hubungan positif diantara kedua indeks tersebut. Dengan kata lain, semakin rendah transparansi negara maka negara tersebut akan semakin rendah nilai CPInya atau dapat dikatakan akan semakin tinggi tingkat korupsinya. Pada dasarnya korupsi merupakan permasalahan yang multi-dimensional sehingga nilai korelasi yang bernilai 0.49 bisa disebabkan karena masih adanya faktor lain yang mendukung terciptanya transparansi selain pengembangan E-Government. Berangkat dari data tersebut maka diperlukan suatu sistem yang mendukung peningkatan transparansi.")


# In[ ]:


st.subheader("Peran E-Government")


# In[ ]:


st.write("E-Government merupakan salah satu sistem yang dapat diterapkan untuk meningkatkan transparansi suatu instansi. Simarmata (2017) menyampaikan bahwa pemanfaatan  internet, dalam hal ini e-government, sebagai  alat  transparansi tidak hanya meningkatkan kejujuran aparat pemerintah namun lebih jauh dari itu telah menyumbangkan efektifitas dan efisiensi kinerja pemerintah dalam upaya meningkatkan akuntabilitas dan mencegah terjadinya korupsi. Melalui argumen tersebut maka perlu didalami bagaimana hubungan pengembangan E-government dengan tingkat korupsi.")


# In[ ]:


with st.expander("Apa itu E-Government?"):
    st.write("“E-Government” mengacu pada penggunaan teknologi informasi oleh lembaga pemerintah (seperti Jaringan Area Luas, Internet, dan komputasi bergerak) yang memiliki kemampuan untuk mengubah hubungan dengan warga, bisnis, dan perangkat pemerintah lainnya. Teknologi ini dapat melayani berbagai tujuan yang berbeda: penyampaian layanan pemerintah yang lebih baik kepada warga, interaksi yang lebih baik dengan bisnis dan industri, pemberdayaan warga melalui akses ke informasi, atau manajemen pemerintah yang lebih efisien.")
    st.write("Sumber: https://www.worldbank.org/en/topic/digitaldevelopment/brief/e-government#:~:text=%E2%80%9CE%2DGovernment%E2%80%9D%20refers%20to,and%20other%20arms%20of%20government.")


# In[3]:


df3=pd.read_excel('Plot EGDI CPI.xlsx')
fig3 = px.scatter(df3, x="EGDI", y="CPI", animation_frame="Tahun", hover_name='Negara', size_max=10, title="Tahukah kalian bahwa EGDI selalu memiliki hubungan yang erat dengan CPI setiap tahunnya?")
fig3.update_traces(marker={'size': 10})
st.plotly_chart(fig3)


# In[ ]:


with st.expander("Nilai korelasi per tahun"):
    dfCorrCPIEGDI=pd.read_excel('tabel_korelasi.xlsx')
    st.dataframe(dfCorrCPIEGDI)
    st.write("Nilai korelasi antara CPI dengan EGDI bernilai cukup tinggi setiap tahunnya sehingga pengembangan E-Government erat kaitannya dengan tingkat korupsi di suatu negara")


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


# In[26]:


df4=pd.read_excel('Plot EGDI.xlsx')
means=df4.groupby('Tahun')['Index'].mean() 
fig, ax=plt.subplots(figsize=(15,6)) 
sns.pointplot(x=means.index,y=means.values, color='green', ax=ax) 
plt.legend(labels=['Rata-rata Skor EGDI'],title="Keterangan") 
sns.boxplot(data=df4,x='Tahun', y='Index', ax=ax, color='skyblue', showfliers=False) 
plt.title("Pemusatan Distribusi EGDI Mengalami Peningkatan Setiap Tahun")
st.pyplot(plt)


# In[ ]:


st.write("Pengembangan E-Government dinilai bisa menjadi harapan bagi upaya pemberantasan korupsi. Berdasarkan data indeks EGDI pada tiap tahun pengukurannya dapat dilihat bahwa tingkat pengembangan E-Government di dunia cenderung mengalami peningkatan. Hal ini tentu memberikan harapan bagi dunia bahwa semua negara sedang berusaha meningkatkan tingkat pemanfaatan teknologi dalam tata kelola negaranya. Dimana pada akhirnya memberikan jalan untuk menurunkan praktik korupsi secara khusus dalam meningkatkan transparansi.")


# In[ ]:


st.subheader("Apa yang perlu dipersiapkan oleh setiap negara?")


# In[ ]:


st.image('Kolaborasi.jpg')


# In[21]:


st.write("Setelah kita mengetahui bahwa kondisi E-Government membukakan harapan bagi pemberantasan korupsi, hal selanjutnya yang perlu kita pahami adalah cara untuk mendukung pengembangan E-Government pada suatu negara. Analisis ini menggunakan pendekatan kolaborasi dimana akan dibahas peran masyarakat, sektor bisnis dan sektor pemerintah dalam memaksimalkan perannya untuk meningkatkan pengembangan E-Goernment. Adapun penjabarannya sebagai berikut:")
st.write("1. Masyarakat: Peran dalam partisipasi terhadap sistem elektronik (E-Participation).")
st.write("2. Sektor Bisnis: Peran dalam meningkatkan penetrasi internet mobile (Active mobile-broadband subscriptions).")
st.write("3. Sektor Pemerintah: Peran untuk berkomitmen dalam memberikan layanan publik yang bersih (Government Effectiveness).")


# In[4]:


fig5 = px.scatter(df3, title="Hubungan E-Participation Dengan EGDI Semakin Membentuk Garis Lurus Di Tahun 2014", x="E-Participation", y="EGDI", color="CPI", animation_frame="Tahun", hover_name='Negara', size_max=20)
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


st.write("Berdasarkan grafik diatas dapat dilihat bahwa saat ini penduduk di suatu negara sudah mulai terbiasa untuk menggunakan sistem elektronik yang disediakan oleh pemerintah. Pola keterhubungan ini sudah mulai terlihat jelas sejak tahun 2014. Hal ini menunjukkan bahwa saat ini peningkatan E-Participation terhadap EGDI semakin menuju pada tingkat korelasi yang lebih kuat sehingga semakin penduduk terlibat dalam menggunakan sistem elektronik semakin baik pula tingkat pengembangan E-Government.")


# In[52]:


df5=pd.read_excel('Internet Broadband.xlsx')
fig6 = px.scatter(df5, title="Hubungan Yang Kuat Antara Penetrasi Internet Mobile dan EGDI Mulai Terasa Di Tahun 2012", x="Active mobile-broadband subscriptions per 100 inhabitants", y="EGDI", color="CPI", animation_frame="Tahun", range_x=[0,160], range_y=[0,1], hover_name='Negara', size_max=20)
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


st.write("Sama seperti indeks E-Participation, jumlah langganan mobile-broadband terus meningkat setiap tahunnya. Adapun saat ini korelasi antara pelanggan aktif mobile-broadband dan EGDI semakin membentuk garis lurus sehingga menunjukkan bahwa semakin tinggi proporsi pelanggan aktif mobile broadband memungkinkan tinggi indeks EGDI suatu negara.")


# In[54]:


fig7 = px.scatter(df3, title="Government Effectiveness dan EGDI Terus Membentuk Hubungan Yang Kuat Setiap Tahun", x="Government Effectiveness", y="EGDI", color="CPI", animation_frame="Tahun", hover_name='Negara', size_max=20)
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


st.write("Berdasarkan hasil analisis dapat disampaikan bahwa pemberantasan korupsi melalui pengembangan E-Government merupakan agenda setiap pemangku kepentingan. Tidak hanya komitmen dari sektor pemerintah tetapi kesediaan warga negara menjadi hal penting untuk meningkatkan pendayagunaan sistem elektronik. Adapun tingginya penetrasi internet broadband mobile harus menjadi peluang yang dimanfaatkan oleh pemerintah dalam pengembangan E-Government. Terlebih pada masa pasca covid ini warga negara dinilai telah terbiasa untuk melakukan kegiatan secara virtual. Pada akhirnya saat ini dapat dinilai sebagai momentum yang tepat untuk mengembangkan E-Government shingga dapat meningkatkan tingkat transparansi suatu negara meskipun terdapat stagnansi dalam peningkatan skor CPI secara global.")


# In[ ]:


st.subheader("Referensi")


# In[ ]:


st.write("1. https://aclc.kpk.go.id/action-information/lorem-ipsum/20220411-null")
st.write("2. https://www.weforum.org/communities/gfc-on-transparency-and-anti-corruption")
st.write("3. Simarmata, M.H. 2017. Peranan e-Government dan Media Sosial untuk Mewujudkan Budaya Transparansi dan Pemberantasan Korupsi. Integritas : Jurnal Antikorupsi. 3, 2 (Oct. 2017), 203–230. DOI:https://doi.org/10.32697/integritas.v3i2.108.")
st.write("4. https://www.undp.org/guyana/press-releases/international-anti-corruption-day-2020")
st.write("5. https://www.freepik.com/free-photo/asian-businessmen-businesswomen-meeting-brainstorming-ideas-about-creative-web-design-planning-application-developing-template-layout-mobile-phone-project-working-together-small-office_10075800.html")

