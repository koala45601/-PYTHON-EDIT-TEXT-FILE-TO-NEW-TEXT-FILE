import datetime


#date time down load file // Daily file SG@Cyymmdd
date_1=datetime.datetime.now()
date_download="SG@C"+date_1.strftime("%y%m%d")
#print(date_download)


try:
    RT1=open(f'D:/SVS_WEB/Back_up/{date_download}.txt','r')
    RT2=open(f'D:/SVS_WEB/Back_up/{date_download}.txt','r')
    RT3=open(f'D:/SVS_WEB/Back_up/{date_download}.txt','r')
    RT_read=open(f'D:/SVS_WEB/Back_up/{date_download}.txt','r')
    count=0
    select_line1=RT1.readlines()
    select_line2=RT2.readlines()
    select_line3=RT3.readlines()
    select_line_read=RT_read.readlines()
    #ltr=[266,267]
    #line 267
    Temp_line1=select_line1[266]
    Temp_text1=(Temp_line1[0:50])
    #create line len = 122
    #print(Temp_text1)
    #print('{:<122}'.format(Temp_text1))

    #line 268
    Temp_line2=select_line2[267]
    Temp_text2=(Temp_line2[62:72])
    #line_cre=f'{Temp_text1:<112}{Temp_text2}'
    T1=Temp_line1
    T2=Temp_text2

    #UPDATE LINE 268
    select_line3[266]=f'{Temp_text1:<112}{Temp_text2}'
    #print(select_line3[266])
    #print(len(select_line3[266]))

    RT4=open(f'D:/SVS_WEB/Back_up/{date_download}.txt','w')
    RT4.writelines(select_line3)


    #delete line 268
    RT5=open(f'D:/SVS_WEB/download/{date_download}.txt','w')
    print(select_line3[267])
    for line in select_line3:
        if line != select_line3[267]:
            RT5.writelines(line)
        count+=1
        print("Line: "+str(count)+': '+line)

    #close function read/write text file
    RT1.close()
    RT2.close()
    RT3.close()
    RT4.close()
    RT5.close()

    #for p, line in enumerate(RT):
    #    if p in ltr:
    #        print(line)

    #print(RT.readline())
    #print(len(RT.readline()))'''
except:
    print('No Working is file not found!! or file is not match. Please check file in path and try again.')