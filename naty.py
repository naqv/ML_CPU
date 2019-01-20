import pandas as pd
import math

#CONSTANTS

NCORES = 8
T_inf =22
I= 6
V=1
activity_factor= 0.1
cp=0.1
h=50
as_motherboard = 60*(10**-4)
mass= 50*(10**-3)
C=900
t=41
tp_0= 293.15
e0=0.642
k=0.000863
mttftpo= 27800

def load_csv():
	try:
		df = pd.read_csv('results.csv', delimiter = ',', low_memory = False)
		return df
  	except Exception as e:
   		print('error reading file')
    	print(e)

def add_metrics_to_new_csv(mtt,mtt_upper,mtt_lower):
	try:
		df = pd.read_csv('results.csv', delimiter = ',', low_memory = False)
		df = df.assign(MTT = mtt.values)
		df = df.assign(MTT_upper = mtt_upper.values)
		df = df.assign(MTT_lower = mtt_lower.values)
		df.to_csv('results_out.csv', sep = ';')
	except Exception as e:
		print('error reading file')
		print(e)



# this get the dataframe from the CSV using pandas.
def getDataframeFromCsv(filePath, delimiter):
	try:
		return pd.read_csv(filePath, delimiter)
	except Exception as e:
		print('Error reading CSV')
		print(e)

#this describeDataFrame.
def describeDataFrame(df):
	try:
		print(df.describe())
	except Exception as e:
		print('Error describing dataframe')
		print(e)

#null features.
def describeNullFeature(dataframe, feature):
    try:
        records = len(dataframe)
        feature_nulls = dataframe[feature].isnull().sum()
    
        print('# records: ', records)
        print('flow traffic null: ', feature_nulls)
        print('% null flow traffic: ', (100*feature_nulls/(1.0*records)))
    except Exception as e:
        print('Error describing csv, dataframe and/or feature invalid')
        print(e)

#function that get the cpu_frecuency from the vnf cpu usage
#equation 1
def get_average_cpu_freceuncy(dataframe):
	ec_1 = dataframe['vnf cpu usage'] * NCORES * 2.3
	return ec_1

#equation 2
def output_frequency(vectorFrequency):
  factor_a = ((I * V) + (activity_factor * cp * V**2 ) ) / ( h * as_motherboard )
  factor_b = (1 - math.e ** (-((h * as_motherboard * 3600) / (mass * 900)  )* 1000))
  ec_2 = T_inf + factor_a * vectorFrequency * factor_b 
  return ec_2

#equation 3
def mttf(temperature):
	mtt= mttftpo*(math.e**((e0/k)*(1/temperature - 1/tp_0)))
	return mtt

#upper
def mtt_upper(mtt):
	mtt_upper = mtt + mtt*0.5
	return mtt_upper

#lower
def mtt_lower(mtt):
	mtt_lower = mtt - mtt*05 
	return mtt_lower

def main():
	df = load_csv()
	df = getDataframeFromCsv('results.csv',',')
	mtt= mttf(output_frequency(get_average_cpu_freceuncy(df)))
	add_metrics_to_new_csv(mtt,mtt_upper(mtt),mtt_lower(mtt))

if __name__ == '__main__':
	main()

