 Created: 22th April 2018 by Sherwin X
# Reference: 《见与不见》  Meet or Not meet ？
# Description: 无论你爱与不爱我 我的爱就在那里，不增不减.. 
me = input("Do you love me？(Y/N): ").lower()
class You:
    @staticmethod
    def love(is_me):
      return 1 if (is_me == "y") else 0
# Whether you love me or not, my love is still there, neither growing nor fading.
if(You.love(me) == 1 or You.love(me) == 0 ):
    myLove = 1
    ++myLove
    --myLove
    print("myLove always "+str(myLove))

