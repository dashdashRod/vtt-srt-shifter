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
                #NOTE print(f"primeiro valor {datetime.strftime(final[0],'%M:%S.%f')[:-3]}  Segundo valor {datetime.strftime(final[1],'%M:%S.%f')[:-3]}")
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
                #NOTE  print(f"primeiro valor {datetime.strftime(final2[0],'%H:%M:%S.%f')[:-3]}  Segundo valor {datetime.strftime(final2[1],'%H:%M:%S.%f')[:-3]}")
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
    

nome_arquivo = 'KuroNeko-Subtitles.vtt'
new_nome = 'I.Live.In.Fear.English-WWW.MY-SUBS.CO.srt'
# funcao(nome_arquivo=nome_arquivo,segundos=0)

# algo = 70
# novo = 35
# # converted = time.strptime(algo).strftime('%M:%S.%f')
# # print(datetime.strftime('%M:%S.%f',time.gmtime(algo)))
# result = datetime.fromtimestamp(algo).strftime('%M:%S.%f')[:-3]
# # novo = datetime.fromtimestamp(novo).strftime('%M:%S.%f')[:-3]
# # print(datetime.strptime(result,'%M:%S.%f') + datetime.strptime(novo,'%M:%S.%f'))
# resultado = datetime.fromtimestamp(algo).strftime('%M:%S.%f')[:-3]
# final = datetime.strptime(resultado,'%M:%S.%f')
# final = datetime.strftime(final,'%M:%S.%f')
# print(final)

if __name__ == '__main__':
    nome_arquivo = new_nome
    if(splitext(nome_arquivo)[1] == '.vtt'):
        temp = True
    else:
        temp = False
    funcao_positiva(nome_arquivo=nome_arquivo,segundos=20,operator=True,sub_type=temp)






