class Solution:

    def encode(self, strs: List[str]) -> str:

        encStr = ""
        for s in strs:
            length = len(s)
            encStr += str(length)+"#"+s

        return encStr

    def decode(self, s: str) -> List[str]:
        decList = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            decList.append(word)
            i = j+1+length

        return decList

