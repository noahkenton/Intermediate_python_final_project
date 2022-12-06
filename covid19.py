import pymysql
from flask import Flask
import json



class Config:
    # Configuration file handler
    def __init__(self):
        con_params = self.__read_config()
        self.db_conn = pymysql.connect(host=con_params["host"],
                             user=con_params["user"],
                             password=con_params["password"],
                             db=con_params["db"],
                             charset=con_params["charset"],
                             cursorclass=pymysql.cursors.DictCursor)

    def __read_config(self):
        # Read config file for accessing sql database

        try:
            with open("config.txt", "r") as file_name:
                data = file_name.read()
                return dict(json.loads(data))
        finally:
            file_name.close()


class Country:
    def __init__(self, country_id='', country_name=''):

        self.__country_name = country_name

        if country_id == "":
            # self.__doctor_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO country (country_id, country_name)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__country_id, self.__country_name))
                    con.commit()
            finally:
                con.close()
        else:
            # Get
            self.__country_id = country_id

            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM country WHERE country_id = '" + country_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__doctor_id = row["country_id"]
                        self.__fist_name = row["country_name"]

            finally:
                con.close()

    def get_country_name(self):
        return self.__country_name

    def set_country_name(self, country_name):
        self.__country_name = country_name

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE country SET country_name = %s WHERE country_id = %s;'
                print(qry)
                cur.execute(qry, (self.__country_name, self.__country_id))
                con.commit()
        finally:
            pass


class Locationz:
    def __init__(self, location_id='', location_name='', location_state='', fk_country_id=''):
        self.__location_name = location_name
        self.__location_state = location_state
        self.__fk_country_id = fk_country_id
        if location_id == "":
           # self.__doctor_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO LOCATIONZ (location_id, location_name, location_state, fk_country_ide)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__location_id, self.__location_name,
                                      self.__location_state, self.__fk_country_id))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__location_id = location_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM LOCATIONZ WHERE location_id = '" + location_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__location_id = row["location_id"]
                        self.__location_name = row["location_name"]
                        self.__location_state = row["location_state"]
                        self.__fk_country_id = row["fk_country_id"]
            finally:
                con.close()

    def get_location_id(self):
        return self.__location_id

    def get_location_name(self):
        return self.__location_name

    def set_location_name(self, location_name):
        self.__location_name = location_name

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE LOCATIONZ SET location_name = %s WHERE location_id = %s;'
                print(qry)
                cur.execute(qry, (self.__location_name, self.__location_id))
                con.commit()
        finally:
            pass

    def get_location_state(self):
        return self.__location_state

    def set_location_state(self, location_state):
        self.__location_state = location_state

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE LOCATIONZ SET location_state = %s WHERE location_id = %s;'
                print(qry)
                cur.execute(qry, (self.__location_state, self.__location_id))
                con.commit()
        finally:
            pass


class Duration:
    def __init__(self, month_affected_id='', Month_affected='', year_affected=''):
        self.__month_affected_id = month_affected_id
        self.__Month_affected = Month_affected
        self.__year_affected = year_affected
        if month_affected_id == "":
           # self.__doctor_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO month_affected (month_affected_id, Month_affected, year_affected)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__month_affected_id, self.__Month_affected,
                                      self.__year_affected))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__month_affected_id = month_affected_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM month_affected WHERE month_affected_id = '" + month_affected_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__month_affected_id = row["month_affected_id"]
                        self.__Month_affected = row["Month_affected"]
                        self.__year_affected = row["year_affected"]
            finally:
                con.close()

    def get_Month_affected(self):
        return self.__Month_affected

    def get_year_affected(self):
        return self.__year_affected

    def set__Month_affected(self, Month_affected):
        self.__Month_affected = Month_affected

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE month_affected SET Month_affected = %s WHERE month_affected_id = %s;'
                print(qry)
                cur.execute(qry, (self.__Month_affected, self.__month_affected_id))
                con.commit()
        finally:
            pass

    def set_year_affected(self,  year_affected):
        self.__year_affected = year_affected

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE month_affected SET year_affected = %s WHERE month_affected_id = %s;'
                print(qry)
                cur.execute(qry, (self.__year_affected, self.__month_affected_id))
                con.commit()
        finally:
            pass

    
class Patient:
    def __init__(self, patient_id='', patient_name='', Age='',
                 fk_month_affected_id='', fk_location_id='', fk_duration_id=''):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__Age = Age
        self.__fk_month_affected_id = fk_month_affected_id
        self.__fk_location_id = fk_location_id
        self.__fk_duration_id = fk_duration_id
        if patient_id == "":
            # self.__patient_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO Patient (patient_id, patient_name, Age, fk_month_affected_id, ' \
                          'fk_location_id, fk_duration_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__patient_name, self.__Age, self.__fk_month_affected_id,
                                      self.__fk_location_id, self.__fk_duration_id))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__patient_id = patient_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM Patient WHERE patient_id = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["patient_id"]
                        self.__patient_name = row["patient_name"]
                        self.__Age = row["Age"]
                        self.__fk_month_affected_id = row["fk_month_affected_id"]
                        self.__fk_location_id = row["fk_location_id"]
                        self.__fk_duration_id = row["fk_duration_id"]
            finally:
                con.close()

    def get_patient_name(self):
        return self.__patient_name

    def get_Age(self):
        return self.__Age

    def get_fk_month_affected_id(self):
        return self.__fk_month_affected_id

    def get_fk_location_id(self):
        return self.__fk_location_id

    def get_fk_duration_id(self):
        return self.__fk_duration_id

    def set_patient_name(self, patient_name):
        self.__patient_name = patient_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET patient_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__patient_name, self.__patient_id))
                con.commit()
        finally:
            pass

    def set_Age(self, Age):
        self.__Age = Age
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET Age = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__Age, self.__patient_id))
                con.commit()
        finally:
            pass

    def set_fk_month_affected_id(self, fk_month_affected_id):
        self.__fk_month_affected_id = fk_month_affected_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET fk_month_affected_id = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_month_affected_id, self.__patient_id))
                con.commit()
        finally:
            pass

    def set_fk_location_id(self, fk_location_id):
        self.__fk_location_id = fk_location_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET fk_location_id = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_location_id, self.__patient_id))
                con.commit()
        finally:
            pass

    def set_fk_duration_id(self, fk_duration_id):
        self.__fk_duration_id = fk_duration_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET fk_duration_id = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_duration_id, self.__patient_id))
                con.commit()
        finally:
            pass


class Symptoms:
    def __init__(self, symptoms_id='', symptom_name=''):
        self.__symptoms_id = symptoms_id
        self.__symptom_name = symptom_name
        if patient_id == "":
            # self.__patient_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO SYMPTOMS (symptoms_id, symptom_name)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__symptoms_id, self.__symptom_name))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__symptoms_id = symptoms_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM SYMPTOMS WHERE symptoms_id = '" + symptoms_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__symptoms_id = row["symptoms_id"]
                        self.__symptom_name = row["symptom_name"]
            finally:
                con.close()

    def get_symptom_name(self):
        return self.__symptom_name

    def set_symptom_name(self, symptom_name):
        self.__symptom_name = symptom_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE SYMPTOMS SET symptom_name = %s WHERE symptoms_id = %s;'
                print(qry)
                cur.execute(qry, (self.__symptom_name, self.__symptoms_id))
                con.commit()
        finally:
            pass


class previous_health_issues:
    def __init__(self):
        pass


class  patient_previous_health_issues:
    def __init__(self):
        pass
class Treatments:
    def __init__(self):
        pass
class Treatments_used_by_patient:
    def __init__(self):
        pass