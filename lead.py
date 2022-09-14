from dataclasses import replace
from pprint import pprint
import  requests
from bs4 import BeautifulSoup


#read all elements in bitrix and put contact in old list and comparsion with new contact
url  = 'https://b24-8w7tjp.bitrix24.com/rest/1/bgrb1zcnrq98r55u/lists.element.get.json?IBLOCK_TYPE_ID=bitrix_processes&IBLOCK_ID=31'
r = requests.get(url)
el = r.json()['result']
old = []
for i in el :
    for k ,l in i['PROPERTY_117'].items():
        old.append(l)


  



#list of Type company
company_type=['طبية',
    'قانونية',
    'تعليم',
    'سياحة',
    'ترجمة',
    'تقنية وبرمجات',
    'محاسبة',
    'سكرتارية',
    'اعلام',
    'مبيعات وتسويق',
    'شحن ونقل']
# links 
cont =['https://www.adwhit.com/%D8%A7%D9%84%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%A9',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D9%82%D8%A7%D9%86%D9%88%D9%86%D9%8A%D8%A9-%D9%88%D8%A7%D8%B3%D8%AA%D8%B4%D8%A7%D8%B1%D9%8A%D8%A9',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%AA%D8%AF%D8%B1%D9%8A%D8%B3',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%AD%D8%A9',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%AA%D8%B1%D8%AC%D9%85%D8%A9',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D9%85%D8%AD%D8%A7%D8%B3%D8%A8%D8%A9',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%B3%D9%83%D8%B1%D8%AA%D8%A7%D8%B1%D9%8A%D8%A9',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%A7%D8%B9%D9%84%D8%A7%D9%85',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA-%D9%88%D8%A7%D9%84%D8%AA%D8%B3%D9%88%D9%8A%D9%82',
    'https://www.adwhit.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%A7%D9%84%D8%B4%D8%AD%D9%86-%D9%88%D8%A7%D9%84%D9%86%D9%82%D9%84']

def Adwite():
    #base url 
    ad= 'https://www.adwhit.com/'
    #jops contenrs section
    url = requests.get('https://www.adwhit.com/index.php?page=jobs')
    soop =  BeautifulSoup(url.content, 'html.parser')
    #all jop counter
    #cont = soop.find_all('div',{'class':'newJobListingTitle'})
    c=2
    cc=0
    for i in cont:
        #link of jop catagory 
        #link = ad+ i.text.replace(' ','-')

        url = requests.get(i)
        soop = BeautifulSoup(url.content,'html.parser')
        jopcard = soop.find('div',{'class':'listingBlock'})
        try:#git link each company
            joplink = jopcard.find('a')
            plink=ad +joplink['href']
                #read data from internal jop 
            url = requests.get(plink)
            soop = BeautifulSoup(url.content,'html.parser')
            alldata = soop.find('div',{'class':'listingBody'}).find_all('b')
            joptitle = soop.find('div',{'class':'listingTitle'}).text
            companyname = alldata[0].text
            pushdate = alldata[1].text
            disc = soop.find('div',{'class':'description newFont jobText unselectable'}).text
            mail = soop.find('a',{'class':'accessJobMethod'}).text
            phone = soop.find('div',{'class':'accessJobMethodContent'}).text
            print(companyname)
            
            print('-----------------------')
            jop_link1=plink
            
            
            jop_title1 = joptitle
            jop_date1=pushdate
            jop_contact1=phone
            jop_company1=companyname
            # if new contact in old contact do no thing
            if jop_contact1 in old:
                print ('Contact exists      ' , jop_contact1)
            else: # else add contact to bitrix 
                bitrixurl = f'https://b24-8w7tjp.bitrix24.com/rest/1/th1vdiumfrl0npik/crm.lead.add.json?FIELDS[TITLE]={jop_company1}&FIELDS[UF_CRM_1662105748]={jop_link1}&FIELDS[UF_CRM_1662105774]= {jop_title1}&FIELDS[UF_CRM_1662105853]={jop_contact1}& FIELDS[UF_CRM_1662105792]={jop_date1}&FIELDS[UF_CRM_1662160096141]={company_type[c]}'
                requests.get(bitrixurl)
                c=c+1
                
                print('This contact has been added to the list')
                

                cc = cc+1
        
        except:
            x=0
    


Adwite()