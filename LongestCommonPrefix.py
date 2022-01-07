    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=201
        for m in range(len(strs)) :
            if len(strs[m])<l :
                l=len(strs[m])
        
        c=0
        k=''
        if k in strs :
            return k
        elif len(strs)==1:
            return(strs[0])
        else :
            for i in range(l) :
                for j in range(len(strs)) :
                    if strs[0][i]==strs[j][i] :
                        pass
                    else :
                        return strs[0][0:c]
                c+=1
            return strs[0][0:c]
        
