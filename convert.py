from os import listdir
path = "C:\\Users\\pmhra\\Pictures\\Bohemia\\"

fnames = listdir(path)
for fname in fnames:
    if fname[-4:] == ".htm":
        print('*********')
        print(fname)
        print('*********')
        fhtm = open(path+fname,'r',encoding='utf-8')
        lines = fhtm.readlines()
        fhtm.close()
        content = False
        tag = False
        tag_name = False
        tags = []
        text = ''
        for line in lines:
            if '<div class="entry-content entry--item">' in line:
                content = True
            if content:
                for c in line:
                    if c == '<':
                        tag = True
                        tag_name = True
                        tags.append('')
                    elif tag:
                        if c == '>':
                            tag = False
                            tag_name = False
                        elif tag_name:
                            if c == ' ':
                                tag_name = False
                            else:
                                tags[-1] += c
                    else:
                        text += c
        text = '\n'.join([t.replace('\n','') for t in text.split('\n\n\n\n')]).split('FacebookTweetPrint')[0]
        if len('Bohemia '.join(text.split('Bohemia ')[1:]).split(' ')[0].split('\n')[0].split('/')) == 2:
            text = 'Bohemia '.join(text.split('Bohemia ')[1:])
            issue = text.split(' ')[0].split('\n')[0].split('/')[0]
            volume = text.split(' ')[0].split('\n')[0].split('/')[1]
            text = ' '.join(text.split(' ')[1:])
        else:
            issue = '0'
            volume = '1990'
        title = fname.split(' – ')[0]
        print(issue)
        print(volume)
        print(title)
        
        fmdname = fname.split(' – ')[0].lower().replace(' ','_').replace('”','').replace('!','').replace('?','').replace('.','')
        fmdname = fmdname.replace('ě','e').replace('š','s').replace('č','c').replace('ř','r').replace('ž','z').replace('ý','y').replace('á','a').replace('í','i').replace('é','e')
        fmdname = fmdname.replace('ů','u').replace('ú','u').replace('ó','o').replace('ä','a').replace('ö','o').replace('å','a')
        fmdname = f'{volume}-{issue}-01-{fmdname}'
        fmd = open("_posts/"+fmdname[:-4]+'.md','w',encoding='utf-8')
        fmd.write('---\n')
        fmd.write(f'title: {title}\n')
        fmd.write('layout: clanek\n')
        fmd.write(f'date: {volume}-{issue}-01 00:00:00 +0200\n')
        fmd.write('category: bohemia\n')
        fmd.write('tags: [fi]\n')
        fmd.write(f'volume: {volume}\n')
        fmd.write(f'issue: {issue}\n')
        fmd.write('---\n')
        fmd.write(text)
        fmd.close()