'''
Created on 10/04/2012

@author: lucask
'''
import urllib2
import cookielib,urllib
from bs4 import BeautifulSoup
import sys
import re


if __name__ == '__main__':
    base_url = 'http://legendas.tv'
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    username = raw_input('Login: ')
    password = raw_input('Senha:')
    login_data = urllib.urlencode({'txtLogin':username,'txtSenha':password})
    request = urllib2.Request(base_url+'/login_verificar.php',login_data)
    response = urllib2.urlopen(request).read()
    
    if response.__contains__('Dados incorretos'):
        print 'Ooops dados incorretos...'
        raw_input('Pressione uma tecla para sair...')
        sys.exit()
    else:
        print 'Logado com sucesso!'
    print 'Fazendo busca:'
    print '--------------'
    
    busca = raw_input('Buscar por: ')
    tipo = raw_input('Tipo:(1 - Release, 2- Filme, 3 - Usuario):')
    idioma = raw_input('Idioma: (1 - Portugues,2 - Ingles,99 - Todos)')
    
    search_dict = {'txtLegenda':busca,'selTipo':tipo,'int_idioma':idioma}
    search_data = urllib.urlencode(search_dict)
    request = urllib2.Request(base_url+'/index.php?opcao=buscarlegenda',search_data)
    response = urllib2.urlopen(request)
    page = response.read()
    
    soup = BeautifulSoup(page)
    
    span_results = soup.find('td',{'id':'conteudodest'}).findAll('span')
    
    i = 0
    list_download_ids = []
    for span in span_results:
    
        # ha dois tipos de span na busca. 
        #Este nao contem o que nos gente queremos
        if span.attrs == [('class', 'brls')]:
            continue
    
        td = span.find('td',{'class':'mais'})
    
        #parent encontra o elemento pai. 
        #ex: td.parent aponta para tr e tr.parent aponta para table
        release = td.parent.parent.find('span',{'class':'brls'}).contents[0]
    
        sub_name = td.contents[0].contents[0]
        downloads = td.contents[5]
        comentarios = td.contents[7]
        avaliacao = td.contents[10]
        data = span.findAll('td')[2].contents[0]
    
        #recupera o ID do download que ta no codigo javascript
        download_id_js = td.parent.parent.attrs[1][1]
        download_id = re.search('[a-z0-9]{32}',download_id_js).group(0)
        list_download_ids.append(download_id)
        i+=1
        print 'Opcao: '+str(i)
        print 'Serie: '+sub_name
        print 'Release: '+release
        print 'Downloads: '+downloads
        print 'Comentarios: '+comentarios
        print 'Avaliacao: '+avaliacao
        print 'Data: '+data
        print '-------------------------------------'
    
    download_op =  int(raw_input('Qual opcao deseja baixar? '))
    url_request = base_url+'/info.php?d='+list_download_ids[download_op-1]+'&c=1'
    request =  urllib2.Request(url_request)
    response = urllib2.urlopen(request)
    legenda = response.read()
    
    #eu acho que todas as legendas estao em formato rar
    #mas so pro caso de eu estar errado.
    fname = str(download_op)
    if response.info().get('Content-Type').__contains__('rar'):
        fname += '.rar'
    else:
        fname += '.zip'
    f = open(fname,'w')
    f.write(legenda)
    f.close()
    print 'Legenda '+fname+' salva com sucesso!'