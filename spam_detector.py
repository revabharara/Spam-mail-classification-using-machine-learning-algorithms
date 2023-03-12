import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# reading the csv file
df_mail=pd.read_csv('mail_data.csv')

# label encoding
df_mail.loc[df_mail['Category']=='spam', 'Category']=1
df_mail.loc[df_mail['Category']=='ham', 'Category']=0

# splitting the dataset

X_train=df_mail['Message']
Y_train=df_mail['Category']

# creating feature vectors from the data

vectorizer=TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

X_train_vector=vectorizer.fit_transform(X_train)

# converting the labels as type int
Y_train=Y_train.astype('int')

#creating the classification object
clf=RandomForestClassifier(n_jobs=2, random_state=1)

# training the classification object
clf.fit(X_train_vector, Y_train)


def spamornot():
    if mail_var.get()=="":
        messagebox.showerror('Invalid details', "The content field was left empty!")
    else:
        Y_test_vector=vectorizer.transform([mail_var.get()])
        yhat=clf.predict(Y_test_vector)
        
        if yhat==0:
            messagebox.showinfo('Not Spam', 'The content enetred is not spam.')
            
        else:
            messagebox.showinfo('Spam', 'The content enetred is spam.')
#creating a main window
root=tk.Tk()

# configuring the basic elements of the window
root.title('Email Spam Detector')
root.geometry('900x600')
root.configure(background='#393053')
root.resizable(0,0)

# adding the title farme
frame_title=tk.Frame(root, bg='#443C68')
frame_title.pack(side="top", fill="x")

# adding the title of the application
label_title=tk.Label(frame_title,text='Spam Mail Classifier', fg="white", bg="#443C68", font="ariel 24 bold")
label_title.pack(fill='x', pady=20)

created_by=tk.Label(frame_title, text=''' MADE BY : REVA BHARARA
    CONTACT INFO:
    revabharara@gmail.com
    Linkedin: https://www.linkedin.com/in/reva-bharara-a83a78241/
    ''', fg="white", bg="#443C68", font="ariel 13 bold")
created_by.pack(pady=5)

# creating a main frame to show the content
frame_main=tk.Frame(root, bg='#393053')
frame_main.pack(side='top', fill='x')

label_entry=tk.Label(frame_main, text='Enter the email content: ', fg="white", bg="#393053", font="ariel 14")
label_entry.grid(row=0, column=0, pady=30, padx=(40,10))

mail_var=tk.StringVar()

mail_entry=tk.Entry(frame_main, width=73,bg='#d7d3e3',font=("arial", 15), textvariable=mail_var)
mail_entry.grid(row=1, column=0, padx=(40,10), sticky='NSEW')

# creating the check button

button=tk.Button(frame_main,text='Check', bg='#635985', font="ariel 15", fg='#18122B', command=spamornot)
button.grid(row=2, column=0, padx=70, pady=30)

# image frame
frame_image=tk.Frame(root, bg='#393053')
frame_image.pack(side='top')
img= (Image.open("border.png"))
resized_image= img.resize((900,400), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
image_label=tk.Label(frame_image,image=new_image, bg='#393053')
image_label.grid(row=0,column=0)




root.mainloop()