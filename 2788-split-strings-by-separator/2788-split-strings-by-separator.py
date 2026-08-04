class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        an=[]
        for i in words:
            for b in i.split(separator):
                 if b:
                    an.append(b)
        return an
        