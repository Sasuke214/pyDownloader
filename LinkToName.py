import pytube

def linkToName(links,q):
        names=[]
        for l in links:
                try:
                        m=pytube.YouTube(l)
                        tempdict={m.title:l}
                        q.put(tempdict)
                except:
                        hoo=1
