import pytube

link=input('Enter the link of video:')

#
yt=pytube.YouTube(link)
#
allstreams=yt.fmt_streams

val=input('1.Audio\n2.Video\n')
if(val=='1' or val=='2'):
        downindex=0
        for s in allstreams:
                if val=='2':
                        if s.type=='video':
                                #
                                print(s.resolution+" "+s.subtype)
                elif val=='1':
                        if s.type=='audio':
                                print(s.subtype)
                        else:
                                downindex+=1
                                
                
        choice=0
        if val=='2':
                choice=input('Enter the appropriate resolution and type:')
                choice=int(choice)
        else:
                choice=input('Enter the appropriate type:')
                choice=int(choice)+downindex
        
        choice-=1
        outputpath=input('Enter the output location:')
        #
        allstreams[choice].download(outputpath)
