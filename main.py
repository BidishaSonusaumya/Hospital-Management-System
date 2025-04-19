from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    lines_list=[]   #making an empty list to store all the lists of line
    #######################
    #### PUT YOUR CODE HERE
    #######################
    try:
        with open(fileName, 'r') as file:
            file_data=file.readlines()  #reading all the lines in the file
            file.close()
        line_number=0           #counter to count line number
        for line in file_data:
            line_number+=1
            line=line.strip()       #stripping to remove the white spaces or escape sequences
            items=line.split(",")   #splitting all the elements(across ',') and putting in a list
            
            if len(items)!=8:         #checking if the data has 7 values or not
                print(f"Invalid number of fields({len(items)}) in line: {line}")  
            else:
                try:
                    patient_id=int(items[0])             #typecasting the value in the list
                    date=items[1]                        #keeping the date same as string
                    temperature=float(items[2])
                    heart_rate=int(items[3])
                    respiratory_rate=int(items[4])
                    sys_blood_pressure=int(items[5])
                    dias_blood_pressure=int(items[6])
                    oxygen_saturation=int(items[7])

                    if (35<=temperature<=42)==False:                    #checking the condition for temperature
                        print(f"Invalid temperature value({temperature}) in line: {line}")
                        continue
                    elif (30<=heart_rate<=180)==False:                 #checking the condition for heart rate
                        print(f"Invalid heart rate value({heart_rate}) in line: {line}")
                        continue
                    elif (5<=respiratory_rate<=40)==False:               #checking the condition for respiratory rate
                        print(f"Invalid respiratory rate value({respiratory_rate}) in line: {line}")
                        continue
                    elif (70<=sys_blood_pressure<=200)==False:             #checking the condition for systolic blood pressure
                        print(f"Invalid  Systolic blood pressure value({sys_blood_pressure}) in line: {line}")
                        continue
                    elif (40<=dias_blood_pressure<=120)==False:               #checking the condition for diastolic blood pressure
                        print(f"Invalid Diastolic blood pressure value({dias_blood_pressure}) in line: {line}")
                        continue
                    elif (70<=oxygen_saturation<=100)==False:                  #checking the condition for oxygen saturation
                        print(f"Invalid Oxygen saturation value({oxygen_saturation}) in line: {line}")
                        continue
                    else:
                        processed_list=[date,temperature,heart_rate,respiratory_rate,sys_blood_pressure,dias_blood_pressure,oxygen_saturation]
                        lines_list.append(processed_list)
                    
                    if patient_id in patients:
                        patients[patient_id].append(processed_list)            #appending the processed list to dictionary5
                    else:
                        patients[patient_id]=[processed_list]
                except ValueError:                    
                    print(f"Invalid data type in line: {line}")     #printing message if there is an unexpected error
                    continue
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")      #printing message if file is not found 
        exit()
    except Exception as e:
        print("An unexpected error occurred while reading the file")
        print(e)
        exit()
          
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
    
    patientId_list=[key for key in patients]     #storing the id's of the patients in a list
    if patientId!=0 and patientId not in patientId_list:
        print(f"Patient with ID {patientId} not found")
        return
    else:
        if patientId==0:
            for pat_id in patientId_list:   #iterating the id's one by one in patientid list and printing info
                print(f"Patient ID: {pat_id}")
                for i in range(len(patients[pat_id])):
                    print(f"      Visit Date: {patients[pat_id][i][0]}")
                    print(f"\tTemperature: {patients[pat_id][i][1]} deg C")
                    print(f"\tHeart rate: {patients[pat_id][i][2]} bpm")
                    print(f"\tRespiratory rate: {patients[pat_id][i][3]} bpm")
                    print(f"\tSystolic blood pressure: {patients[pat_id][i][4]} mmHg")
                    print(f"\tDiastolic blood pressure: {patients[pat_id][i][5]} mmHg")
                    print(f"\tOxygen saturation: {patients[pat_id][i][6]} %")
                    print("\n")
        else:
            print(f"Patient ID: {patientId}")
            for i in range(len(patients[patientId])):
                print(f"      Visit Date: {patients[patientId][i][0]}")
                print(f"\tTemperature: {patients[patientId][i][1]} deg C")
                print(f"\tHeart rate: {patients[patientId][i][2]} bpm")
                print(f"\tRespiratory rate: {patients[patientId][i][3]} bpm")
                print(f"\tSystolic blood pressure: {patients[patientId][i][4]} mmHg")
                print(f"\tDiastolic blood pressure: {patients[patientId][i][5]} mmHg")
                print(f"\tOxygen saturation: {patients[patientId][i][6]} %")
                print("\n")    



def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
    if type(patients) is not dict:              #checking the type of patient if it is dictionary or not
        print("Error:'patients' should be a dictionary")
        return
    else:
        try:
            patientId=int(patientId)     #checking patient id is an integer or not if not except block executes
            patientId_list=[key for key in patients]     #storing the id's of the patients in a list
            avg_temperature=0
            avg_heart_rate=0
            avg_respiratory_rate=0
            avg_systolic_bp=0
            avg_diastolic_bp=0
            avg_oxygen_saturation=0
            count=0
    
            #if block to find the average of all the patient IDs
            if patientId==0:
                for pat_id in patientId_list:
                    for i in range(len(patients[pat_id])):
                        avg_temperature += patients[pat_id][i][1]
                        avg_heart_rate += patients[pat_id][i][2]
                        avg_respiratory_rate += patients[pat_id][i][3]
                        avg_systolic_bp += patients[pat_id][i][4]
                        avg_diastolic_bp += patients[pat_id][i][5]
                        avg_oxygen_saturation += patients[pat_id][i][6]
                        count+=1
                print("Vital signs for all patients:")        
                print(f"  Average temperature: {round(avg_temperature/count,2)} C")       
                print(f"  Average heart rate: {round(avg_heart_rate/count,2)} bpm")       
                print(f"  Average respiratory rate: {round(avg_respiratory_rate/count,2)} bpm")       
                print(f"  Average systolic blood pressure: {round(avg_systolic_bp/count,2)} mmHg")       
                print(f"  Average diastolic blood pressure: {round(avg_diastolic_bp/count,2)} mmHg")       
                print(f"  Average oxygen saturation: {round(avg_oxygen_saturation/count,2)} %")       
            
            #else block to find the average of a particular patient ID
            else:
                if patientId not in patientId_list:  #checking if patient id is present in patient id list or not
                    print(f"No data found for patient with ID {patientId}")
                    return
                else:
                    for i in range(len(patients[patientId])):
                        avg_temperature += patients[patientId][i][1]
                        avg_heart_rate += patients[patientId][i][2]
                        avg_respiratory_rate += patients[patientId][i][3]
                        avg_systolic_bp += patients[patientId][i][4]
                        avg_diastolic_bp += patients[patientId][i][5]
                        avg_oxygen_saturation += patients[patientId][i][6]
                        count+=1
                print(f"Vital signs for patient {patientId}:")        
                print(f"  Average temperature: {round(avg_temperature/count,2)} C")       
                print(f"  Average heart rate: {round(avg_heart_rate/count,2)} bpm")       
                print(f"  Average respiratory rate: {round(avg_respiratory_rate/count,2)} bpm")       
                print(f"  Average systolic blood pressure: {round(avg_systolic_bp/count,2)} mmHg")       
                print(f"  Average diastolic blood pressure: {round(avg_diastolic_bp/count,2)} mmHg")       
                print(f"  Average oxygen saturation: {round(avg_oxygen_saturation/count,2)} %")          
        except ValueError:
            print("Error:'patient ID should be an integer")
            return   



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
    patient_data=[]      #creating an empty list to store patient data after checking conditions
    patient_data.append(patientId)
    try:
        #checking the date conditions
        if date[4]=='-' and date[7]=='-' and 1<=int(date[8:])<=31 and 1<=int(date[5:7])<=12 and int(date[:4])>=1900:
            patient_data.append(date)
        else:
            print("Invalid date.Please enter a valid date")
            return
        #checking the temperature conditions
        if 35.0<=temp<=42.0:
            patient_data.append(temp)
        else:
            print("Invalid temperature.Please enter a temperature between 35.0 and 42.0 degrees Celsius")
            return
        #checking the heart rate conditions
        if 30<=hr<=180:
            patient_data.append(hr)
        else:
            print("Invalid heart rate.Please enter a heart rate between 30 and 180 bpm") 
            return   
        #checking the respiratory rate conditions
        if 5<=rr<=40:
            patient_data.append(rr)
        else:
            print("Invalid respiratory rate.Please enter a respiratory rate between 5 and 40 bpm") 
            return   
        #checking the systolic blood pressure conditions
        if 70<=sbp<=200:
            patient_data.append(sbp)
        else:
            print("Invalid systolic blood pressure.Please enter a systolic blood pressure between 70 and 200 mmHg") 
            return   
        #checking the diastolic blood pressure conditions
        if 40<=dbp<=120:
            patient_data.append(dbp)
        else:
            print("Invalid diastolic blood pressure.Please enter a diastolic blood pressure between 40 and 120 mmHg") 
            return   
        #checking the oxygen saturation conditions
        if 70<=spo2<=100:
            patient_data.append(spo2)
        else:
            print("Invalid oxygen saturation.Please enter a oxygen saturation between 70 and 100 %") 
            return
        
        #appending the data in the patients file
        with open(fileName, 'a') as file:
            formatted_data = '\n'+','.join(map(str, patient_data))
            file.write(formatted_data)
    
        #inserting the new data of patient into dictionary
        if patientId in patients:
            patients[patientId].append(patient_data)
        else:
            patients[patientId]=[patient_data]   
        print(f"Visit is saved successfully for patient #{patientId}")
    except Exception:
        print("An unexpected error occurred while adding new data")
        return


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    patientId_list=[key for key in patients]   #appending the patient id's in a list

    #checking the condition if someone enters year as 0
    if year==None and month!=None:  
        return visits
    
    else:
        #checking the conditions for year is given and month is not given in parameters or not
        if year!=None and month==None:
            if year>=1900 and len(str(year))==4:           #checking the validity of year
                for pat_id in patientId_list:
                        for i in range(len(patients[pat_id])):
                            #checking if the year matches in the dictionary
                            if int(patients[pat_id][i][0][:4])==year:   
                                data_tuple=(pat_id,patients[pat_id][i])          #storing it in a tuple first
                                visits.append(data_tuple)                        #appending that tuple in visits list
        
        #checking the conditions for both year and month are not given in parameters or not
        elif year!=None and month!=None:
            if year>=1900 and len(str(year))==4 and 1<=month<=12:                #checking the validity of both year and month
                for pat_id in patientId_list:
                        for i in range(len(patients[pat_id])):
                            #checking if the year and month matches in the dictionary
                            if int(patients[pat_id][i][0][:4])==year and int(patients[pat_id][i][0][5:7])==month:
                                data_tuple=(pat_id,patients[pat_id][i])
                                visits.append(data_tuple)
        
    
        
        #else block operates on all the years and months of dictionary
        else:
            for pat_id in patientId_list:
                for i in range(len(patients[pat_id])):
                    data_tuple=(pat_id,patients[pat_id][i])
                    visits.append(data_tuple)                     

    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    patientId_list=[key for key in patients]   #appending the patient id's in a list

    for pat_id in patientId_list:
        for i in range(len(patients[pat_id])):
            #assigning the values in dictionary to variables
            heart_rate=patients[pat_id][i][2]
            systolic_bp=patients[pat_id][i][4]
            diastolic_bp=patients[pat_id][i][5]
            oxygen_saturation=patients[pat_id][i][6]

            #checking the conditions for the patients to follow up
            if heart_rate>100 or heart_rate<60 or systolic_bp>140 or diastolic_bp>90 or oxygen_saturation<90:
                if pat_id not in followup_patients:
                    followup_patients.append(pat_id)

    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
    
    if patientId not in patients:                                   #printing message if patient not found
        print(f"No data found for patient with ID {patientId}")
    else:
        patients.pop(patientId)
        file=open(filename,'w')
        for pat_id in patients:
            for visit in range(len(patients[pat_id])):
                patient_data=[pat_id]                              #making a list named patient data with its patient id
                patient_data.extend(patients[pat_id][visit])         #extending the information to the list
                formatted_data = ','.join(map(str, patient_data)) + '\n'
                file.write(formatted_data)
        file.close()
        print(f"Data for patient {patientId} has been deleted")



###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile(r"C:\Users\DELL\Python\patients.txt")
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, r"C:\Users\DELL\Python\patients.txt")
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), r'C:\Users\bhakt\PycharmProjects\pythonProject\python course\project\patients_22BCSI11.txt')
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
