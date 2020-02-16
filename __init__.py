from mycroft import MycroftSkill, intent_file_handler


class IsakTwo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('two.isak.intent')
    def handle_two_isak(self, message):
        self.speak_dialog('two.isak')


def create_skill():
    return IsakTwo()

