import pytube

def Download(url,destination):
        yt=pytube.YouTube(url)
        allstreams=yt.fmt_streams

        val=input('1.Audio\n2.Video\n')
        index=1
        if(val=='1' or val=='2'):
                downindex=0
                for s in allstreams:
                        if val=='2':
                                if s.type=='video':
                                        #
                                        print(str(index)+" "+s.resolution+" "+s.subtype)
                        elif val=='1':
                                if s.type=='audio':
                                        print(str(downindex+1)+" "+s.subtype)
                                else:
                                        downindex+=1
                        index+=1
                                        
                        
                choice=0
                if val=='2':
                        choice=input('Enter the appropriate resolution and type:')
                        choice=int(choice)
                else:
                        choice=input('Enter the appropriate type:')
                        choice=int(choice)+downindex
                
                choice-=1
                #
                allstreams[choice].download(destination)

