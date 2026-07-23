class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maximum = max(len(sentence.split()) for sentence in sentences)
    
        return maximum