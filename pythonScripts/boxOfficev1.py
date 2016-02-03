# characteristic of Box Office
# 75th Percentile: 51,900,000
# 25th Percentile: 300,000
# Maximum        : 760,500,000
# Minimum        : 181
# Median         : 11,900,000
# Mean           : 42,335,355
bin0 = 181          # minimum_boxOffice
bin1 = 200000       # percent_25th
bin2 = 5000000      # median_oneHalf
bin3 = 20000000     # median_1x
bin4 = 40000000     # median_2x
bin5 = 80000000     # median_3x
#bin6 = 59500000     # median_5x
#bin7 = 760500000    # maximum_boxOffice
#
cnt_bin0 = 0
cnt_bin1 = 0
cnt_bin2 = 0
cnt_bin3 = 0
cnt_bin4 = 0
cnt_bin5 = 0
cnt_bin6 = 0



import csv

#f = open('E:/239 mining/Project/Goudamy/Cmpe239ProjData.csv')
#j = open('E:/239 mining/Project/Goudamy/Cmpe239ProjData_v1.csv','wb')
f = open('E:/239 mining/Project/Goudamy/Transformed/actorDirctorProdTransform.csv')
j = open('E:/239 mining/Project/Goudamy/Transformed/actorDirctorProdTransform_v2.csv','wb')

csv_f = csv.reader(f)
writer = csv.writer(j)
cnt = 0
tf_row = 18 # when counting from 0
#writer.writerow('Title,Genre,Actors,Director,Award,Production,imdbRating,imdbVotes,Released,tomatoUserReviews,tomatoUserRating,tomatoUserMeter,BoxOffice,Rated,Metascore,Wikistats')

for row in csv_f:
    #a = row[tf_row]
    #b = float(a)
    cnt = cnt + 1
    #new_row = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[13],row[14],row[15]]
    #print new_row
    if (cnt>1):
        if (float(row[tf_row]) >= bin0 and float(row[tf_row]) < bin1):
            row[tf_row] = 0
            writer.writerow(row)
            cnt_bin0 += 1
        elif (float(row[tf_row]) >= bin1 and float(row[tf_row]) < bin2):
            row[tf_row] = 1
            writer.writerow(row)
            cnt_bin1 += 1
        elif (float(row[tf_row]) >= bin2 and float(row[tf_row]) < bin3):
            row[tf_row] = 2
            writer.writerow(row)
            cnt_bin2 += 1
        elif (float(row[tf_row]) >= bin3 and float(row[tf_row]) < bin4):
            row[tf_row] = 3
            writer.writerow(row)           
            cnt_bin3 += 1
        elif (float(row[tf_row]) >= bin4 and float(row[tf_row]) < bin5):
            row[tf_row] = 4
            writer.writerow(row)           
            cnt_bin4 += 1
        elif (float(row[tf_row]) >= bin5) :
            row[tf_row] = 5
            writer.writerow(row)           
            cnt_bin5 += 1
        
       

              # print(b)

print('Range of each bin')
print(bin0, bin1, bin2, bin3, bin4, bin5)
print('Number of Box Office in each bin')
print(cnt_bin0, cnt_bin1, cnt_bin2, cnt_bin3, cnt_bin4, cnt_bin5, cnt_bin6)

f.close()
j.close()
