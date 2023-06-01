import pandas as pd
import streamlit as st
import io
import requests
import os
pd.set_option('display.max_columns', None)
st.set_page_config(layout="wide")  #use 'wide' mode and use column controls to make it two-column website?

#streamlit run "C:/Users/yuhao1/Desktop/diversity/landing_online.py"

st.write("username:", st.secrets["username"])
st.write("password:", st.secrets["password"])
st.write(
    "Has environment variables been set:",
    os.environ["username"] == st.secrets["password"],
)

st.title('Office of Institutional Research and Assessment Data Inventory')
st.text("")
st.text("")


c1, c2, c3 = st.columns([5, 0.1, 1])
with c1:
    search1 = st.text_input('Search Box (To search, type in key words and press Enter; To cancel search, clear all texts in the search box and press enter)',
                            help='Will return resources where name or contents contain the words searched here')
with c3:
    option1 = st.radio("Search By", ('Name','Contents'),horizontal=True)
st.text("")
st.text("")
st.text("")


c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    domain = st.multiselect('Domain (all selected by default)',('Student', 'Employee', 'Program', 'Department', 'Finance', 'Training'))
with c2:
    type = st.multiselect('Type (all selected by default)',('Excel', 'PDF', 'Power BI Dashboard', 'Website'))
with c3:
    level = st.multiselect('Access Level (all selected by default)',('Public', 'Internal', 'Restricted'))

c1, c2 = st.columns([1, 2])
with c1:
    sortby = st.radio("Sort By", ('Name','Type','Data Domain', 'Responsible Office'),horizontal=True)
with c2:
    orderby = st.radio("Sort Order", ('Ascending', 'Descending'), horizontal=True)
st.text("")
st.text("")
st.text("")


d1, d2, d3, d4, d5, d6, d7 = st.columns([2, 1, 3, 1, 1.5, 1, 0.5])
with d1:
    st.subheader("Name",anchor=None)
with d2:
    st.subheader("Type",anchor=None)
with d3:
    st.subheader("Contents",anchor=None)
with d4:
    st.subheader("Data Domain",anchor=None)
with d5:
    st.subheader("Responsible Office",anchor=None)
with d6:
    st.subheader("Access Levels",anchor=None)
with d7:
    st.subheader("Visit",anchor=None)
st.divider()


@st.cache_data
def get_df():
    url = 'https://github.com/660324/Landing-Page/blob/main/inventory.csv?raw=true'
    df = pd.read_csv(url,index_col=False)
    return df

#df=original_df[original_df['Include']=='Yes']
df=get_df()

if option1=='Name' :
    k='Name'
if option1=='Contents' :
    k='Contents'


if domain==[]:
    domain=['Student', 'Employee', 'Program', 'Department', 'Finance', 'Training']
if type==[]:
    type=['Excel', 'PDF', 'Power BI Dashboard', 'Website']
if level==[]:
    level=['Public', 'Internal', 'Restricted']

df=df[df['Data Domain'].apply(lambda x: any(word in x for word in domain)) & df['Type'].apply(lambda x: any(word in x for word in type))
               & df['Access Levels'].apply(lambda x: any(word in x for word in level)) & df[k].str.contains(search1,case=False) ]

if orderby=='Ascending' :
    orderby=True
if orderby=='Descending' :
    orderby=False

df=df.sort_values(by=sortby, ascending=orderby)

list = df.values.tolist()

for i in list:
    e1, e2, e3, e4, e5, e6, e7 = st.columns([2, 1, 3, 1, 1.5, 1, 0.5])
    with e1:
        st.write(i[1].replace("\n", " "))
    with e2:
        st.write(i[3].replace("\n", " "))
    with e3:
        st.write(i[4].replace("\n", " "))
    with e4:
        st.write(i[5].replace("\n", " "))
    with e5:
        st.write(i[6].replace("\n", " "))
    with e6:
        st.write(i[7].replace("\n", " "))
    with e7:
        link="[Visit]"+"("+ i[2]+")"
        st.write(link)
    st.divider()
