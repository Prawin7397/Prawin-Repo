Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> Info = pd.read_csv('C:\\Users\\Lenovo\\Documents\\hr_analytics.csv')
>>> Info.columns
Index(['Employee ID', 'Year of Joining', 'Month of Joining', 'Day of Joining',
       'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18',
       'OverTime', 'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
       'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager', 'Age', 'Attrition', 'BusinessTravel',
       'DailyRate', 'Department', 'DistanceFromHome', 'Education',
       'EducationField', 'EmployeeCount', 'EmployeeNumber',
       'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement',
       'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus'],
      dtype='object')
>>> Info[('MaritalStatus')]
0         Married
1          Single
2         Married
3         Married
4        Divorced
           ...   
49995    Divorced
49996      Single
49997      Single
49998      Single
49999      Single
Name: MaritalStatus, Length: 50000, dtype: object
>>> Info[('JobSatisfaction')]
0        1
1        3
2        2
3        1
4        2
        ..
49995    2
49996    3
49997    3
49998    4
49999    2
Name: JobSatisfaction, Length: 50000, dtype: int64
>>> Ins[('Gender')]
0          Male
1        Female
2        Female
3        Female
4          Male
          ...  
49995    Female
49996    Female
49997    Female
49998      Male
49999    Female
Name: Gender, Length: 50000, dtype: object
>>> Ins[('PerformanceRating')]
0        4
1        1
2        3
3        3
4        3
        ..
49995    4
49996    1
49997    4
49998    1
49999    4
Name: PerformanceRating, Length: 50000, dtype: int64


>>> Info.groupby(['MaritalStatus'])['JobSatisfaction'].count()
MaritalStatus
Divorced    16616
Married     16681
Single      16703
Name: JobSatisfaction, dtype: int64

>>> It.to_csv('C:\\Users\\Lenovo\\Desktop\\Full demo\\Project.csv')

Info.groupby(['MaritalStatus'])['PerformanceRating'].count()
MaritalStatus
Divorced    16616
Married     16681
Single      16703
Name: PerformanceRating, dtype: int64
Info.groupby('Gender')['JobSatisfaction'].count()
Gender
Female    24941
Male      25059
Name: JobSatisfaction, dtype: int64
Info.groupby(['JobSatisfaction'])['Gender'].max()
JobSatisfaction
1    Male
2    Male
3    Male
4    Male
Name: Gender, dtype: object
Info.groupby(['JobSatisfaction'])['MaritalStatus'].max()
JobSatisfaction
1    Single
2    Single
3    Single
4    Single
Name: MaritalStatus, dtype: object

Info[['Employee ID','Gender']].head(3)
  
   Employee ID  Gender
0            1    Male
1            2  Female
2            3  Female

Info[['Employee ID','Gender','HourlyRate']].head(50)
  
    Employee ID  Gender  HourlyRate
0             1    Male          42
1             2  Female          66
2             3  Female          96
3             4  Female          71
4             5    Male         122
5             6  Female         195
6             7  Female          80
7             8    Male         165
8             9    Male         134
9            10  Female         137
10           11    Male         159
11           12  Female          51
12           13  Female         189
13           14  Female          69
14           15    Male         127
15           16  Female         151
16           17    Male         181
17           18  Female          92
18           19  Female          81
19           20  Female          66
20           21  Female         157
21           22    Male         162
22           23    Male          44
23           24  Female          71
24           25    Male          44
25           26  Female          69
26           27    Male         146
27           28    Male          83
28           29  Female         112
29           30  Female         135
30           31    Male         161
31           32  Female          47
32           33  Female         100
33           34    Male          86
34           35    Male         111
35           36    Male         186
36           37  Female         103
37           38  Female         175
38           39  Female          64
39           40    Male         106
40           41    Male         129
41           42    Male         136
42           43    Male         138
43           44  Female         154
44           45  Female          48
45           46  Female          56
46           47    Male          44
47           48  Female          98
48           49  Female          85
49           50  Female          95

Info[['Employee ID','Gender','HourlyRate']].head(10)
   Employee ID  Gender  HourlyRate
0            1    Male          42
1            2  Female          66
2            3  Female          96
3            4  Female          71
4            5    Male         122
5            6  Female         195
6            7  Female          80
7            8    Male         165
8            9    Male         134
9           10  Female         137

A= Info.nsmallest(20,'HourlyRate','first')
A
      Employee ID  Year of Joining  ...  JobSatisfaction  MaritalStatus
247           248             2014  ...                4        Married
312           313             1993  ...                2       Divorced
360           361             1986  ...                1        Married
540           541             2015  ...                2         Single
601           602             1984  ...                2         Single
936           937             1984  ...                1        Married
947           948             1992  ...                2         Single
1032         1033             2013  ...                2        Married
1046         1047             2019  ...                4       Divorced
1280         1281             1995  ...                4        Married
1337         1338             1985  ...                2       Divorced
1751         1752             2011  ...                2         Single
1762         1763             2004  ...                1        Married
1846         1847             2018  ...                2       Divorced
1943         1944             1987  ...                3         Single
2532         2533             2002  ...                3         Single
2630         2631             2001  ...                2         Single
2644         2645             1993  ...                3        Married
2970         2971             1988  ...                2       Divorced
3315         3316             1992  ...                3       Divorced

[20 rows x 39 columns]

A.to_csv('C:\\Users\\Lenovo\\Desktop\\Full demo\\Project2.csv')

Info.nsmallest(20,'HourlyRate','first').max()
Employee ID                                 3316
Year of Joining                             2019
Month of Joining                              12
Day of Joining                                27
MonthlyIncome                              45913
MonthlyRate                              1279890
NumCompaniesWorked                             8
Over18                                         Y
OverTime                                     Yes
PercentSalaryHike                             49
PerformanceRating                              4
RelationshipSatisfaction                       4
StandardHours                                 80
StockOptionLevel                               4
TotalWorkingYears                             38
TrainingTimesLastYear                          6
WorkLifeBalance                                4
YearsAtCompany                                34
YearsInCurrentRole                            24
YearsSinceLastPromotion                       23
YearsWithCurrManager                          17
Age                                           60
Attrition                                    Yes
BusinessTravel                     Travel_Rarely
DailyRate                                   1489
Department                               Support
DistanceFromHome                              50
Education                                      5
EducationField                  Technical Degree
EmployeeCount                                  1
EmployeeNumber                              3316
EnvironmentSatisfaction                        4
Gender                                      Male
HourlyRate                                    30
JobInvolvement                                 4
JobLevel                                       5
JobRole                     Sales Representative
JobSatisfaction                                4
MaritalStatus                             Single
dtype: object
B= Info.nsmallest(20,'HourlyRate','first').max()
B.to_csv('C:\\Users\\Lenovo\\Desktop\\Full demo\\Project3.csv')

I = Info.nlargest(20,'JobSatisfaction','first')
I
    Employee ID  Year of Joining  ...  JobSatisfaction  MaritalStatus
6             7             2018  ...                4       Divorced
7             8             2020  ...                4         Single
8             9             2014  ...                4       Divorced
12           13             1992  ...                4        Married
14           15             2020  ...                4        Married
15           16             1995  ...                4       Divorced
24           25             2007  ...                4       Divorced
25           26             2000  ...                4        Married
29           30             2019  ...                4        Married
34           35             2015  ...                4       Divorced
35           36             2010  ...                4         Single
38           39             1983  ...                4        Married
41           42             1988  ...                4         Single
52           53             1994  ...                4       Divorced
63           64             1990  ...                4         Single
67           68             2011  ...                4        Married
72           73             1982  ...                4         Single
77           78             1998  ...                4         Single
79           80             1998  ...                4         Single
83           84             2008  ...                4        Married

[20 rows x 39 columns]
I.to_csv('C:\\Users\\Lenovo\\Desktop\\Full demo\\Project4.csv')
S = Info.nlargest(20,'JobSatisfaction','first').max()
S
Employee ID                                   84
Year of Joining                             2020
Month of Joining                              12
Day of Joining                                24
MonthlyIncome                              50393
MonthlyRate                              1061606
NumCompaniesWorked                             7
Over18                                         Y
OverTime                                     Yes
PercentSalaryHike                             48
PerformanceRating                              4
RelationshipSatisfaction                       4
StandardHours                                 80
StockOptionLevel                               4
TotalWorkingYears                             40
TrainingTimesLastYear                          6
WorkLifeBalance                                4
YearsAtCompany                                31
YearsInCurrentRole                            14
YearsSinceLastPromotion                       18
YearsWithCurrManager                          18
Age                                           60
Attrition                                    Yes
BusinessTravel                     Travel_Rarely
DailyRate                                   1464
Department                               Support
DistanceFromHome                              50
Education                                      5
EducationField                  Technical Degree
EmployeeCount                                  1
EmployeeNumber                                84
EnvironmentSatisfaction                        4
Gender                                      Male
HourlyRate                                   200
JobInvolvement                                 4
JobLevel                                       5
JobRole                     Sales Representative
JobSatisfaction                                4
MaritalStatus                             Single
dtype: object
S.to_csv('C:\\Users\\Lenovo\\Desktop\\Full demo\\Project5.csv')
