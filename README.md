# annotation-generation

This application generates an introduction for term papers on a given topic (only Ru)

Example of how the app works:
![photo.png](https://im.wampi.ru/2023/12/03/photo.png)

Steps required to run:
1. create venv:
```sh
python -m venv venv
```
2. activate venv:
```sh
venv/Scripts/activate
```
 or 
 ```sh
source venv/bin/activate 
```
3. install dependencies:
```sh
pip install -r requirements.txt
```
4. apply migrations:
```sh
python annotation-generation/manage.py migrate
```
5. run app:
```
python annotation-generation/manage.py runserver
```
