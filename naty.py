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

#this function just load the csv 
def load_csv():
	try:
		df = pd.read_csv('results.csv', delimiter = ',', low_memory = False)
		return df
		#metric_1 = df['vnf min cpu'] * df['min mem affinity']
		#df = df.assign(metric_1 = metric_1.values)
		#df.to_csv('results_out.csv', sep = ';')
	except Exception as e:
		print('error reading file')
		print(e)


def load_csv2():
	try:
		df = pd.read_csv('results.csv', delimiter = ',', low_memory = False)
		metric_1 = df['vnf min cpu'] * df['min mem affinity']
		df = df.assign(metric_1 = metric_1.values)
		df.to_csv('results_out.csv', sep = ';')
	except Exception as e:
		print('error reading file')
		print(e)

df = load_csv()



	
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

#equation 1
def get_average_cpu_freceuncy(dataframe):
	ec_1 = dataframe['vnf cpu usage'] * NCORES * 2.3
	return ec_1

def out_put_frecuency(averga_cpu_frecuency):
	T_ing =22
	l= 6
	V=1
	activity_factor= 0.1
	cp=0.1
	h=50
	as_motherboard = 60*(10**-4)
	mass= 50*(10**-3)
	C=900
	t=41
	ec_2= 22 + 0.033*averga_cpu_frecuency
	print ec_2[1]
	return ec_2

def main():
	df = getDataframeFromCsv('results.csv',',')
	#getMTTF(df)
	out_put_frecuency(get_average_cpu_freceuncy(df))

	

	
if __name__ == '__main__':
	main()

