class Solution(object):
    def longestCommonPrefix(self, strs):
                
        pl = []
        
        if len(strs) == 1:
            return strs[0]
        
        elif len(strs) > 1 and len(strs[0]) > 0 and len(strs[1]) > 0 and strs[0][0] != strs[1][0]:
            return ""
        
        else:
        
            for l in range (len(strs[0])):
                pl.append(strs[0][l])
                for w in range (len(strs)):
                    if w < len(strs) and l < len(strs[w]) and strs[w][l] == pl[l]:
                        continue
                    else:
                        removedElement = strs[0][l]
                        for i in range(len(pl) - 1, -1, -1):
                            if pl[i] == removedElement:
                                del pl[i]
                                return ''.join(pl)                        
                        
        prefix = ''.join(pl)            
        return(prefix)        