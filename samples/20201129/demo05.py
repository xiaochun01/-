class Demo05:
    def __init__(self):
        self.function = {
            'json_key':self.key_check,
            'key_value_check':self.key_value_check
        }

    def key_check(self):
        print('key_check')

    def key_value_check(self):
        print('key_value_check')

    def run_check(self,check_type):
        self.function[check_type]()


