from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import Place, StringVar, Variable, ttk, IntVar, messagebox


r = tk.Tk()
r.title('Regform')
r.geometry('650x800')
r.config(bg='khaki')

def register():
    name = name_entry.get()
    sex = select_sex.get()
    subject = []

    if subj1.get() == 1:
        subject.append("ENGLISH")
    if subj2.get() == 1:
        subject.append("PHILOSOPHY")
    if subj3.get() == 1:
        subject.append("PROGRAMMING")
    if subj4.get() == 1:
        subject.append("A.I")

    department = dep_combo.get()
    address = add_txt.get("1.0", "end")

    print("NAME: ", name.title())
    print("SEX: ", sex)
    print("SUBJECT: ",', '.join(subject))
    print("DEPARTMENT: ",department)
    print("ADDRESS: ",address.title())
    tk.messagebox.showinfo("ATTENTION!", "YOU ARE NOW REGISTERED")

#LABEL
reg = tk.Label(r, width=30, text="STUDENT REGISTRATION FORM", bg="#003f5c",  font=('Arial Black', 20), fg='khaki')
reg.place(x=35, y=30)

#name
name_label = tk.Label(r, width=10, bg='khaki', text="NAME :",  font=('Arial Black', 10), fg="#003f5c")
name_label.place(x=35, y=100)

name_entry = tk.Entry(r, width=50, bg='LightCyan',  font=('Arial', 10))
name_entry.place(x=159, y=100)

#SEX
sex_label = tk.Label(r, width=10, bg='khaki', text="SEX :",  font=('Arial Black', 10), fg="#003f5c")
sex_label.place(x=35, y=150)

select_sex = StringVar()
male_btn = tk.Radiobutton(r, width=5, text="MALE", bg='khaki', value="MALE",  font=('Arial', 9), variable= select_sex)
male_btn.place(x=159, y=150)

female_btn = tk.Radiobutton(r, width=6, text="FEMALE", bg='khaki', value="FEMALE",  font=('Arial', 9), variable= select_sex)
female_btn.place(x=250, y=150)

#SUBJECTS
sub_label = tk.Label(r, width=10, bg='khaki', text="SUBJECT :",  font=('Arial Black', 10), fg="#003f5c")
sub_label.place(x=35, y=200)

#SUBJECT CHECKBUTTON
subj1 = IntVar()
sub1 = tk.Checkbutton(r, width=8, bg='khaki', text="ENGLISH",  font=('Arial', 9), variable=subj1)
sub1.place(x=159, y=200)

subj2 = IntVar()
sub2 = tk.Checkbutton(r, width=11, bg='khaki', text="PHILOSOPHY",  font=('Arial', 9), variable=subj2)
sub2.place(x=159, y=225)

subj3 = IntVar()
sub3 = tk.Checkbutton(r, width=13, bg='khaki', text="PROGRAMMING",  font=('Arial', 9), variable=subj3)
sub3.place(x=159, y=250)

subj4 = IntVar()
sub4 = tk.Checkbutton(r, width=2, bg='khaki', text="A.I",  font=('Arial', 9), variable=subj4)
sub4.place(x=159, y=275)

#DEPARTMENT
dep_label = tk.Label(r, width=12, bg='khaki', text="DEPARTMENT  :",  font=('Arial Black', 10), fg="#003f5c")
dep_label.place(x=35, y=325)

dep_combo = StringVar()
dep_list = [ "BS Information Technology" , "BS Public Administration" , "BS Entrepreneur" , "BS Computer Science"]
dep_combo = ttk.Combobox(r, width=25, value=dep_list, font=('Arial', 10))
dep_combo.place(x=159, y=325)

#ADDRESS
add_label = tk.Label(r, width=12, bg='khaki', text="ADDRESS  :",  font=('Arial Black', 10), fg="#003f5c")
add_label.place(x=35, y=375)

add_txt = tk.Text(r, width=50, bg='LightCyan', height=15,  font=('Arial', 10))
add_txt.place(x=159, y=375)

#SAVE BUTTON
save = tk.Button(r, width=13, bg="#003f5c", text="REGISTER",  font=('Arial black', 10), command=lambda:register(), fg='khaki')
save.place(x=487, y=720)


r.mainloop()
