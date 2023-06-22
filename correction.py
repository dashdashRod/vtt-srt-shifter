from datetime import datetime, timedelta
from os.path import splitext

def funcao_positiva(nome_arquivo:str,segundos:int,operator:bool,sub_type:bool):
    result = []
    counter = 0
    with open(nome_arquivo,'r') as f:
        final = f.readlines() 
    # print(list(map(lambda x: x.split('-->'),final)))
    for x in final:
        if(x.__contains__('-->')):
            result = (x.replace(' ','').replace(',','.').replace('\n','').split('-->'))
            # print(result)
            if(len(result[0].split(':')) == 2):
                if(operator):
                    final1 = [datetime.strptime(result[0],'%M:%S.%f') + timedelta(seconds=segundos),datetime.strptime(result[1],'%M:%S.%f') + timedelta(seconds=segundos)]
                else:
                    final1 = [datetime.strptime(result[0],'%M:%S.%f') - timedelta(seconds=segundos),datetime.strptime(result[1],'%M:%S.%f') - timedelta(seconds=segundos)]
                x = x.replace(result[0],datetime.strftime(final1[0],'%M:%S.%f')[:-3])
                x = x.replace(result[1],datetime.strftime(final1[1],'%M:%S.%f')[:-3])
                if(sub_type == False):
                    x = x.replace('.',',')
                final[counter] = x
            if(len(result[0].split(':')) == 3):
                if(operator):
                    final2 = [datetime.strptime(result[0],'%H:%M:%S.%f') + timedelta(seconds=segundos),datetime.strptime(result[1],'%H:%M:%S.%f') + timedelta(seconds=segundos)]
                else:
                    final2 = [datetime.strptime(result[0],'%H:%M:%S.%f') - timedelta(seconds=segundos),datetime.strptime(result[1],'%H:%M:%S.%f') - timedelta(seconds=segundos)]
                x = x.replace(',','.')
                x = x.replace(result[0],datetime.strftime(final2[0],'%H:%M:%S.%f')[:-3])
                x = x.replace(result[1],datetime.strftime(final2[1],'%H:%M:%S.%f')[:-3])
                if(sub_type == False):
                    x = x.replace('.',',')
                final[counter] = x
        counter += 1
    final_name = splitext(nome_arquivo)[0]+'-syncd'+splitext(nome_arquivo)[1]
    with open(final_name,'w') as f:
        f.writelines(final)
    print('Finished\n')

