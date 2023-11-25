from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
import datetime
import pymysql


class Library:
    def __init__(self, root):
        self.root = root
        self.configure_root()
        self.create_string_vars()
        self.create_frames()
        self.create_label()
        self.create_calendar()
        self.create_listbox()
        self.create_treeview()
        self.create_buttons()


    def configure_root(self):
        self.root.title("Library Management Systems")
        self.root.configure(background='cadetblue')
        window_width, window_height = 1350, 700
        position_right = int(self.root.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.root.winfo_screenheight()/2 - window_height/2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")


    def create_string_vars(self):
        self.vars = {name: StringVar() for name in [
            'Member', 'MType', 'Title', 'Firstname', 'Surname', 'Address', 'Address2', 'PostCode', 'MobileNo',
            'BookISBN', 'BookTitle', 'BookType', 'Author', 'DateBorrowed', 'DateDue', 'SellingPrice',
            'LateReturnFine', 'DateOverDue', 'DaysOnLoan'
        ]}


    def create_frames(self):
        self.MainFrame = self.create_frame(self.root, bg='skyblue')
        self.MainFrame.grid()
        
        self.TitleFrame = self.create_frame(self.MainFrame, bd=10, width=1350, padx=60, relief=RIDGE)
        self.TitleFrame.pack(side=TOP)
        
        self.lblTitle = Label(self.TitleFrame, width=38, font=('Times New Roman', 40,'bold'), text="\tLibrary Management System\t", fg='darkblue')
        self.lblTitle.grid()
        
        self.ButtonFrame = self.create_frame(self.MainFrame, bd=10, width=1350, height=50, relief=RIDGE)
        self.ButtonFrame.pack(side=BOTTOM)
        
        self.DataFrame = self.create_frame(self.MainFrame, bd=10, width=1300, height=400, relief=RIDGE)
        self.DataFrame.pack(side=BOTTOM)
        
        self.DataFrameLEFTCover = self.create_label_frame(self.DataFrame, bd=10, width=800, height=300, relief=RIDGE,
                                        bg='skyblue', font=('Times New Roman', 12,'bold'), text="Library Membership Info:", fg='darkblue')
        self.DataFrameLEFTCover.pack(side=LEFT, padx=10)
        self.DataFrameLEFT = self.create_frame(self.DataFrameLEFTCover, bd=10, width=800, height=300, padx=13, pady=2, relief=RIDGE)
        self.DataFrameLEFT.pack(side=TOP)
        self.DataFrameLEFTb = self.create_label_frame(self.DataFrameLEFTCover, bd=10, width=800, height=100, pady=4, padx=10, relief=RIDGE,
                                        font=('Times New Roman', 12,'bold'), text="Library Membership Info:", fg='darkblue')
        self.DataFrameLEFTb.pack(side=TOP)
        
        self.DataFrameRIGHT = self.create_label_frame(self.DataFrame, bd=10, width=450, height=300, padx=10, relief=RIDGE,
                                        bg='skyblue', font=('Times New Roman', 12,'bold'), text="Book Details:", fg='darkblue')
        self.DataFrameRIGHT.pack(side=RIGHT)



    def create_frame(self, parent, **options):
        frame = Frame(parent, **options)
        return frame


    def create_label_frame(self, parent, **options):
        frame = LabelFrame(parent, **options)
        return frame


    def set_book_details(self, w):
        books = {
            "Harry Potter": {
                "BookISBN": "ISBN 123456789012",
                "BookTitle": "The Philosopher's Stone",
                "Author": "J.K. Rowling",
                "LateReturnFine": "£3.50",
                "SellingPrice": "£15.99",
                "DaysOnLoan": 21
            },
            "The Hobbit": {
                "BookISBN": "ISBN 987654321098",
                "BookTitle": "There and Back Again",
                "Author": "J.R.R. Tolkien",
                "LateReturnFine": "£4.00",
                "SellingPrice": "£20.99",
                "DaysOnLoan": 30
            },
            "To Kill a Mockingbird": {
                "BookISBN": "ISBN 112233445566",
                "BookTitle": "To Kill a Mockingbird",
                "Author": "Harper Lee",
                "LateReturnFine": "£2.50",
                "SellingPrice": "£10.99",
                "DaysOnLoan": 14
            },
            "1984": {
                "BookISBN": "ISBN 998877665544",
                "BookTitle": "1984",
                "Author": "George Orwell",
                "LateReturnFine": "£3.00",
                "SellingPrice": "£15.99",
                "DaysOnLoan": 21
            },
            "Pride and Prejudice": {
                "BookISBN": "ISBN 223344556677",
                "BookTitle": "Pride and Prejudice",
                "Author": "Jane Austen",
                "LateReturnFine": "£2.75",
                "SellingPrice": "£11.99",
                "DaysOnLoan": 14
            },
            "The Great Gatsby": {
                "BookISBN": "ISBN 334455667788",
                "BookTitle": "The Great Gatsby",
                "Author": "F. Scott Fitzgerald",
                "LateReturnFine": "£3.25",
                "SellingPrice": "£16.99",
                "DaysOnLoan": 21
            },
            "Moby Dick": {
                "BookISBN": "ISBN 445566778899",
                "BookTitle": "Moby Dick",
                "Author": "Herman Melville",
                "LateReturnFine": "£2.95",
                "SellingPrice": "£12.99",
                "DaysOnLoan": 14
            },
            "War and Peace": {
                "BookISBN": "ISBN 556677889900",
                "BookTitle": "War and Peace",
                "Author": "Leo Tolstoy",
                "LateReturnFine": "£3.45",
                "SellingPrice": "£17.99",
                "DaysOnLoan": 21
            },
            "The Catcher in the Rye": {
                "BookISBN": "ISBN 667788990011",
                "BookTitle": "The Catcher in the Rye",
                "Author": "J.D. Salinger",
                "LateReturnFine": "£3.15",
                "SellingPrice": "£13.99",
                "DaysOnLoan": 14
            },
            "The Lord of the Rings": {
                "BookISBN": "ISBN 778899001122",
                "BookTitle": "The Lord of the Rings",
                "Author": "J.R.R. Tolkien",
                "LateReturnFine": "£3.65",
                "SellingPrice": "£18.99",
                "DaysOnLoan": 21
            },
            "The Adventures of Huckleberry Finn": {
                "BookISBN": "ISBN 889900112233",
                "BookTitle": "The Adventures of Huckleberry Finn",
                "Author": "Mark Twain",
                "LateReturnFine": "£3.35",
                "SellingPrice": "£14.99",
                "DaysOnLoan": 14
            },
            "The Chronicles of Narnia": {
                "BookISBN": "ISBN 990011223344",
                "BookTitle": "The Chronicles of Narnia",
                "Author": "C.S. Lewis",
                "LateReturnFine": "£3.85",
                "SellingPrice": "£19.99",
                "DaysOnLoan": 21
            },
            "Alice's Adventures in Wonderland": {
                "BookISBN": "ISBN 112233445566",
                "BookTitle": "Alice's Adventures in Wonderland",
                "Author": "Lewis Carroll",
                "LateReturnFine": "£3.55",
                "SellingPrice": "£15.99",
                "DaysOnLoan": 14
            },
            "The Da Vinci Code": {
                "BookISBN": "ISBN 223344556677",
                "BookTitle": "The Da Vinci Code",
                "Author": "Dan Brown",
                "LateReturnFine": "£4.05",
                "SellingPrice": "£20.99",
                "DaysOnLoan": 21
            }
        }
            
        if w in books:
            book = books[w]
            self.vars['BookISBN'].set(book["BookISBN"])
            self.vars['BookTitle'].set(book["BookTitle"])
            self.vars['Author'].set(book["Author"])
            self.vars['LateReturnFine'].set(book["LateReturnFine"])
            self.vars['SellingPrice'].set(book["SellingPrice"])
            self.vars['DaysOnLoan'].set(str(book["DaysOnLoan"]))

            d1 = datetime.date.today()
            d2 = datetime.timedelta(days=book["DaysOnLoan"])
            d3 = (d1 + d2)
            self.vars['DateBorrowed'].set(d1)
            self.vars['DateDue'].set(d3)
            self.vars['DateOverDue'].set("No")


    def SelectedBook(self, evt):
        values = str(self.booklist.get(self.booklist.curselection()))
        w = values
        self.set_book_details(w)


    def LibraryInfo(self, ev):
        sqlCon = pymysql.connect(host="localhost", user="root", password="1234", database="library")
        cur = sqlCon.cursor()
        cur.execute("select * from library where member=%s", self.vars['Member'].get())
        row = cur.fetchone()
        
        if row is not None:
            self.vars['Member'].set(row[0])
            self.vars['Firstname'].set(row[1])
            self.vars['Surname'].set(row[2])
            self.vars['Address'].set(row[3])
            self.vars['DateBorrowed'].set(row[4])
            self.vars['DateDue'].set(row[5])
            self.vars['DateOverDue'].set(row[6])
            self.vars['Author'].set(row[7])
            self.vars['BookISBN'].set(row[8])
            self.vars['BookTitle'].set(row[9])
        else:
            print("No record found for member: ", self.vars['Member'].get())

            
    def create_label(self):
        self.lblMemberType = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(self.DataFrameLEFT, textvariable=self.vars['MType'], state='readonly',
                                        font=('arial', 12,'bold'), width=34)
        self.cboMemberType['value'] = ('','Student','Lecturer','Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookISBN = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Book ID:", padx=2, pady=2)
        self.lblBookISBN.grid(row=0, column=2, sticky=W)
        self.txtBookISBN = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['BookISBN'], width=31)
        self.txtBookISBN.grid(row=0, column=3)

        self.lblRef = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Reference No:", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['Member'], width=36)
        self.txtRef.grid(row=1, column=1)

        self.lblBookTitle = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Book Title:", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['BookTitle'], width=31)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblTitle = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)

        self.cboTitle = ttk.Combobox(self.DataFrameLEFT, textvariable=self.vars['Title'], state='readonly',
                                    font=('arial', 12,'bold'), width=34)
        self.cboTitle['value'] = ('','Mr.','Miss.','Mrs.','Dr.','Capt.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Author:", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['Author'], width=31)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstname = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Firstname:", padx=2, pady=2)
        self.lblFirstname.grid(row=3, column=0, sticky=W)
        self.txtFirstname = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['Firstname'], width=36)
        self.txtFirstname.grid(row=3, column=1)

        self.lblDateBorrowed = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Date Borrowed:", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['DateBorrowed'], width=31)
        self.txtDateBorrowed.grid(row=3, column=3)

        self.lblSurname = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Surname:", padx=2, pady=6)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['Surname'], width=36)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateDue = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Date Due:", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['DateDue'], width=31)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAddress1 = Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Address 1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.txtAddress1 = Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['Address'], width=36)
        self.txtAddress1.grid(row=5, column=1)

        self.lblAddress1 =Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Address 1:",padx=2,pady=2)
        self.lblAddress1.grid(row=5, column=0,sticky=W)
        self.txtAddress1=Entry(self.DataFrameLEFT, font=('arial', 12,'bold'), textvariable=self.vars['Address'], width=36)
        self.txtAddress1.grid(row=5, column=1)

        self.lblDaysOnLoan=Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Days on Loan:",padx=2,pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2,sticky=W)
        self.txtDaysOnLoan=Entry(self.DataFrameLEFT,font=('arial', 12,'bold'),textvariable = self.vars["DaysOnLoan"] ,width=31)
        self.txtDaysOnLoan.grid(row=5, column=3)

        self.lblAddress2 =Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Address 2:",padx=2,pady=2)
        self.lblAddress2.grid(row=6, column=0,sticky=W)
        self.txtAddress2=Entry(self.DataFrameLEFT, font=('arial', 12,'bold'),textvariable = self.vars["Address2"], width=36)
        self.txtAddress2.grid(row=6, column=1)

        self.lblLateReturnFine=Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Late Return Fine:",padx=2,pady=2)
        self.lblLateReturnFine.grid(row=6, column=2,sticky=W)
        self.txtLateReturnFine=Entry(self.DataFrameLEFT,font=('arial', 12,'bold'),textvariable = self.vars["LateReturnFine"], width=31)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPostCode =Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Post Code:",padx=2,pady=2)
        self.lblPostCode.grid(row=7, column=0,sticky=W)
        self.txtPostCode=Entry(self.DataFrameLEFT, font=('arial', 12,'bold'),textvariable = self.vars["PostCode"], width=36)
        self.txtPostCode.grid(row=7, column=1)

        self.lblDateOverDue=Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Date Over Due:",padx=2,pady=2)
        self.lblDateOverDue.grid(row=7, column=2,sticky=W)
        self.txtDateOverDue=Entry(self.DataFrameLEFT,font=('arial', 12,'bold'),textvariable = self.vars["DateOverDue"] ,width=31)
        self.txtDateOverDue.grid(row=7, column=3)
        
        self.lblMobileNo =Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Mobile No:",padx=2,pady=2)
        self.lblMobileNo.grid(row=8, column=0,sticky=W)
        self.txtMobileNo=Entry(self.DataFrameLEFT, font=('arial', 12,'bold'),textvariable = self.vars["MobileNo"], width=36)
        self.txtMobileNo.grid(row=8, column=1)

        self.lblSellingPrice=Label(self.DataFrameLEFT, font=('arial', 12,'bold'), text="Selling Price:",padx=2,pady=2)
        self.lblSellingPrice.grid(row=8, column=2,sticky=W)
        self.txtSellingPrice=Entry(self.DataFrameLEFT,font=('arial', 12,'bold'),textvariable = self.vars["SellingPrice"],width=31)
        self.txtSellingPrice.grid(row=8, column=3)


    def create_calendar(self):
        cal = Calendar(self.DataFrameRIGHT, selectmode="day", year=2023, month=11, day=25, date_pattern='yyyy-mm-dd',
                    font=('arial', 12,'bold'), padx=10)
        cal.grid(row=0, column=0, pady=10)


    def create_listbox(self):
        scrollbar = Scrollbar(self.DataFrameRIGHT, orient=VERTICAL)        
        scrollbar.grid(row=1, column=1, sticky='ns')

        ListOfBooks = ['Harry Potter', 'The Hobbit', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Great Gatsby', 'Moby Dick', 'The Da Vinci Code',
                    'War and Peace', 'The Catcher in the Rye', 'The Lord of the Rings', 'The Adventures of Huckleberry Finn', 'The Chronicles of Narnia', 'Alice\'s Adventures in Wonderland']

        self.booklist = Listbox(self.DataFrameRIGHT, width=40, height=12, font=('times', 11, 'bold'), yscrollcommand=scrollbar.set)
        self.booklist.bind('<<ListboxSelect>>', self.SelectedBook)
        self.booklist.grid(row=1, column=0, padx=3)
        scrollbar.config(command=self.booklist.yview)

        for items in ListOfBooks:
            self.booklist.insert(END, items)


    def create_treeview(self):
        scroll_x = Scrollbar(self.DataFrameLEFTb, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.DataFrameLEFTb, orient=VERTICAL)

        columns = ("member", "firstname", "surname", "address", "dateborrowed", "datedue", "dayoverdue", "author", "bookisbn", "booktitle")
        self.library_records = ttk.Treeview(self.DataFrameLEFTb, height=5, columns=columns, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        column_widths = {"member": 70, "firstname": 100, "surname": 100, "address": 100, "dateborrowed": 70, "datedue": 70, "dayoverdue": 100, "author": 100, "bookisbn": 70, "booktitle": 70}

        for col in columns:
            self.library_records.heading(col, text=col.capitalize())
            self.library_records.column(col, width=column_widths[col])

        self.library_records['show'] = 'headings'
        self.library_records.pack(fill=BOTH, expand=1)
        self.library_records.bind("<ButtonRelease-1>", self.LibraryInfo)
        self.DisplayData()

    
    def create_buttons(self):
        buttons = [
            ("Display Data", self.addData, 1),
            ("Delete", self.DeleteDB, 2),
            ("Reset", self.iReset, 3),
            ("Search", self.SearchDB, 4),
            ("Exit", self.iExit, 5)
        ]

        for btn_text, btn_command, column in buttons:
            Button(
                self.ButtonFrame, 
                text=btn_text, 
                font=('arial', 19,'bold'), 
                padx=4,
                width=16, 
                bd=4, 
                bg='cadetblue', 
                command=btn_command
            ).grid(row=0, column=column, padx=3)


    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management Systems","Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return


    def iReset(self):
        for var in self.vars.values():
            var.set("")


    def addData(self):
        if self.vars['Member'].get() == "" or self.vars['Firstname'].get() == "" or self.vars['Surname'].get() == "":
            tkinter.messagebox.showerror("Enter correct members details")
        else:
            sqlCon = pymysql.connect(host="localhost", user="root", password="1234", database="library")
            cur = sqlCon.cursor()
            
            cur.execute("""
                INSERT INTO library (Member, Firstname, Surname, dateborrowed, datedue, dayoverdue, author, bookisbn, booktitle) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.vars['Member'].get(),
                self.vars['Firstname'].get(),
                self.vars['Surname'].get(),
                self.vars['DateBorrowed'].get(),
                self.vars['DateDue'].get(),
                self.vars['DateOverDue'].get(),
                self.vars['Author'].get(),
                self.vars['BookISBN'].get(),
                self.vars['BookTitle'].get(),
            ))

            sqlCon.commit()
            self.DisplayData()
            sqlCon.close()
            self.vars['DateDue'].set(self.cal.get_date())
            self.vars['DateOverDue'].set("Yes")
            tkinter.messagebox.showinfo("Library Management Systems", "Record Entered Successfully")


    def DisplayData(self):
        sqlCon = pymysql.connect(host="localhost", port=3306, user="root", password="1234", database="library")
        cur = sqlCon.cursor()
        cur.execute("select * from library")
        result = cur.fetchall()
        if len(result)!= 0:
            self.library_records.delete(*self.library_records.get_children())
            for row in result:
                self.library_records.insert('',END,values =row)
            sqlCon.commit()
        sqlCon.close()


    def DeleteDB(self):
        sqlCon = pymysql.connect(host="localhost", port=3306, user="root", password="1234", database="library")
        cur = sqlCon.cursor()
        cur.execute("delete from library where member=%s", self.vars['Member'].get())
        sqlCon.commit()
        self.DisplayData()
        sqlCon.close()
        tkinter.messagebox.showinfo("Library Management Systems","Record Successfully Deleted")


    def SearchDB(self):
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="1234", database="library")
            cur = sqlCon.cursor()
            cur.execute("select * from library where member=%s", self.vars['Member'].get())

            row = cur.fetchone()

            self.vars['Member'].set(row[0])
            self.vars['Firstname'].set(row[1])
            self.vars['Surname'].set(row[2])
            self.vars['Address'].set(row[3])
            self.vars['DateBorrowed'].set(row[4])
            self.vars['DateDue'].set(row[5])
            self.vars['DateOverDue'].set(row[6])
            self.vars['Author'].set(row[7])
            self.vars['BookISBN'].set(row[8])
            self.vars['BookTitle'].set(row[9])

            sqlCon.commit()
        except:           
            tkinter.messagebox.showinfo("Library Management Systems","No Such Record Found")
            sqlCon.close()        

    
    
if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()













    


    
