# # https://programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC


#         # 0,1,2,3,4,5
# vec[i] = [1,2,3,3,2,5]
# p[i] =   [1,3,6,9,11,16]

# p[i] = vec[0] + vec[1] + ... + vec[i]

# the sum of vec[i] ... vec[j] = p[j] - p[i-1]
# because 

# p[j] - p[i-1] = 
# (v[0] + v[1] + ... + v[i-1] + v[i] + v[i+1] + ... + v[j]) - 
# (v[0] + v[1] + ... + v[i-1] )

# = v[i] + v[i+1] + ... + v[j]

# = p[j] - p[i-1]