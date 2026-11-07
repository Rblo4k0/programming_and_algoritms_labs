# Лаба №6  

## Команды запуска сценариев

```bash
# Установка зависимости
pip install -r requirements.txt
```
  
  
### cli_text.py  

```bash
# запуск
python -m src.lab06.cli_text cat --input data/samples/people.csv -n
```  
![Downloading failed](/img/lab06/cat_demo.png 'cat_demo')  

```bash
# запуск
python -m src.lab06.cli_text stats --input data/samples/people.txt --top 5
```  
![Downloading failed](/img/lab06/stats_demo.png 'stats_demo')  

```bash
# запуск
python -m src.lab06.cli_text --help
```  
![Downloading failed](/img/lab06/help_demo.png 'help_demo')  

```bash
# запуск
python -m src.lab06.cli_text stats --input data/samples/people.txt --top -11
```  
![Downloading failed](/img/lab06/error_demo.png 'error_demo')  


### cli_convert.py  

```bash
# JSON -> CSV
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_cli.csv
```  
![Downloading failed](/img/lab06/json2csv.png 'json2csv')  

```bash
# CSV -> JSON
python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_cli.json
```  
![Downloading failed](/img/lab06/csv2json.png 'csv2json')  

```bash
# CSV -> XLSX
python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people_cli.xlsx
```  
![Downloading failed](/img/lab06/csv2xlsx.png 'csv2xlsx')  

```bash
# Вызов справки
python -m src.lab06.cli_convert --help
```  
![Downloading failed](/img/lab06/help.png 'help')  
