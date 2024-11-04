name1 =input("write your name= ")
name2=input("write her/his name= ")
combine_string= name1+name2
lower_case_string = combine_string.lower()
t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t+r+u+e

l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
Love=l+o+v+e

love_score=int(str(true)+str(Love))
if   love_score > 90:
    print(f" your love score is {love_score}")
elif  love_score >50 or  love_score<90:
    print(f" your love score is {love_score}")
elif love_score >= 40 or love_score <= 50 :
    print(f" your love score is {love_score}   you are alright together ")
elif love_score < 10:
    print("your love score is ")
else:
    print(f" kamm chal jaega biduu dekh lo {love_score}")
