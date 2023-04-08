import requests
import pandas as pd

##FUNÇÃO PARA COLETA DOS GENEROS CADASTRADOS NO TMDB UTILIZANDO API DISPONIBILIZADO PELA PLATAFORMA
def get_genres_tmdb():

    print("Iniciando coleta dos generos de filmes...")

    ##Realiza a execução do método GET utilizando API disponibilizado pela plataforma. O atributo API_Key é fornecida pelo TMDB;
    res = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=f05ac50c99ed339e1a5a2e33c7c19d51&language=en-US')

    dicRequest = res.json()
    print(dicRequest)
    list =[]

    ##Percorre o resultado da requisição e inclui o resultado em uma lista
    for oGeneros in dicRequest["genres"]:

        data = {"id": oGeneros['id'],
                "name": oGeneros['name'],                        
            }
        
        list.append(data)

    ##Atribui a lista a um dataframe pandas.    
    df = pd.DataFrame(list)

    ##Salva em CSV para futura re-utilização.
    df.to_csv('C:\\Erenilson\\Data Science\\Imdb_Recommendation\data\\raw\\generos.csv',index=False)

    print("Coleta dos generos de filmes concluida.")

#def insert_postgres(df, cTabela):

    

get_genres_tmdb()
