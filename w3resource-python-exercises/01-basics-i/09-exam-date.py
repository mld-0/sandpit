import datetime
exam_st_date = (11, 12, 2014)
exam_date = datetime.datetime(*exam_st_date[::-1])
print(exam_st_date)
print(exam_date)
