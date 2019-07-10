class Solution:
    def longestPalindrome_bruteforce(self, s):
        if not s:
            return s

        ret = ""
        for i in range(len(s)):
            j = i+1

            while j <= len(s):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(ret):
                    ret = s[i:j]
                j = j+1

        return ret

    def longestPalindrome_manacher(self, s):
        a = "#"+"#".join(s)+"#"  # preprocess
        mx = 0  # the fastest index that ever reached
        id = 0  # the centor of the string above

        mp = [0]*(len(a))
        for i in range(len(a)):
            if mx > i:
                mp[i] = min(mp[2*id-i], mx-i)
            else:
                mp[i] = 1
            while i+mp[i] < len(a) and i-mp[i] >= 0 and a[i+mp[i]] == a[i-mp[i]]:
                mp[i] = mp[i]+1
            if i+mp[i] > mx:
                mx = i+mp[i]
                id = i

        length = max(mp)
        i = mp.index(max(mp))
        ret = a[(i-length+1):(i+length-1)]
        return ret.replace('#','')


""" 
Input: "babad"
Output: "bab"
"""

input = "babad"

solution = Solution()
print(solution.longestPalindrome_bruteforce(input))
print(solution.longestPalindrome_manacher(input))
