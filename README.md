# environment
python 2.7.12
django 1.11.5

# commands
## 翻译成sql语言
```shell
python manage.py sqlmigrate restaurants 0001
```

## 为所有app建立migration目录
```shell
python manage.py makemigration
```

## makemigration 之后，将改动应用到数据库文件
```shell
python manage.py migrate
```

## 查看model是否正确
```shell
python manage.py check
```




