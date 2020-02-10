import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import re

def phishing_or_not(url):
    #IP_ADDRESS
    ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url)
    if ip:
        flag_ip=1
    else:
        flag_ip=-1


    #URL_LENGTH
    url_len = len(url)
    if url_len<=40:
        flag_url_len=-1
    elif url_len>40 and url_len<70:
        flag_url_len=0
    else:
        flag_url_len=1


    #HAVING_AT_SYMBOL
    at = re.search(r'@', url)
    if at:
        flag_at=1
    else:
        flag_at=-1


    #DOUBLE_SLASH_REDIRECTING
    slash = re.search(r'//', url)
    if slash:
        flag_slash=1
    else:
        flag_slash=-1


    #PREFIX_SUFFIX
    presuf = re.search(r'-',url)
    if presuf:
        flag_presuf=1
    else:
        flag_presuf=-1


    #HTTPS_TOKEN
    http = re.subn(r'http', '', url)[1]
    https = re.subn(r'https', '', url)[1]
    if http>=2 or https>=2:
        flag_http=1
    else:
        flag_http=-1


    #SFH
    sfh = re.search(r'about\:blank', url)
    if sfh:
        flag_sfh=0
    else:
        flag_sfh=-1


    #TEST DATASET
    
    df_test = pd.DataFrame([[flag_ip, flag_url_len, flag_at, flag_slash, flag_presuf, flag_http, flag_sfh]], 
                          columns=['having_IPhaving_IP_Address','URLURL_Length','having_At_Symbol','double_slash_redirecting','Prefix_Suffix','HTTPS_token','SFH'])
    randomforest_new = pickle.load(open('model.sav', 'rb'))
    prediction=randomforest_new.predict(df_test)
    #print(prediction)
    result = 0
    if prediction==-1:
        print("-1, Not a phishing website.")
        result = -1
    elif prediction==1:
        print("1, Phishing website.")
        result = 1
    return str(result)
