import streamlit as st
import pandas as pd
import plotly.express as px


st.title("🚢Titanic Data Dashboard")
st.write("The Titanic dataset is Based on the real story of the RMS Titanic, a massive British passenger ship that sank in the year 1912 after hitting an iceberg on its first voyage from England to the U.S ")


#Baics stats
st.subheader("1.Dataset Preview")
df=pd.read_csv("ChanDarren_RaiTaran_Lab2a.csv")
df_stat=df.describe()
st.dataframe(df.head())
st.subheader("2.Statistic Info")
st.dataframe(df_stat)

#Gender Distribution.
st.subheader("3.Gender Distribution")
fig1=px.histogram(df,x="Sex",color="Survived",barmode="group",title="Survival Count by Gender")
st.plotly_chart(fig1)

#Age Distribution
st.subheader("4.Age Distribution.")
fig2=px.histogram(df,x="Age",nbins=30,color="Survived",title="Survival Count by Age.")
st.plotly_chart(fig2)

#Fare By Passenger class and Survived.
st.subheader("5. Fare by Passenger Class & Survival.")
fig3=px.box(df,x="Pclass",y="Fare",color="Survived",title="SURVIVAL RATE BY PASSENGER CLASS AND FARE SPENT.")
st.plotly_chart(fig3)

#: C = Cherbourg, Q = Queenstown, S = Southampton.
#Heatmap: Survival Rate By Pclass and Embarked.
st.subheader("6. Survival Rate Heatmap by Class & Embarkation")
df_group1=df.groupby(["Pclass","Embarked"],as_index=False)["Survived"].mean()
pivot_df=df_group1.pivot(index="Pclass",columns="Embarked",values="Survived")
fig4=px.imshow(pivot_df,labels=dict(x="Embarked",y="Passenger class",color="Survived"),color_continuous_scale="Purples",text_auto="Survived",
               title="SURVIVAL RATE HEATMAP BY PASSENGER CLASS AND EMBARKATION")
df_group1
st.plotly_chart(fig4)

df_survived=df[df["Survived"]==1]
df_group2=df_survived.groupby(["Pclass","Sex"],as_index=False)["Survived"].count()
fig5=px.bar(df_group2,x="Sex",y="Pclass",color="Survived",title="SURVIVAL RATE BASED BY PCLASS AND SEX")
st.plotly_chart(fig5)