import pymysql
from flask import Flask
import json
import unittest


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
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO country (country_name)'
                    qry = qry + 'VALUES( %s)'
                    print(qry)
                    cur.execute(qry, self.__country_name)
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

    def get_id(self):
        return self.__country_id

    def to_json(self):
        fields_data = {
            "country_id": self.__country_id,
            "country_name": self.__country_name
        }
        return json.dumps(fields_data)


class Locationz:
    def __init__(self, location_id='', location_name='', location_state='', fk_country_id=''):
        self.__location_name = location_name
        self.__location_state = location_state
        self.__fk_country_id = fk_country_id
        if location_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO LOCATIONZ (location_name, location_state, fk_country_id)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__location_name, self.__location_state, self.__fk_country_id))
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

    def get_fk_country_id(self):
        return self.__fk_country_id

    def set_fk_country_id(self, fk_country_id):
        self.__fk_country_id = fk_country_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE LOCATIONZ SET fk_country_id = %s WHERE location_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_country_id, self.__location_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__location_id

    def to_json(self):
        fields_data = {
            "location_id": self.__location_id,
            "location_name": self.__location_name,
            "location_state": self.__location_state,
            "fk_country_id": self.__fk_country_id
        }
        return json.dumps(fields_data)


class Duration:
    def __init__(self, duration_id='', duration_length_in_days=''):
        self.__duration_length_in_days = duration_length_in_days
        if duration_id == "":
            # self.duration_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO duration (duration_length_in_days)'
                    qry = qry + 'VALUES(%s)'
                    print(qry)
                    cur.execute(qry, self.__duration_length_in_days)
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__duration_id = duration_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM duration WHERE duration_id = '" + duration_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__duration_id = row["duration_id"]
                        self.__duration_length_in_days = row["duration_length_in_days"]

            finally:
                con.close()

    def get_duration_length_in_days(self):
        return self.__duration_length_in_days

    def set_duration_length_in_days(self, duration_length_in_days):
        self.__duration_length_in_days = duration_length_in_days
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE duration SET duration_length_in_days = %s WHERE duration_id = %s;'
                print(qry)
                cur.execute(qry, (self.__duration_length_in_days, self.__duration_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__duration_id

    def to_json(self):
        fields_data = {
            "duration_id": self.__duration_id,
            "duration_length_in_days": self.__duration_length_in_days
        }
        return json.dumps(fields_data)


class MonthAffected:
    def __init__(self, month_affected_id='', month_affected='', year_affected=''):
        self.__month_affected_id = month_affected_id
        self.__month_affected = month_affected
        self.__year_affected = year_affected
        if month_affected_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO month_affected (Month_affected, year_affected)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__month_affected, self.__year_affected))
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
                        self.__month_affected = row["Month_affected"]
                        self.__year_affected = row["year_affected"]
            finally:
                con.close()

    def get_month_affected(self):
        return self.__month_affected

    def get_year_affected(self):
        return self.__year_affected

    def set__month_affected(self, month_affected):
        self.__month_affected = month_affected

        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE month_affected SET Month_affected = %s WHERE month_affected_id = %s;'
                print(qry)
                cur.execute(qry, (self.__month_affected, self.__month_affected_id))
                con.commit()
        finally:
            pass

    def set_year_affected(self, year_affected):
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

    def get_id(self):
        return self.__month_affected_id

    def to_json(self):
        fields_data = {
            "month_affected_id": self.__month_affected_id,
            "month_affected": self.__month_affected,
            "year_affected": self.__year_affected
        }
        return json.dumps(fields_data)


class Patient:
    def __init__(self, patient_id='', patient_name='', age='', fk_month_affected_id='',
                 fk_location_id='', fk_duration_id=''):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__age = age
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
                    qry = 'INSERT INTO Patient (patient_name, Age, fk_month_affected_id, ' \
                          'fk_location_id, fk_duration_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_name, self.__age, self.__fk_month_affected_id,
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
                        self.__age = row["Age"]
                        self.__fk_month_affected_id = row["fk_month_affected_id"]
                        self.__fk_location_id = row["fk_location_id"]
                        self.__fk_duration_id = row["fk_duration_id"]
            finally:
                con.close()

    def get_patient_name(self):
        return self.__patient_name

    def get_age(self):
        return self.__age

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

    def set_age(self, age):
        self.__age = age
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET Age = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__age, self.__patient_id))
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

    def get_id(self):
        return self.__patient_id

    def to_json(self):
        fields_data = {
             "patient_id": self.__patient_id,
             "patient_name": self.__patient_name,
             "Age": self.__age,
             "fk_month_affected_id": self.__fk_month_affected_id,
             "fk_location_id": self.__fk_location_id,
             "fk_duration_id": self.__fk_duration_id
        }
        return json.dumps(fields_data)


class Symptoms:
    def __init__(self, symptoms_id='', symptom_name=''):
        self.__symptoms_id = symptoms_id
        self.__symptom_name = symptom_name
        if symptoms_id == "":
            # self.__patient_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO SYMPTOMS (symptom_name)'
                    qry = qry + 'VALUES(%s)'
                    print(qry)
                    cur.execute(qry, self.__symptom_name)
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

    def get_id(self):
        return self.__symptoms_id

    def to_json(self):
        fields_data = {
             "symptoms_id": self.__symptoms_id,
             "symptom_name": self.__symptom_name
        }
        return json.dumps(fields_data)


class PreviousHealthIssues:
    def __init__(self, health_issues_id='', health_issue_name=''):
        self.__health_issues_id = health_issues_id
        self.__health_issue_name = health_issue_name
        if health_issues_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO previous_health_issues (health_issue_name)'
                    qry = qry + 'VALUES(%s)'
                    print(qry)
                    cur.execute(qry, self.__health_issue_name)
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__health_issues_id = health_issues_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM previous_health_issues WHERE health_issues_id = '" + health_issues_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__health_issues_id = row["health_issues_id"]
                        self.__health_issue_name = row["health_issue_name"]
            finally:
                con.close()

    def get_health_issues_id(self):
        return self.__health_issues_id

    def get_health_issue_name(self):
        return self.__health_issue_name

    def set_health_issue_name(self, health_issue_name):
        self.__health_issue_name = health_issue_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE previous_health_issues SET health_issue_name = %s WHERE health_issues_id = %s;'
                print(qry)
                cur.execute(qry, (self.__health_issue_name, self.__health_issues_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__health_issues_id

    def to_json(self):
        fields_data = {
            "health_issues_id": self.__health_issues_id,
            "health_issue_name": self.__health_issue_name
        }
        return json.dumps(fields_data)


class PatientPreviousHealthIssues:
    def __init__(self, patient_previous_health_issues_id='', fk_patient_id='', fk_previous_health_issues_id=''):
        self.__patient_previous_health_issues_id = patient_previous_health_issues_id
        self.__fk_patient_id = fk_patient_id
        self.__fk_previous_health_issues_id = fk_previous_health_issues_id
        if patient_previous_health_issues_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO previous_health_issues (fk_patient_id, fk_previous_health_issues_id)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__fk_patient_id, self.__fk_previous_health_issues_id))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__patient_previous_health_issues_id = patient_previous_health_issues_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient_previous_health_issues  WHERE patient_previous_health_issues_id = '" \
                          + patient_previous_health_issues_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_previous_health_issues_id = row["patient_previous_health_issues_id"]
                        self.__fk_patient_id = row["fk_patient_id"]
                        self.__fk_previous_health_issues_id = row["fk_previous_health_issues_id"]
            finally:
                con.close()

    def get_patient_previous_health_issues_id(self):
        return self.__patient_previous_health_issues_id

    def get_fk_patient_id(self):
        return self.__fk_patient_id

    def get_fk_previous_health_issues_id(self):
        return self.__fk_previous_health_issues_id

    def set_fk_patient_id(self, fk_patient_id):
        self.__fk_patient_id = fk_patient_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient_previous_health_issues SET fk_patient_id = %s ' \
                      'WHERE patient_previous_health_issues_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_patient_id, self.__patient_previous_health_issues_id))
                con.commit()
        finally:
            pass

    def set_fk_previous_health_issues_id(self, fk_previous_health_issues_id):
        self.__fk_previous_health_issues_id = fk_previous_health_issues_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE patient_previous_health_issues SET fk_previous_health_issues_id = %s ' \
                      'WHERE patient_previous_health_issues_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_previous_health_issues_id, self.__patient_previous_health_issues_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__patient_previous_health_issues_id

    def to_json(self):
        fields_data = {
            "patient_previous_health_issues_id": self.__patient_previous_health_issues_id,
            "fk_patient_id": self.__fk_patient_id,
            "fk_previous_health_issues_id": self.__fk_previous_health_issues_id
        }
        return json.dumps(fields_data)


class Treatments:
    def __init__(self, treatments_used_id='', treatment_name='', treatment_functionality=''):
        self.__treatments_used_id = treatments_used_id
        self.__treatment_name = treatment_name
        self.__treatment_functionality = treatment_functionality
        if treatments_used_id == "":
            # self.__treatments_used_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO TREATMENTS (treatment_name, treatment_functionality)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__treatment_name, self.__treatment_functionality))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__treatments_used_id = treatments_used_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM TREATMENTS  WHERE treatments_used_id = '" + treatments_used_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__treatments_used_id = row["treatments_used_id"]
                        self.__treatment_name = row["treatment_name"]
                        self.__treatment_functionality = row["treatment_functionality"]
            finally:
                con.close()

    def get_treatment_name(self):
        return self.__treatment_name

    def set_treatment_name(self, treatment_name):
        self.__treatment_name = treatment_name
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE TREATMENTS SET treatment_name = %s WHERE treatments_used_id = %s;'
                print(qry)
                cur.execute(qry, (self.__treatment_name, self.__treatments_used_id))
                con.commit()
        finally:
            pass

    def get_treatment_functionality(self):
        return self.__treatment_functionality

    def set_treatment_functionality(self, treatment_functionality):
        self.__treatment_functionality = treatment_functionality
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE TREATMENTS SET treatment_functionality = %s WHERE treatments_used_id = %s;'
                print(qry)
                cur.execute(qry, (self.__treatment_functionality, self.__treatments_used_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__treatments_used_id

    def to_json(self):
        fields_data = {
            "treatments_used_id": self.__treatments_used_id,
            "treatment_name": self.__treatment_name,
            "treatment_functionality": self.__treatment_functionality
        }
        return json.dumps(fields_data)


class TreatmentsUsedByPatient:
    def __init__(self, treatments_used_by_patient_id='', fk_patient_id='', fk_treatments_used_id=''):
        self.__treatments_used_by_patient_id = treatments_used_by_patient_id
        self.__fk_patient_id = fk_patient_id
        self.__fk_treatments_used_id = fk_treatments_used_id
        if treatments_used_by_patient_id == "":
            # self.__treatments_used_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO Treatments_used_by_patient (fk_patient_id, fk_treatments_used_id)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__fk_patient_id, self.__fk_treatments_used_id))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__treatments_used_by_patient_id = treatments_used_by_patient_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM Treatments_used_by_patient  WHERE Treatments_used_by_patient_id = '" \
                          + treatments_used_by_patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__treatments_used_id = row["Treatments_used_by_patient_id"]
                        self.__fk_patient_id = row["fk_patient_id"]
                        self.__fk_treatments_used_id = row["fk_treatments_used_id"]
            finally:
                con.close()

    def get_fk_patient_id(self):
        return self.__fk_patient_id

    def set_fk_patient_id(self, fk_patient_id):
        self.__fk_patient_id = fk_patient_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Treatments_used_by_patient SET fk_patient_id = %s ' \
                      'WHERE Treatments_used_by_patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_patient_id, self.__treatments_used_by_patient_id))
                con.commit()
        finally:
            pass

    def get_fk_treatments_used_id(self):
        return self.__fk_treatments_used_id

    def set_treatment_functionality(self, fk_treatments_used_id):
        self.__fk_treatments_used_id = fk_treatments_used_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Treatments_used_by_patient SET fk_treatments_used_id = %s ' \
                      'WHERE Treatments_used_by_patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_treatments_used_id, self.__treatments_used_by_patient_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__treatments_used_by_patient_id

    def to_json(self):
        fields_data = {
            "treatments_used_by_patient_id": self.__treatments_used_by_patient_id,
            "fk_patient_id": self.__fk_patient_id,
            "fk_treatments_used_id": self.__fk_treatments_used_id
        }
        return json.dumps(fields_data)


class MaskUse:
    def __init__(self, mask_use_id='', mask_type='', usage_frequency=''):
        self.__mask_type = mask_type
        self.__usage_frequency = usage_frequency
        if mask_use_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO MASK_USE (MASK_TYPE, USAGE_FREQUENCY)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__mask_type, self.__usage_frequency))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__mask_use_id = mask_use_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM MASK_USE WHERE MASK_USE_ID = '" + mask_use_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__mask_use_id = row["MASK_USE_ID"]
                        self.__mask_type = row["MASK_TYPE"]
                        self.__usage_frequency = row["USAGE_FREQUENCY"]
            finally:
                con.close()

    def get_mask_type(self):
        return self.__mask_type

    def set_mask_type(self, mask_type):
        self.__mask_type = mask_type
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE MASK_USE SET MASK_TYPE = %s WHERE MASK_USE_ID = %s;'
                print(qry)
                cur.execute(qry, (self.__mask_type, self.__mask_use_id))
                con.commit()
        finally:
            pass

    def get_usage_frequency(self):
        return self.__usage_frequency

    def set_usage_frequency(self, usage_frequency):
        self.__usage_frequency = usage_frequency
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE MASK_USE SET USAGE_FREQUENCY = %s WHERE MASK_USE_ID = %s;'
                print(qry)
                cur.execute(qry, (self.__usage_frequency, self.__mask_use_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__mask_use_id

    def to_json(self):
        fields_data = {
            "mask_use_id": self.__mask_use_id,
            "mask_type": self.__mask_type,
            "usage_frequency": self.__usage_frequency
        }
        return json.dumps(fields_data)


class PatientMaskUse:
    def __init__(self, patient_mask_use_id='', fk_patient_id='', fk_mask_id=''):
        self.__fk_patient_id = fk_patient_id
        self.__fk_mask_id = fk_mask_id
        if patient_mask_use_id == "":
            # self.__mask_use_id = str(uuid.uuid4())
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO PATIENT_MASK_USE (fk_patient_id, fk_mask_id)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__fk_patient_id, self.__fk_mask_id))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__patient_mask_use_id = patient_mask_use_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM PATIENT_MASK_USE  WHERE patient_mask_use_id = '" + patient_mask_use_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_mask_use_id = row["patient_mask_use_id"]
                        self.__fk_patient_id = row["fk_patient_id"]
                        self.__fk_mask_id = row["fk_mask_id"]
            finally:
                con.close()

    def get_fk_patient_id(self):
        return self.__fk_patient_id

    def set_fk_patient_id(self, fk_patient_id):
        self.__fk_patient_id = fk_patient_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE PATIENT_MASK_USE SET fk_patient_id = %s WHERE patient_mask_use_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_patient_id, self.__patient_mask_use_id))
                con.commit()
        finally:
            pass

    def get_fk_mask_id(self):
        return self.__fk_mask_id

    def set_fk_mask_id(self, fk_mask_id):
        self.__fk_mask_id = fk_mask_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE PATIENT_MASK_USE SET fk_mask_id = %s WHERE patient_mask_use_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_mask_id, self.__patient_mask_use_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__patient_mask_use_id

    def to_json(self):
        fields_data = {
            "patient_mask_use_id": self.__patient_mask_use_id,
            "fk_patient_id": self.__fk_patient_id,
            "fk_mask_id": self.__fk_mask_id
        }
        return json.dumps(fields_data)


class RecentTravel:
    def __init__(self, recent_travel_id='', travel_destination='', exposure_intensity=''):
        self.__recent_travel_id = recent_travel_id
        self.__travel_destination = travel_destination
        self.__exposure_intensity = exposure_intensity
        if recent_travel_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO RECENT_TRAVEL (travel_destination, exposure_intensity)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__travel_destination, self.__exposure_intensity))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__recent_travel_id = recent_travel_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM RECENT_TRAVEL  WHERE recent_travel_id = '" + recent_travel_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__recent_travel_id = row["recent_travel_id"]
                        self.__travel_destination = row["travel_destination"]
                        self.__exposure_intensity = row["exposure_intensity"]
            finally:
                con.close()

    def get_travel_destination(self):
        return self.__travel_destination

    def set_travel_destination(self, travel_destination):
        self.__travel_destination = travel_destination
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE RECENT_TRAVEL SET travel_destination = %s WHERE recent_travel_id = %s;'
                print(qry)
                cur.execute(qry, (self.__travel_destination, self.__recent_travel_id))
                con.commit()
        finally:
            pass

    def get_exposure_intensity(self):
        return self.__exposure_intensity

    def set_exposure_intensity(self, exposure_intensity):
        self.__exposure_intensity = exposure_intensity
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE RECENT_TRAVEL SET exposure_intensity = %s WHERE recent_travel_id = %s;'
                print(qry)
                cur.execute(qry, (self.__exposure_intensity, self.__recent_travel_id))
                con.commit()
        finally:
            pass

    def to_json(self):
        fields_data = {
            "recent_travel_id": self.__recent_travel_id,
            "travel_destination": self.__travel_destination,
            "exposure_intensity": self.__exposure_intensity
        }
        return json.dumps(fields_data)


class PatientRecentTravel:
    def __init__(self, patient_recent_travel_id='', fk_patient_id='', fk_recent_travel=''):
        self.__fk_patient_id = fk_patient_id
        self.__fk_recent_travel = fk_recent_travel
        if patient_recent_travel_id == "":
            try:
                config = Config()
                con = config.db_conn

                # parameterize arguments

                with con.cursor() as cur:
                    qry = 'INSERT INTO PATIENT_RECENT_TRAVEL (fk_patient_id, fk_recent_travel)'
                    qry = qry + 'VALUES(%s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__fk_patient_id, self.__fk_recent_travel))
                    con.commit()
            finally:
                pass
        else:
            # Get
            self.__patient_recent_travel_id = patient_recent_travel_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM PATIENT_RECENT_TRAVEL WHERE patient_recent_travel_id = '" \
                          + patient_recent_travel_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_recent_travel_id = row["patient_recent_travel_id"]
                        self.__fk_patient_id = row["fk_patient_id"]
                        self.__fk_recent_travel = row["fk_recent_travel"]
            finally:
                con.close()

    def get_fk_patient_id(self):
        return self.__fk_patient_id

    def set_fk_patient_id(self, fk_patient_id):
        self.__fk_patient_id = fk_patient_id
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE PATIENT_RECENT_TRAVEL SET fk_patient_id = %s WHERE patient_recent_travel_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_patient_id, self.__patient_recent_travel_id))
                con.commit()
        finally:
            pass

    def get_fk_recent_travel(self):
        return self.__fk_recent_travel

    def set_fk_recent_travel(self, fk_recent_travel):
        self.__fk_recent_travel = fk_recent_travel
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE PATIENT_RECENT_TRAVEL SET fk_recent_travel = %s WHERE patient_recent_travel_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_recent_travel, self.__patient_recent_travel_id))
                con.commit()
        finally:
            pass

    def get_id(self):
        return self.__patient_recent_travel_id

    def to_json(self):
        fields_data = {
            "patient_recent_travel_id": self.__patient_recent_travel_id,
            "fk_patient_id": self.__fk_patient_id,
            "fk_recent_travel": self.__fk_recent_travel
        }
        return json.dumps(fields_data)


app = Flask(__name__)


@app.route('/')
def index():
    country = Country(country_id='1')
    location = Locationz(location_id='1')
    duration = Duration(duration_id='1')
    month_affected = MonthAffected(month_affected_id='1')
    patient = Patient(patient_id='1')
    symptoms = Symptoms(symptoms_id='1')
    phi = PreviousHealthIssues(health_issues_id='1')
    pphi = PatientPreviousHealthIssues(patient_previous_health_issues_id='1')
    treatments = Treatments(treatments_used_id='1')
    tubp = TreatmentsUsedByPatient(treatments_used_by_patient_id='1')
    mask_use = MaskUse(mask_use_id='1')
    pmu = PatientMaskUse(patient_mask_use_id='1')
    recent_travel = RecentTravel(recent_travel_id='1')
    prt = PatientRecentTravel(patient_recent_travel_id='1')

    dict_results = {
        "country": country.to_json(),
        "location": location.to_json(),
        "duration": duration.to_json(),
        "month_affected": month_affected.to_json(),
        "patient": patient.to_json(),
        "symptoms": symptoms.to_json(),
        "phi": phi.to_json(),
        "pphi": pphi.to_json(),
        "treatments": treatments.to_json(),
        "tubp": tubp.to_json(),
        "mask_use": mask_use.to_json(),
        "pmu": pmu.to_json(),
        "recent_travel": recent_travel.to_json(),
        "prt": prt.to_json()
    }

    return json.dumps(dict_results)


app.run()


class Tester(unittest.TestCase):
    def update_Patient_name(self):
        # update last_name value of doctor
        update1 = Patient(patient_id='4')
        update2 = Locationz(location_id='2')
        update3 = RecentTravel(recent_travel_id='3')
        self.run(update1.set_age('12'))
        self.run(update2.set_location_name('Rome'))
        self.run(update3.set_travel_destination('Mexico'))

    def create_duration(self):
        # create new doctor entry
        new_entry = Duration(duration_length_in_days="20")
        new_entry2 = PatientMaskUse(fk_patient_id='3', fk_mask_id='4')
        new_entry3 = PatientPreviousHealthIssues(fk_patient_id='4', fk_previous_health_issues_id='2')
        self.run(new_entry)
        self.run(new_entry2)
        self.run(new_entry3)

    def delete_row(self, table, id_key, id_value):
        # delete doctor with given name from doctor table
        try:
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = f"DELETE * FROM {table} WHERE {id_key} = '" + id_value + "'"
                print(qry)
                cur.execute(qry)
        finally:
            con.close()

        self.run(self.delete_row(table='country', id_key='country_id', id_value='1'))
        self.run(self.delete_row(table='Duration', id_key='duration_id', id_value='1'))
        self.run(self.delete_row(table='treatments', id_key='treatments_used_by_patient_id', id_value='1'))
