import pandas as pd

#CONSTANTS

NCORES = 8

T_ing =22
l= 6
V=1
alpha= 0.1
c_p=0.1
h=50
a_s = 60 * (10 ** -4)
m = 50 * (10 ** 3)
C = 900
t = 41


try:
	'''
	metric_1 = df['vnf min cpu'] * df['min mem affinity']
	df = df.assign(metric_1 = metric_1.values)
	df.to_csv('results_out.csv', sep = ';')
	'''
except Exception as e:
	print('error reading file')
	print(e)


	
def getDataframeFromCsv(filePath, delimiter):
	try:
		return pd.read_csv(filePath, delimiter)
	except Exception as e:
		print('Error reading CSV')
		print(e)

def describeDataFrame(df):
	try:
		print(df.describe())
	except Exception as e:
		print('Error describing dataframe')
		print(e)

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

def getMTTF(dataframe):
	#equation # 1
	ec_1 = dataframe['vnf cpu usage'] * NCORES * 2.3
	#Pending equation 2,3,4 and assign to dataframe to save in output csv file
		
def main():
	df = getDataframeFromCsv('results.csv',',')
	

	
if __name__ == '__main__':
	main()