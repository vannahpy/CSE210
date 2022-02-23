class Phone:
    def __init__(self, number):
        self.phone_number = number
        self.text_messages = []

    def place_call(number_to_call):
        return number_to_call

    def place_text(number_to_text, message_to_send):
        return message_to_send
    
    def save_text(self, message_to_save):
        self.text_messages.append(message_to_save)
    
    def get_texts(self):
        return self.text_messages
    
    def get_number(self):
        return self.phone_number

class CameraPhone(Phone):
    def __init__(self, number):
        super().__init__(number)
        self.pictures = []
    
    def take_picture(self, picture_name):
        self.pictures.append(picture_name)


camera = CameraPhone(2357088)
print(camera.get_number())
camera.save_text("This is the first message")
camera.save_text("This is the second")
print(camera.get_texts())