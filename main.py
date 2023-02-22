from flask import Flask, render_template
from flask.globals import request
import undetected_chromedriver as uc
from time import sleep
from json import loads
import pandas as pd
from bs4 import BeautifulSoup as bs
from recaptcha_solver import recaptcha_solver

# Início
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

def result():
    def pesquisar():
        opt = uc.ChromeOptions()
        opt.add_argument('--headless')
        driver = uc.Chrome(executable_path='/Busca_Produtor (Python)/chromedriver.exe', options=opt)
        driver.get('https://www.registrorural.com.br/accounts/login/?next=/')
        sleep(1)
        email = 'everton.tec@manejebem.com'
        senha = 'RREve@123'

        # Login
        sleep(1)
        campo_email = driver.find_element("css selector", "#id_login")
        sleep(1)
        campo_email.send_keys(email)

        campo_senha = driver.find_element("css selector", "#id_password")
        sleep(1)
        campo_senha.send_keys(senha)

        btn_entrar = driver.find_element("css selector", ".btn.btn-primary.w-100.mt-2.primaryAction")
        btn_entrar.click()

        # Pesquisa

        pesquisa = request.form["pesquisa"]

        campo_pesquisa = driver.find_element("css selector", "#searchInput")
        sleep(1)
        campo_pesquisa.send_keys(pesquisa)

        btn_pesquisar = driver.find_element("css selector", "#searchButton")
        btn_pesquisar.click()

        # Captura do JSON

        txt = driver.find_element("css selector", "#geoData")
        text = txt.get_attribute('value')
        resultado = loads(text)

        # Aplicando o Padrão

        i_zero = resultado[0]
        res = []

        def indice_zero():
            try:
                res.append({
                    "indice": '0',
                    "Cod_Parcela": i_zero['cod_parcela'],
                    "Cod_Imovel": i_zero['area']['cod_imovel'],
                    "Nome_Imovel": i_zero['area']['denominacao'],
                    "Nome_Proprietario": i_zero['titular']['nome'],
                    "CPF_Proprietario": i_zero['titular']['cpfcnpj_part'],
                    "Responsavel_Tecnico": i_zero['responsavel_tecnico']['nome'],
                    "Municipio": i_zero['registro']['municipio'],
                    "Situacao": i_zero['area']['situacao'],
                    "Natureza": i_zero['area']['natureza'],
                    "Coordenadas": i_zero['geometry']['coordinates'][0][0]
                })
                df = pd.DataFrame(res)
                return df
            except:
                res.append({
                    "indice": '0',
                    "Nome_Proprietario": i_zero['proprietariosPosseirosConcessionarios'][0]['nome'],
                    "CPF": i_zero['proprietariosPosseirosConcessionarios'][0]['cpfCnpj'],
                    "Nascimento": i_zero['proprietariosPosseirosConcessionarios'][0]['dataNascimento'],
                    "CAR": i_zero['car'],
                    "Area_Total (ha)": i_zero['area'],
                    "Municipio": i_zero['mun'],
                    "Estado": i_zero['uf'],
                    "Coordenadas": i_zero['geometry']['coordinates'][0][0]
                })
                df = pd.DataFrame(res)
                return df

        try:
            i_um = resultado[1]
        except:
            i_um = None
        res_um = []

        def indice_um():
            try:
                res_um.append({
                    "indice": '1',
                    "Cod_Parcela": i_um['cod_parcela'],
                    "Cod_Imovel": i_um['area']['cod_imovel'],
                    "Nome_Imovel": i_um['area']['denominacao'],
                    "Nome_Proprietario": i_um['titular']['nome'],
                    "CPF_Proprietario": i_um['titular']['cpfcnpj_part'],
                    "Responsavel_Tecnico": i_um['responsavel_tecnico']['nome'],
                    "Municipio": i_um['registro']['municipio'],
                    "Situacao": i_um['area']['situacao'],
                    "Natureza": i_um['area']['natureza'],
                    "Coordenadas": i_um['geometry']['coordinates'][0][0]
                })
                df_um = pd.DataFrame(res_um)
                return df_um
            except:
                res_um.append({
                    "indice": '1',
                    "Nome_Proprietario": i_um['proprietariosPosseirosConcessionarios'][0]['nome'],
                    "CPF": i_um['proprietariosPosseirosConcessionarios'][0]['cpfCnpj'],
                    "Nascimento": i_um['proprietariosPosseirosConcessionarios'][0]['dataNascimento'],
                    "CAR": i_um['car'],
                    "Area_Total (ha)": i_um['area'],
                    "Municipio": i_um['mun'],
                    "Estado": i_um['uf'],
                    "Coordenadas": i_um['geometry']['coordinates'][0][0]
                })
                df_um = pd.DataFrame(res_um)
                return df_um

        try:
            i_dois = resultado[2]
        except:
            i_dois = None
        res_dois = []

        def indice_dois():
            try:
                res_dois.append({
                    "indice": '2',
                    "Cod_Parcela": i_dois['cod_parcela'],
                    "Cod_Imovel": i_dois['area']['cod_imovel'],
                    "Nome_Imovel": i_dois['area']['denominacao'],
                    "Nome_Proprietario": i_dois['titular']['nome'],
                    "CPF_Proprietario": i_dois['titular']['cpfcnpj_part'],
                    "Responsavel_Tecnico": i_dois['responsavel_tecnico']['nome'],
                    "Municipio": i_dois['registro']['municipio'],
                    "Situacao": i_dois['area']['situacao'],
                    "Natureza": i_dois['area']['natureza'],
                    "Coordenadas": i_dois['geometry']['coordinates'][0][0]
                })
                df_dois = pd.DataFrame(res_dois)
                return df_dois
            except:
                res_dois.append({
                    "indice": '2',
                    "Nome_Proprietario": i_dois['proprietariosPosseirosConcessionarios'][0]['nome'],
                    "CPF": i_dois['proprietariosPosseirosConcessionarios'][0]['cpfCnpj'],
                    "Nascimento": i_dois['proprietariosPosseirosConcessionarios'][0]['dataNascimento'],
                    "CAR": i_dois['car'],
                    "Area_Total (ha)": i_dois['area'],
                    "Municipio": i_dois['mun'],
                    "Estado": i_dois['uf'],
                    "Coordenadas": i_dois['geometry']['coordinates'][0][0]
                })
                df_dois = pd.DataFrame(res_dois)
                return df_dois

        def append():
            if i_um == None:
                df = indice_zero()
                df_html = df.to_html()
                return df_html
            elif i_dois == None:
                df = indice_zero()
                df_um = indice_um()
                index_zero = []
                index_um = []
                for a in df:
                    index_zero.append(a)
                for b in df_um:
                    index_um.append(b)
                if index_zero == index_um:
                    df_2 = pd.concat([df, df_um])
                    df2_html = df_2.to_html()
                    return df2_html
                else:
                    df_html = df.to_html()
                    dfum_html = df_um.to_html()
                    return df_html + dfum_html
            else:
                df = indice_zero()
                df_um = indice_um()
                df_dois = indice_dois()

                index_zero = []
                index_um = []
                index_dois = []

                for a in df:
                    index_zero.append(a)

                for b in df_um:
                    index_um.append(b)

                for c in df_dois:
                    index_dois.append(c)

                if index_zero == index_um:
                    df_r1 = pd.concat([df, df_um])
                    dfr1_html = df_r1.to_html()
                    dfdois_html = df_dois.to_html()
                    return dfr1_html + dfdois_html
                elif index_zero == index_dois:
                    df_r1 = pd.concat([df, df_dois])
                    dfr1_html = df_r1.to_html()
                    dfum_html = df_um.to_html()
                    return dfr1_html + dfum_html
                else:
                    df_r1 = pd.concat([df_um, df_dois])
                    dfr1_html = df_r1.to_html()
                    df_html = df.to_html()
                    return dfr1_html + df_html
        return append()

    # Renderizando DataFrame no html
    soup1 = bs(pesquisar(), "html.parser")
    html = open("/Busca_Produtor/templates/pesquisa.html", 'r', encoding='UTF-8')
    soup = bs(html, "html.parser")
    body = soup.body
    body.append(soup1)
    resultado_html = open("/Busca_Produtor/templates/resultado.html", "w",  encoding='UTF-8')
    resultado_html.write(str(soup.prettify()))
    return 'OK'

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    result()
    return render_template("resultado.html")



# Fim
if __name__ == "__main__":
    app.run(debug=True)