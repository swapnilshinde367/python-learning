# pylint: skip-file

import math
import numpy as np
import matplotlib as plt
import pandas as pd

from matplotlib import pylab, mlab, pyplot

# pyplot.plot( np.arange(5))

# pyplot.show()

df = pd.read_csv( 'train.csv' )

# print df.head(10)

# print df.describe()

print df['Property_Area'].value_counts()
# print df['Gender'].value_counts()
# print df['Self_Employed'].value_counts()
# print df['Education'].value_counts()

# Histogram
# df['ApplicantIncome'].hist(bins=50)
# pyplot.show()

# Boxplot
# df.boxplot(column='ApplicantIncome')
# pyplot.show()

# Boxplot by Gender and Education
df.boxplot(column='ApplicantIncome', by=['Gender','Education'])
pyplot.show()

# Histogram
# df['LoanAmount'].hist(bins=50)
# pyplot.show()

# Boxplot
# df.boxplot(column='LoanAmount')
# pyplot.show()

# temp1 = df['Credit_History'].value_counts(ascending=True)
# temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x:x.map({'Y':1,'X':0}).mean())
# print 'Frequency Table for Credit History:'
# print temp1

# print '\nProbility of getting loan for each Credit History class:'
# print temp2


# print df.loc[(df["Gender"]=="Male") & (df["Education"]=="Not Graduate") & (df["Loan_Status"]=="N"), ["Gender","Education","Loan_Status"]]
