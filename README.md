# eth_scrapper

## Un script para guardar transacciones recurrentes internas de una wallet ethereum a GoogleSheet

Sigue estas instrucciones para conseguir tu creds.json (Google Sheet), ponlo por fuera de la carpeta src/
>  Inside console.cloud.google.com
>
>  New project -> name and No organization
>
>  Go to APIs overview -> Library -> Google Drive -> enable
>>     Create credentials -> Google Drive API, Web server, Application data, "No, I'm not using them"
>>     name, Role=Editor, json
> Go to APIs overview -> Library -> Google Sheets -> enable
>
> Inside the json file, copy the email and share the spreadsheet with that email


## Para ejecutar sin docker necesitas tener estos envs (cambialos):
  * ETH_WALLET=0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45
  * SHEET_NAME=NombreDelDocumento
  * WORKSHEET_NAME=NombreDeLaHoja

```
$(which pipenv) run python main.py
```

## En docker:
```
docker run --rm \
  -e ETH_WALLET=0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45 \
  -e SHEET_NAME=NombreDelDocumento \
  -e WORKSHEET_NAME=NombreDeLaHoja \
  -v $PWD/creds.json:/app/creds.json \
  eth_scrapper:latest
'''

## En docker-compose tienes el ejemplo.