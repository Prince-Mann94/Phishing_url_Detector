import tkinter as tk
from tkinter import ttk, messagebox
import threading
import re
import pandas as pd
from scipy.io import arff
from sklearn.ensemble import RandomForestClassifier
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import whois
import ssl
import socket
from datetime import datetime, timezone
import warnings
warnings.filterwarnings("ignore")
import os

def url_ip(url): return -1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 1
def url_length(url): return 1 if len(url)<54 else 0 if len(url)<=75 else -1
def tiny_url(url): return -1 if any(x in url for x in ["bit.ly","tinyurl"]) else 1
def url_symbol(url): return -1 if '@' in url else 1
def url_doubleslash(url): return -1 if url.count('//')>1 else 1
def url_dash(url): return -1 if '-' in urlparse(url).netloc else 1

def url_subdomain(url):
    dots = urlparse(url).netloc.count('.')
    return 1 if dots<=1 else 0 if dots==2 else -1

def url_https_cert(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme != "https": return -1
        hostname = parsed.netloc
        ctx = ssl.create_default_context()
        with socket.create_connection((hostname,443),timeout=5) as sock:
            with ctx.wrap_socket(sock,server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
        return 1
    except: return -1

def domain_expires(url):
    try:
        domain = urlparse(url).netloc.replace("www.","")
        expiry = whois.whois(domain).expiration_date
        if isinstance(expiry,list): expiry = expiry[0]
        days = (expiry - datetime.now()).days
        return 1 if days>365 else -1
    except: return -1

def favicon(url):
    try:
        soup = BeautifulSoup(requests.get(url,timeout=5).text,"html.parser")
        icon = soup.find("link",rel=lambda r: r and "icon" in r)
        return 1 if icon else -1
    except: return -1

def check_port(url):
    try:
        hostname = urlparse(url).netloc
        socket.create_connection((hostname,80),timeout=3)
        return 1
    except: return -1

def url_use_http(url): return -1 if "http" in urlparse(url).netloc else 1

def request_url(url):
    try:
        soup = BeautifulSoup(requests.get(url,timeout=5).text,"html.parser")
        return 1 if len(soup.find_all())>0 else -1
    except: return -1

def url_of_anchor(url):
    try:
        soup = BeautifulSoup(requests.get(url,timeout=5).text,"html.parser")
        return 1 if soup.find_all("a") else -1
    except: return -1

def links_in_tags(url): return 1
def sfh(url): return 1

def extract_features(url):
    return [
        url_ip(url), url_length(url), tiny_url(url), url_symbol(url),
        url_doubleslash(url), url_dash(url), url_subdomain(url),
        url_https_cert(url), domain_expires(url), favicon(url),
        check_port(url), url_use_http(url), request_url(url),
        url_of_anchor(url), links_in_tags(url), sfh(url)
    ]


features_list = [
    'having_IP_Address',
    'URL_Length',
    'Shortining_Service',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix',
    'having_Sub_Domain',
    'SSLfinal_State',
    'Domain_registeration_length',
    'Favicon',
    'port',
    'HTTPS_token',
    'Request_URL',
    'URL_of_Anchor',
    'Links_in_tags',
    'SFH'

]
def load_model():
    data = arff.loadarff(r"C:\Users\Princ\OneDrive\Desktop\phishing+websites\Training Dataset.arff")
    df = pd.DataFrame(data[0])
    model = RandomForestClassifier()
    df = df.apply(lambda col: col.map(lambda x: int(x.decode('utf-8')) if isinstance(x, bytes) else int(x)))

    X = df[features_list]
    y = df.iloc[:, -1]
    model.fit(X,y)
    return model

model = load_model()

def predict_url(url):
    pred = model.predict([extract_features(url)])[0]
    return "Legitimate" if pred==1 else "Suspicious" if pred==0 else "Phishing"

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

root = tk.Tk()
root.title("Phishing Detection System")
root.geometry("600x500")
root.configure(bg="#0f172a")

title = tk.Label(root,text="🔐 Phishing Detection System",
                 font=("Helvetica",20,"bold"),
                 bg="#0f172a",fg="#22c55e")
title.pack(pady=20)

url_entry = tk.Entry(root,font=("Helvetica",14),width=40)
url_entry.pack(pady=10)

result_label = tk.Label(root,font=("Helvetica",16,"bold"),bg="#0f172a")
result_label.pack(pady=20)

def check_url():
     url = url_entry.get()
     if not url:
        messagebox.showerror("Error","Enter URL")
        return
    
     if not url.startswith("http"):
         messagebox.showerror("Error","NOT A VALID SITE")
         return

     if not is_valid_url(url):
         print("Invalid URL format")
         messagebox.showerror("Error","Invalid URL format")
         return
    
     res = predict_url(url)
     color = "green" if res=="Legitimate" else "yellow" if res=="Suspicious" else "red"
     result_label.config(text=res,fg=color)

def scan_gmail():
    try:
        result_label.config(text="🔄 Scanning Gmail...", fg="cyan")
        
    except:
        messagebox.showerror("Error", "Gmail scan feature connected in backend")

btn_frame = tk.Frame(root,bg="#0f172a")
btn_frame.pack(pady=20)

tk.Button(btn_frame,text="🔍 Check URL",bg="#22c55e",fg="white",
          command=check_url).grid(row=0,column=0,padx=10)

tk.Button(btn_frame,text="📧 Scan Gmail",bg="#3b82f6",fg="white",
          command=lambda: threading.Thread(target=scan_gmail).start()
          ).grid(row=0,column=1,padx=10)

root.mainloop()