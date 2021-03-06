from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import re

def reverse_complementary(a): #функция построения комплементарной цепи ДНК
    comp=[]
    for i in a:
        if i =='A':
            comp.append('T')
        elif i =='T':
            comp.append('A')
        elif i =='G':
            comp.append('C')
        elif i =='C':
            comp.append('G')
    comp = comp[-1::-1]
    return comp

def primer_1(n): #функция для подбора праймеров в первом варианте интеграции вставок (при наличии MCS)
    primers=[]
    primersL = good_sitesL[n] + vstavki_sort[n][0:21]
    primers.append(primersL)
    primersRb = ''.join(reverse_complementary(vstavki_sort[n][-1:-16:-1]))
    primersR = good_sitesL[n] + primersRb
    primers.append(primersR)
    return primers

def primer_2(n): #функция для подбора праймеров во втором варианте интеграции вставок (при отсутствии MCS)
    primers=[]
    primersL = unic_sites[n] + vstavki_sort[n][0:21]
    primers.append(primersL)
    primersRb = ''.join(reverse_complementary(vstavki_sort[n][-1:-16:-1]))
    primersR = unic_sites[n] + unic_sites[n+1] + primersRb #к обратному праймеру добавляем первый + второй сайты
    primers.append(primersR)
    return primers

ER_d = {'GACGTC': 'ZraI', 'GGTACC': 'KpnI-HFВ®', 'CCGC': 'AciI', 'AACGTT': 'AclI', 'CTGAAG': 'AcuI', 'AGCGCT': 'AfeI', 'CTTAAG': 'AflII', 'ACCGGT': 'AgeI-HFВ®', 'AGCT': 'AluI', 'GGATC': 'Nt.AlwI', 'GGGCCC': 'PspOMI', 'GTGCAC': 'ApaLI', 'GGCGCGCC': 'AscI', 'ATTAAT': 'AseI', 'GCGATCGC': 'AsiSI', 'CCTAGG': 'AvrII', 'GGATCC': 'BamHI ', 'GAAGAC': 'BbsI ', 'CCTCAGC': 'Nt.BbvCI', 'GCAGC': 'BbvI', 'CCATC': 'BccI', 'ACGGC': 'BceAI', 'GTATCC': 'BciVI', 'TGATCA': 'BclI ', 'GTCTC': 'Nt.BsmAI', 'CTAG': 'BfaI', 'ACCTGC': 'BspMI', 'AGATCT': 'BglII', 'CACGTC': 'BmgBI', 'ACTGGG': 'BmrI', 'GCTAGC': 'NheI-HFВ®', 'CTGGAG': 'BpmI', 'CTTGAG': 'BpuEI', 'GGTCTC': 'BsaI-HFВ®v2', 'GAGGAG': 'BseRI', 'CCCAGC': 'BseYI', 'GTGCAG': 'BsgI', 'CGTACG': 'BsiWI-HFВ®', 'CGTCTC': 'Esp3I', 'GGGAC': 'BsmFI', 'GAATGC': 'Nb.BsmI', 'CTCAG': 'BspCNI', 'ATCGAT': 'ClaI', 'TCCGGA': 'BspEI', 'TCATGA': 'BspHI', 'GCTCTTC': 'SapI', 'CCGCTC': 'BsrBI', 'GCAATG': 'Nb.BsrDI', 'TGTACA': 'BsrGI-HFВ®', 'ACTGG': 'BsrI', 'GCGCGC': 'BssHII', 'CACGAG': 'Nb.BssSI', 'TTCGAA': 'BstBI', 'CGCG': 'BstUI', 'GTATAC': 'BstZ17I-HFВ®', 'GCGATG': 'BtgZI', 'GGATG': 'FokI', 'CAGTG': 'BtsIMutI', 'GCAGTG': 'Nb.BtsI', 'CATG': 'NlaIII', 'GTAC': 'RsaI', 'GATC': 'Sau3AI', 'TTTAAA': 'DraI', 'CGGCCG': 'EagI-HFВ®', 'CTCTTC': 'EarI', 'GGCGGA': 'EciI', 'GAGCTC': 'SacI-HFВ®', 'CAGCAG': 'EcoP15I', 'GAATTC': 'EcoRI ', 'GATATC': 'EcoRV-HFВ®', 'CCCGC': 'FauI', 'GGCCGGCC': 'FseI', 'TGCGCA': 'FspI', 'GGCC': 'HaeIII', 'GACGC': 'HgaI', 'GCGC': 'HinP1I', 'AAGCTT': 'HindIII ', 'GTTAAC': 'HpaI', 'CCGG': 'MspI', 'GGTGA': 'HphI', 'CCTTC': 'HpyAV', 'ACGT': 'HpyCH4IV', 'TGCA': 'HpyCH4V', 'GGCGCC': 'SfoI', 'GAAGA': 'MboII', 'CAATTG': 'MfeI-HFВ®', 'AATT': 'MluCI', 'ACGCGT': 'MluI-HFВ®', 'GAGTC': 'PleI', 'CCTC': 'MnlI', 'TGGCCA': 'MscI', 'TTAA': 'MseI', 'GCCGGC': 'NgoMIV', 'CCATGG': 'NcoI-HFВ®', 'CATATG': 'NdeI', 'GCCGAG': 'NmeAIII', 'GCGGCCGC': 'NotI-HFВ®', 'TCGCGA': 'NruI-HFВ®', 'ATGCAT': 'NsiI-HFВ®', 'TTAATTAA': 'PacI', 'CTCGAG': 'XhoI', 'ACATGT': 'PciI', 'GTTTAAAC': 'PmeI', 'CACGTG': 'PmlI', 'TTATAA': 'PsiI-v2', 'CTGCAG': 'PstI-HFВ®', 'CGATCG': 'PvuI-HFВ®', 'CAGCTG': 'PvuII-HFВ®', 'CCGCGG': 'SacII', 'GTCGAC': 'SalI-HFВ®', 'CCTGCAGG': 'SbfI-HFВ®', 'AGTACT': 'ScaI-HFВ®', 'GCATC': 'SfaNI', 'CCCGGG': 'XmaI', 'TACGTA': 'SnaBI', 'ACTAGT': 'SpeI-HFВ®', 'GCATGC': 'SphI-HFВ®', 'GCCCGGGC': 'SrfI', 'AATATT': 'SspI-HFВ®', 'AGGCCT': 'StuI', 'ATTTAAAT': 'SwaI', 'TCGA': 'TaqI-v2', 'TCTAGA': 'XbaI'}

vector = open(input("Задайте адрес к файлу с векторной последовательностью: "),'r') #последовательность вектора
records = parse(vector, "fasta")
for record in records:
    vector_sequence = record.seq
vector_sequence=str(vector_sequence)
print(vector_sequence)

vst_format = input("Укажите формат документа со вставками (fasta/txt): ")
vst_numb = input("Укажите количество вставок для интеграции в вектор: ")
order = list(map(int, input('Введите порядок организации вставок в векторе: ').split()))

if vst_format == 'fasta':
    vstavki = []
    for i in range(3):
        vst = open(input("Задайте адрес к файлу со вставкой: "), 'r') #открываем файл со вставками в формате fasta
        vst_seq = parse(vst, 'fasta')
        for j in vst_seq:
            vst1 = j.seq
            v = str(vst1)
        vstavki.append(v)
        vst.close()
    vstavki_sort = []
    count_order = 1
    numb_order = len(order)
    while count_order != len(order) + 1:
        ind_order = order.index(count_order)
        vstavki_sort.append(vstavki[ind_order])
        count_order += 1

elif vst_format == 'txt':
    vstavki = []
    vst = open(input("Задайте адрес к файлу с вставками: "), 'r') #открываем файл со вставками в формате txt
    vstavki = [i for i in vst.read().splitlines() if i]
    count_order=1
    numb_order=len(order)
    vstavki_sort=[]
    while count_order!=len(order)+1:
        ind_order=order.index(count_order)
        vstavki_sort.append(vstavki[ind_order])
        count_order+=1


#открываем файл с сайтами рестрикции
sites1 = open(input("Задайте адрес к файлу с сайтами рестрикции: "), 'r')
sites = [i for i in sites1.read().splitlines() if i]

# Подбираем сайты рестрикции и сортируем в порядке включения в последовательность для организации вставок в необходимом порядке
for i in sites:
    count = 0
    if i in vstavki:
            sites.remove(i)  # удаляем из списка сайты, которые есть в вставках
good_sites= {}
for i in sites:
    if i in vector_sequence:
        if vector_sequence.count(i) == 1:
            good_sites[i] = vector_sequence.find(i)  #ищем все сайты с единичным вхождением в вектор

good_sitesL = sorted(good_sites,reverse=True)

#проверяем наличие участка множественного клонирования MCS
sites_distance = []
for i in good_sitesL:
    sites_distance.append(vector_sequence.index(i)) #находим расстояния между возможными сайтами растрикции

MCS = True
for i in sorted(sites_distance):
    col = len(vstavki_sort)
    c = 0
    if abs(i - (i+1)) < 100:  #считаем кол-во сайтов, расстояние между которыми не превышает 100 нуклеотидов
        c +=1
if c < col: #если расположенных рядом сайтов меньше, чем число вставок, считаем что MCS нет/он не подходит
    MCS = False

if MCS: #если сайты расположены близко
    numb_restr = len(vstavki_sort)
    i=0
    result=vector_sequence
    while i!=numb_restr: #вставляем все вставки
        site_restr=good_sitesL[i]
        a, b = result.split(site_restr,1) #"разрезаем вектор по сайту рестрикции #C
        result = a+site_restr+vstavki_sort[i]+site_restr + b #теперь берем сайт рестриции и добавляем вставку #C
        i+=1
    #подбираем праймеры:
    primers_res = []
    for i in vstavki_sort:
        primers_res.append(primer_1(vstavki_sort.index(i))) #используем функцию подбора праймеров для варианта 1


#второй вариант (нет MCS)
else:
    ###### первая вставка = сайт рестрикции 1 + сама вставка + уникальный сайт рестрикции 2 + сайт рестрикции1
    unic_sites = []
    for i in sites:
        if i not in vector_sequence:
            unic_sites.append(i)  #список сайтов, не встречающихся в векторе, но доступных пользователю для использования
        if i in vstavki:
            unic_sites.remove(i)

    numb_restr = len(vstavki_sort) #число сайтов
    a, b = vector_sequence.split(good_sitesL[0], 1) #"разрезаем вектор по сайту рестрикции #C
    result = a + good_sitesL[0] + vstavki_sort[0] + unic_sites[0] + good_sitesL[0] + b #вставили первую вставку, добавив за ней уникальный сайт #C

    i=0
    while i!=numb_restr-1: #вставляем все вставки, кроме первой, поскольку у нее одной есть сайт, находящийся в векторе
        a, b = result.split(unic_sites[i],1) #C
        result = a+unic_sites[i]+vstavki_sort[i+1]+ unic_sites[i+1] + unic_sites[i] + b #теперь берем сайт рестриции и добавляем вставку с сайтами #C
        i+=1

    primers_res = []
    for i in vstavki_sort:
        primers_res.append(primer_2(vstavki_sort.index(i))) # списки праймеров для варианта 2 для каждой вставки

    unic_sites.insert(0, good_sitesL[0])
    good_sitesL = unic_sites #переименовали для однотипного названия переменной с сайтами в случае 1го и 2го варианта

#выходные данные:
new_file = input('Введите название нового файла: ')         #C
my_file = open(new_file, "w") #C
print("Инструкция с последовательностью действий находится в указанном вами файле.")
my_file.write("Шаг 1. Заказ праймеров. \n") #C
for i in range(len(primers_res)):
    my_file.write(f"Для вставки {i+1} закажите следующие праймеры: \nпрямой: {primers_res[i][0]}\nобратный: {primers_res[i][1]}") #C
    my_file.write('\n')
my_file.write(f"\nПоставьте ПЦР реакции вставок с соответствующими праймерами. Очистите продукты ПЦР.\n") #C


for i in range(len(vstavki_sort)):
    my_file.write(f"Шаг 2.{i+1} Порежьте вектор рестриктазой {ER_d[good_sitesL[i]]}.\n") #C
    my_file.write(f"Порежьте вставку рестриктазой {ER_d[good_sitesL[i]]}.\n") #C
    my_file.write(f"Очистите продукты рестрикции.\n") #C
    my_file.write(f"Проведите реакцию лигирования вектора и вставки.\n") #C
    my_file.write(f"Проверьте корректность встраивания вставки с помощью рестрикционного анализа.\n") #C
    my_file.write('\n')


my_file.close()
vector.close()
vst.close()
sites1.close()