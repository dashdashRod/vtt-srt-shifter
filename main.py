import correction
import argparse

parser = argparse.ArgumentParser(description='Time shift captions in a srt or vtt file')
parser.add_argument('-i','--input',type=str,metavar='',help='.vtt or .srt file input',required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-p','--plus',type=str,metavar='',help='Add to the captions in seconds')
group.add_argument('-m','--minus',type=str,metavar='',help='Subtract to the captions in seconds')
args = parser.parse_args()

if __name__ == '__main__':
    name_file = args.input
    if (correction.splitext(name_file)[1] == '.vtt'):
        temp = True #Boolean for vtt or srt
    elif(correction.splitext(name_file)[1] == '.srt'):
        temp = False
    if(args.plus):
        r = int(args.plus)
        t = True #Operator Plus
    elif(args.minus):
        r = int(args.minus)
        t = False #Operator Minus
    correction.funcao_positiva(nome_arquivo=name_file,segundos=r,operator=t,sub_type=temp)


