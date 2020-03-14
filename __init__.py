from mycroft import MycroftSkill, intent_file_handler


class Slur(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('slur.intent')
    def handle_slur(self, message):
        self.speak_dialog('slur')


def create_skill():
    return Slur()

