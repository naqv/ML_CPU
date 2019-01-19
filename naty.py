import pandas as pd

try:
	df = pd.read_csv('results.csv', delimiter = ',', low_memory = False)
	metric_1 = df['vnf min cpu'] * df['min mem affinity']
	df = df.assign(metric_1 = metric_1.values)
	df.to_csv('results_out.csv', sep = ';')
except Exception as e:
	print('error reading file')
	print(e)

