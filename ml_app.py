import numpy as np
import pandas as pd
import pickle
from sklearn import *

df = pickle.load(open('df.pkl','rb'))
model = pickle.load(open('rf.pkl','rb'))

st.title('Laptop Price Prediction')
st.header('Fill Details to Predict Price of Laptop')

#Fetures
#Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',
 #      'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],
     # dtype='object')

company = st.selectbox('Company',df['Company'].unique())
typeName = st.selectbox('TypeName',df['TypeName'].unique())
ram = st.selectbox('RAM(in GB)',[8, 16, 4 , 2, 12, 6, 32, 24,64])
weight = st.number_input('Weight of the Laptop')
touchscreen = st.selectbox('TouchScreen',['Yes','No'])
ips = st.selectbox('IPS',['Yes','No'])
cpu = st.selectbox('CPU brand',df['Cpu brand'].unique())
hdd = st.selectbox('HDD',[0, 500, 1000, 2000, 32, 128])
ssd = st.selectbox('SSD',[0, 128, 256, 512, 32, 64, 1000, 1024, 16, 768, 180, 240, 8])
gpu = st.selectbox('GPU',df[df['Gpu brand'].unique()])
os = st.selectbox('OS',df['os'].unique())