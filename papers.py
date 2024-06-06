import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
def titles_author(author_profile_url):
    page_number = 0
    n=0
    data=[]
    data_author=set()
    while True:
        
        url=f"{author_profile_url}&cstart={page_number * 20}"
        response=requests.get(url,headers=headers)
        #print(response)
        new_papers=True
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paper_links = soup.find_all('a', {'class': 'gsc_a_at'})
            year_elements = soup.find_all('span', {'class': 'gsc_a_h gsc_a_hc gs_ibl'})
            
            for link, year_elem in zip(paper_links,year_elements):
                title = link.text
                year = year_elem.text.strip()
                print(title,year)
                #paper_id=(year,title)
                if title not in data_author:
                    data.append({'Title': title, 'Year': year})
                    data_author.add(title)

            if not paper_links:
                new_papers = False
                break
            page_number+=1
            #print(n,new_papers)
        if new_papers==False:
            break
    return data
    #print('saliendo')

soares='https://scholar.google.com/citations?hl=es&user=EwWccccAAAAJ&view_op=list_works&sortby=pubdate'
hans='https://scholar.google.com/citations?hl=es&user=IuhidDAAAAAJ&view_op=list_works&sortby=pubdate'

miller='https://scholar.google.com/citations?hl=es&user=1QxL70MAAAAJ&view_op=list_works&sortby=pubdate'
jazmin='https://scholar.google.com/citations?hl=es&user=02cfJoAAAAAJ&view_op=list_works&sortby=pubdate'

#authors=['hans','soares']
#auth=[miller,jazmin]
auth=[hans,soares]

'''for i in range(0,len(auth)):
    papers1=titles_author(auth[i])
    df_name = f"df{i+1}"
    globals()[df_name] = pd.DataFrame(papers1)'''
papers1=titles_author(hans)
df1=pd.DataFrame(papers1)
papers2=titles_author(soares)
df2=pd.DataFrame(papers2)

common_titles_df = pd.merge(df1, df2, on='Title')

common_titles_df = common_titles_df.rename(columns={'Year_x': 'Year'})
common_titles_df = common_titles_df.sort_values(by='Year')
print(common_titles_df)
filtered_df2 = common_titles_df.iloc[:, :-1]
filtered_df2.to_csv('filtered_papers.csv',sep=';', index=False)