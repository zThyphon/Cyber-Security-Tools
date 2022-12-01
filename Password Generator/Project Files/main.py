#Import Libraries
#Import System Library
import sys
#Import PyQt5 (Graphical User Interface Library)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QPixmap
#Import Random Module(For Generating Password)
import random

#Define Fonts
header_font = QFont("Arial",36)
label_font = QFont("Verdana",14)

#Create Window Class
class Window(QWidget):
    def __init__(self):
        super().__init__()

        #Define Window Attributes
        self.setWindowTitle("Password Generator by zThyphon")
        self.setGeometry(600,250,650,550)
        self.setWindowIcon(QIcon("icons\password_icon.png"))
        self.setStyleSheet("background-color:#00BFFF")

        self.UI()

    #User Interface
    def UI(self):

        #Header
        header_label = QLabel("Password Generator by zThyphon",self)
        header_label.setFont(header_font)

        #Header Icon
        header_icon = QLabel(self)
        header_icon.setPixmap(QPixmap("icons/password_icon.png"))

        #Header Layout
        header_hlayout = QHBoxLayout()
        header_hlayout.addStretch()
        header_hlayout.addWidget(header_icon)
        header_hlayout.addWidget(header_label)
        header_hlayout.addStretch()

        #Password Length Entry
        password_length_label = QLabel("Enter Length of Password: ",self)
        password_length_label.setFont(label_font)
        self.password_length_line = QLineEdit()
        self.password_length_line.setPlaceholderText("Enter Total Length")
        self.password_length_line.setStyleSheet("background-color:white")

        #Uppercase Letter Length Entry
        uppercase_label = QLabel("How Many Uppercase Letters Will Password Include: ",self)
        uppercase_label.setFont(label_font)
        self.uppercase_label_line = QLineEdit()
        self.uppercase_label_line.setPlaceholderText("Enter How Many Uppercase Letters Will Password Include")
        self.uppercase_label_line.setStyleSheet("background-color:white")

        #Number Entry (How many number will password include)
        number_label = QLabel("How Many Number Will Password Include: ",self)
        number_label.setFont(label_font)
        self.number_label_line = QLineEdit()
        self.number_label_line.setPlaceholderText("Enter How Many Number Will Password Include")
        self.number_label_line.setStyleSheet("background-color:white")

        #Special Character Length Entry
        special_character_label = QLabel("How Many Special Characters (Like !,@,%) Will Password Include: ",self)
        special_character_label.setFont(label_font)
        self.special_character_line = QLineEdit()
        self.special_character_line.setPlaceholderText("Enter How Many Special Characters Will Password Include")
        self.special_character_line.setStyleSheet("background-color:white")

        #Generate Button
        password_generate_button = QPushButton(" Generate Password ",self)
        password_generate_button.setStyleSheet("background-color:white")
        password_generate_button.setFont(label_font)
        password_generate_button.setIcon(QIcon("icons/generate_password.png"))
        password_generate_button.clicked.connect(self.Generate_password)

        #Show Created Password(It is invisible when onclicked generate button it'll be shown)
        self.password_show_textbox = QTextEdit()
        self.password_show_textbox.setPlaceholderText("When Password Generated It Will be Shown Here")
        self.password_show_textbox.setReadOnly(True)
        self.password_show_textbox.setStyleSheet("background-color:white")
        self.password_show_textbox.hide()

        #Password Length Entry Layout
        password_layout = QHBoxLayout()
        password_layout.addStretch()
        password_layout.addWidget(password_length_label)
        password_layout.addWidget(self.password_length_line)
        password_layout.addStretch()

        #Uppercase Letter Length Layout
        uppercase_layout = QHBoxLayout()
        uppercase_layout.addStretch()
        uppercase_layout.addWidget(uppercase_label)
        uppercase_layout.addWidget(self.uppercase_label_line)
        uppercase_layout.addStretch()
        
        #Number Length Layout
        number_layout = QHBoxLayout()
        number_layout.addStretch()
        number_layout.addWidget(number_label)
        number_layout.addWidget(self.number_label_line)
        number_layout.addStretch()

        #Button Layout
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(password_generate_button)
        button_layout.addStretch()

        #Special Character Layout
        special_character_layout = QHBoxLayout()
        special_character_layout.addStretch()
        special_character_layout.addWidget(special_character_label)
        special_character_layout.addWidget(self.special_character_line)
        special_character_layout.addStretch()

        #Password Show Layout
        password_show_layout = QHBoxLayout()
        password_show_layout.addStretch()
        password_show_layout.addWidget(self.password_show_textbox)
        password_show_layout.addStretch()

        #Main Layout
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addLayout(header_hlayout)
        main_layout.addStretch()
        main_layout.addLayout(password_layout)
        main_layout.addStretch()
        main_layout.addLayout(uppercase_layout)
        main_layout.addStretch()
        main_layout.addLayout(number_layout)
        main_layout.addStretch()
        main_layout.addLayout(special_character_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        main_layout.addLayout(password_show_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.show()

    #Password Generate Function
    def Generate_password(self):
        #Define Uppercase Letters
        uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        #Define Lowercase Letter
        lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        #Define Numbers
        number_letters = ["0","1","2","3","4","5","6","7","8","9"]

        #Define Special Letters
        special_letters = ["!","^","#","+","$","%","&","{","}","[","]","(",")","=","?","*","-","~","@","<",">","|"]
        

        try:
            #Take Password Informations from User
            password_length = int(self.password_length_line.text())
            uppercase_letter_number = int(self.uppercase_label_line.text())
            number_count = int(self.number_label_line.text())
            special_letter_number = int(self.special_character_line.text())
            lowercase_letter_number = password_length-(uppercase_letter_number+number_count+special_letter_number)
            
            sequal_password = ""

            #Select from Uppercase, Lowercase, Number and Special Letters, then Combine Them
            if((password_length>0)and(lowercase_letter_number>=0)and(uppercase_letter_number>=0)and(number_count>=0)and(special_letter_number>=0)):
                for i in range(0,uppercase_letter_number,1):
                    sequal_password+= random.choice(uppercase_letters)

                for i in range(0,lowercase_letter_number,1):
                    sequal_password+= random.choice(lowercase_letters)

                for i in range(0,number_count,1):
                    sequal_password+= random.choice(number_letters)

                for i in range(0,special_letter_number,1):
                    sequal_password+= random.choice(special_letters)

                #Generate Password Randomly
                password_list = list(sequal_password)

                password = ""

                for i in range(0,password_length,1):
                    selected_word = random.choice(password_list)
                    password+= selected_word
                    password_list.remove(selected_word)
                
                self.password_show_textbox.setText(password)
                self.password_show_textbox.show()

        #Error Messages
            else:
                QMessageBox.information(self,"Fail","Password Couldn't Created Please Check Your Entries. \n1)Password Length Must be Greater than 0.\n2)Total of Uppercase Letters, Lowercase Letters, Number of Special Letters and Numbers Mustn't Exceed Length of Password.")
        except:
            QMessageBox.information(self,"Fail","Password Couldn't Created Please Check Your Entries. \nEnter Number Only ! \nIf You Don't Want to any Type of Letter Enter 0.")

#Start App
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()