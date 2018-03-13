import matplotlib.pyplot as plt
import q36

word_list = q36.make_word_list("../neko.txt")
word_ranking = q36.make_word_ranking(word_list)

freq_list = list(map(lambda x:x[1],word_ranking))

plt.xscale("log")
plt.yscale("log")
plt.plot(range(1,len(freq_list)+1),freq_list)
plt.show()
