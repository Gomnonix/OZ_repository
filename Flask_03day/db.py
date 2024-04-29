from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 
#각각의 파일 별로 따로 관리를 해주기 위해서는 SQLAlchemy()를 중앙으로에서 관리하는 방벙으로 관리해야한다.