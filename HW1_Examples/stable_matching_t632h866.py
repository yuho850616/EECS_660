import sys

class Man:
    def __init__(self, rank_list):
        self.spouse = -1
        self.ranking = rank_list
        self.status_engaged = False #no partner

class Woman:
    def __init__(self, rank_list):
        self.spouse = 1
        self.ranking = rank_list
        self.status_engaged = False #no partner

def stable_matching( size, m_preference_list, w_preference_list ):
    m_list = []
    w_list = []
    for i in range(size):
        m_list.append(Man(m_preference_list[i])) # Initial all m are free
        w_list.append(Woman(w_preference_list[i]))# Initial all w are free

    m_married = 0

    while m_married < size: # While there is a man m who is free and hasn't proposed to every woman.
        for j in range (size):
            if m_list[j].status_engaged == False:# Choose such a man m
                top_rank_woman = m_list[j].ranking[0]-1 # Let w be the highest-ranked woman in m's preference list to whom m has not yet proposed
                m_list[j].ranking.pop(0)
                if w_list[top_rank_woman].status_engaged == False: # If w is free then
                    #(m,w) become engaged
                    m_list[j].status_engaged = True
                    m_list[j].spouse = top_rank_woman
                    w_list[top_rank_woman].status_engaged = True
                    w_list[top_rank_woman].spouse = j
                    m_married += 1
                else: # Else w is currently engaged to m'
                    engaged_woman = w_list[top_rank_woman].spouse
                    if w_list[top_rank_woman].ranking.index(j+1) > w_list[top_rank_woman].ranking.index(engaged_woman+1):# If w prefers m' to m then
                        pass # m remains free
                    else: #Else w prefers m to m'
                        #(m,w) become engaged
                        #m' becomes free
                        m_list[j].status_engaged = True
                        m_list[j].spouse = top_rank_woman
                        w_list[top_rank_woman].status_engaged = True
                        w_list[top_rank_woman].spouse = j
                        m_list[engaged_woman].status_engaged = False
                        m_list[engaged_woman].spouse = -1
    for k in range(size): #stdout
        print (str(k+1)+', '+str(m_list[k].spouse+1))


def main(): # read file and pass in two 2D list for stable matching function
    my_file = open( sys.argv[ 1 ], 'r' )
    amount = my_file.readline() # the number of men and women in the stable matching problem
    size = int(amount) # string to int
    m_preference_list = [] # empty men list
    w_preference_list = [] # empty women list
    for i in range (size):
        m_preference_list.append([]) # 2d size*size empty men list
        w_preference_list.append([]) # 2d size*size empty women list
    my_file.readline() # read the empty line

    for i in range (size):
        temp = my_file.readline() # read each men's preference
        temp = temp.strip("\n") # remove the \n at the end of each line
        m_preference_list[i] = temp.split(",") # split the whole string to each individual number
        m_preference_list[i] = list(map(int, m_preference_list[i])) # map int to each string number

    my_file.readline() # read the empty line

    for i in range (size):
        temp = my_file.readline() # read each women's preference
        temp = temp.strip("\n")  # remove the \n at the end of each line
        w_preference_list[i] = temp.split(",")# split the whole string to each individual number
        w_preference_list[i] = list(map(int, w_preference_list[i])) # map int to each string number

    stable_matching(size, m_preference_list, w_preference_list) # call the stable matching function

main()
