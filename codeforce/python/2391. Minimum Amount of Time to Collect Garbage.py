class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m = 0
        m_dis = 0
        g = 0
        g_dis = 0
        p = 0
        p_dis = 0
        for i in range(len(garbage)):
            for j in garbage[i]:
                if j == "M":
                    m+=1
                    m_dis = i
                elif j == "G":
                    g +=1
                    g_dis = i
                else:
                    p +=1
                    p_dis = i
        m_dis = sum(travel[:m_dis])
        g_dis = sum(travel[:g_dis])
        p_dis = sum(travel[:p_dis])
        return m + g + p + m_dis + g_dis + p_dis