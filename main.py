import customtkinter as ctk
from views.main_window import MainWindow
from views.login_frame import LoginFrame
from utils.config import Config

class App:
    def __init__(self):
        # 设置主题
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # 初始化配置
        self.config = Config()
        
        # 创建主窗口
        self.root = ctk.CTk()
        self.root.title("英语听写软件")
        self.root.geometry("900x600")
        
        # 显示登录界面
        self.show_login()
    
    def show_login(self):
        self.login_frame = LoginFrame(self.root, self.on_auth_success)
        self.login_frame.pack(fill="both", expand=True)
    
    def on_auth_success(self, user_manager):
        # 登录成功后，移除登录界面，显示主界面
        self.login_frame.pack_forget()
        self.main_window = MainWindow(self.root, self.config, user_manager)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run() 