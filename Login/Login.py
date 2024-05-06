from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.lang import Builder
from Builders import *
from Database_man import *




class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red" #Application theme..
        self.theme_cls.primary_hue = "900" #For manipulating hue of the application's theme..
        self.theme_cls.theme_style = "Dark" #Background theme..

        
        #Initializing screen...
        screen = Screen() 

        title = MDLabel(
            text="Login!", 
            halign='center', 
            font_style='H3', 
            pos_hint={'center_x': 0.5, 'center_y':0.8})
        
        self.username = Builder.load_string(username_builder)
        self.password = Builder.load_string(password_builder)

        submit_btn = MDRectangleFlatButton(
            text="Login",
            pos_hint={'center_x': 0.5, 'center_y':0.27},
            on_release=self.login)
        
        screen.add_widget(title)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(submit_btn)
        
        return screen
    
    #Utility methods..
    def cls_success_dg(self, obj):
        self.success_dg.dismiss()
        
    def cls_err_dg(self, obj):
        self.err_dg.dismiss()

    def cls_empty_uname_dg(self, obj):
        self.empty_uname_err_dg.dismiss()

    def cls_empty_passwd_dg(self, obj):
        self.empty_passwd_err_dg.dismiss()

     
    #Login button's action..
    def login(self, obj):
        success_dg_cls_btn = MDFlatButton(text="Close", on_release=self.cls_success_dg)
        err_dg_cls_btn = MDFlatButton(text="Close", on_release=self.cls_err_dg)
        empty_uname_dg_cls_btn = MDFlatButton(text="Close", on_release=self.cls_empty_uname_dg)
        empty_passwd_dg_cls_btn = MDFlatButton(text="Close", on_release=self.cls_empty_passwd_dg)
        reg_btn = MDFlatButton(text="Register", on_release=register)
        
        if self.username.text:
            #If, user enters username..
            if self.password.text:
                #If, user enters password..
                

                if logged_in(self.username.text, self.password.text):
                    #If, entered credentials are correct..
                    self.success_dg = MDDialog(             
                        title="Welcome!",
                        text=self.username.text,
                        size_hint=(0.6, 1), 
                        buttons=[success_dg_cls_btn])
                
                    self.success_dg.open()
                
                else:
                    #If, enetered credentials are incorrect..
                    self.err_dg = MDDialog(
                        title="Error!", 
                        text="Incorrect credentials provided. Please do check", 
                        size_hint=(0.6, 1), 
                        buttons=[err_dg_cls_btn, reg_btn])
        
                    self.err_dg.open()
 
            else:
                #If, password field is empty..
                self.empty_passwd_err_dg = MDDialog(
                    title="Error!",
                    text="Please, input your password!",
                    size_hint=(0.6, 1), 
                    buttons=[empty_passwd_dg_cls_btn]
                )

                self.empty_passwd_err_dg.open()

        else:
            #If, username field is empty..
            self.empty_uname_err_dg = MDDialog(
                title="Error!",
                text="Please, input your username!",
                size_hint=(0.6, 1), 
                buttons=[empty_uname_dg_cls_btn]
            )

            self.empty_uname_err_dg.open()

           



        

        
    


if __name__ == "__main__":
    Login().run()