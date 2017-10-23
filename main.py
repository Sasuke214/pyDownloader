from ManjilSearch import search
from LinkToName import linkToName
from ManjilDownload import Download
import threading
import webbrowser
import queue
import os
from time import sleep


class ManjilTube:
        def __init__(self):
                self.name_list=queue.Queue()
                self.MainProcess()

        def ProcessThreads(self,urls):
                global name_list
                t1=threading.Thread(target=linkToName,args=(urls, self.name_list,))
                t1.start()
                return t1

        def DivideIntoThreads(self,lists_of_urls):
                totallen=len(lists_of_urls)
                totallen=totallen//2
                
                
                n1=lists_of_urls[:totallen]
                n2=lists_of_urls[totallen:totallen*2]
                n3=lists_of_urls[totallen*2:totallen*3]
                n4=lists_of_urls[totallen*3:]


                t1=self.ProcessThreads(n1)
                t2=self.ProcessThreads(n2)
                t3=self.ProcessThreads(n3)
                t4=self.ProcessThreads(n4)
                t1.join()
                t2.join()
                t3.join()
                t4.join()



        def MainProcess(self):
                search_value=input('Enter the name that you want to search: ')
                while len(search_value.strip(' '))==1:
                        search_value=input('Enter the name that you want to search: ')
        
                lists_of_urls=search(search_value)

                count_request=0
                while len(lists_of_urls)<=0:
                        if count_request==20:
                                return
                        count_request+=1
                        sleep(1)
                        lists_of_urls=search(search_value)
                        
                
                self.DivideIntoThreads(lists_of_urls)
                index=0
                for elem in list(self.name_list.queue):
                        index+=1
                        dict_elem=list(elem.keys())[0]
                        print(str(index)+"- "+dict_elem+'\n')

                while True:
                        choice=input('Enter your choice from the list: ')
                        choice=int(choice)-1

                        while choice>=len(list(self.name_list.queue)):
                                choice=input('Enter your choice to download: ')
                                choice=int(choice)-1                        
                        
                        destination=''
                        value=list(self.name_list.queue)[choice]
                        key=list(value.keys())[0]
                        
                        url_to_download=value[key]
                        print('1.View\n2.Download')
                        choiceval=input('What u wanna do:')
                        if choiceval=='1':
                                webbrowser.open(url_to_download)
                        elif choiceval=='2':
                                break
                        else:
                                print('Enter appropriate choice....')


                destination=input('Enter the destination: ')
                state=True
                while state:
                        try:
                                state=os.chdir(destination)
                                state=False
                        except:
                                destination=input('Enter the valid destination: ')
                                state=True
                                
                Download(url_to_download,destination)
  
                

if __name__=='__main__':
        mt=ManjilTube()

