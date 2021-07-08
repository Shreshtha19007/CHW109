import pandas as pd
import csv
import statistics

df=pd.read_csv("data.csv")
gender_list = df["gender"].to_list()
race_list = df["race/ethnicity"].to_list()
parent_list = df["parental level of education"].to_list()
lunch_list = df["lunch"].to_list()
test_list = df["test preparation course"].to_list()
math_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()




gender_mean=statistics.mean(gender_list)
gender_median=statistics.median(gender_list)
gender_mode=statistics.mode(gender_list)
race_mean=statistics.mean(race_list)
race_median=statistics.median(race_list)
race_mode=statistics.mode(race_list)
parent_mean=statistics.mean(parent_list)
parent_median=statistics.median(parent_list)
parent_mode=statistics.mode(parent_list)
lunch_mean=statistics.mean(lunch_list)
lunch_median=statistics.median(lunch_list)
lunch_mode=statistics.mode(lunch_list)
test_mean=statistics.mean(test_list)
test_median=statistics.median(test_list)
test_mode=statistics.mode(test_list)
math_mean=statistics.mean(math_list)
math_median=statistics.median(math_list)
math_mode=statistics.mode(math_list)
reading_mean=statistics.mean(reading_list)
reading_median=statistics.median(reading_list)
reading_mode=statistics.mode(reading_list)
writing_mean=statistics.mean(writing_list)
writing_median=statistics.median(writing_list)
writing_mode=statistics.mode(writing_list)


print("Mean,median,mode of the gender data is".format(gender_mean,gender_median,gender_mode))
print("Mean,median,mode of the race data is".format(race_mean,race_median,race_mode))
print("Mean,median,mode of the parent data is".format(parent_mean,parent_median,parent_mode))
print("Mean,median,mode of the lunch data is".format(lunch_mean,lunch_median,lunch_mode))
print("Mean,median,mode of the test data is".format(test_mean,test_median,test_mode))
print("Mean,median,mode of the math data is".format(math_mean,math_median,math_mode))
print("Mean,median,mode of the reading data is".format(reading_mean,reading_median,reading_mode))
print("Mean,median,mode of the writing data is".format(writing_mean,writing_median,writing_mode))