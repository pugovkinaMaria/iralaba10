'''
Лабораторная работа, 10
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('udemy_courses.csv')
free = df[df["price"] == 0]
short = df['content_duration']

sortedd = free.sort_values(by=['num_subscribers'])
shortsort = df.sort_values(by=['content_duration'])

top = sortedd.head(10)
topshort = shortsort.head(10)
print(top, topshort)

plt.plot(top['num_subscribers'],top['course_title'])
plt.show()

plt.plot(topshort['content_duration'],topshort['course_title'])
plt.show()
