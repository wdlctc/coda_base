import os 
import json
import statistics

g = os.walk(r"./")  

results = {}

for path,dir_list,file_list in g:  
    for file_name in file_list: 
        if '.log' in file_name:
            with open(os.path.join(path, file_name),'r') as f:
                result = {'signal_level':[],
                          'ebno': []}
                for line in f:
                    if 'signal_level' in line and '=' in line:
                        result['signal_level'].append(float(line.split()[-1]))
                    if 'ebno' in line and '=' in line:
                        result['ebno'].append(float(line.split()[-1]))
                if len(result['signal_level']):
                    result['signal_level_mean'] = statistics.mean(result['signal_level'])
                    result['signal_level_stdev'] = statistics.stdev(result['signal_level'])
                    result['signal_level_1DB'] = sum([abs(signal_level - result['signal_level_mean']) < 1 for signal_level in result['signal_level']]) / len(result['signal_level'])
                    result['signal_level_3DB'] = sum([abs(signal_level - result['signal_level_mean']) < 3 for signal_level in result['signal_level']]) / len(result['signal_level'])
                    result['signal_level_5DB'] = sum([abs(signal_level - result['signal_level_mean']) < 5 for signal_level in result['signal_level']]) / len(result['signal_level'])
                    result['signal_level_10DB'] = sum([abs(signal_level - result['signal_level_mean']) < 10 for signal_level in result['signal_level']]) / len(result['signal_level'])
                    print(os.path.join(path, file_name), result['signal_level_mean'], result['signal_level_stdev'], result['signal_level_1DB'],result['signal_level_3DB'],result['signal_level_5DB'])
                if len(result['ebno']):
                    result['ebno_mean'] = statistics.mean(result['ebno'])
                    result['ebno_stdev'] = statistics.stdev(result['ebno'])
                    result['ebno_1NO'] = sum([abs(signal_level - result['ebno_mean']) < 1 for signal_level in result['ebno']]) / len(result['signal_level'])
                    result['ebno_3NO'] = sum([abs(signal_level - result['ebno_mean']) < 3 for signal_level in result['ebno']]) / len(result['signal_level'])
                    result['ebno_5NO'] = sum([abs(signal_level - result['ebno_mean']) < 5 for signal_level in result['ebno']]) / len(result['signal_level'])
                    result['ebno_10NO'] = sum([abs(signal_level - result['ebno_mean']) < 10 for signal_level in result['ebno']]) / len(result['signal_level'])
                results[os.path.join(path, file_name)] = result
                
            # print(os.path.join(path, file_name))
json.dump(results, open('results.log', 'w'))
