from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
from bs4 import BeautifulSoup
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import warnings
import pickle
warnings.filterwarnings("ignore")
model1 = pickle.load(open('model1.pkl','rb'))
model2 = pickle.load(open('model2.pkl','rb'))
model3 = load_model('model3.h5')

app=Flask(__name__)


# Home Page of the website
@app.route("/")
def home():
    
    return render_template("home.html")

def job_links_headlines(target_url):
    source=requests.get(target_url)
    soup = BeautifulSoup(source.content, "html.parser")
    job_elements = soup.find_all('a', class_='JobCard_jobTitle___7I6y')

    job_list = []

    for job in job_elements:
        job_text = job.text
        job_link = job['href']
        job_tuple = (job_text, job_link)
        job_list.append(job_tuple)

    return job_list



def predict(df):
    output1 = 1 if model1.predict_proba(df.reshape(1,-1))[0][0] < 0.5 else 0
    output2 = 1 if model2.predict_proba(df.reshape(1,-1))[0][0] < 0.5 else 0
    output3 = 1 if model3.predict(df.reshape(-1,17))[0][0] < 0.5 else 0

    if output1+output2+output3 >= 2:
        return "Job is not for Freshers."
    else:
        return "Job is for Freshers."

def counts(w, data):
  data = str(data).lower()
  w = w.lower()
  return data.count(w)

def features_extraction(content):
    dic = {}
    lst = ['experience', 'advance','minimum','excellent','atleast','strong','expert','senior', 'deep', 'previous','fresher','basic','proficient']

    for i in lst:
        dic[i+'_count'] = counts(i, content)

    dic['col1'] = dic['minimum_count']+dic['atleast_count']
    dic["col2"] = dic['advance_count']+dic['expert_count']+dic['deep_count']+dic['previous_count']
    dic['col3'] = dic['excellent_count'] + dic['strong_count']
    dic['col4'] = dic['basic_count']+dic['proficient_count']+dic['fresher_count']

    features = [dic[i] for i in dic ]
    return np.array(features)

def extract_text(url):
    source=requests.get(url)
    soup = BeautifulSoup(source.content, "html.parser")

    job=soup.find_all('div', class_="JobDetails_jobDescription__uW_fK JobDetails_blurDescription__vN7nh")

    description=''
    for data in job:
        description+=data.get_text().strip()
    return description.replace('\n\n',' ')


@app.route('/jobDetails')
def jobDetails():
    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/job-listing/sr-director-strategy-analytics-glassdoor-JV_IC1128808_KO0,30_KE31,40.htm?jl=1009230852766&cs=1_3b64d045&s=21&t=ESR&pos=104&src=GD_JOB_AD&guid=0000018ecbc5b317ae8e5309b9511577&jobListingId=1009230852766&ea=1&ao=1136043&vt=w&jrtk=5-yul1-0-1hr5sbcsdikfu800-a5fa077afc33e2b5&cb=1712815715333&ctt=1712815719976&srs=EI_JOBS&dynamic=false'

    job_links_headlines1=job_links_headlines(target_url)
    headers=["Job headline","URL of Jobs", "Copy URL"]

    return render_template('home.html', job_links_headlines1=job_links_headlines1 , headers=headers )

@app.route('/submit', methods=['POST'])
def submit():
    # url = request.form['url']
    if request.method == 'POST':
        if request.form['submit'] == "url":
           
            print(123)
            url = request.form['url']
            original_url=url
            url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url='+url+'&dynamic=false'
            job_text=extract_text(url)
            # print(job_text) 
            df = features_extraction(job_text)  
            print(234)
            result = predict(df)
            print(567)
            print(result) 
            return render_template('home.html', text=result, url_job=original_url, url=234) 
    
  
        elif request.form['submit'] == "job_website":
            selected_option = None        
            selected_option = request.form.get('job_website')
            headers=["Job headline","URL of Jobs", "Copy URL"]
            try:

                if selected_option == 'QA':
                    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/Job/work-from-home-qa-jobs-SRCH_FW0,14_KO15,17.htm&dynamic=false'

                    
                elif selected_option == 'ML':
                    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/Job/remote-machine-learning-jobs-SRCH_IL.0,6_IS12563_KO7,23.htm&dynamic=false'
                    
                elif selected_option == 'Web':
                    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/Job/remote-front-end-engineer-jobs-SRCH_IL.0,6_IS12563_KO7,25.htm&dynamic=false'

                    
                elif selected_option == 'Law':
                    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/Job/remote-law-jobs-SRCH_IL.0,6_IS12563_KO7,10.htm&dynamic=false'
                                      
                    
                elif selected_option == 'DM':
                    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/Job/remote-digital-marketing-jobs-SRCH_IL.0,6_IS12563_KO7,24.htm&dynamic=false'

                elif selected_option=='CS':
                    target_url='https://api.scrapingdog.com/scrape?api_key=66177cdf8eb18b440dc70d8b&url=https://www.glassdoor.co.in/Job/remote-cyber-security-jobs-SRCH_IL.0,6_IS12563_KO7,21.htm&dynamic=false'

                job_links_headlines1=job_links_headlines(target_url)  
                return render_template('home.html', job_links_headlines1=job_links_headlines1 , headers=headers )
            except:
                return render_template('home.html' , message12="Website is under maintaining")


# Login Page of the website
@app.route("/login",methods=('POST','GET'))
def login():
    return render_template("login.html")

#Signup Page of the website
@app.route("/signup",methods=('POST','GET'))
def sign(): 
    return render_template("signup.html")

#Contact us Page of the website
@app.route("/contact",methods=('POST','GET'))
def contact():
    return render_template("contact.html")

# About us Page of the website
@app.route("/about",methods=('POST','GET'))
def about():
    return render_template("about.html")

#Profile Page of the website
@app.route("/profile",methods=('POST','GET'))
def profile():
    return render_template("profile.html")

if __name__=='__main__':
    app.run(debug=True)
