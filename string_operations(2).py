'''Given s = "bad python bad teacher bad lecture"
Replace all occurrences of bad to good
Replace first occurrence of bad to good
find the leftmost bad
find the second bad from left
Replace the second bad to worst and display from that point of string and also display the whole string'''


s = "bad python bad teacher bad lecture"
print(s.replace('bad','good'))
print(s.replace('bad','good',1))
print(s.index('bad'))
print(s.index('bad',s.index('bad')+len('bad')))
i=s.index('bad',s.index('bad')+len('bad'))
print(i)
print(s[i:].replace('bad','worst',1))
print(s[:i]+s[i:].replace('bad','worst',1))
