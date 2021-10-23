Results will be printed on the console

Dependency installation
```
Python>=3.5
install/upgrade pip (python package installer)
$ python3 -m pip install --upgrade pip


Create virtual environment and install dependencies in that:
$ pip3 install virtualenv
$ virtualenv -p python3 myenv
$ source myenv/bin/activate


$ cd <path_to_repository_root>/
$ pip install -r requirements.txt
```

### Unit testing:
```
$ python -m unittest
```

### Main Function:
```
$ python main.py
```

### Folder Structure
```
├── README.md
├── __init__.py
├── main.py
├── requirements.txt
├── resources
│   └── input.txt
├── src
│   ├── __init__.py
│   ├── controller
│   │   ├── balancecontroller.py
│   │   ├── controller.py
│   │   ├── loancontroller.py
│   │   └── paymentcontroller.py
│   ├── dto
│   │   ├── entities
│   │   │   ├── bank.py
│   │   │   ├── loan.py
│   │   │   ├── payment.py
│   │   │   ├── transaction.py
│   │   │   └── user.py
│   │   ├── enums
│   │   │   └── commandType.py
│   │   └── payload
│   │       └── payload.py
│   ├── impl
│   │   └── inMemStorage.py
│   └── util
│       ├── constants.py
│       └── queryparser.py
└── test
    ├── __init__.py
    └── test_main.py
```
