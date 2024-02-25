# Author: Ajinkya Salunke
# Date: 25 Feb 2024
# Time: 15:37
# Problem statement: Build a quiz application using OOP




# Importing random module
import random


# Quizes class
class Quezes:
    
    
    # Constructor
    def __init__(self):
        self.score = 0
    
    
    # private staticmethod for welcome screen
    @staticmethod
    def __welcome_message():
        print("                              ---Welcome to the quiz game---")
        print("""
                Quiz scoring system : 
                                    1. Correct answer   = + 10%
                                    2. Incorrect answer = - 2.5%
        """)
        
        
    # Boolean method for user permission on playing game
    def play_or_not(self):
        
        # Welcome screen
        Quezes.__welcome_message()
        
        # Taking user's input as permission
        permission = input("Do you want to play the game or not (y/n) ?\n\t").lower()
        
        # Judging the user input returning true for yes and false for no
        if permission == "y":
            return True
        elif permission == "n":
            return False
        else:
            print("Please select a valid option....")
      
      
    # Question and answers set a private function
    def __q_n_a_sets(self):
        
        # Storing questions and answers into a dictionary
        q_n_a_set = {
            "What is the long form of CPU?": "central processing unit",
            "What is the long form of GPU?": "graphics processing unit",
            "What is the long form of RAM?": "random access memory",
            "What is the long form of ROM?": "read only memory",
            "What is the long form of HDD?": "hard disk drive",
            "What is the long form of SSD?": "solid state drive",
            "What is the long form of BIOS?": "basic input output system",
            "What is the long form of HTML?": "hypertext markup language",
            "What is the long form of CSS?": "cascading style sheets",
            "What is the long form of HTTP?": "hypertext transfer protocol",
            "What is the long form of HTTPS?": "hypertext transfer protocol secure",
            "What is the long form of URL?": "uniform resource locator",
            "What is the long form of IP?": "internet protocol",
            "What is the long form of LAN?": "local area network",
            "What is the long form of WAN?": "wide area network",
            "What is the long form of WLAN?": "wireless local area network",
            "What is the long form of TCP?": "transmission control protocol",
            "What is the long form of UDP?": "user datagram protocol",
            "What is the long form of SMTP?": "simple mail transfer protocol",
            "What is the long form of FTP?": "file transfer protocol",
            "What is the long form of API?": "application programming interface",
            "What is the long form of GUI?": "graphical user interface",
            "What is the long form of CLI?": "command line interface",
            "What is the long form of DNS?": "domain name system",
            "What is the long form of DHCP?": "dynamic host configuration protocol",
            "What is the long form of VPN?": "virtual private network",
            "What is the long form of RFID?": "radio-frequency identification",
            "What is the long form of IoT?": "internet of things",
            "What is the long form of API?": "application programming interface",
            "What is the long form of JSON?": "javascript object notation",
            "What is the long form of SQL?": "structured query language",
            "What is the long form of XML?": "extensible markup language",
            "What is the long form of AJAX?": "asynchronous javascript and xml",
            "What is the long form of REST?": "representational state transfer",
            "What is the long form of CRUD?": "create, read, update, delete",
            "What is the long form of ORM?": "object relational mapping",
            "What is the long form of OOP?": "object oriented programming",
            "What is the long form of MVC?": "model view-controller",
            "What is the long form of API?": "application programming interface",
            "What is the long form of CMS?": "content management system",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross-site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
            "What is the long form of XSS?": "cross site scripting",
            "What is the long form of CSRF?": "cross site request forgery",
            "What is the long form of JWT?": "json web token",
            "What is the long form of HMAC?": "hash based message authentication code",
            "What is the long form of SSL?": "secure sockets layer",
            "What is the long form of TLS?": "transport layer security",
        }
        return q_n_a_set
        
        
    # A private function for a random question and it's answer
    def __q_n_a(self):
        question, answer  = random.choice(list(self.__q_n_a_sets().items()))
        return question, answer
        
        
    # Method to varify the user's answer with actual answer and returning a boolean value
    def ask_question_check_answer(self):
        question, answer = self.__q_n_a()
        users_answer  = input(question + "\n\t").lower()
        
        # Checking the answer
        if answer == users_answer:
            print("Your answer correct !\n")
            self.score += 1
        else:
            print("Your answer is incorrect and here is correct one - ", answer, ".\n")
            self.score -= 0.25


    # Printing the final score
    def final_score(self):
        percentages = (self.score/10)*100
        print("Your final score for the quiz is:", "{: .2f}%".format(percentages))
        print("---Thanks for playing ---")



# Driver code
if __name__ == "__main__":
    # Object creation
    quiz = Quezes()
    
    # User judgment
    if quiz.play_or_not():
        for i in range(1, 11):
            print("Question", i, end=". ")
            quiz.ask_question_check_answer()
            
        quiz.final_score()
    else:
        print("We are sad to see you go...")
        quit()
    
    
    












