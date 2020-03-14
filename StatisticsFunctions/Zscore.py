from scipy import stats
class zscore():
    @staticmethod
    def zscore(data):
        return stats.zscore(data)