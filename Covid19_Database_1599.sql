-- -----------------------------------------------------------------------
# Creates Database
-- -----------------------------------------------------------------------
CREATE DATABASE sot18;

-- -----------------------------------------------------------------------
# Uses Database
-- -----------------------------------------------------------------------
USE sot18;


-- ------------------------------------------------------------------------
# Creates a table with name country and inserts records into it
-- ------------------------------------------------------------------------
CREATE TABLE country (
country_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
country_name VARCHAR (45) NOT NULL) ENGINE = InnoDB;

INSERT into country (country_id,country_name) VALUES
('1','United States'),
('2','India'),
('3','Spain'),
('4','Italy'),
('5','Brazil'),
('6','Russia'),
('7','Canada'),
('8','Romania'),
('9','Switzerland'),
('10','Sweden');
  -- ------------------------------------------------------------------------
# Creates a table with name locationz and inserts records into it
-- --------------------------------------------------------------------------
  CREATE TABLE LOCATIONZ (
  `location_id` INT NOT NULL AUTO_INCREMENT,
  `location_name` VARCHAR(45) NOT NULL,
  `location_state` VARCHAR(45) NOT NULL,
  `fk_country_id` INT NOT NULL,
  PRIMARY KEY (`location_id`),
  CONSTRAINT `SDHFSJDFH`
  FOREIGN KEY (`location_id`)
  REFERENCES `country` (`country_id`)) Engine = InnoDB;
  
INSERT into LOCATIONZ (location_id,location_name,location_state,fk_country_id) values 
('1','Allegheny','Pittsburgh','1'),
('2','Brugg','Argau','9'),
('3','Rome', 'Lazio','4'),
('4','Akron', 'Ohio','1'),
('5','Borlänge', 'Dalarna','10'),
('6','Osasco', 'São Paulo','5'),
('7','Calgary', 'Alberta','7'),
('8','Getxo', 'biscay','3'),
('9','Seattle', 'Washington','1'),
('10','Orlando', 'Florida', '1');

-- ------------------------------------------------------------------------
# Creates a table with name month_affected and inserts records into it
-- ------------------------------------------------------------------------   
CREATE TABLE month_affected(
month_affected_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Month_affected VARCHAR(45) NOT NULL,
year_affected INT NOT NULL) Engine = InnoDB;

INSERT into month_affected (month_affected_id, Month_affected, year_affected) values
('1', 'December', '2019'),
('2', 'January', '2020'),
('3', 'February','2020'),
('4', 'March','2020'),
('5', 'April','2020'),
('6', 'May','2020'),
('7', 'June','2020'),
('8', 'July','2020'),
('9', 'August','2020'),
('10', 'September','2020'),
('11', 'October','2020'),
('12', 'November','2020');

-- ------------------------------------------------------------------------
# Creates a table with name duration
#              and inserts records into it
-- ------------------------------------------------------------------------
CREATE TABLE duration(
duration_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
duration_length_in_days INT NOT NULL) Engine = InnoDB;

INSERT INTO duration(duration_id, duration_length_in_days) values
('1','13'),
('2','21'),
('3','18'),
('4','28'),
('5','25'),
('6','23'),
('7','30'),
('8','14'),
('9','19'),
('10','20');

-- ------------------------------------------------------------------------
# Creates a table with name patient and inserts records into it
-- ------------------------------------------------------------------------
CREATE TABLE Patient(
`patient_id` INT NOT NULL AUTO_INCREMENT,
  `patient_name` VARCHAR(45) NOT NULL,
  `Age` INT NOT NULL,
  `fk_month_affected_id` INT NOT NULL,
  `fk_location_id` INT NOT NULL,
  `fk_duration_id` INT NOT NULL,
  PRIMARY KEY (`patient_id`),
  CONSTRAINT `fdhjahd`
    FOREIGN KEY (`patient_id`)
    REFERENCES `LOCATIONZ` (`location_id`),
    CONSTRAINT`JHDFJHS`
    FOREIGN KEY (`patient_id`)
    REFERENCES `month_affected` (`month_affected_id`),
    constraint `ghjgj`
    FOREIGN KEY(`PATIENT_ID`)
    REFERENCES `duration` (`DURATION_ID`)) Engine = InnoDB;
    
  
INSERT into Patient (patient_id,patient_name, Age,fk_month_affected_id,fk_location_id, fk_duration_id ) values 
('1','Sarah Smith', '18','3','3','3'),
('2','Sowmya Talasila', '19','10','1','2'),
('3','Marie Tang', '40','5','1','8'),
('4', 'Sri K Talasila', '48','10','1','4'),
('5','Vasundhara Devi Talasila', '40','10','1','2'),
('6','Rosanna Hopper','60','6','2','9'),
('7','Alexandre Mcclain','68','12','8','7'),
('8','T-Jay Young','27','12','7','5'),
('9','Lilian Coleman','9','8','4','1'),
('10','Lauryn Garcia','35','2','9','6');

-- ------------------------------------------------------------------------
# Creates a table with name symptoms and inserts records into it
-- ------------------------------------------------------------------------
  CREATE TABLE SYMPTOMS(
  `symptoms_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `symptom_name` VARCHAR(45) NOT NULL
  ) Engine = InnoDB;
  
  INSERT into SYMPTOMS (symptoms_id, symptom_name) values
  ('1', 'Cough'),
  ('2', 'Headache'),
  ('3', 'Fatigue'),
  ('4', 'Shortness of Breathe'),
  ('5', 'Nausea or vomiting'),
  ('6', 'Fever or chills'),
  ('7', 'Loss of taste'),
  ('8', 'Loss of smell'),
  ('9', 'Muscle or body aches'),
  ('10', 'Diarrhea'),
  ('11', 'Congestion or runny nose'),
  ('12', 'Pain or pressure in chest'),
  ('13', 'New Confusion'),
  ('14', 'Asymptomatic');
  
-- ------------------------------------------------------------------------
# Creates a table with name patient_symptoms and inserts records into it
-- ------------------------------------------------------------------------
  CREATE TABLE PATIENT_SYMPTOMS(
  `patient_symptoms_id` INT NOT NULL AUTO_INCREMENT,
  `fk_patient_id` INT NOT NULL,
  `fk_symptoms_id` INT NOT NULL,
  PRIMARY KEY (`patient_symptoms_id`),
  INDEX `gjhj_idx` (`fk_patient_id` ASC) VISIBLE,
  INDEX `hjhj_idx` (`fk_symptoms_id` ASC) VISIBLE,
  CONSTRAINT `gjhj`
    FOREIGN KEY (`fk_patient_id`)
    REFERENCES `Patient` (`patient_id`),
  CONSTRAINT `hjhj`
    FOREIGN KEY (`fk_symptoms_id`)
    REFERENCES `SYMPTOMS` (`symptoms_id`)) Engine = InnoDB;
  
   INSERT into PATIENT_SYMPTOMS (patient_symptoms_id, fk_patient_id, fk_symptoms_id) values
   ('1','2','1'),
   ('2','2','2'),
   ('3','2','3'),
   ('4','2','5'),
   ('5','2','7'),
   ('6','2','8'),
   ('7','5','2'),
   ('8','5','3'),
   ('9','5','7'),
   ('10','5','8'),
   ('11','5','9'),
   ('12','4','1'),
   ('13','4','2'),
   ('14','4','5'),
   ('15','4','7'),
   ('16','4','8'),
   ('17','4','10'),
   ('18','1','14'),
   ('21','3','2'),
   ('22','3','3'),
   ('23','3','1'),
   ('24','8','1'),
   ('25','8', '5'),
   ('26','10','1'),
   ('27','10','2'),
   ('28','7','1'),
   ('29','7','2'),
   ('30','7','3'),
   ('31','7','12'),
   ('32','7','13'),
   ('33','7','7'),
   ('34','7','8'),
   ('35','10','14'),
   ('36','6','4'),
   ('37','6','10'),
   ('38','6','9'),
   ('39','6','13'),
   ('40','6','1'),
   ('41','9','1'),
   ('42','9','2'),
   ('43','9','3'),
   ('44','9','8');

-- ------------------------------------------------------------------------
# Creates a table with name previous_health_issues and inserts 
#                       records into it
-- ------------------------------------------------------------------------
CREATE TABLE previous_health_issues(
`health_issues_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
`health_issue_name` VARCHAR(45) NOT NULL) Engine = InnoDB;

INSERT into previous_health_issues (health_issues_id,health_issue_name) VALUES
('1','Asthma'),
('2','Thyroid'),
('3','Diabetes'),
('4','Hypertension'),
('5','Immune deficiencies'),
('6','Obesity'),
('7','Chronic kidney disease'),
('8','Heart conditions'),
('9','Pregnancy'),
('10','Organ Transplantation'),
('11', 'none');

-- ------------------------------------------------------------------------
# Creates a table with name patient_previous_health_issues 
#              and inserts records into it
-- ------------------------------------------------------------------------
CREATE TABLE patient_previous_health_issues(
patient_previous_health_issues_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
fk_patient_id INT NOT NULL,
fk_previous_health_issues_id INT NOT NULL,
  INDEX `gjhjl_idx` (`fk_patient_id` ASC) VISIBLE,
  INDEX `hjhjk_idx` (`fk_previous_health_issues_id` ASC) VISIBLE,
  CONSTRAINT `gjhjl`
    FOREIGN KEY (`fk_patient_id`)
    REFERENCES `Patient` (`patient_id`),
  CONSTRAINT `hjhjk`
    FOREIGN KEY (`fk_previous_health_issues_id`)
    REFERENCES `previous_health_issues` (`health_issues_id`)) Engine = InnoDB;

INSERT into patient_previous_health_issues (patient_previous_health_issues_id,fk_patient_id,fk_previous_health_issues_id) VALUES
('1','2','11'),
('2','9','11'),
('3','1','11'),
('4','5','1'),
('5','5','2'),
('6','4','11'),
('7','7','6'),
('8','7','10'),
('9','8','5'),
('10','6','4'),
('11','6','8');

-- ------------------------------------------------------------------------
# Creates a table with name Treatments and inserts records into it
-- ------------------------------------------------------------------------
CREATE TABLE Treatments (
treatments_used_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
treatment_name VARCHAR(60) NOT NULL,
treatment_functionality VARCHAR (90) NOT NULL) Engine = InnoDB;

INSERT into Treatments (treatments_used_id, treatment_name, treatment_functionality) VALUES
('1','Tylenol','cough and cold. Helps with headaches and fever as well'),
('2','Muscinex','Severe cough and congestion'),
('3','Aleve','fever and body pains'),
('4','Ibuoprofen','Pain killer'),
('5','Vitamin C',' Boosts immune system'),
('6','Vitamin D','Boosts immune system'),
('7',' blood thinners',' Cure blood clots for patients with severe symptoms'),
('8','supplementary oxygen and mechanical ventilatory support','helps patients with breathing problems'),
('9','Zinc','Boosts immune system'),
('10','Vitamin K','maintains blood clotting/thinning balance');

-- ------------------------------------------------------------------------
# Creates a table with name Treatments_used_by_patient
#              and inserts records into it
-- ------------------------------------------------------------------------

CREATE TABLE Treatments_used_by_patient(
Treatments_used_by_patient_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
fk_patient_id INT NOT NULL,
fk_Treatments_used_id INT NOT NULL,
INDEX `gjhjlas_idx` (`fk_patient_id` ASC) VISIBLE,
  INDEX `hjhjkas_idx` (`fk_Treatments_used_id` ASC) VISIBLE,
  CONSTRAINT `gjhjlas`
    FOREIGN KEY (`fk_patient_id`)
    REFERENCES `Patient` (`patient_id`),
  CONSTRAINT `hjhjkas`
    FOREIGN KEY (`fk_Treatments_used_id`)
    REFERENCES `Treatments` (`treatments_used_id`))Engine = InnoDB;

INSERT into Treatments_used_by_patient(Treatments_used_by_patient_id, fk_patient_id,fk_Treatments_used_id) VALUES
('1','1','3'),
('2','2','1'),
('3','2','2'),
('4','2','5'),
('5','2','6'),
('6','8','1'),
('7','8','2'),
('8','10','2'),
('9','10','3'),
('10','5','1');

drop table if exists mask_use cascade;
CREATE TABLE MASK_USE(
MASK_USE_ID INT NOT NULL PRIMARY KEY,
MASK_TYPE VARCHAR(20) NOT NULL,
USAGE_FREQUENCY VARCHAR(20) NOT NULL
)Engine = InnoDB;

INSERT INTO MASK_USE (MASK_USE_ID,MASK_TYPE, USAGE_FREQUENCY) VALUES
(1, 'Cloth', 'rare'),
(2, 'Cloth', 'always'),
(3, 'Surgical', 'sometimes'),
(4, 'Surgical', 'always'),
(5, 'N95', 'rare');

drop table if exists patient_mask_use;
CREATE TABLE PATIENT_MASK_USE(
patient_mask_use_id int not null primary key,
fk_patient_id int not null,
fk_mask_id int not null,
FOREIGN KEY(fk_patient_id) references Patient(patient_id),
FOREIGN KEY(fk_mask_id) references MASK_USE(mask_use_id)
) Engine = InnoDB;

INSERT INTO PATIENT_MASK_USE (PATIENT_MASK_USE_ID,FK_PATIENT_ID, FK_MASK_ID) VALUES
(1, 5, 5),
(2, 1, 3),
(3, 3, 1),
(4, 4, 4),
(5, 1, 2);

drop table if exists recent_travel;
CREATE TABLE RECENT_TRAVEL (
recent_travel_id int not null primary key,
travel_destination varchar(50) not null,
exposure_intensity varchar(50) not null
) Engine = InnoDB;

INSERT INTO RECENT_TRAVEL(recent_travel_id, travel_destination, exposure_intensity) values
(1, 'India', 'Medium'),
(2, 'Mexico', 'Low'),
(3, 'Bahamas', 'Medium'),
(4, 'Myrtle Beach', 'High'),
(5, 'Ocean City', 'High');

drop table if exists patient_recent_travel cascade;
CREATE TABLE PATIENT_RECENT_TRAVEL(
patient_recent_travel_id int not null primary key,
fk_patient_id int not null,
fk_recent_travel int not null,
foreign key(fk_patient_id) references Patient(patient_id),
foreign key(fk_recent_travel) references RECENT_TRAVEL(recent_travel_id)
) Engine = InnoDB;

INSERT INTO PATIENT_RECENT_TRAVEL(patient_recent_travel_id, fk_patient_id, fk_recent_travel) values
(1, 1, 4),
(2, 1, 5),
(3, 6, 2),
(4, 2, 3),
(5, 4, 1);

START TRANSACTION; 
DELETE FROM PATIENT_RECENT_TRAVEL WHERE FK_RECENT_TRAVEL = 5;
#SELECT * FROM PATIENT_RECENT_TRAVEL;
ROLLBACK;
#SELECT * FROM PATIENT_RECENT_TRAVEL;

DROP VIEW IF EXISTS FREQUENCE_OF_COUGH_WITHIN_PATIENTS CASCADE;
CREATE VIEW FREQUENCE_OF_COUGH_WITHIN_PATIENTS 
AS SELECT COUNT(*) AS FREQUENCE_OF_COUGH_WITHIN_PATIENTS 
FROM PATIENT_SYMPTOMS 
WHERE FK_SYMPTOMS_ID = 1;

DROP VIEW IF EXISTS PREVIOUS_HEALTH_HISTORY CASCADE;
CREATE VIEW PREVIOUS_HEALTH_HISTORY AS
SELECT Patient.patient_name as 'Patient Name' ,Patient.age as 'Age', previous_health_issues.health_issue_name as 'Health Issue Name'
FROM (patient_previous_health_issues
INNER JOIN Patient ON patient_previous_health_issues.fk_Patient_id = Patient.patient_id
INNER JOIN previous_health_issues ON patient_previous_health_issues.fk_previous_health_issues_id = previous_health_issues.health_issues_id)
ORDER BY patient_name;

DROP VIEW IF EXISTS SYMPTOMS_EXPERIENCED CASCADE;
CREATE VIEW SYMPTOMS_EXPERIENCED AS
SELECT PATIENT_SYMPTOMS.patient_symptoms_id as 'Id', Patient.patient_name as 'Patient Name',Patient.age as 'Age', SYMPTOMS.symptom_name as 'Symptom Name'
FROM (PATIENT_SYMPTOMS
INNER JOIN Patient ON PATIENT_SYMPTOMS.fk_Patient_id = Patient.patient_id
INNER JOIN SYMPTOMS ON PATIENT_SYMPTOMS.fk_symptoms_id = SYMPTOMS.symptoms_id)
ORDER BY Patient.age;

