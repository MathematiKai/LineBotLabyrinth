from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def up(self, event):
        text = event.message.text
        return text.lower() == "up"

    def down(self, event):
        text = event.message.text
        return text.lower() == "down"


    def left(self, event):
        text = event.message.text
        return text.lower() == "left"

    def right(self, event):
        text = event.message.text
        return text.lower() == "right"


    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1\n Retart Maze Traverse")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
    
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
    
    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state4")
    
    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state5")
    
    def on_enter_state6(self, event):
        print("I'm entering state6")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state6")
    
    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state7")
    
    def on_enter_state8(self, event):
        print("I'm entering state8")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state8")
    
    def on_enter_state9(self, event):
        print("I'm entering state9")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state9")
    
    def on_enter_state10(self, event):
        print("I'm entering state10")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state10")
    
    def on_enter_state11(self, event):
        print("I'm entering state11")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state11")
    
    def on_enter_state12(self, event):
        print("I'm entering state12")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state12")
    
    def on_enter_state13(self, event):
        print("I'm entering state13")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state13")
    
    def on_enter_state14(self, event):
        print("I'm entering state14")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state14")
    
    def on_enter_state15(self, event):
        print("I'm entering state15")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state15")
    
    def on_enter_state16(self, event):
        print("I'm entering state16")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state16\nEnd of Maze Traverse")
        self.go_back()
    
    



    def on_exit_state1(self,event):
        print("Leaving state1")

    def on_exit_state2(self,event):
        print("Leaving state2")

    def on_exit_state3(self,event):
        print("Leaving state3")

    def on_exit_state4(self,event):
        print("Leaving state4")

    def on_exit_state5(self,event):
        print("Leaving state5")

    def on_exit_state6(self,event):
        print("Leaving state6")

    def on_exit_state7(self,event):
        print("Leaving state7")

    def on_exit_state8(self,event):
        print("Leaving state8")

    def on_exit_state9(self,event):
        print("Leaving state9")

    def on_exit_state10(self,event):
        print("Leaving state10")

    def on_exit_state11(self,event):
        print("Leaving state11")

    def on_exit_state12(self,event):
        print("Leaving state12")

    def on_exit_state13(self,event):
        print("Leaving state13")

    def on_exit_state14(self,event):
        print("Leaving state14")

    def on_exit_state15(self,event):
        print("Leaving state15")

    def on_exit_state16(self,event):
        print("Leaving state16")

    
