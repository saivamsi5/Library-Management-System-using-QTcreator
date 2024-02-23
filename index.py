from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql
pymysql.install_as_MySQLdb()
from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')


class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        #self.Dark_Orange_Theme()

        self.Show_Category()
        self.Show_Author()
        self.Show_Publisher()

        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()


    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
            self.groupBox_3.hide()


    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_8.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_30.clicked.connect(self.Open_Clients_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_10.clicked.connect(self.Search_Books)
        self.pushButton_9.clicked.connect(self.Edit_Books)
        self.pushButton_11.clicked.connect(self.Delete_Books)

        self.pushButton_12.clicked.connect(self.Add_Category)
        self.pushButton_13.clicked.connect(self.Add_Author)
        self.pushButton_14.clicked.connect(self.Add_Publisher)

        self.pushButton_16.clicked.connect(self.Add_New_User)
        self.pushButton_19.clicked.connect(self.Login)
        self.pushButton_24.clicked.connect(self.Edit_User)

        self.pushButton_15.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_17.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_20.clicked.connect(self.QDark_Theme)

        self.pushButton_21.clicked.connect(self.Add_New_Client)
        self.pushButton_23.clicked.connect(self.Search_Client)
        self.pushButton_22.clicked.connect(self.Edit_Client)
        self.pushButton_25.clicked.connect(self.Delete_Client)




        ##########################################################
        ############ opening tabs ################################
    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Clients_Tab(self):
        self.tabWidget.setCurrentIndex(2)
    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(4)

        ##########################################################
        ############ Books ################################

    def Add_New_Book(self):

        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentIndex()
        book_author = self.comboBox_4.currentIndex()
        book_publisher = self.comboBox_5.currentIndex()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s , %s , %s , %s , %s , %s , %s)
        ''' ,(book_title , book_description , book_code , book_category , book_author , book_publisher , book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')







    def Search_Books(self):

        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_9.text()

        sql = '''SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(sql , [(book_title)])

        data = self.cur.fetchone()

        self.lineEdit_11.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_10.setText(data[3])
        self.comboBox_11.setCurrentIndex(data[4])
        self.comboBox_9.setCurrentIndex(data[5])
        self.comboBox_10.setCurrentIndex(data[6])
        self.lineEdit_8.setText(str(data[7]))


    def Edit_Books(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_11.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_10.text()
        book_category = self.comboBox_11.currentIndex()
        book_author = self.comboBox_9.currentIndex()
        book_publisher = self.comboBox_10.currentIndex()
        book_price = self.lineEdit_8.text()

        search_book_title = self.lineEdit_9.text()

        self.cur.execute('''
            UPDATE book SET book_name = %s , book_description = %s , book_code = %s , book_category = %s , book_author = %s , book_publisher = %s , book_price = %s WHERE book_name = %s        
        ''', (book_title,book_description,book_code,book_category,book_author,book_publisher,book_price,search_book_title))

        self.db.commit()
        self.statusBar().showMessage('Book Updated')

    def Delete_Books(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_9.text()

        warning = QMessageBox.warning(self , 'Delete Book' , "are you sure? Do you want to delete this book?" , QMessageBox.Yes | QMessageBox.No )
        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM book WHERE book_name = %s '''
            self.cur.execute(sql , [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

    ##########################################################
    ############ Clients ################################

    def Add_New_Client(self):
        client_name = self.lineEdit_5.text()
        client_email = self.lineEdit_6.text()
        client_nationalid = self.lineEdit_7.text()

        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO clients(client_name , client_email , client_nationalid)
            VALUES (%s , %s , %s)
        ''', (client_name, client_email, client_nationalid))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New CLient Added')


    def Show_All_Clients(self):
        pass

    def Search_Client(self):
        client_national_id = self.lineEdit_26.text()
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM clients WHERE client_nationalid = %s '''
        self.cur.execute(sql, [(client_national_id)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_32.setText(data[1])
        self.lineEdit_30.setText(data[2])
        self.lineEdit_31.setText(data[3])


    def Edit_Client(self):
        client_original_national_id = self.lineEdit_26.text()
        client_name = self.lineEdit_32.text()
        client_email = self.lineEdit_30.text()
        client_national_id = self.lineEdit_31.text()

        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            UPDATE clients SET client_name = %s , client_email = %s , client_nationalid = %s WHERE client_nationalid = %s
        ''' , (client_name , client_email , client_national_id , client_original_national_id))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('Client Data Updated')

    def Delete_Client(self):
        client_original_national_id = self.lineEdit_26.text()

        warning_message = QMessageBox.warning(self, "Delete Client", "are you sure you want to delete this client", QMessageBox.Yes | QMessageBox.No)

        if warning_message == QMessageBox.Yes:
            self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
            self.cur = self.db.cursor()

            sql = ''' DELETE FROM clients WHERE client_nationalid = %s '''
            self.cur.execute(sql, [(client_original_national_id)])

            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('Client Deleted')






    ##########################################################
        ############ Users ################################

    def Add_New_User(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        username = self.lineEdit_12.text()
        email = self.lineEdit_13.text()
        password = self.lineEdit_14.text()
        password2 = self.lineEdit_15.text()

        if password == password2 :
            self.cur.execute('''
                INSERT INTO users(user_name , user_email , user_password)
                VALUES (%s , %s , %s)
            ''' , (username , email, password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_9.setText('Please enter valid password twice!!!')


    def Login(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        username = self.lineEdit_17.text()
        password = self.lineEdit_16.text()

        sql = ''' SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data :
            if username == row[1] and password == row[3]:
                print('user match')
                self.statusBar().showMessage('Valid username and Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_20.setText(row[1])
                self.lineEdit_18.setText(row[2])
                self.lineEdit_19.setText(row[3])
                #self.lineEdit_21



    def Edit_User(self):

        username = self.lineEdit_20.text()
        email = self.lineEdit_18.text()
        password = self.lineEdit_19.text()
        password2 = self.lineEdit_21.text()

        original_name = self.lineEdit_17.text()

        if password == password2 :
            self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' 
                UPDATE users SET user_name = %s , user_email = %s , user_password = %s WHERE user_name = %s
            ''', (username , email , password , original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            print('make sure you have entered correct password')



##########################################################
        ############ settings ################################

    def Add_Category(self):

        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_22.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_22.setText('')
        self.Show_Category()
        self.Show_Category_Combobox()

    def Show_Category(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()


        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def Add_Author(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_23.text()

        self.cur.execute('''
                    INSERT INTO authors (author_name) VALUES (%s)
                ''', (author_name,))

        self.db.commit()
        self.lineEdit_23.setText('')
        self.statusBar().showMessage('New Author Added')
        self.Show_Author()
        self.Show_Author_Combobox()

    def Show_Author(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Add_Publisher(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_24.text()

        self.cur.execute('''
                    INSERT INTO publisher (publisher_name) VALUES (%s)
                ''', (publisher_name,))

        self.db.commit()
        self.lineEdit_24.setText('')
        self.statusBar().showMessage('New Publisher Added')
        self.Show_Publisher()
        self.Show_Publisher_Combobox()

    def Show_Publisher(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


 ##########################################################
 ############ show settings data in UI ################################

    def Show_Category_Combobox(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        self.comboBox_3.clear()
        for category in data :
            self.comboBox_3.addItem(category[0])
            self.comboBox_11.addItem(category[0])

    def Show_Author_Combobox(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data = self.cur.fetchall()

        self.comboBox_4.clear()
        for authors in data:
            self.comboBox_4.addItem(authors[0])
            self.comboBox_9.addItem(authors[0])


    def Show_Publisher_Combobox(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Vamsisai@74', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        self.comboBox_5.clear()
        for publisher in data:
            self.comboBox_5.addItem(publisher[0])
            self.comboBox_10.addItem(publisher[0])

##########################################################
############ UI Themes ###################################

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)







def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()