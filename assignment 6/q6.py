def student_data(student_id, **kwargs):
  print("Student ID :",student_id)
  if 'student_name' in kwargs:
    print("Student Name :",kwargs['student_name'])
  if 'student_class' in kwargs:
    print("Student Class :",kwargs['student_class'])
  print()    

    
student_data(student_id='1')
student_data(student_id='1', student_name='Abhhiraj Singh Virk')
student_data(student_id='1', student_name='Abhiraj Singh Virk', student_class ='CIVIL')  

