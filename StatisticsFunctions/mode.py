class mode:
    @staticmethod
    def mode(data):
        if data == []:
            return None
        else:
            return max(set(data), key=data.count)