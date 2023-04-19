import pandas as pd
import streamlit as st
import io
import requests
pd.set_option('display.max_columns', None)
st.set_page_config(layout="wide")  #use 'wide' mode and use column controls to make it two-column website?

#streamlit run "C:/Users/yuhao1/Desktop/diversity/landing page.py"

st.title('Office of Institutional Research and Assessment Data Inventory')
st.text("")


search1 = st.text_input('Search Box')
option1 = st.radio("Search By", ('Title','Content'),horizontal=True)
st.text("")
st.text("")


c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    cka = st.selectbox('Domain',(' ','Student', 'Employee', 'Program', 'Department', 'Finance', 'Training'))
with c2:
    mhk = st.selectbox('Type',(' ','Excel', 'PDF', 'Power BI Dashboard', 'Website'))
with c3:
    mhk = st.selectbox('Access Level',(' ','Public', 'Internal', 'OIRA Only'))
option2 = st.radio("Sort By", ('Name','Type','Domain', 'Responsible Office'),horizontal=True)
st.text("")
st.text("")

d1, d2, d3, d4, d5, d6, d7 = st.columns([1, 1, 3, 1, 2, 1, 1])
with d1:
    st.subheader("Name")
with d2:
    st.subheader("Type")
with d3:
    st.subheader("Description")
with d4:
    st.subheader("Domain")
with d5:
    st.subheader("Responsible Office")
with d6:
    st.subheader("Access Level")
with d7:
    st.subheader("Visit")

st.write (u'\u2500' * 150)

e1, e2, e3, e4, e5, e6, e7 = st.columns([1, 1, 3, 1, 2, 1, 1])
with e1:
    st.write("Academic Program Review and Revitalization")
with e2:
    st.write("Power BI Dashboard")
with e3:
    st.write("Programs by 5-year change in enrollment; headcounts; degrees conferred; admission funnel; enrolled termst o degree by graduation year; program demand trends; undergraduate student learning outcomes; freshman retention and completion rates")
with e4:
    st.write("Program")
with e5:
    st.write("Office of Institutional Research and Assessment")
with e6:
    st.write("Internal")
with e7:
    st.write("[Visit](https://app.powerbi.com/groups/b98a8ec7-54b2-4a8a-86af-35faab818004/reports/5d6d52a7-cfd6-4080-ad93-bb434bdf4230/ReportSection3f3d540c2b5787230238)")
st.write (u'\u2500' * 150)

e1, e2, e3, e4, e5, e6, e7 = st.columns([1, 1, 3, 1, 2, 1, 1])
with e1:
    st.write("Applicant - Hire Demographics")
with e2:
    st.write("Power BI Dashboard")
with e3:
    st.write("Applicant to hire rates by race and gender; applicant pool demographics;unsuccessful application by race and gender; total hires by employee type by race, gender and year;")
with e4:
    st.write("Employee")
with e5:
    st.write("Office of Institutional Research and Assessment")
with e6:
    st.write("Internal")
with e7:
    st.write("[Visit](https://app.powerbi.com/groups/b98a8ec7-54b2-4a8a-86af-35faab818004/reports/bdb513f2-77bb-4f9d-b598-35e931a6098c/ReportSectionbd7bd44d0b0679284215)")
st.write (u'\u2500' * 150)

#
#
#
# st.title('DEIB Resources Inventory')
# st.text("")
#
# ######sort##########
# st.sidebar.text("")
# st.sidebar.text("")
# option1 = st.sidebar.selectbox('Sort by',('Title', 'Submitter', 'Location'))
# st.sidebar.write('You selected:', option1)
#
# if option1=='Submitter' :
#     option1='Name'
# if option1=='Location' :
#     option1='Location of effort (city/state/country/etc.)'
#
# option1_1 = st.sidebar.radio("Order", ('Ascending','Descending'))
# if option1_1=='Ascending' :
#     option1_1=True
# if option1_1=='Descending' :
#     option1_1=False
# ########################
#
#
# ######tag##########
# st.sidebar.text("")
# st.sidebar.text("")
# st.sidebar.text("")
# option2=st.sidebar.multiselect('Select All Tags that apply',
#                                ['Age','Culture' ,'Different Ideas and Perspectives','Disability','Ethnicity','First Generation Status','Familial Status',
#                                 'Gender Identity and Expression','Geographic Background','Marital Status','National Origin','Race', 'Religious and Spiritual Beliefs'
#                                 ,'Sex','Sexual Orientation','Socioeconomic Status','Student Organization','Veteran Status'],help='Select as many tags as you want')
# ########################
#
#
# ###########download form##########
# st.sidebar.text("")
# st.sidebar.text("")
# st.sidebar.text("")
# st.sidebar.write("Visit our [website](https://www.k-state.edu/diversity-inclusion) for more information")
# # st.sidebar.download_button(
# #     label="Download Form",
# #     data=DEIBInventoryForm,
# #     file_name='form.pdf')
# ########################
#
#
# ######title##########
# title_lis=original_df['Title'].values.tolist()
# title=st.multiselect('Go to',title_lis,help='Select as many events as you want')
# if not title:
#     title_lis1 = title_lis
# else:
#     title_lis1=title
# ########################
#
#
# ######search and check##########
# search1 = st.text_input('Search Title and Description')
#
# c1, c2 = st.columns([3, 2])
# with c1:
#     cka = st.checkbox('Expand All')
# with c2:
#     mhk = st.checkbox('See Manhattan Campus Only',help='Check this box to ignore events in Salina and Olathe campus')
# st.text("")
#
# if cka:
#     check1=True
# else:
#     check1=False
#
# if mhk:
#     check2='Manhattan'
# else:
#     check2=','
# ########################
#
#
#
# df=original_df.sort_values(by=option1, ascending=option1_1)
#
# df=df[df['Title'].isin(title_lis1)
# &df[['Title', 'Brief Description for Listing']].apply(lambda x: x.str.contains(search1, case=False)).any(axis=1)
# & df['Location of effort (city/state/country/etc.)'].str.contains(check2,case=False)
# & df['Tags (Please select all categories that apply)'].apply(lambda x: all(word in x for word in option2))]
# # df=df[df['Location of effort (city/state/country/etc.)'].str.contains(check2,case=False)]
#
# key = 0
# for i,j in df.iterrows():  # i is index, j is the row content
#     #print (j)
#     # print (j['Title'])
#     # print ('Organized by: '+j['Name']+'   ' + 'At: '+str(j['Location of effort (city/state/country/etc.)']))
#     # print (j['Brief Description for Listing'])
#     # print ('Web: '+j['Website'])
#     # print ('Full Description: '+j['Description'].replace("\n", " ")+'\nFrequency: '+j['Frequency']+'\nSubmitted at: '+str(j['Completion time'])
#     #        +'\nContact: '+j['Contact (please provide principle contact name and email/preferred contact number)']+'\nUnit: '+j['College/Academic Unit/Office'])
#     # print (u'\u2500' * 50)   #print a horizon line
#
#     st.subheader(j['Title'])
#
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         st.caption('Submitted by: ' + j['Name'])
#     with col2:
#         st.caption('At: '+str(j['Location of effort (city/state/country/etc.)']))
#
#     st.write(j['Brief Description for Listing'])
#
#     st.write('Web: '+j['Website'])
#
#
#
#     with st.expander("See more details", expanded=check1):
#         st.write('Full Description: '+j['Description'].replace("\n", " "))
#         st.write('Contact: '+j['Contact (please provide principle contact name and email/preferred contact number)'])
#         st.write('Tag: ' + j['Tags (Please select all categories that apply)'].replace(";", ", ").rstrip(', '))
#         st.write('Audience: ' + j['Audience (Please select all that apply)'].replace(";", ", ").rstrip(', '))
#         st.text('Frequency: '+j['Frequency']+'\nSubmitted at: '+str(j['Completion time'])+'\nUnit: '+j['College/Academic Unit/Office']
#                 + '\nEffort Dates: ' + str(j["This Year's Effort Dates (Start Date)"])+'\nPartners: ' +str(j['Collaborative Partner(s)'])
#                 + '\nNumber of Participants: ' + str(j['Number of Participants (please provide your best estimate if/when applicable)'])
#                 + '\nEffort Type: ' + j['Effort Type (Please select all categories that apply)'].replace(";", ", ").rstrip(', '))
#
#         st.download_button(
#             label="Download Form",
#             data=DEIBInventoryForm,
#             key=key,
#             file_name='form.pdf')
#
#     st.write (u'\u2500' * 62)   #print a horizon line
#
#     key = key + 1

